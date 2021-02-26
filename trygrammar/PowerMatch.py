from mnkytw import LiteralMatch, MatchJoin
import config

class PowerMatch:
    def __init__(self, innerMatch):
        self.matcher = MatchJoin([
            innerMatch,
            LiteralMatch("^"),
            innerMatch
        ])
    
    def parser(self, body : str, hard_fail = True):
        if config.verbose:
            print(f"Match {body} from root {config.previous} to PowerMatch")
            config.previous = "PowerMatch"
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
        if config.verbose:
            print(f"Matched {body} from root {config.previous} to PowerMatch")
            config.previous = "PowerMatch"
        
        mantissa = result[0][0]
        exponent = result[0][2]

        return [{
            'mantissa': mantissa,
            'exponent': exponent,
            'type': 'power'
        }, result[1]]

    def __str__(self):
        return str(self.matcher)