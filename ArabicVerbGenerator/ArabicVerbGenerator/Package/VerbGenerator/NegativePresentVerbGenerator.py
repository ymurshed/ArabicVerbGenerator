from ..Constants.Indicators.NegativePresentVerbIndicators import NegativePresentVerbIndicators

class NegativePresentVerbGenerator:
    def get_forms(self, present_forms):
        negative_present_forms = [NegativePresentVerbIndicators.prefixes[0] + " " +  item for item in present_forms]
        return negative_present_forms