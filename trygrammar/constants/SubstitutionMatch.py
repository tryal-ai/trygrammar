from mnkytw import RegexMatch
 

## Variable Symbols
class SubstitutionMatch:
    def __init__(self):
        self.matcher = RegexMatch(r"\![a-zA-Z]")

    def parser(self, body : str, hard_fail = True):
         
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
         
        return [{
            'val': result[0],
            'type': 'substitution'
        }, result[1]]

    def __str__(self):
        return str(self.matcher)
