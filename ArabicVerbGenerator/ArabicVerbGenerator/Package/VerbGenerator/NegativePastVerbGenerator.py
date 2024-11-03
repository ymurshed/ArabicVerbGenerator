from ..Constants.Indicators.NegativePastVerbIndicators import NegativePastVerbIndicators

class NegativePastVerbGenerator:
    def get_forms(self, past_forms):
        negative_past_forms = [NegativePastVerbIndicators.prefixes[0] + " " + item for item in past_forms]
        return negative_past_forms