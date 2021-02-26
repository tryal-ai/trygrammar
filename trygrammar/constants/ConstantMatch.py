from mnkytw import MatchAlternation, MatchJoin, LiteralMatch

import config
from trygrammar.constants.RealMatch import RealMatch
from trygrammar.constants.IntegerMatch import IntegerMatch
from trygrammar.constants.GreekSymbolMatch import GreekSymbolMatch
from trygrammar.constants.VariableMatch import VariableMatch

class PositiveConstantMatch:
    def __init__(self, powerMatch):
        self.matcher = MatchAlternation([
            RealMatch(),
            IntegerMatch(),
            GreekSymbolMatch(),
            VariableMatch(powerMatch)
        ])
    
    def parser(self, body : str, hard_fail = True):
        if config.verbose:
            print(f"Matching {body} from root {config.previous} to PositiveConstantMatch")
            config.previous = "PositiveConstantMatch"
        return self.matcher.parser(body, hard_fail)

    def set_power_match(self, powerMatch):
        self.matcher = MatchAlternation([
            RealMatch(),
            IntegerMatch(),
            GreekSymbolMatch(),
            VariableMatch(powerMatch)
        ])

    def __str__(self):
        return str(self.matcher)

class NegativeConstantMatch:
    def __init__(self, powerMatch):
        self.matcher = MatchJoin([LiteralMatch("-"), PositiveConstantMatch(powerMatch)])

    def parser(self, body : str, hard_fail = True):
        if config.verbose:
            print(f"Match {body} from root {config.previous} to NegativeConstantMatch")
            config.previous = "NegativeConstantMatch"
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
        if config.verbose:
            print(f"Matched {body} from root {config.previous} to NegativeConstantMatch")
            config.previous = "NegativeConstantMatch"
        return [{
            'val': result[0][1],
            'type': 'negation'
        }, result[1]]

    def set_power_match(self, powerMatch):
        self.matcher = MatchJoin([LiteralMatch("-"), PositiveConstantMatch(powerMatch)])

    def __str__(self):
        return str(self.matcher)

def ConstantMatch(powerMatch):
    return MatchAlternation([NegativeConstantMatch(powerMatch), PositiveConstantMatch(powerMatch)])
