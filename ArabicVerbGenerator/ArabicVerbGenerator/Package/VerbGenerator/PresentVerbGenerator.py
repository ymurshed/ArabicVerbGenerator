from ..Constants.Bab import Bab
from ..Constants.Diacritic import Diacritic
from ..Constants.GSheetValues import GSheetValues
from ..Constants.PresentVerbIndicators import PresentVerbIndicators

class PresentVerbGenerator:
    def get_forms(self, root, bab, masder):
        if masder == GSheetValues.SAHEE_MASDER:
            return self.__get_sahee_forms(root, bab)
        else:
            return self.__get_ghair_sahee_forms(root, bab)

    def __get_sahee_forms(self, root, bab):
        try:
            root = self.__set_present_verb_aen_kalima(root, bab)

            # Replace the first diacritic char with SUKUN
            root = root[0] + Diacritic.SUKUN + root[2:]

            # Remove the last diacritic char if present
            if root[-1] in (Diacritic.KASRA + Diacritic.FATHA + Diacritic.DAMMA):
                root = root[:-1]
    
            # Generate conjugations
            conjugations = []
            prefixes = PresentVerbIndicators.prefixes
            suffixes = PresentVerbIndicators.suffixes 

            for i in range(len(suffixes)):
                if i == 3:
                    conjugated = f"{prefixes[i]}{root}{Diacritic.KASRA}{suffixes[i]}"
                else:
                    conjugated = f"{prefixes[i]}{root}{suffixes[i]}"
            
                conjugations.append(conjugated)

        except Exception as e:  
             print(f"An error occurred in PresentVerbGenerator: {e}")

        return conjugations

    def __get_ghair_sahee_forms(self, root, bab):
        try:
            # Remove the last diacritic char if present
            if root[-1] in (Diacritic.KASRA + Diacritic.FATHA + Diacritic.DAMMA):
                root = root[:-1]
    
            # Generate conjugations
            conjugations = []
            prefixes = PresentVerbIndicators.prefixes
            suffixes = PresentVerbIndicators.suffixes 

            for i in range(len(suffixes)):
                conjugated = f"{prefixes[i]}{self.__set_ghair_sahee_present_verb_aen_kalima(root, bab)}{suffixes[i]}"
                conjugations.append(conjugated)

        except Exception as e:  
             print(f"An error occurred in PresentVerbGenerator: {e}")

        return conjugations

    def __set_present_verb_aen_kalima(self, root, bab):
        if len(root) == 6: 
            match bab:
                case Bab.NASARA_YANSURU:
                    root = root[0:3] + Diacritic.DAMMA + root[4:6]

                case Bab.DARABA_YADRIBU:
                    root = root[0:3] + Diacritic.KASRA + root[4:6]

                case Bab.SAMIA_YASMAU:
                    root = root[0:3] + Diacritic.FATHA + root[4:6]

                case Bab.FATAHA_YAFTAHU:
                   root = root[0:3] + Diacritic.FATHA + root[4:6]
        return root

    def __set_ghair_sahee_present_verb_aen_kalima(self, root, bab):
        if len(root) == 4: 
            match bab:
                case Bab.NASARA_YANSURU:
                    root = root[0] + Diacritic.DAMMA + Diacritic.WA_HARFE_ATT + root[3]

                case Bab.DARABA_YADRIBU:
                     root = root[0] + Diacritic.KASRA + Diacritic.YA_HARFE_ATT_1 + root[3]

                case Bab.SAMIA_YASMAU:
                     root = root[0] + Diacritic.FATHA + Diacritic.ALIF + root[3]
        return root