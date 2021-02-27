from mnkytw import MatchAlternation

import config
from trygrammar.constants.RealMatch import RealMatch
from trygrammar.constants.IntegerMatch import IntegerMatch

class ConstantMatch:
    def __init__(self):
        self.matcher = MatchAlternation([
            RealMatch(),
            IntegerMatch(),
        ])
    
    def parser(self, body : str, hard_fail = True):
        return self.matcher.parser(body, hard_fail)

    def __str__(self):
        return str(self.matcher)


