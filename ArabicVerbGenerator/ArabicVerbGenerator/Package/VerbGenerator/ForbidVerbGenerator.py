from ..Constants.Diacritic import Diacritic
from ..Constants.ForbidVerbIndicators import ForbidVerbIndicators

class ForbidVerbGenerator:
    def get_forms(self, order_forms):
        try:
            # Generate conjugations
            conjugations = []
            for i in range(len(order_forms)):
                root = order_forms[i].strip()
            
                conjugated = f"{ForbidVerbIndicators.prefixes[0]}{root[2:]}"
                conjugations.append(conjugated)
        
        except Exception as e:  
             print(f"An error occurred in ForbidVerbGenerator: {e}")

        return conjugations