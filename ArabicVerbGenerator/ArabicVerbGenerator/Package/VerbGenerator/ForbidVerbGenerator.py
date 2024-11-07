from Package.Constants.Bab import Bab
from ..Constants.Diacritic import Diacritic
from ..Constants.GSheetValues import GSheetValues
from ..Constants.Indicators.ForbidVerbIndicators import ForbidVerbIndicators

class ForbidVerbGenerator:
    def get_forms(self, order_forms, bab, masder):
        if masder == GSheetValues.SAHEE_MASDER:
            return self.__get_sahee_forms(order_forms, bab)
        else:
            return self.__get_ghair_sahee_forms(order_forms, bab)

    def __get_sahee_forms(self, order_forms, bab):
        try:
            # Generate conjugations
            conjugations = []
            prefix = ForbidVerbIndicators.prefixes_ifal[0] if bab == Bab.BABUL_IFAL else ForbidVerbIndicators.prefixes[0]
            
            for i in range(len(order_forms)):
                root = order_forms[i].strip()
                
                conjugated = f"{prefix}{root[2:]}"
                conjugations.append(conjugated)
        
        except Exception as e:  
             raise f"An error occurred in ForbidVerbGenerator: {e}"

        return conjugations

    def __get_ghair_sahee_forms(self, order_forms, bab):
        try:
            # Generate conjugations
            conjugations = []
            
            for i in range(len(order_forms)):
                root = order_forms[i].strip()
                
                if bab == Bab.BABUL_IFAL:
                    root = root.replace(Diacritic.ALIF_HAMJA_FATHA, "")
                    prefixes = ForbidVerbIndicators.prefixes_ifal
                else:
                    prefixes = ForbidVerbIndicators.prefixes
                
                conjugated = f"{prefixes[0]}{root}"
                conjugations.append(conjugated)
        
        except Exception as e:  
             raise f"An error occurred in ForbidVerbGenerator: {e}"

        return conjugations