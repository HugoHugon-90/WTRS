import sympy as sym
from helpers.dsolver import Dsolver

x = sym.symbols('x')

def run():
    dsolver = Dsolver()
    dsolver.integrator()

if __name__ == '__main__':
    run()