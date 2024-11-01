from ..Helpers.RuleManager import RuleManager
from ..Constants.GSheetValues import GSheetValues
from ..GSheetHandler.GSheetReader import GSheetReader
from ..GSheetHandler.GSheetWritter import GSheetWritter
from ..VerbGenerator.ForbidVerbGenerator import ForbidVerbGenerator
from ..VerbGenerator.OrderVerbGenerator import OrderVerbGenerator
from ..VerbGenerator.PastVerbGenerator import PastVerbGenerator
from ..VerbGenerator.PresentVerbGenerator import PresentVerbGenerator
from ..VerbGenerator.NegativeFutureVerbGenerator import NegativeFutureVerbGenerator
from ..VerbGenerator.ForPresentVerbGenerator import ForPresentVerbGenerator

class VerbManager:
    def __init__(self, root, bab, masder):
        self.__root   = root
        self.__bab    = bab
        self.__masder = masder

    def generate_forms(self):
        past_verb_generator = PastVerbGenerator()
        self.__past_forms = past_verb_generator.get_forms(self.__root, self.__bab, self.__masder)
        self.__past_forms.insert(0, self.__root)
                
        present_verb_generator = PresentVerbGenerator()
        self.__present_forms = present_verb_generator.get_forms(self.__root, self.__bab, self.__masder)
                
        order_verb_generator = OrderVerbGenerator()
        self.__order_forms = order_verb_generator.get_forms(self.__present_forms[2:4], self.__bab, self.__masder)
                
        forbid_verb_generator = ForbidVerbGenerator()
        self.__forbid_forms = forbid_verb_generator.get_forms(self.__order_forms, self.__bab, self.__masder)

        negative_future_verb_generator = NegativeFutureVerbGenerator()
        self.__negative_future_forms = negative_future_verb_generator.get_forms(self.__present_forms)
                
        for_present_verb_generator = ForPresentVerbGenerator()
        self.__for_present_forms = for_present_verb_generator.get_forms(self.__present_forms)

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

    def write_forms(self, gsheet_reader):
        sheet = gsheet_reader.sheet
        current_row = gsheet_reader.current_row
        gsheet_writter = GSheetWritter(sheet, current_row, 
                                       self.__past_forms, self.__present_forms, self.__order_forms, self.__forbid_forms, 
                                       self.__negative_future_forms, self.__for_present_forms)
        gsheet_writter.write_forms()