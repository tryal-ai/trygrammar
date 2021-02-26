from mnkytw import MatchAlternation, MatchJoin, RegexMatch, LiteralMatch
import config

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
        if config.verbose:
            print(f"Match {body} from root {config.previous} to IntegerMatch")
            config.previous = "IntegerMatch"
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
        if config.verbose:
            print(f"Matched {body} from root {config.previous} to IntegerMatch")
            config.previous = "IntegerMatch"
        return [{
            'val': int("".join(result[0])),
            'type': 'integer'    
        }, result[1]]
    
    def __str__(self):
        return str(self.matcher)
