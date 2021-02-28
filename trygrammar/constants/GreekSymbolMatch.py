from mnkytw import LiteralMatch, MatchAlternation, MatchJoin
from trygrammar.LeastMatchingExponent import LeastMatchingExponent
 

## Greek Symbols
Pi = LiteralMatch("pi")
Epsilon = LiteralMatch("epsilon")
Theta = LiteralMatch("theta")

class GreekSymbolMatch:
    def __init__(self, powerMatch = None):
        if powerMatch:
            self.matcher = MatchAlternation([
                MatchJoin([
                    MatchAlternation([Pi, Epsilon, Theta]),
                    LiteralMatch("^"),
                    LeastMatchingExponent(powerMatch)
                ]),
                MatchAlternation([Pi, Epsilon, Theta]),
            ])
        else:
            self.matcher = MatchAlternation([Pi, Epsilon, Theta])

    def parser(self, body : str, hard_fail = True):
         
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
         
        if type(result[0]) is list:
            return [{
                'val': result[0][0],
                'power': result[0][2],
                'type': 'greek'
            }, result[1]]
        return [{
            'val': result[0],
            'type': 'greek'
        }, result[1]]

    def set_power_match(self, powerMatch):
        self.matcher = MatchAlternation([
                MatchJoin([
                    MatchAlternation([Pi, Epsilon, Theta]),
                    LiteralMatch("^"),
                    LeastMatchingExponent(powerMatch)
                ]),
                MatchAlternation([Pi, Epsilon, Theta])
            ])

    def __str__(self):
        return str(self.matcher)
