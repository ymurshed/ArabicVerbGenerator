import time
import json
from Package.Constants.GSheetValues import GSheetValues
from Package.GSheetHandler.GSheetReader import GSheetReader
from Package.Helpers.VerbManager import VerbManager

def main():
    
    print("Welcome to the arabic verb generator!")
    
    # Load configs
    config = load_config('config.json')
    max_row_process_per_iteration = config["sheet_config"]["max_row_process_per_iteration"]
    write_delay_per_iteration = config["sheet_config"]["write_delay_per_iteration"]
    
    # Iterate each bab sheet
    for key, value in GSheetValues.BAB_SHEET_MAPPING.items():
        try:
            print(f"Start processing {key} bab ---> ")
            if key != "بَابُ الإفْعَالِ":
                continue

            current_row = 0
            root_processed = 0
            gsheet_reader = GSheetReader(config, value)
            
            while True:
                root, bab, masder = gsheet_reader.get_root_bab_masder(current_row)
                if root is None or bab is None or masder is None:
                    break

                if current_row == 0:
                    current_row = gsheet_reader.current_row
                
                verb_manager = VerbManager(root, bab, masder)
                verb_manager.generate_forms()
                verb_manager.apply_rules()
                verb_manager.print_forms()
                verb_manager.write_forms(gsheet_reader)

                current_row += 2
                root_processed += 1

                if root_processed % max_row_process_per_iteration == 0:
                    print(f"Root processed: {root_processed}")
                    time.sleep(write_delay_per_iteration)

            print(f"Complete processing {key} bab <--- ")

        except Exception as e:  
            print(f"An error occurred in Main while processing {key} bab. Exception details: {e}")

def load_config(file_path):
    try:
        with open(file_path, 'r') as config_file:
            return json.load(config_file)
    except Exception as e:  
            print(f"An error occurred in load_config. Exception details: {e}")

if __name__ == "__main__":
    main()
