from mnkytw import LiteralMatch, MatchJoin
import config

class BracketsMatch:
    def __init__(self, innerMatch):
        self.matcher = MatchJoin([
            LiteralMatch("("),
            innerMatch,
            LiteralMatch(")")
        ])
    
    def parser(self, body : str, hard_fail = True):
        if config.verbose:
            print(f"Match {body} from root {config.previous} to BracketsMatch")
            config.previous = "BracketsMatch"
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
        if config.verbose:
            print(f"Matched {body} from root {config.previous} to BracketsMatch")
            config.previous = "BracketsMatch"
        return [{
            'expression': result[0][1],
            'type': 'brackets'
        }, result[1]]

    def set_inner(self, innerMatch):
        self.matcher = MatchJoin([
            LiteralMatch("("),
            innerMatch,
            LiteralMatch(")")
        ])

    def __str__(self):
        return str(self.matcher)