from math import sqrt
from math import cos, pi
from random import random

from single_mode.setup import Setup

# 2-D evolution eqs for the MonteCarlo rays; single mode in the x-direction
class MonteCarloRays:

    def __init__(self, setup: Setup):

        self.setup = setup

        self.phi_realizations = []
        for _ in range(self.setup.mc_num_realizations):
            self.phi_realizations.append(2 * pi * random())

        self.it = 0
        self.p = [self.setup.amplitude, self.setup.q0_vector[0], self.phi_realizations[self.it]]

    def set_phi(self, it):
        self.it = it
        self.p = [self.setup.amplitude, self.setup.q0_vector[0], self.phi_realizations[self.it]]

    # Ray tracing equations for single mode, not expanding asymptotically, thus
    # keeping the random component of the turbulence /phi to be instantiated
    # for each Monte Carlo ray (Bizarro et. al paper)
    @staticmethod
    def mc_aux_integrator_func(w, t, p):
        x, y, kx, ky = w

        dne, q, phi = p

        dxdt = kx / (1 + dne * cos(q * x + phi))

        dydt = ky / (1 + dne * cos(q * x + phi))

        dkxdt = abs(sqrt(kx ** 2 + ky ** 2)) * (-1) * \
                dne * cos(q * x + phi) / (1 + dne * cos(q * x + phi))

        dkydt = 0

        dfdt = [dxdt, dydt, dkxdt, dkydt]

        return dfdt
