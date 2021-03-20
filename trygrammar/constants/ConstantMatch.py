from mnkytw import MatchAlternation

 
from trygrammar.constants.RealMatch import RealMatch
from trygrammar.constants.IntegerMatch import IntegerMatch

class ConstantMatch:
    def __init__(self, powerMatch):
        self.matcher = MatchAlternation([
            RealMatch(powerMatch),
            IntegerMatch(powerMatch),
        ])
    
    def parser(self, body : str, hard_fail = True):
        return self.matcher.parser(body, hard_fail)

    def set_power_matcher(self, powerMatch):
        self.matcher = MatchAlternation([
            RealMatch(powerMatch),
            IntegerMatch(powerMatch),
        ])

    def __str__(self):
        return str(self.matcher)


