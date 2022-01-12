from cmath import sqrt

from single_mode.average_rays import Average_Ray_Equations

from scipy.integrate import odeint


# Solver for system of coupled 1st-order differential equations
# https://scipy-cookbook.readthedocs.io/items/CoupledSpringMassSystem.html
# https://apmonitor.com/pdc/index.php/Main/SolveDifferentialEquations
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html


class Dsolver(Average_Ray_Equations):

    def vectorfield(w, t, p):

        """
        Arguments:
            w :  vector of the state variables
            t :  time
            p :  vector of the parameters

        """
        x, y, kx, ky, dx, dy, dkx, dky,  dxdx, dxdy, dydy, dkxdkx, dkxdky, dkydky, dxdne, dydne, dkxdne, dkydne, dxdnedr, dydnedr, dnedne = w

        k = sqrt(kx ** 2 + ky ** 2)
        k3 = k ** 3
        k5 = k ** 5
        ky2 = ky ** 2
        ky3 = ky ** 3
        kx2 = kx ** 2
        kx3 = kx ** 3

        #Eq. A1 with <ne> = 1
        dxdt = kx / k + (3/2) * ( kx * ky2 * dkydky + 2* kx * ky * dkxdky + kx3 * dkxdkx ) / k5
        - ( (3/2)( kx * dkxdkx ) + (1/2) * ( kx * dkydky + 2 * ky * dkxdky ) ) / k3
        - dkxdne / k + (kx2 * dkxdne + kx * ky * dkydne) / k3
        - (kx / k) (dxdnedr + dydnedr) - kx * dnedne / k

        #TODO: Finish writing all the partial equations

        dfdt = [dxdt]
        return dfdt

    odeint()
