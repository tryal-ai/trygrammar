from mnkytw import MatchAlternation, MatchQuantity, MatchJoin
 
from trygrammar.constants.ConstantMatch import ConstantMatch
from trygrammar.constants.MultiVariableTermMatch import MultiVariableTermMatch

class ConstantCoeffTermMatch:
    def __init__(self, powerMatch):
        self.matcher = MatchJoin([
            MatchQuantity(ConstantMatch(powerMatch), 0, 1),
            MatchQuantity(MultiVariableTermMatch(powerMatch), 0, 1)
        ])

    def parser(self, body : str, hard_fail = True):
        result = self.matcher.parser(body, hard_fail)
        
        if not result:
            return result
        
        if len(result[0][0]) == 0 and len(result[0][1]) == 0:
            return None
        if len(result[0][1]) == 0:
            return [result[0][0][0], result[1]]
        if len(result[0][0]) == 0:
            return [result[0][1][0], result[1]]

        result[0][1][0]['coeff'] = result[0][0][0]
        return [result[0][1][0], result[1]]
        
    
    def set_power_match(self, powerMatch):
        self.matcher = MatchJoin([
            MatchQuantity(ConstantMatch(powerMatch), 0, 1),
            MatchQuantity(MultiVariableTermMatch(powerMatch), 0, 1)
        ])

    def __str__(self):
        return str(self.matcher)