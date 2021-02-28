from mnkytw import MatchAlternation, MatchJoin, RegexMatch, LiteralMatch
 

## Integers
class IntegerMatch:
    def __init__(self):
        self.matcher = MatchAlternation([
            MatchJoin([
                RegexMatch(r"[1-9]"), 
                RegexMatch(r"[0-9]*")
            ]),
            LiteralMatch("0")
        ])
    
    def parser(self, body : str, hard_fail = True):
         
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
         
        return [{
            'val': int("".join(result[0])),
            'type': 'integer'    
        }, result[1]]
    
    def __str__(self):
        return str(self.matcher)
