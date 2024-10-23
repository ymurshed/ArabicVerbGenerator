from ..Constants.Bab import Bab
from ..Constants.Diacritic import Diacritic
from ..Constants.GSheetValues import GSheetValues
from ..Constants.PastVerbIndicators import PastVerbIndicators

class PastVerbGenerator:
    def get_forms(self, root, bab, masder):
        if masder == GSheetValues.SAHEE_MASDER:
            return self.__get_sahee_forms(root, bab)

    def __get_sahee_forms(self, root, bab):
        try:
            root = self.__set_past_verb_aen_kalima(root, bab)

            # Remove the last diacritic char if present
            if root[-1] in (Diacritic.KASRA + Diacritic.FATHA + Diacritic.DAMMA):
                root = root[:-1]
    
            # Generate conjugations
            conjugations = []
            suffixes = PastVerbIndicators.suffixes 

            for i in range(len(suffixes)):
                if i == 0:
                    conjugated = f"{root}{Diacritic.FATHA}{suffixes[i]}"
                else:
                    conjugated = f"{root}{Diacritic.SUKUN}{suffixes[i]}"
            
                conjugations.append(conjugated)
        
        except Exception as e:  
             print(f"An error occurred in PastVerbGenerator: {e}")

        return conjugations

    def __set_past_verb_aen_kalima(self, root, bab):
        # 3 character root 
        if len(root) == 6: 
            match bab:
                case Bab.FATAHA_YAFTAHU:
                   root = root[0:3] + Diacritic.FATHA + root[4:6]

                case Bab.NASARA_YANSURU:
                    root = root[0:3] + Diacritic.FATHA + root[4:6]

                case Bab.DARABA_YADRIBU:
                    root = root[0:3] + Diacritic.FATHA + root[4:6]

                case Bab.SAMIA_YASMAU:
                    root = root[0:3] + Diacritic.KASRA + root[4:6]
        return root