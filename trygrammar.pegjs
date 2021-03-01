// Tryal

Equation = 
    L: Operation "=" R:Equation {
        return {
            lhs: L,
            rhs: R,
            symbol: "=",
            type: 'operation',
        }
    } / C: Operation { 
        return C; 
    }

Expression
    = O: (Function / AddSubtract / MultiplyDividePower / Brackets / ConstantCoeffTerm) {
        return O;
    }

Function = 
    F: UnaryFunctionSymbols "(" O: Operation ")" {
        return {
            symbol: F,
            expression: O,
            type: 'function',
        }
    }

MultiplyDividePower 
    = L: (Function / ConstantCoeffTerm / "(" O: Operation ")" { return {
        ...O,
        brackets: true,
        }; })
        S: ("*" / "/" / "^" / "") 
        R: (ConstantCoeffTerm / "(" O: Operation ")" { return { 
            ...O,
            brackets: true, 
        }; }) {
            return {
                lhs: L,
                symbol: S !== "" ? S : "x",
                rhs: R,
                type: 'operation',
            }
        }

AddSubtract = L: (MultiplyDividePower / Function / ConstantCoeffTerm) S:("+" / "-") R: Operation {
    return {
        lhs: L,
        rhs: R,
        symbol: S,
        type: 'operation',
    }
} 

Power = M: (Brackets / Function) "^" E: Expression {
    
}

Function = S: UnaryFunctionSymbols "(" E: Expression ")" {
    return {
        symbol: S,
        expression: E,
        type: 'function'
    }
}

Brackets
    = "(" E: Expression ")" {
        return {
            expression: E,
            type: 'brackets'
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
        }
    }

Constant "constant"
    = V: (Real / Integer) {
        return V;
    }


MultiVariableTerm "multi-variable term"
    = V: (GreekSymbols / Variable)+ {
        return {
            'vars': V,
            'type': 'terms'
        }

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
    = "#" S:("pi" / "epsilon" / "theta") "^" E: Expression {
        return {
            val: S,
            power: E,
            type: "greek"
        }
    } / "#" S:("pi" / "epsilon" / "theta") {
        return {
            val: S,
            type: "greek"
        }
    }

Variable = (V: [a-zA-Z] "^" E: Expression) {
        return {
            vars: V,
            power: E,
            type: 'term'
        };
    } / V:[a-zA-Z] {
        return {
            vars: V,
            type: 'term',
        }
    }


//A Real begins with an integer or a zero, followed by a decimal
Real "real"
    = ("0" / Integer) "." [0-9]+ { 
        return {
            val: parseFloat(text(), 10),
            type: 'real',
        } 
    }

//An integer is any set of digits beginning with a digit between 1-9 
Integer "integer"
    = ([1-9][0-9]* / "0") { 
        return {
            val: parseInt(text(), 10),
            type: 'integer'
        }
    }
