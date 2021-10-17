import re
import sys

class operators(object):
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        return x / y


o = operators()
omap = {
    '+': (lambda x,y: o.add(x, y)),
    '-': (lambda x,y: o.sub(x, y)),
    '*': (lambda x,y: o.mul(x, y)),
    '/': (lambda x,y: o.div(x, y)),
     }

def solve_term(tokens):
    tokens = re.split('(/|\*)', tokens)
    ret = float(tokens[0])
    for op, num in zip(tokens[1::2], tokens[2::2]):
        num = float(num)
        if op == '*':
            ret = omap['*'](ret, num)
        else:
            ret = omap['/'](ret,  num)
    return ret

def main(args):
    # remove whitespaces
    tokens = re.sub('\s+', '', args)

    # split by addition/subtraction operators
    tokens = re.split('(-|\+)', tokens)

    result = solve_term(tokens[0])

    for op, num in zip(tokens[1::2], tokens[2::2]):
        num = float(num)
        if op == '+':
            result = omap['+'](result, num)
        else:
            result = omap['-'](result, num)

    print result


if __name__ == "__main__":
    main(''.join(sys.argv[1:]))
