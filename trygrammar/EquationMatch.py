from mnkytw import MatchJoin, LiteralMatch, MatchQuantity
import config
from trygrammar.ExpressionMatch import expression

class EquationTail:
    def __init__(self):
        self.matcher = MatchJoin([
            LiteralMatch("="),
            expression
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


class EquationMatch:
    def __init__(self):
        self.matcher = MatchJoin([
            expression,
            MatchQuantity(EquationTail(), 1)
        ])
    
    def parser(self, body : str, hard_fail = True):
        if config.verbose:
            print(f"Match {body} from root {config.previous} to EquationMatch")
            config.previous = "EquationMatch"
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
        if config.verbose:
            print(f"Matched {body} from root {config.previous} to EquationMatch")
            config.previous = "EquationMatch"
        
        terms = [result[0][0], *result[0][1]]

        return [{
            'expressions': terms,
            'type': 'equation'
        }, result[1]]
    
    def __str__(self):
        return str(self.matcher)