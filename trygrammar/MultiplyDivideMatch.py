from mnkytw import MatchJoin, LiteralMatch, MatchAlternation, MatchQuantity
 

class MultiplyDivideTail:
    def __init__(self, innerMatch):
        self.matcher = MatchJoin([
            MatchAlternation([
                LiteralMatch("*"),
                LiteralMatch("/")
            ]),
            innerMatch
        ])
    def parser(self, body : str, hard_fail : True):
         
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
         
        symbol = result[0][0]
        term = result[0][1]
        if symbol == "/":
            return [{
                'numer': {
                    'val': 1,
                    'type': 'integer'
                },
                'denom': term,
                'type': 'fraction'
            }, result[1]]
        return [term, result[1]]

    def __str__(self):
        return str(self.matcher)

class MultiplyDivideMatch:
    def __init__(self, innerMatch):
        self.matcher = MatchJoin([
            innerMatch,
            MatchQuantity(MultiplyDivideTail(innerMatch), 0)
        ])

    def parser(self, body : str, hard_fail = True):
        result = self.matcher.parser(body, hard_fail)
        
        if not result:
            return result
        
        if len(result[0][1]) == 0:
            return [result[0][0], result[1]]
        terms = [result[0][0], *result[0][1]]

        return [{
            'terms': terms,
            'type': 'multiplication',
        }, result[1]]
        

    def __str__(self):
        return str(self.matcher)