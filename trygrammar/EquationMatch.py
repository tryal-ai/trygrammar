from mnkytw import MatchJoin, LiteralMatch, MatchQuantity
from trygrammar.ExpressionMatch import expression

class EquationTail:
    def __init__(self):
        self.matcher = MatchJoin([
            LiteralMatch("="),
            expression
        ])

    def parser(self, body : str, hard_fail = True):
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
        
        return [result[0][1], result[1]]
    
    def __str__(self):
        return str(self.matcher)


class EquationMatch:
    def __init__(self):
        self.matcher = MatchJoin([
            expression,
            MatchQuantity(EquationTail(), 0)
        ])
    
    def parser(self, body : str, hard_fail = True):
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result

        if len(result[0][1]) == 0:
            return [result[0][0], result[1]]

        terms = [result[0][0], *result[0][1]]

        return [{
            'expressions': terms,
            'type': 'equation'
        }, result[1]]
    
    def __str__(self):
        return str(self.matcher)