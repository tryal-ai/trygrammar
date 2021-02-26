from mnkytw import MatchJoin, LiteralMatch
import config
from trygrammar.symbols.UnaryFunctionSymbolsMatch import UnaryFunctionSymbolsMatch

class FunctionsMatch:
    def __init__(self, innerMatcher):
        self.matcher = MatchJoin([
            UnaryFunctionSymbolsMatch(),
            LiteralMatch("("),
            innerMatcher,
            LiteralMatch(")")
        ])

    def parser(self, body : str, hard_fail = True):
        if config.verbose:
            print(f"Match {body} from root {config.previous} to FunctionMatch")
            config.previous = "FunctionMatch"
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
        if config.verbose:
            print(f"Matched {body} from root {config.previous} to FunctionMatch")
            config.previous = "FunctionMatch"
        func = result[0][0]
        op = result[0][2]

        return [{
            'symbol': func,
            'expression': op,
            'type': 'function'
        }, result[1]]

    def set_inner(self, innerMatch):
        self.matcher = MatchJoin([
            UnaryFunctionSymbolsMatch(),
            LiteralMatch("("),
            innerMatch,
            LiteralMatch(")")
        ])
    
    def __str__(self):
        return str(self.matcher)