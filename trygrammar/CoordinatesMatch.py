from mnkytw import MatchJoin, LiteralMatch, MatchQuantity
from trygrammar.constants import TermMatch
 

class CoordinatesTail:
    def __init__(self, expression):
        self.matcher = MatchJoin([
            LiteralMatch(","),
            expression
        ])

    def parser(self, body : str, hard_fail = True):
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
        
        return [result[0][1], result[1]]

    def set_power_match(self, expression):
        self.matcher = MatchJoin([
            LiteralMatch(","),
            expression
        ])

    def __str__(self):
        return str(self.matcher)


class CoordinatesMatch:
    def __init__(self, expression):
        self.matcher = MatchJoin([
            LiteralMatch("("),
            expression,
            MatchQuantity(CoordinatesTail(expression), 1),
            LiteralMatch(")")
        ])

    def parser(self, body : str, hard_fail = True):
        print(body)
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
        return [{
            'points': [result[0][1], *result[0][2]],
            'type': 'coordinate'
        }, result[1]]

    def set_power_match(self, expression):
        self.matcher = MatchJoin([
            LiteralMatch("("),
            expression,
            MatchQuantity(CoordinatesTail(expression), 1),
            LiteralMatch(")")
        ])
    
    def __str__(self):
        return str(self.matcher)