import sys
import pprint
from trygrammar import parser

if __name__ == "__main__":
    pp = pprint.PrettyPrinter()
    block = False
    if len(sys.argv) > 1:
        result = parser(sys.argv[1])
        pp.pprint(result)
        block = True

    body = input("Please enter an expression to pass\n") if not block else ".exit"
    while body != ".exit":
        try:
            result = parser(body)
            pp.pprint(result)
            body = input("Please enter an expression to pass\n")
        except:
            print("Could not parse")
            body = input("Please enter an expression to pass\n")