from ..Constants.Diacritic import Diacritic
from ..Constants.Exceptions import Exceptions

class RuleManager:
    def __init__(self, conjugations):
        self.conjugations = self.__apply_exceptional_rule(conjugations)
        self.conjugations = self.__remove_ya_harfe_att(conjugations)
        
    def __apply_exceptional_rule(self, conjugations):
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

    def __remove_ya_harfe_att(self, conjugations):
        updated_conjugations = []

        for conjugated in conjugations:
            is_updated = False
            
            if conjugated.endswith(Diacritic.YA_HARFE_ATT_1):
                is_updated = True
                updated_conjugations.append(conjugated[:-1])
            
            if is_updated == False:
                updated_conjugations.append(conjugated)
        
        return updated_conjugations