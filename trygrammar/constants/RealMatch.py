from mnkytw import RegexMatch, MatchJoin, LiteralMatch, MatchAlternation
 

class FixedRealMatch:
    def __init__(self):
        self.matcher = MatchJoin([
            RegexMatch(r"[0-9]+"),
            RegexMatch(r"\."),
            RegexMatch(r"[0-9]+")
        ])
    
    def parser(self, body : str, hard_fail = True):
         
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
         
        return [{
            'val': float("".join([str(v) for v in result[0]])),
            'type': 'real'
        }, result[1]]

    def __str__(self):
        return str(self.matcher)

class RealMatch:
    def __init__(self, powerMatch = None):
        if powerMatch:
            self.matcher = MatchAlternation([
                MatchJoin([
                    FixedRealMatch(),
                    LiteralMatch("^"),
                    powerMatch
                ]),
                FixedRealMatch()
            ])
        else:
            self.matcher = FixedRealMatch()

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
                FixedRealMatch(),
                LiteralMatch("^"),
                powerMatch
            ]),
            FixedRealMatch()
        ])

    def __str__(self):
        return str(self.matcher)