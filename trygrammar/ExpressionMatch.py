from mnkytw import MatchAlternation
import config
from trygrammar.constants import TermMatch
from trygrammar.PowerMatch import PowerMatch
from trygrammar.BracketsMatch import BracketsMatch
from trygrammar.MultiplyDivideMatch import MultiplyDivideMatch
from trygrammar.AddSubMatch import AddSubtractMatch
from trygrammar.FunctionsMatch import FunctionsMatch

brackets = BracketsMatch(None)
functions = FunctionsMatch(None)
term = TermMatch(None)

# A power can either apply to a term, or to a bracket
power = PowerMatch(MatchAlternation([
        brackets,
        functions,
        term
    ]) 
)

multiplyDivide = MultiplyDivideMatch(MatchAlternation([
        brackets,
        functions,
        power,
        term
    ])
)

addSubtract = AddSubtractMatch(multiplyDivide)

brackets.set_inner(addSubtract)

functions.set_inner(addSubtract)

expression = addSubtract

term.set_power_match(expression)