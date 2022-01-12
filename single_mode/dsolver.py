from single_mode.average_rays import Average_Rays
from scipy.integrate import odeint


# Solver for system of coupled 1st-order differential equations
# https://scipy-cookbook.readthedocs.io/items/CoupledSpringMassSystem.html
# https://apmonitor.com/pdc/index.php/Main/SolveDifferentialEquations
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html


class Dsolver(Average_Rays):

    def vectorfield(self, w, t, p):

        """
        Arguments:
            w :  vector of the state variables
            t :  time
        """
        x, y, kx, ky, dx, dy, dkx, dky,  dxdx, dxdy, dydy, dkxdkx, dkxdky, dkydky, dxdne, dydne, dkxdne, dkydne, dxdnedr, dydnedr, dnedne = w

        dxdt = self.dxdt(w)

        dfdt = [dxdt]
        return dfdt

    odeint()
