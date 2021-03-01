from mnkytw import MatchJoin, LiteralMatch, MatchAlternation, MatchQuantity
 

class AddSubTail:
    def __init__(self, innerMatch):
        self.matcher = MatchJoin([
            MatchAlternation([
                LiteralMatch("+"),
                LiteralMatch("-")
            ]),
            innerMatch
        ])

    def parser(self, body : str, hard_fail = True):
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
        
        symbol = result[0][0]
        term = result[0][1]
        if symbol == "-":
            return [{
                'val': term,
                'type': 'negation'
            }, result[1]]
        return [term, result[1]]

    def __str__(self):
        return str(self.matcher)

class AddSubtractMatch:
    def __init__(self, innerMatch):
        self.matcher = MatchJoin([
            innerMatch,
            MatchQuantity(AddSubTail(innerMatch), 0)
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
            'type': 'addition'
        }, result[1]]

    def set_inner_matcher(self, innerMatch):
        self.matcher = MatchJoin([
            innerMatch,
            MatchQuantity(AddSubTail(innerMatch), 0)
        ])

    def __str__(self):
        return str(self.matcher)