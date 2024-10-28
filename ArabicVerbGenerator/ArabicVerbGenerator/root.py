import time
from Package.Constants.GSheetValues import GSheetValues
from Package.Helpers.RuleManager import RuleManager
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
                
                present_verb_generator = PresentVerbGenerator()
                present_forms = present_verb_generator.get_forms(root, bab, masder)
                
                order_verb_generator = OrderVerbGenerator()
                order_forms = order_verb_generator.get_forms(present_forms[2:4], bab, masder)
                
                forbid_verb_generator = ForbidVerbGenerator()
                forbid_forms = forbid_verb_generator.get_forms(order_forms, bab, masder)
                
                # Apply rules
                rule_manager = RuleManager(past_forms)
                past_forms = rule_manager.conjugations
                rule_manager = RuleManager(present_forms)
                present_forms = rule_manager.conjugations
                rule_manager = RuleManager(order_forms)
                order_forms = rule_manager.conjugations
                rule_manager = RuleManager(forbid_forms)
                forbid_forms = rule_manager.conjugations
                print(f"Past Forms: {' | '.join(past_forms)}")
                print(f"Present/Future Forms: {' | '.join(present_forms)}")
                print(f"Order Forms: {' | '.join(order_forms)}")
                print(f"Forbid Forms: {' | '.join(forbid_forms)}")

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
