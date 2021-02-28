from mnkytw import MatchJoin, LiteralMatch
 
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
         
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
         
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