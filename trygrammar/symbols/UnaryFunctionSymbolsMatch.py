from mnkytw import MatchAlternation, MatchJoin, LiteralMatch
 
from trygrammar.constants.IntegerMatch import IntegerMatch

class UnaryFunctionSymbolsMatch:
    def __init__(self):
        self.matcher = MatchAlternation([
            LiteralMatch("SQRT"),
            MatchJoin([LiteralMatch("ROOT"), IntegerMatch()]),
            MatchJoin([LiteralMatch("LOG"), IntegerMatch()]),
            LiteralMatch("LN"),
            LiteralMatch("SIN"),
            LiteralMatch("COS"),
            LiteralMatch("TAN"),
            LiteralMatch("ARCSIN"),
            LiteralMatch("ARCCOS"),
            LiteralMatch("ARCTAN"),
        ])

    def parser(self, body : str, hard_fail = True):
         
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result
         
        function = "".join([str(v) for v in result[0]])
        if function == 'ROOT2':
            #Lazy fix to convert ROOT2 to SQRT
            function = "SQRT"
        return [function, result[1]]

    def __str__(self):
        return str(self.matcher)
