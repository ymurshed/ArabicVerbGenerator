from ..Constants.Diacritic import Diacritic
from ..Constants.Exceptions import Exceptions
from ..Constants.OrderVerbIndicators import OrderVerbIndicators

class OrderVerbGenerator:
    def get_forms(self, present_forms):
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
                conjugations.append(self.__apply_exceptional_rule(conjugated))
        
        except Exception as e:  
             print(f"An error occurred in OrderVerbGenerator: {e}")

        return conjugations

    def __get_first_haref_by_aen_kalima(self, root):
        if root[3] == Diacritic.DAMMA:
            return OrderVerbIndicators.prefixes[0] 
        else:
            return OrderVerbIndicators.prefixes[1] 
    
    def __apply_exceptional_rule(self, conjugated):
        for key, value in Exceptions.REMOVE_HAREF_MAPPING.items():
            if key == conjugated:
                conjugated = conjugated.replace(value, "")
        return conjugated