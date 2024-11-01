from gspread.worksheet import Worksheet
from ..Helpers.RuleManager import RuleManager
from ..GSheetHandler.GSheetWritter import GSheetWritter
from ..VerbGenerator.ForbidVerbGenerator import ForbidVerbGenerator
from ..VerbGenerator.OrderVerbGenerator import OrderVerbGenerator
from ..VerbGenerator.PastVerbGenerator import PastVerbGenerator
from ..VerbGenerator.PresentVerbGenerator import PresentVerbGenerator
from ..VerbGenerator.NegativeFutureVerbGenerator import NegativeFutureVerbGenerator
from ..VerbGenerator.ForPresentVerbGenerator import ForPresentVerbGenerator
from ..VerbGenerator.ObjectVerbGenerator import ObjectVerbGenerator

class VerbManager:
    def __init__(self, root, bab, masder):
        self.__root   = root
        self.__bab    = bab
        self.__masder = masder

    def generate_forms(self):
        self.__generate_past_forms()
        self.__generate_present_forms()
        self.__generate_order_forms()
        self.__generate_forbid_forms()
        self.__generate_negative_future_forms()
        self.__generate_for_present_forms()
        self.__generate_object_forms()
                
    def apply_rules(self):
        rule_manager = RuleManager(self.__past_forms)
        self.__past_forms = rule_manager.conjugations
        rule_manager = RuleManager(self.__present_forms)
        self.__present_forms = rule_manager.conjugations
        rule_manager = RuleManager(self.__order_forms)
        self.__order_forms = rule_manager.conjugations
        rule_manager = RuleManager(self.__forbid_forms)
        self.__forbid_forms = rule_manager.conjugations
    
    def print_forms(self):
        print(f"Past Forms: {' | '.join(self.__past_forms)}")
        print(f"Present/Future Forms: {' | '.join(self.__present_forms)}")
        print(f"Order Forms: {' | '.join(self.__order_forms)}")
        print(f"Forbid Forms: {' | '.join(self.__forbid_forms)}")
        print(f"Negative Future Forms: {' | '.join(self.__negative_future_forms)}")
        print(f"For Present Forms: {' | '.join(self.__for_present_forms)}")

    def write_forms(self, gsheet_reader: Worksheet):
        sheet = gsheet_reader.sheet
        current_row = gsheet_reader.current_row
        gsheet_writter = GSheetWritter(sheet, current_row, 
                                       self.__past_forms, self.__present_forms, self.__order_forms, self.__forbid_forms, 
                                       self.__negative_future_forms, self.__for_present_forms)
        gsheet_writter.write_forms()

    def __generate_past_forms(self):
        past_verb_generator = PastVerbGenerator()
        self.__past_forms = past_verb_generator.get_forms(self.__root, self.__bab, self.__masder)
        self.__past_forms.insert(0, self.__root)

    def __generate_past_forms_with_params(self, root, bab, masder):
        past_verb_generator = PastVerbGenerator()
        past_forms = past_verb_generator.get_forms(root, bab, masder)
        past_forms.insert(0, root)
        return past_forms

    def __generate_present_forms(self):
        present_verb_generator = PresentVerbGenerator()
        self.__present_forms = present_verb_generator.get_forms(self.__root, self.__bab, self.__masder)

    def __generate_present_forms_with_params(self, root, bab, masder):
        present_verb_generator = PresentVerbGenerator()
        present_forms = present_verb_generator.get_forms(root, bab, masder)
        return present_forms

    def __generate_order_forms(self):
        order_verb_generator = OrderVerbGenerator()
        self.__order_forms = order_verb_generator.get_forms(self.__present_forms[2:4], self.__bab, self.__masder)

    def __generate_forbid_forms(self):
        forbid_verb_generator = ForbidVerbGenerator()
        self.__forbid_forms = forbid_verb_generator.get_forms(self.__order_forms, self.__bab, self.__masder)

    def __generate_negative_future_forms(self):
        negative_future_verb_generator = NegativeFutureVerbGenerator()
        self.__negative_future_forms = negative_future_verb_generator.get_forms(self.__present_forms)

    def __generate_for_present_forms(self):
        for_present_verb_generator = ForPresentVerbGenerator()
        self.__for_present_forms = for_present_verb_generator.get_forms(self.__present_forms)

    def __generate_object_forms(self):
        main_verb_root      = "أَرَادَ"
        main_verb_bab       = "بَابُ الإفْعَالِ"
        main_verb_masder    = "صحيح"

        past_forms = self.__generate_past_forms_with_params(main_verb_root, main_verb_bab, main_verb_masder)
        present_forms = self.__generate_present_forms_with_params(main_verb_root, main_verb_bab, main_verb_masder)
        
        rule_manager = RuleManager(past_forms)
        past_forms = rule_manager.conjugations
        rule_manager = RuleManager(present_forms)
        present_forms = rule_manager.conjugations

        object_verb_generator = ObjectVerbGenerator()
        self.__object_forms = object_verb_generator.get_forms(self.__present_forms)

        self.__object_past_forms    = [a + " " + b for a, b in zip(past_forms, self.__object_forms)]
        self.__object_present_forms = [a + " " + b for a, b in zip(present_forms, self.__object_forms)]
        x = 10