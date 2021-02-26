from mnkytw import MatchQuantity
import config
from trygrammar.constants.VariableMatch import VariableMatch

class MultiVariableTermMatch:
    def __init__(self, powerMatch = None):
        self.matcher = MatchQuantity(VariableMatch(powerMatch), 1)
    
    def parser(self, body : str, hard_fail = True):
        if config.verbose:
            print(f"Match {body} from root {config.previous} to MultiVariableTermMatch")
            config.previous = "MultiVariableTermMatch"
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
        if config.verbose:
            print(f"Matched {body} from root {config.previous} to MultiVariableTermMatch")
            config.previous = "MultiVariableTermMatch"
        return [{
            'vars': result[0],
            'type': 'terms'
        }, result[1]]

    def set_power_matcher(self, powerMatch):
        self.matcher = MatchQuantity(VariableMatch(powerMatch), 1)

    def __str__(self):
        return str(self.matcher)