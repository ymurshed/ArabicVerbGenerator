from ..Constants.Diacritic import Diacritic
from ..Constants.Indicators.ForPresentVerbIndicators import ForPresentVerbIndicators

class ForPresentVerbGenerator:
    def get_forms(self, present_forms):
        try:
            # Generate conjugations
            conjugations = []

            for i in range(len(present_forms)):
                root = present_forms[i].strip()
            
                last_two_chars = root[-2:]

                # Remove the last present verb haref if that is NA
                if last_two_chars == Diacritic.NA:
                    root = root[:-2]
                
                # Remove the last diacritic char if present
                root = root[:-1]
                
                conjugated = f"{ForPresentVerbIndicators.prefixes[0]}{root}"
                
                if i != 3:
                    conjugated = f"{conjugated}{Diacritic.FATHA}"
                
                conjugations.append(conjugated)
        
        except Exception as e:  
             print(f"An error occurred in ForPresentVerbGenerator: {e}")

        return conjugations

    