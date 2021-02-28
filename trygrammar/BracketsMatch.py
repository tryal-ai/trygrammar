from mnkytw import LiteralMatch, MatchJoin
 

class BracketsMatch:
    def __init__(self, innerMatch):
        self.matcher = MatchJoin([
            LiteralMatch("("),
            innerMatch,
            LiteralMatch(")")
        ])
    
    def parser(self, body : str, hard_fail = True):
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
        return [{
            'expression': result[0][1],
            'type': 'brackets'
        }, result[1]]

    def set_inner(self, innerMatch):
        self.matcher = MatchJoin([
            LiteralMatch("("),
            innerMatch,
            LiteralMatch(")")
        ])

    def __str__(self):
        return str(self.matcher)