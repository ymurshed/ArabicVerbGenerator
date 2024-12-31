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

            if bab == Bab.BABUL_IFAL:
                prefix = ForbidVerbIndicators.prefixes_ifal[0]
            elif bab == Bab.BABUT_TAFEL:
                prefix = ForbidVerbIndicators.prefixes_tafel[0]
            elif bab == Bab.BABUT_TAFAUL:
                prefix = ForbidVerbIndicators.prefixes_tafaul[0]
            else:
                prefix = ForbidVerbIndicators.prefixes[0]
            
            for i in range(len(order_forms)):
                root = order_forms[i].strip()
                
                if bab == Bab.BABUT_TAFEL or bab == Bab.BABUT_TAFAUL:
                    conjugated = f"{prefix}{root}"
                else:    
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
                elif bab == Bab.BABUL_ISTEFAL:
                    root = root.replace(Diacritic.ALIF_KASRA, "")
                    prefixes = ForbidVerbIndicators.prefixes_istefal
                else:
                    prefixes = ForbidVerbIndicators.prefixes
                
                conjugated = f"{prefixes[0]}{root}"
                conjugations.append(conjugated)
        
        except Exception as e:  
             raise f"An error occurred in ForbidVerbGenerator: {e}"

        return conjugations