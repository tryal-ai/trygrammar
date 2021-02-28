from mnkytw import LiteralMatch, MatchJoin
from trygrammar.LeastMatchingExponent import LeastMatchingExponent
 

class PowerMatch:
    def __init__(self, innerMatch):
        self.matcher = MatchJoin([
            innerMatch,
            LiteralMatch("^"),
            LeastMatchingExponent(innerMatch)
        ])
    
    def parser(self, body : str, hard_fail = True):
         
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
         
        
        mantissa = result[0][0]
        exponent = result[0][2]

        return [{
            'mantissa': mantissa,
            'exponent': exponent,
            'type': 'power'
        }, result[1]]

    def __str__(self):
        return str(self.matcher)