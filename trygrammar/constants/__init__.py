from mnkytw import MatchAlternation
import config
from trygrammar.constants.MultiVariableTermMatch import MultiVariableTermMatch
from trygrammar.constants.ConstantCoeffTermMatch import ConstantCoeffTermMatch
from trygrammar.constants.ConstantFractionMatch import NegativeConstantFractionMatch
from trygrammar.constants.SubstitutionMatch import SubstitutionMatch
from trygrammar.constants.GreekSymbolMatch import GreekSymbolMatch

#Matches either variables or constants or coeff variables

class TermMatch:
    def __init__(self, powerMatch):
        self.matcher = MatchAlternation([
            #match greek symbol
            GreekSymbolMatch(powerMatch),
            #xyz
            MultiVariableTermMatch(),
            #2xyz
            ConstantCoeffTermMatch(powerMatch),
            #2/3 or 2 or -3 or pi
            NegativeConstantFractionMatch(powerMatch),
            ## example such as !a
            SubstitutionMatch(),
        ])
    
    def parser(self, body : str, hard_fail = True):
        if config.verbose:
            print(f"Matching {body} from root {config.previous} to TermMatch")
            config.previous = "TermMatch"
        return self.matcher.parser(body, hard_fail)

    def set_power_match(self, powerMatch):
        self.matcher = MatchAlternation([
            #match greek symbol
            GreekSymbolMatch(powerMatch),
            #xyz
            MultiVariableTermMatch(),
            #2xyz
            ConstantCoeffTermMatch(powerMatch),
            #2/3 or 2 or -3 or pi
            NegativeConstantFractionMatch(powerMatch),
            ## example such as !a
            SubstitutionMatch(),
        ])

    def __str__(self):
        return str(self.matcher)
