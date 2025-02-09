from Package.Constants.Bab import Bab
from ..Constants.Diacritic import Diacritic
from ..Constants.GSheetValues import GSheetValues
from ..Constants.Indicators.OrderVerbIndicators import OrderVerbIndicators

class OrderVerbGenerator:
    def get_forms(self, present_forms, bab, masder):
        if masder == GSheetValues.SAHEE_MASDER:
            return self.__get_sahee_forms(present_forms, bab)
        else:
            return self.__get_ghair_sahee_forms(present_forms, bab)

    def __get_sahee_forms(self, present_forms, bab):
        try:
            # Generate conjugations
            conjugations = []

            for i in range(len(present_forms)):
                root = present_forms[i].strip()
            
                last_two_chars = root[-2:]

                # Remove the last haref if that is HARFE_ATT
                if last_two_chars in (Diacritic.WA_HARFE_ATT + Diacritic.YA_HARFE_ATT_1 + Diacritic.YA_HARFE_ATT_2):
                    root = root[:-2]

                # Remove the last present verb haref if that is NA
                if last_two_chars == Diacritic.NA:
                    root = root[:-2]
              
                # Remove the first present verb haref
                root = root[2:]
                
                # Set the first present verb haref 
                if bab == Bab.BABUL_IFALI:
                    first_haref = Diacritic.ALIF_HAMJA_FATHA
                elif bab == Bab.BABUT_TAFELI or bab == Bab.BABUT_TAFAULI or Bab.BABUL_MUFAALATI:
                    first_haref = ""
                else:
                    first_haref = self.__get_first_haref_by_aen_kalima(root) 

                conjugated = f"{first_haref}{root[:-1]}{Diacritic.SUKUN}"
                conjugations.append(conjugated)
        
        except Exception as e:  
             raise f"An error occurred in OrderVerbGenerator: {e}"

        return conjugations

    def __get_ghair_sahee_forms(self, present_forms, bab):
        try:
            # Generate conjugations
            conjugations = []

            for i in range(len(present_forms)):
                root = present_forms[i].strip()
            
                last_two_chars = root[-2:]

                # Remove the last present verb haref if that is NA
                if last_two_chars == Diacritic.NA:
                    root = root[:-2]
              
                # Remove the first present verb haref
                root = root[2:]
                
                # Set the first present verb haref 
                if bab == Bab.BABUL_IFALI:
                    first_haref = Diacritic.ALIF_HAMJA_FATHA
                elif bab == Bab.BABUL_ISTEFALI:
                    first_haref = Diacritic.ALIF_KASRA
                else:
                    first_haref = ""
                
                if i == 0:
                    conjugated = f"{first_haref}{root[0:len(root) - 4]}{root[-2]}{Diacritic.SUKUN}"
                else:
                    conjugated = f"{first_haref}{root}"

                conjugations.append(conjugated)
        
        except Exception as e:  
             raise f"An error occurred in OrderVerbGenerator: {e}"

        return conjugations

    def __get_first_haref_by_aen_kalima(self, root):
        if root[3] == Diacritic.DAMMA:
            return OrderVerbIndicators.prefixes[0] 
        else:
            return OrderVerbIndicators.prefixes[1] 
    
    