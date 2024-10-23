from ..Constants.Diacritic import Diacritic
from ..Constants.GSheetValues import GSheetValues
from ..Constants.Exceptions import Exceptions
from ..Constants.OrderVerbIndicators import OrderVerbIndicators

class OrderVerbGenerator:
    def get_forms(self, present_forms, masder):
        if masder == GSheetValues.SAHEE_MASDER:
            return self.__get_sahee_forms(present_forms)
    
    def apply_exceptional_rule(self, conjugations):
        updated_conjugations = []

        for conjugated in conjugations:
            is_updated = False
            for key, value in Exceptions.REMOVE_HAREF_MAPPING.items():
                if key == conjugated:
                    is_updated = True
                    updated_conjugations.append(conjugated.replace(value, ""))
            if is_updated == False:
                updated_conjugations.append(conjugated)

        return updated_conjugations

    def __get_sahee_forms(self, present_forms):
        try:
            # Generate conjugations
            conjugations = []

            for i in range(len(present_forms)):
                root = present_forms[i].strip()
            
                last_two_chars = root[-2:]

                # Remove the last haref if that is HARFE_ATT
                if last_two_chars in (Diacritic.WA_HARFE_ATT + Diacritic.YA1_HARFE_ATT + Diacritic.YA2_HARFE_ATT):
                    root = root[:-2]

                # Remove the last present verb haref if that is NA
                if last_two_chars == Diacritic.NA:
                    root = root[:-2]
              
                # Remove the first present verb haref
                root = root[2:]
                
                conjugated = f"{self.__get_first_haref_by_aen_kalima(root)}{root[:-1]}{Diacritic.SUKUN}"
                conjugations.append(conjugated)
        
        except Exception as e:  
             print(f"An error occurred in OrderVerbGenerator: {e}")

        return conjugations

    def __get_first_haref_by_aen_kalima(self, root):
        if root[3] == Diacritic.DAMMA:
            return OrderVerbIndicators.prefixes[0] 
        else:
            return OrderVerbIndicators.prefixes[1] 
    
    