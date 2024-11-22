import os
import sys
import time
import json
from Package.Constants.Errors import Errors
from Package.Constants.GSheetValues import GSheetValues
from Package.GSheetHandler.GSheetReader import GSheetReader
from Package.Helpers.LogManager import LogManager
from Package.Helpers.VerbManager import VerbManager

def main():
    # Get logger
    log_manager = LogManager(os.getcwd())
    logger = log_manager.get_logger()
    logger.info("The arabic verb generator started ---------->")

    asset_dir = "" if is_executable() else "Assets"
    config = load_config()
    max_row_process_per_iteration = config["sheet_config"]["max_row_process_per_iteration"]
    write_delay_per_iteration = config["sheet_config"]["write_delay_per_iteration"]
    
    # Iterate each bab sheet
    for key, value in GSheetValues.BAB_SHEET_MAPPING.items():
        try:
            logger.info(f"Start processing {key} bab --->")
            
            root_processed = 0
            gsheet_reader = GSheetReader(logger, config, value, asset_dir)
            current_row = gsheet_reader.get_current_row_by_bab(value)

            while True:
                try:
                    root, bab, masder = gsheet_reader.get_root_bab_masder(current_row)
                    if root is None or bab is None or masder is None:
                        break

                    if current_row == 0:
                        current_row = gsheet_reader.current_row
                
                    verb_manager = VerbManager(logger, root, bab, masder)
                    verb_manager.generate_forms()
                    verb_manager.apply_rules()
                    verb_manager.log_forms()
                    verb_manager.write_forms(gsheet_reader)

                    current_row += 2
                    root_processed += 1

                    if root_processed % max_row_process_per_iteration == 0:
                        logger.debug(f"Root processed: {root_processed}")
                        time.sleep(write_delay_per_iteration)
                
                except Exception as e:  
                    if Errors.QUOTA_ERROR in str(e):
                        logger.debug(f"Starting retry for: {root} root.") 
                        time.sleep(write_delay_per_iteration)

                    elif Errors.UNPACK_ERROR in str(e): 
                        break

                    else:
                        logger.exception(f"An error occurred in Main while processing {root} root. Exception details: {e}")
            
            gsheet_reader.set_current_row_by_bab(value, current_row)
            logger.info(f"Complete processing {key} bab <--- ")
              
        except Exception as e:  
            if Errors.TYPE_ERROR in str(e): 
                continue

            else:
                logger.exception(f"An error occurred in Main while processing {key} bab. Exception details: {e}")
        
        # Add a delay before each bab sheet processing 
        time.sleep(write_delay_per_iteration)

    logger.info("The arabic verb generator finished <----------")

def load_config():
    try:
        asset_dir = "Assets"

        if is_executable(): 
            asset_dir = "_internal"
            bundle_dir = os.path.dirname(sys.executable)
        else:
            bundle_dir = os.path.dirname(__file__)
    
        config_path = os.path.join(bundle_dir, asset_dir, 'config.json')

        with open(config_path, 'r') as config_file:
            return json.load(config_file)

    except Exception as e:  
        raise e

def is_executable():
    return getattr(sys, 'frozen', False) == True

if __name__ == "__main__":
    main()
