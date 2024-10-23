﻿import time
from Package.Constants.GSheetValues import GSheetValues
from Package.VerbGenerator.ForbidVerbGenerator import ForbidVerbGenerator
from Package.VerbGenerator.OrderVerbGenerator import OrderVerbGenerator
from Package.VerbGenerator.PastVerbGenerator import PastVerbGenerator
from Package.VerbGenerator.PresentVerbGenerator import PresentVerbGenerator
from Package.GSheetHandler.GSheetReader import GSheetReader
from Package.GSheetHandler.GSheetWritter import GSheetWritter

def main():
    
    print("Welcome to the arabic verb generator!")
        
    # Iterate each bab sheet
    for key, value in GSheetValues.BAB_SHEET_MAPPING.items():
        try:
            print(f"Start processing {key} bab ---> ")

            current_row = 0
            root_processed = 0
            gsheet_reader = GSheetReader(value)
            
            while True:
                # Get root and bab from the sheet
                root, bab, masder = gsheet_reader.get_root_bab_masder(current_row)

                if root is None or bab is None or masder is None:
                    break

                # Generate verb forms 
                past_verb_generator = PastVerbGenerator()
                past_forms = past_verb_generator.get_forms(root, bab, masder)
                past_forms.insert(0, root)
                print(f"Possible Past Forms: {' | '.join(past_forms)}")

                present_verb_generator = PresentVerbGenerator()
                present_forms = present_verb_generator.get_forms(root, bab, masder)
                print(f"Possible Present/Future Forms: {' | '.join(present_forms)}")

                order_verb_generator = OrderVerbGenerator()
                order_forms = order_verb_generator.get_forms(present_forms[2:4], masder)
                
                forbid_verb_generator = ForbidVerbGenerator()
                forbid_forms = forbid_verb_generator.get_forms(order_forms, masder)
                print(f"Possible Forbid Forms: {' | '.join(forbid_forms)}")

                # Apply exceptional rule for order forms
                order_forms = order_verb_generator.apply_exceptional_rule(order_forms)
                print(f"Possible Order Forms: {' | '.join(order_forms)}")

                # Write forms to the sheet
                sheet = gsheet_reader.sheet
                current_row = gsheet_reader.current_row
                gsheet_writter = GSheetWritter(sheet, current_row, past_forms, present_forms, order_forms, forbid_forms)
                gsheet_writter.write_forms()

                current_row += 2
                root_processed += 1

                if root_processed % 3 == 0:
                    print(f"Root processed: {root_processed}")
                    time.sleep(60)

            print(f"Complete processing {key} bab <--- ")

        except Exception as e:  
            print(f"An error occurred in Main while processing {key} bab. Exception details: {e}")


if __name__ == "__main__":
    main()
