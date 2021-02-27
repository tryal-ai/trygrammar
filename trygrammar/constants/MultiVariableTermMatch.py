from mnkytw import MatchQuantity, MatchAlternation
import config
from trygrammar.constants.VariableMatch import VariableMatch
from trygrammar.constants.GreekSymbolMatch import GreekSymbolMatch
from trygrammar.symbols.UnaryFunctionSymbolsMatch import UnaryFunctionSymbolsMatch

def reverse_match(result : list):
    current = ""
    matcher = UnaryFunctionSymbolsMatch()
    for term in reversed(result):
        current = term['val'] + current
        isMatch = matcher.parser(current, False)
        if isMatch:
            return len(current)
    return False

class MultiVariableTermMatch:
    def __init__(self, powerMatch = None):
        self.matcher = MatchQuantity(MatchAlternation([
            GreekSymbolMatch(powerMatch),
            VariableMatch(powerMatch)
        ]), 1)
    
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
        
        test_for_function = reverse_match(result[0])
        if test_for_function:
            result = (result[0][:-test_for_function], result[1] - test_for_function)

        return [{
            'vars': result[0],
            'type': 'terms'
        }, result[1]]

    def set_power_matcher(self, powerMatch):
        self.matcher = MatchQuantity(MatchAlternation([
            GreekSymbolMatch(powerMatch),
            VariableMatch(powerMatch)
        ]), 1)

    def __str__(self):
        return str(self.matcher)