from mnkytw import peg_parse, MatchAlternation
from trygrammar.ExpressionMatch import expression
from trygrammar.EquationMatch import EquationMatch

def parser(body : str):
    return peg_parse(body, MatchAlternation([
        #EquationMatch(),
        expression
    ]))