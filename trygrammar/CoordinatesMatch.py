from mnkytw import MatchJoin, LiteralMatch, MatchQuantity
from trygrammar.constants import TermMatch
import config

class CoordinatesTail:
    def __init__(self, powerMatch):
        self.matcher = MatchJoin([
            LiteralMatch(","),
            TermMatch(powerMatch)
        ])

    def parser(self, body : str, hard_fail = True):
        if config.verbose:
            print(f"Match {body} from root {config.previous} to EquationTail")
            config.previous = "EquationTail"
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
        if config.verbose:
            print(f"Matched {body} from root {config.previous} to EquationTail")
            config.previous = "EquationTail"
        
        return [result[0][1], result[1]]

    def set_power_match(self, powerMatch):
        self.matcher = MatchJoin([
            LiteralMatch(","),
            TermMatch(powerMatch),
            LiteralMatch(")")
        ])

    def __str__(self):
        return str(self.matcher)


class CoordinatesMatch:
    def __init__(self, powerMatch):
        self.matcher = MatchJoin([
            LiteralMatch("("),
            TermMatch(powerMatch),
            MatchQuantity(CoordinatesTail(powerMatch), 1),
            LiteralMatch(")")
        ])

    def parser(self, body : str, hard_fail = True):
        if config.verbose:
            print(f"Match {body} from root {config.previous} to EquationTail")
            config.previous = "EquationTail"
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
        if config.verbose:
            print(f"Matched {body} from root {config.previous} to EquationTail")
            config.previous = "EquationTail"
        return [{
            'points': [result[0][1], *result[0][2]],
            'type': 'coordinate'
        }, result[1]]

    def set_power_match(self, powerMatch):
        self.matcher = MatchJoin([
            LiteralMatch("("),
            TermMatch(powerMatch),
            MatchQuantity(CoordinatesTail(powerMatch), 1),
            LiteralMatch(")")
        ])
    
    def __str__(self):
        return str(self.matcher)