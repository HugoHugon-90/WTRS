from cmath import sqrt
from single_mode.setup import Setup


# 2-D evolution eqs for the average rays; single mode in the x-direction
class AverageRays(Setup):

    def __init__(self):

        super().__init__()

        self.p = [self.amplitude ** 2 / 2, self.q_vector[0]]

    #Equations from Appendix B (Bizarro et. al paper);
    #dydy, dxdy, dxdx, dky, dkx, dy, dx are not used;
    #function is defined so to be compliant with the ODE solver "ODEINT";
    @staticmethod
    def aux_integrator_func(w, t, p):

        x, y, kx, ky, dxdx, dxdy, dydy, dxdkx, dxdky, dydkx, dydky, dkxdkx, dkxdky, dkydky, \
        dxdne, dydne, dkxdne, dkydne, dxdnedx, dydnedx, dkxdnedx, dkydnedx = w

        # A = \delta n_e ^ 2 /2
        A, q = p

        # Eqs. (B1)
        dxdt = kx * (1 + A) / abs(sqrt(kx ** 2 + ky ** 2)) \
               + (3 / 2) * kx * (kx ** 2 * dkxdkx + ky ** 2 * dkydky + 2 * kx * ky * dkxdky) / abs(sqrt(kx ** 2 + ky ** 2)) ** 5 \
               - (kx * (dkxdkx + dkydky) + 2 * (kx * dkxdkx + ky * dkxdky)) / (2 * abs(sqrt(kx ** 2 + ky ** 2)) ** 3) \
               - dkxdne / abs(sqrt(kx ** 2 + ky ** 2)) \
               + kx * (kx * dkxdne + ky * dkydne) / abs(sqrt(kx ** 2 + ky ** 2)) ** 3 \
               - (kx / abs(sqrt(kx ** 2 + ky ** 2)) ) * dxdnedx

        dydt = ky * (1 + A) / abs(sqrt(kx ** 2 + ky ** 2)) \
               + (3 / 2) * ky * (kx ** 2 * dkxdkx + ky ** 2 * dkydky + 2 * kx * ky * dkxdky) / abs(sqrt(kx ** 2 + ky ** 2)) ** 5 \
               + (ky * (dkxdkx + dkydky) + 2 * (kx * dkxdky + ky * dkydky)) / (2 * abs(sqrt(kx ** 2 + ky ** 2)) ** 3) \
               - dkydne / abs(sqrt(kx ** 2 + ky ** 2)) \
               + ky * (kx * dkxdne + ky * dkydne) / abs(sqrt(kx ** 2 + ky ** 2)) ** 3 \
               - (ky / abs(sqrt(kx ** 2 + ky ** 2)) ) * dxdnedx

        # Eqs. (B2)
        dkxdt = (1 / abs(sqrt(kx ** 2 + ky ** 2)) ) * (kx * dkxdnedx + ky * dkydnedx) - q**2 * abs(sqrt(kx ** 2 + ky ** 2)) * dxdne

        dkydt = 0

        # Eqs. (B3)
        ddxdxdt = 2 * dxdkx / abs(sqrt(kx ** 2 + ky ** 2)) - (2 / abs(sqrt(kx ** 2 + ky ** 2)) ** 3) * kx ** 2 * dxdkx + ky * kx * dxdky - (2 / abs(sqrt(kx ** 2 + ky ** 2)) ) * kx * dxdne

        ddydydt = 2 * dydky / abs(sqrt(kx ** 2 + ky ** 2)) - (2 / abs(sqrt(kx ** 2 + ky ** 2)) ** 3) * kx * ky * dydkx + ky ** 2 * dydky - (2 / abs(sqrt(kx ** 2 + ky ** 2)) ) * ky * dydne

        ddxdydt = (1 / abs(sqrt(kx ** 2 + ky ** 2)) ) * (dxdky + dydkx) - (1 / abs(sqrt(kx ** 2 + ky ** 2)) ** 3) * (kx ** 2 * dydkx + ky ** 2 * dxdky + kx * ky * (dxdkx + dydky)) \
                  - (1 / abs(sqrt(kx ** 2 + ky ** 2)) ) * (kx * dydne + ky * dxdne)

        # Eqs. (B4)
        ddkxdkxdt = 2 * abs(sqrt(kx ** 2 + ky ** 2)) * dkxdnedx

        ddkxdkydt = abs(sqrt(kx ** 2 + ky ** 2)) * dkydnedx

        ddkydkydt = 0

        # Eqs. (B5)
        ddxdkxdt = (1 / abs(sqrt(kx ** 2 + ky ** 2)) ) * dkxdkx - (kx / abs(sqrt(kx ** 2 + ky ** 2)) ** 3) * (kx * dkxdkx + ky * dkxdky) - (1 / abs(sqrt(kx ** 2 + ky ** 2)) ) * (kx * dkxdne) + abs(sqrt(kx ** 2 + ky ** 2)) * dxdnedx

        ddydkxdt = (1 / abs(sqrt(kx ** 2 + ky ** 2)) ) * dkxdky - (ky / abs(sqrt(kx ** 2 + ky ** 2)) ** 3) * (kx * dkxdkx + ky * dkxdky) - (1 / abs(sqrt(kx ** 2 + ky ** 2)) ) * (ky * dkxdne) + abs(sqrt(kx ** 2 + ky ** 2)) * dydnedx

        ddxdkydt = (1 / abs(sqrt(kx ** 2 + ky ** 2)) ) * dkxdky - (kx / abs(sqrt(kx ** 2 + ky ** 2)) ** 3) * (kx * dkxdky + ky * dkydky) - (1 / abs(sqrt(kx ** 2 + ky ** 2)) ) * (kx * dkydne)

        ddydkydt = (1 / abs(sqrt(kx ** 2 + ky ** 2)) ) * dkydky - (kx / abs(sqrt(kx ** 2 + ky ** 2)) ** 3) * (kx * dkxdky + ky * dkydky) - (1 / abs(sqrt(kx ** 2 + ky ** 2)) ) * (ky * dkydne)

        # Eqs. (B6)
        ddxdnedt = dxdnedx * dxdt + dkxdne / abs(sqrt(kx ** 2 + ky ** 2)) - (kx / abs(sqrt(kx ** 2 + ky ** 2)) ** 3) * (kx * dkxdne + ky * dkydne) - A * kx / abs(sqrt(kx ** 2 + ky ** 2))

        ddydnedt = dydnedx * dxdt + dkydne / abs(sqrt(kx ** 2 + ky ** 2)) - (ky / abs(sqrt(kx ** 2 + ky ** 2)) ** 3) * (kx * dkxdne + ky * dkydne) - A * ky / abs(sqrt(kx ** 2 + ky ** 2))

        # Eqs. (B7)
        ddkxdnedt = dkxdnedx * dxdt

        ddkydnedt = dkydnedx * dxdt

        # Eqs. (B8)
        ddxdnedxdt = - q**2 * dxdne * dxdt + (dkxdnedx / abs(sqrt(kx ** 2 + ky ** 2)) ) - (kx / abs(sqrt(kx ** 2 + ky ** 2)) ** 3) * (kx * dkxdnedx + ky * dkydnedx)

        ddydnedxdt = - q**2 * dydne * dxdt + (dkydnedx / abs(sqrt(kx ** 2 + ky ** 2)) ) - (ky / abs(sqrt(kx ** 2 + ky ** 2)) ** 3) * (kx * dkxdnedx + ky * dkydnedx)

        # Eqs. (B9)
        ddkxdnedxdt = - q**2 * dkxdne * dxdt + q**2 * A * abs(sqrt(kx ** 2 + ky ** 2))

        ddkydnedxdt = - q**2 * dkydne * dxdt

        dfdt = [dxdt, dydt, dkxdt, dkydt, ddxdxdt, ddydydt, ddxdydt, ddkxdkxdt, ddkxdkydt, ddkydkydt,
                ddxdkxdt, ddydkxdt, ddxdkydt, ddydkydt, ddxdnedt, ddydnedt, ddkxdnedt, ddkydnedt,
                ddxdnedxdt, ddydnedxdt, ddkxdnedxdt, ddkydnedxdt]

        return dfdt

