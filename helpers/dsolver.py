from single_mode.averagerays import AverageRays
from scipy.integrate import odeint


# Solver for system of coupled 1st-order differential equations
# https://scipy-cookbook.readthedocs.io/items/CoupledSpringMassSystem.html
# https://apmonitor.com/pdc/index.php/Main/SolveDifferentialEquations
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html


class Dsolver(AverageRays):

    def __init__(self):
        super().__init__()

    def integrator(self):
        t = [ self.stop_time * float(i) / (self.num_points - 1) for i in range(self.num_points) ]

        p=[]
        wsol = odeint(self.partial_derivatives(), self.w, t, tfirst = True  ,atol=self.abserr, rtol=self.relerr)

        with open(self.file_name, 'w') as f:
            # Print & save the solution.
            for t1, w1 in zip(t, wsol):
                print(f'{t1} \t {w1[0]}', file=f)

        return wsol
