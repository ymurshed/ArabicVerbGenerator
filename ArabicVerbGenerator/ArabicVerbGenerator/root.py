import time
from Package.Constants.GSheetValues import GSheetValues
from Package.GSheetHandler.GSheetReader import GSheetReader
from Package.Helpers.VerbManager import VerbManager

def main():
    
    print("Welcome to the arabic verb generator!")
        
    # Iterate each bab sheet
    for key, value in GSheetValues.BAB_SHEET_MAPPING.items():
        try:
            # if key != "فَتَحَ - يَفْتَحُ":
            #     continue

            print(f"Start processing {key} bab ---> ")

            current_row = 0
            root_processed = 0
            gsheet_reader = GSheetReader(value)
            
            while True:
                root, bab, masder = gsheet_reader.get_root_bab_masder(current_row)
                if root is None or bab is None or masder is None:
                    break

                verb_manager = VerbManager(root, bab, masder)
                verb_manager.generate_forms()
                verb_manager.apply_rules()
                verb_manager.print_forms()
                verb_manager.write_forms(gsheet_reader)

                current_row += 2
                root_processed += 1

                if root_processed % 2 == 0:
                    print(f"Root processed: {root_processed}")
                    time.sleep(60)

            print(f"Complete processing {key} bab <--- ")

        except Exception as e:  
            print(f"An error occurred in Main while processing {key} bab. Exception details: {e}")


if __name__ == "__main__":
    main()
