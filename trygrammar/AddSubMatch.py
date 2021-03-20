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
            MatchQuantity(LiteralMatch("-"), 0, 1),
            innerMatch,
            MatchQuantity(AddSubTail(innerMatch), 0)
        ])

    def parser(self, body : str, hard_fail = True):
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
        
        first_term = result[0][1]
        if len(result[0][0]) > 0:
            first_term = {
                'type': 'negation',
                'val': first_term
            }
        
        if len(result[0][2]) == 0:
            return [first_term, result[1]]
        terms = [first_term, *result[0][2]]
        return [{
            'terms': terms,
            'type': 'addition'
        }, result[1]]

    def set_inner_matcher(self, innerMatch):
        self.matcher = MatchJoin([
            MatchQuantity(LiteralMatch("-"), 0, 1),
            innerMatch,
            MatchQuantity(AddSubTail(innerMatch), 0)
        ])

    def __str__(self):
        return str(self.matcher)