from helpers import constants as c
import sympy as sym

x = sym.symbols('x')

def run():
    print(c.c)
    print(sym.diff(x**3))

if __name__ == '__main__':
    run()