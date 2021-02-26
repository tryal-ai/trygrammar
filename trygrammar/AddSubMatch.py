from mnkytw import MatchJoin, LiteralMatch, MatchAlternation, MatchQuantity
import config

class AddSubTail:
    def __init__(self, innerMatch):
        self.matcher = MatchJoin([
            MatchAlternation([
                LiteralMatch("+"),
                LiteralMatch("-")
            ]),
            innerMatch
        ])

    def parser(self, body : str, hard_fail = True):
        if config.verbose:
            print(f"Match {body} from root {config.previous} to AddSubtractTail")
            config.previous = "AddSubtractTail"
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
        if config.verbose:
            print(f"Matched {body} from root {config.previous} to AddSubtractTail")
            config.previous = "AddSubtractTail"
        
        symbol = result[0][0]
        term = result[0][1]
        if symbol == "-":
            return [{
                'val': term,
                'type': 'negation'
            }, result[1]]
        return [term, result[1]]

    def __str__(self):
        return str(self.matcher)

class AddSubtractMatch:
    def __init__(self, innerMatch):
        self.matcher = MatchJoin([
            innerMatch,
            MatchQuantity(AddSubTail(innerMatch), 1)
        ])

    def parser(self, body : str, hard_fail = True):
        if config.verbose:
            print(f"Match {body} from root {config.previous} to AddSubtractMatcher")
            config.previous = "AddSubtractMatcher"
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
        if config.verbose:
            print(f"Matched {body} from root {config.previous} to AddSubtractMatcher")
            config.previous = "AddSubtractMatcher"
        terms = [result[0][0], *result[0][1]]
        return [{
            'terms': terms,
            'type': 'addition'
        }, result[1]]

    def __str__(self):
        return str(self.matcher)