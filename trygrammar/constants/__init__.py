from mnkytw import MatchAlternation, LiteralMatch, MatchJoin
 
from trygrammar.constants.MultiVariableTermMatch import MultiVariableTermMatch
from trygrammar.constants.ConstantCoeffTermMatch import ConstantCoeffTermMatch
from trygrammar.constants.SubstitutionMatch import SubstitutionMatch
from trygrammar.constants.GreekSymbolMatch import GreekSymbolMatch

#Matches either variables or constants or coeff variables

class TermMatch:
    def __init__(self, powerMatch):
        self.matcher = MatchAlternation([
            # Everything
            ConstantCoeffTermMatch(powerMatch),
            ## example such as !a
            SubstitutionMatch(),
        ])
    
    def parser(self, body : str, hard_fail = True):
         
        return self.matcher.parser(body, hard_fail)

    def set_power_match(self, powerMatch):
        self.matcher = MatchAlternation([
            # Everything
            ConstantCoeffTermMatch(powerMatch),
            ## example such as !a
            SubstitutionMatch(),
        ])

    def __str__(self):
        return str(self.matcher)

class NegativeTermMatch:
    def __init__(self, powerMatch):
        self.matcher = MatchJoin([
            LiteralMatch("-"),
            MatchAlternation([
                # Everything
                ConstantCoeffTermMatch(powerMatch),
                ## example such as !a
                SubstitutionMatch(),
            ])
        ]) 
    
    def parser(self, body : str, hard_fail = True):
        result = self.matcher.parser(body, hard_fail)
        if not result:
            return result

        return [{
            'val': result[0][1],
            'type': 'negation',
        }, result[1]]

    def set_power_match(self, powerMatch):
        self.matcher = MatchJoin([
            LiteralMatch("-"),
            MatchAlternation([
                # Everything
                ConstantCoeffTermMatch(powerMatch),
                ## example such as !a
                SubstitutionMatch(),
            ])
        ]) 

    def __str__(self):
        return str(self.matcher)