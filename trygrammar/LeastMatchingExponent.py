from mnkytw import MatchAlternation
from trygrammar.constants.RealMatch import RealMatch
from trygrammar.constants.IntegerMatch import IntegerMatch
from trygrammar.constants.ConstantCoeffTermMatch import ConstantCoeffTermMatch

class LeastMatchingExponent:
    def __init__(self, innerMatch):
        self.matcher = MatchAlternation([
            RealMatch(),
            IntegerMatch(),
            ConstantCoeffTermMatch(self),
            innerMatch
        ])
    
    def parser(self, body : str, hard_fail = True):
        return self.matcher.parser(body, hard_fail)
    
    def __str__(self):
        return str(self.matcher)