// Tryal

TryGrammar = (Coordinate / Equation)

Equation "equation"
    = L: Expression R: (EquationTail)* {
        if (R.length > 0) {
            return {
                expressions: [L, ...R],
                type: 'equation'
            }
        }
        return L;
    }

EquationTail "equation tail"
    = "=" R: Expression {
        return R;
    }

LeastMatchingExponent "least matching exponent"
    = "^" E: (Real / Integer / ConstantCoeffTerm / Expression) {
        return E;
    }

Expression "expression"
    = L: Multiplication R: (AddSubtractTail)* {
        if (R.length > 0) {
            return {
                terms: [L, ...R],
                type: 'addition'
            };
        }
        return L;
    }

AddSubtractTail "add-subtract tail"
    = "+" T: Multiplication {
        return T;
    } / "-" T: Multiplication {
        return {
            val: T,
            type: 'negation'
        }
    }

Multiplication "multiplication"
    = (MultiplyDivide / ImplicitMultiply)

MultiplyDivide "multiply-divide"
    = L: (Power / Brackets / Function / ConstantCoeffTerm) R: (MultiplyDivideTail)* {
        if (R.length > 0) {
            return {
                terms: [L, ...R],
                type: 'multiplication'
            };
        }
        return L;
    }

MultiplyDivideTail "multiply-divide tail"
    = "*" T: (Power / Brackets / Function / ConstantCoeffTerm) {
        return T;
    } / "/" T: (Power / Brackets / Function / ConstantCoeffTerm) {
        return {
            numer: { val: 1, type: 'integer' },
            denom: T,
            type: 'fraction'
        };
    }

ImplicitMultiply "implicit multiply"
    = C: (ConstantCoeffTerm) T: (Power / Function / Brackets)+ {
        return {
            terms: [C, ...T],
            implicit: true,
            type: 'multiplication'
        };
    } / F: (Power / Function / Brackets) T: (Power / Function / Brackets)+ {
        return {
            terms: [F, ...T],
            implicit: true,
            type: 'multiplication'
        };
    }


Power "power"
    = M: (Brackets / Function) E: LeastMatchingExponent {
        return {
            mantissa: M,
            exponent: E,
            type: 'power'
        };
    }

Function "function"
    = S: UnaryFunctionSymbols "(" E: Expression ")" {
        return {
            symbol: S,
            expression: E,
            type: 'function'
        };
    }

Brackets "brackets"
    = "(" E: Expression ")" {
        return {
            expression: E,
            type: 'brackets'
        };
    }

Coordinate "coordinate"
    = "(" L: (ConstantCoeffTerm) R: ("," A: (ConstantCoeffTerm) {
        return A;
    })+ ")" {
        return {
            points: [L, ...R],
            type: 'coordinate'
        }
    }

ConstantCoeffTerm "constant coefficient term"
    = C: (Constant)? T: (MultiVariableTerm)? {
        if (!C) {
            return T;
        }
        if (!T) {
            return C;
        }
        return {
            ...T,
            coeff: C
        };
    }

Constant "constant"
    = V: (Real / Integer) {
        return V;
    }


MultiVariableTerm "multi-variable term"
    = V: (GreekSymbols / Variable)+ {
        return {
            vars: V,
            type: 'terms'
        };
    }

UnaryFunctionSymbols = 
    ("SQRT" / 
    "ROOT" Integer /
    "LOG" Integer /
    "LN" / 
    "SIN" / 
    "COS" / 
    "TAN" / 
    "ARCSIN" / 
    "ARCCOS" / 
    "ARCTAN") {
        return text();
    }



GreekSymbols "greek symbol"
    = "#" S:("pi" / "epsilon" / "theta") E: LeastMatchingExponent {
        return {
            val: S,
            power: E,
            type: "greek"
        };
    } / "#" S:("pi" / "epsilon" / "theta") {
        return {
            val: S,
            type: "greek"
        };
    }
//TODO: This is greedy, and in the python grammar, powers are least matching
Variable = V: [a-zA-Z] E: LeastMatchingExponent {
        return {
            vars: V,
            power: E,
            type: 'term'
        };
    } / V:[a-zA-Z] {
        return {
            vars: V,
            type: 'term',
        };
    }


//A Real begins with an integer or a zero, followed by a decimal
Real "real"
    = ("0" / Integer) "." [0-9]+ { 
        return {
            val: parseFloat(text(), 10),
            type: 'real',
        };
    }

//An integer is any set of digits beginning with a digit between 1-9 
Integer "integer"
    = ([1-9][0-9]* / "0") { 
        return {
            val: parseInt(text(), 10),
            type: 'integer'
        };
    }
