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

addSubtract = AddSubtractMatch(MatchAlternation([
    brackets,
    functions,
    power,
    multiplyDivide,
    term
]))

brackets.set_inner(MatchAlternation([
    functions,
    power,
    multiplyDivide,
    addSubtract,
    term
]))

functions.set_inner(MatchAlternation([
    power,
    multiplyDivide,
    addSubtract,
    term
]))

expression = MatchAlternation([
    functions,
    power,
    multiplyDivide,
    addSubtract,
    brackets,
    term
])

term.set_power_match(expression)