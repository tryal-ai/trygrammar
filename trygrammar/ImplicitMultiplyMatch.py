from mnkytw import MatchJoin, MatchQuantity

class ImplicitMultiplyMatch:
    def __init__(self, coeffMatch, termMatch):
        self.matcher = MatchJoin([
            MatchQuantity(coeffMatch, 0, 1),
            MatchQuantity(termMatch, 1)
        ])
    
    def parser(self, body : str, hard_fail : bool):
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
        
        if len(result[0][0]) + len(result[0][1]) < 2:
            return None

        return [{
            'terms': [*result[0][0], *result[0][1]],
            'type': 'multiplication'
        }, result[1]]

    def __str__(self):
        return str(self.matcher)