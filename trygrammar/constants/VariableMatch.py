from mnkytw import RegexMatch, MatchAlternation, MatchJoin, LiteralMatch
import config

## Variable Symbols
class VariableMatch:
    def __init__(self, powerMatch = None):
        if powerMatch:
            self.matcher = MatchAlternation([
                MatchJoin([
                    RegexMatch(r"[a-zA-Z]"),
                    LiteralMatch("^"),
                    powerMatch
                ]),
                RegexMatch(r"[a-zA-Z]")
            ])
        else:
            self.matcher = RegexMatch(r"[a-zA-Z]")

    def parser(self, body : str, hard_fail = True):
        if config.verbose:
            print(f"Match {body} from root {config.previous} to VariableMatch")
            config.previous = "VariableMatch"
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
        if config.verbose:
            print(f"Matched {body} from root {config.previous} to VariableMatch")
            config.previous = "VariableMatch"
        if type(result[0]) is list:
            return [{
                'val': result[0][0],
                'power': result[0][2],
                'type': 'term'
            }, result[1]] 
        return [{
            'val': result[0],
            'type': 'term'
        }, result[1]]
    
    def set_power_matcher(self, powerMatch):
        self.matcher = MatchAlternation([
            MatchJoin([
                RegexMatch(r"[a-zA-Z]"),
                LiteralMatch("^"),
                powerMatch
            ]),
            RegexMatch(r"[a-zA-Z]")
        ])

    def __str__(self):
        return str(self.matcher)
