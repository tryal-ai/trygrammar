from mnkytw import peg_parse, MatchAlternation
from trygrammar.ExpressionMatch import expression
from trygrammar.EquationMatch import EquationMatch
from trygrammar.CoordinatesMatch import CoordinatesMatch

def parser(body : str):
    return peg_parse(body, MatchAlternation([
        EquationMatch(),
        CoordinatesMatch(expression)
    ]))