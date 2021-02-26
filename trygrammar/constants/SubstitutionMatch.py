from mnkytw import RegexMatch
import config

## Variable Symbols
class SubstitutionMatch:
    def __init__(self):
        self.matcher = RegexMatch(r"\![a-zA-Z]")

    def parser(self, body : str, hard_fail = True):
        if config.verbose:
            print(f"Match {body} from root {config.previous} to SubstitutionMatch")
            config.previous = "SubstitutionMatch"
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
        if config.verbose:
            print(f"Matched {body} from root {config.previous} to SubstitutionMatch")
            config.previous = "SubstitutionMatch"
        return [{
            'val': result[0],
            'type': 'substitution'
        }, result[1]]

    def __str__(self):
        return str(self.matcher)
