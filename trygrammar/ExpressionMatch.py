from mnkytw import MatchAlternation
 
from trygrammar.constants import TermMatch
from trygrammar.PowerMatch import PowerMatch
from trygrammar.BracketsMatch import BracketsMatch
from trygrammar.MultiplyDivideMatch import MultiplyDivideMatch
from trygrammar.ImplicitMultiplyMatch import ImplicitMultiplyMatch
from trygrammar.AddSubMatch import AddSubtractMatch
from trygrammar.FunctionsMatch import FunctionsMatch

addSubtract = AddSubtractMatch(None)
brackets = BracketsMatch(addSubtract)
functions = FunctionsMatch(addSubtract)
term = TermMatch(addSubtract)

# A power can either apply to a term, or to a bracket
power = PowerMatch(MatchAlternation([
        brackets,
        functions
    ]),
    addSubtract
)

multiplyDivide = MatchAlternation([
    ImplicitMultiplyMatch(
        MatchAlternation([
            power,
            functions,
            brackets,
            term
        ]),
        MatchAlternation([
            power,
            functions,
            brackets
        ])
    ),
    MultiplyDivideMatch(MatchAlternation([
            power,
            brackets,
            functions,
            term
        ])
    )
])

addSubtract.set_inner_matcher(multiplyDivide)

expression = addSubtract