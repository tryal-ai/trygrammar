from mnkytw import LiteralMatch, MatchAlternation, MatchJoin
 

## Greek Symbols
Pi = LiteralMatch("pi")
Epsilon = LiteralMatch("epsilon")
Theta = LiteralMatch("theta")

class GreekSymbolMatch:
    def __init__(self, powerMatch = None):
        if powerMatch:
            self.matcher = MatchAlternation([
                MatchJoin([
                    LiteralMatch("#"),
                    MatchAlternation([Pi, Epsilon, Theta]),
                    LiteralMatch("^"),
                    powerMatch
                ]),
                MatchJoin([
                    LiteralMatch("#"),
                    MatchAlternation([Pi, Epsilon, Theta])
                ])
            ])
        else:
            self.matcher = MatchAlternation([Pi, Epsilon, Theta])

    def parser(self, body : str, hard_fail = True):
         
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
         
        if len(result[0]) > 2:
            return [{
                'val': result[0][1],
                'power': result[0][3],
                'type': 'greek'
            }, result[1]]
        
        return [{
            'val': result[0][1],
            'type': 'greek'
        }, result[1]]

    def set_power_match(self, powerMatch):
        self.matcher = MatchAlternation([
                MatchJoin([
                    LiteralMatch("#"),
                    MatchAlternation([Pi, Epsilon, Theta]),
                    LiteralMatch("^"),
                    powerMatch
                ]),
                MatchJoin([
                    LiteralMatch("#"),
                    MatchAlternation([Pi, Epsilon, Theta])
                ])
            ])

    def __str__(self):
        return str(self.matcher)
