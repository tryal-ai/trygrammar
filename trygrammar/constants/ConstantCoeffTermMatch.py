from mnkytw import MatchAlternation, MatchQuantity, MatchJoin
import config
from trygrammar.constants.ConstantFractionMatch import NegativeConstantFractionMatch
from trygrammar.constants.VariableMatch import VariableMatch
from trygrammar.constants.GreekSymbolMatch import GreekSymbolMatch

class ConstantCoeffTermMatch:
    def __init__(self, powerMatch):
        self.matcher = MatchJoin([
            NegativeConstantFractionMatch(powerMatch),
            MatchAlternation([
                MatchQuantity(GreekSymbolMatch(powerMatch), 1),
                MatchQuantity(VariableMatch(powerMatch), 1)
            ])
        ])

    def parser(self, body : str, hard_fail = True):
        if config.verbose:
            print(f"Match {body} from root {config.previous} to ConstantCoeffTermMatch")
            config.previous = "ConstantCoeffTermMatch"
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
        if config.verbose:
            print(f"Matched {body} from root {config.previous} to ConstantCoeffTermMatch")
            config.previous = "ConstantCoeffTermMatch"
        if result[0][1][0]['type'] == 'greek':
            return [{
                'coeff': result[0][0],
                'val': result[0][1][0]['val'],
                'type': 'greek'
            }, result[1]]

        return [{
            'coeff': result[0][0],
            'vars': result[0][1],
            'type': 'term'
        }, result[1]] 
    
    def set_power_match(self, powerMatch):
        self.matcher = MatchJoin([
            NegativeConstantFractionMatch(powerMatch),
            MatchAlternation([
                MatchQuantity(GreekSymbolMatch(powerMatch), 1),
                MatchQuantity(VariableMatch(powerMatch), 1)
            ])
        ])

    def __str__(self):
        return str(self.matcher)