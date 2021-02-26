from mnkytw import RegexMatch, MatchJoin
import config

class RealMatch:
    def __init__(self):
        self.matcher = MatchJoin([
            RegexMatch(r"[0-9]+"),
            RegexMatch(r"\."),
            RegexMatch(r"[0-9]+")
        ])
    
    def parser(self, body : str, hard_fail = True):
        if config.verbose:
            print(f"Match {body} from root {config.previous} to RealMatch")
            config.previous = "RealMatch"
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
        if config.verbose:
            print(f"Matched {body} from root {config.previous} to RealMatch")
            config.previous = "RealMatch"
        return [{
            'val': float("".join([str(v) for v in result[0]])),
            'type': 'real'
        }, result[1]]

    def __str__(self):
        return str(self.matcher)
