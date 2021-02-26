from mnkytw import LiteralMatch, MatchJoin, MatchAlternation

import config
from trygrammar.constants.ConstantMatch import ConstantMatch

class ConstantFractionMatch:
    def __init__(self, powerMatch):
        self.matcher = MatchJoin([
            ConstantMatch(powerMatch), 
            LiteralMatch('/'), 
            ConstantMatch(powerMatch)
        ])
    
    def parser(self, body : str, hard_fail = True):
        if config.verbose:
            print(f"Match {body} from root {config.previous} to ConstantFractionMatch")
            config.previous = "ConstantFractionMatch"
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
        if config.verbose:
            print(f"Matched {body} from root {config.previous} to ConstantFractionMatch")
            config.previous = "ConstantFractionMatch"
        return [{
            'numer': result[0][0],
            'denom': result[0][2],
            'type': 'fraction'
        }, result[1]]

    def set_power_match(self, powerMatch):
        self.matcher = MatchJoin([
            ConstantMatch(powerMatch), 
            LiteralMatch('/'), 
            ConstantMatch(powerMatch)
        ])

    def __str__(self):
        return str(self.matcher)



class NegativeConstantFractionMatch:
    def __init__(self, powerMatch):
        self.matcher = MatchAlternation([
            MatchJoin([
                LiteralMatch("-"),
                self
            ]),
            MatchAlternation([ConstantFractionMatch(powerMatch), ConstantMatch(powerMatch)])
        ])

    def parser(self, body : str, hard_fail = True):
        if config.verbose:
            print(f"Match {body} from root {config.previous} to NegativeConstantFractionMatch")
            config.previous = "NegativeConstantFractionMatch"
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
        if config.verbose:
            print(f"Matched {body} from root {config.previous} to NegativeConstantFractionMatch")
            config.previous = "NegativeConstantFractionMatch"
        if type(result[0]) is list:
            return [{
                'val': result[0][1],
                'type': 'negation'
            }, result[1]]
        return result

    def set_power_match(self, powerMatch):        
        self.matcher = MatchAlternation([
            MatchJoin([
                LiteralMatch("-"),
                self
            ]),
            MatchAlternation([ConstantFractionMatch(powerMatch), ConstantMatch(powerMatch)])
        ])

    def __str__(self):
        return str(self.matcher)

