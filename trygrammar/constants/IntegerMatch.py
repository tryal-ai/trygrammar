from mnkytw import MatchAlternation, MatchJoin, RegexMatch, LiteralMatch
 

## Integers
class FixedIntegerMatch:
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

class IntegerMatch:
    def __init__(self, powerMatch = None):
        if powerMatch:
            self.matcher = MatchAlternation([
                MatchJoin([
                    FixedIntegerMatch(),
                    LiteralMatch("^"),
                    powerMatch
                ]),
                FixedIntegerMatch()
            ])
        else:
            self.matcher = FixedIntegerMatch()

    def parser(self, body : str, hard_fail = True):
         
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
         
        if type(result[0]) is list:
            result[0][0]['power'] = result[0][2]
            return [result[0][0], result[1]] 
        return [result[0], result[1]]
    
    def set_power_matcher(self, powerMatch):
        self.matcher = MatchAlternation([
            MatchJoin([
                FixedIntegerMatch(),
                LiteralMatch("^"),
                powerMatch
            ]),
            FixedIntegerMatch()
        ])

    def __str__(self):
        return str(self.matcher)