from Package.VerbGenerator.PastVerbGenerator import PastVerbGenerator
from Package.VerbGenerator.PresentVerbGenerator import PresentVerbGenerator
from Package.GSheetHandler.GSheetReader import GSheetReader

def main():
    print("Welcome to the arabic verb generator!")
    
    gsheet_reader = GSheetReader()
    root, bab = gsheet_reader.get_root_and_bab()

    past_verb_generator = PastVerbGenerator()
    past_forms = past_verb_generator.get_forms(root, bab)
    past_forms.insert(0, root)
    print(f"Possible Past Forms: {' | '.join(past_forms)}")

    present_verb_generator = PresentVerbGenerator()
    present_forms = present_verb_generator.get_forms(root, bab)
    print(f"Possible Present/Future Forms: {' | '.join(present_forms)}")

if __name__ == "__main__":
    main()
