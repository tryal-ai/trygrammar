from mnkytw import LiteralMatch, MatchAlternation, MatchJoin
import config

## Greek Symbols
Pi = LiteralMatch("pi")
Epsilon = LiteralMatch("epsilon")
Theta = LiteralMatch("theta")

class GreekSymbolMatch:
    def __init__(self, powerMatch = None):
        if powerMatch:
            self.matcher = MatchAlternation([
                MatchJoin([
                    MatchAlternation([Pi, Epsilon, Theta]),
                    LiteralMatch("^"),
                    powerMatch
                ]),
                MatchAlternation([Pi, Epsilon, Theta]),
            ])
        else:
            self.matcher = MatchAlternation([Pi, Epsilon, Theta])

    def parser(self, body : str, hard_fail = True):
        if config.verbose:
            print(f"Match {body} from root {config.previous} to GreekSymbolMatch")
            config.previous = "GreekSymbolMatch"
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
        if config.verbose:
            print(f"Matched {body} from root {config.previous} to GreekSymbolMatch")
            config.previous = "GreekSymbolMatch"
        if type(result[0]) is list:
            return [{
                'val': result[0][0],
                'power': result[0][2],
                'type': 'greek'
            }]
        return [{
            'val': result[0],
            'type': 'greek'
        }, result[1]]

    def set_power_match(self, powerMatch):
        self.matcher = MatchAlternation([
                MatchJoin([
                    MatchAlternation([Pi, Epsilon, Theta]),
                    LiteralMatch("^"),
                    powerMatch
                ]),
                MatchAlternation([Pi, Epsilon, Theta])
            ])

    def __str__(self):
        return str(self.matcher)
