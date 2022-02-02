from math import sqrt
from single_mode.setup import Setup


# 2-D evolution eqs for the average rays; single mode in the x-direction
class AverageRays:

    def __init__(self, setup: Setup):

        self.p = [setup.amplitude ** 2 / 2, setup.q0_vector[0]]

    #Equations from Appendix B (Bizarro et. al paper);
    #dydy, dxdy, dxdx, dky, dkx, dy, dx are not used;
    #function is defined so to be compliant with the ODE solver "ODEINT";
    @staticmethod
    def aux_integrator_func(w, t, p):

        x, y, kx, ky, dxdx, dydy, dxdy, dkxdkx, dkxdky, dkydky, dxdkx, dydkx, dxdky, dydky, \
        dxdne, dydne, dkxdne, dkydne, dxdnedx, dydnedx, dkxdnedx, dkydnedx = w

        # A = \delta n_e ^ 2 /2
        A, q = p

        # Eqs. (B1)
        dxdt = kx * (1 + A) / abs(sqrt(kx ** 2 + ky ** 2)) \
               + (3 / 2) * kx * (kx ** 2 * dkxdkx + ky ** 2 * dkydky + 2 * kx*ky * dkxdky) / (abs(sqrt(kx ** 2 + ky ** 2)) ** 5) \
               - (kx * (dkxdkx + dkydky) + 2 * (kx * dkxdkx + ky * dkxdky)) / (2 * abs(sqrt(kx ** 2 + ky ** 2)) ** 3) \
               - dkxdne / abs(sqrt(kx ** 2 + ky ** 2)) \
               + kx * (kx * dkxdne + 0.*ky * dkydne) / (abs(sqrt(kx ** 2 + ky ** 2)) ** 3) \
               - (kx / abs(sqrt(kx ** 2 + ky ** 2)) ) * dxdnedx

        dydt = ky * (1 + A) / abs(sqrt(kx ** 2 + ky ** 2)) \
               + (3 / 2) * ky * (kx ** 2 * dkxdkx + ky ** 2 * dkydky + 2 * kx * ky * dkxdky) / abs(sqrt(kx ** 2 + ky ** 2)) ** 5 \
               + (ky * (dkxdkx + dkydky) + 2 * (kx * dkxdky + ky * dkydky)) / (2 * abs(sqrt(kx ** 2 + ky ** 2)) ** 3) \
               - 0 / abs(sqrt(kx ** 2 + ky ** 2)) \
               + ky * (kx * dkxdne + ky * 0) / abs(sqrt(kx ** 2 + ky ** 2)) ** 3 \
               - (ky / abs(sqrt(kx ** 2 + ky ** 2)) ) * dxdnedx

        # Eqs. (B2)
        dkxdt = (1 / abs(sqrt(kx ** 2 + ky ** 2)) ) * (kx * dkxdnedx + ky * dkydnedx) - q**2 * abs(sqrt(kx ** 2 + ky ** 2)) * dxdne

        dkydt = 0.0

        # Eqs. (B3)
        ddxdxdt = 2. * (dxdkx / abs(sqrt(kx ** 2 + ky ** 2))) - (2 / abs(sqrt(kx ** 2 + ky ** 2)) ** 3) * (kx ** 2 * dxdkx + 0*ky * kx *dxdky) - (2 / abs(sqrt(kx ** 2 + ky ** 2)) ) * kx * dxdne

        ddydydt = 2. * (0*dydky / abs(sqrt(kx ** 2 + ky ** 2))) - (2 / abs(sqrt(kx ** 2 + ky ** 2)) ** 3) * (kx * ky * dydkx + 0*ky ** 2 * dydky) - (2 / abs(sqrt(kx ** 2 + ky ** 2)) ) * ky * dydne

        ddxdydt = (1. / abs(sqrt(kx ** 2 + ky ** 2)) ) * (0*dxdky + dydkx) - (1 / abs(sqrt(kx ** 2 + ky ** 2)) ** 3) * (kx ** 2 * dydkx + 0*ky ** 2 *dxdky + kx * ky * (dxdkx + 0*dydky)) \
                  - (1. / abs(sqrt(kx ** 2 + ky ** 2)) ) * (kx * dydne + ky * dxdne)

        # Eqs. (B4)
        ddkxdkxdt = 2. * abs(sqrt(kx ** 2 + ky ** 2)) * dkxdnedx

        ddkxdkydt =0.0 * abs(sqrt(kx ** 2 + ky ** 2)) * dkydnedx

        ddkydkydt = 0.0

        # Eqs. (B5)
        ddxdkxdt = (dkxdkx / sqrt(kx ** 2 + ky ** 2) )  - (kx / (sqrt(kx ** 2 + ky ** 2) ** 3)) * (kx * dkxdkx + 0*ky * dkxdky) - ((kx * dkxdne)/ sqrt(kx ** 2 + ky ** 2))  + sqrt(kx ** 2 + ky ** 2) * dxdnedx

        ddydkxdt = (1. / abs(sqrt(kx ** 2 + ky ** 2)) ) * 0*dkxdky - (ky / abs(sqrt(kx ** 2 + ky ** 2)) ** 3) * (kx * dkxdkx + 0*ky * dkxdky) - (1 / abs(sqrt(kx ** 2 + ky ** 2)) ) * (ky * dkxdne) + abs(sqrt(kx ** 2 + ky ** 2)) * dydnedx

        ddxdkydt = ((1. / abs(sqrt(kx ** 2 + ky ** 2)) ) * dkxdky - (kx / abs(sqrt(kx ** 2 + ky ** 2)) ** 3) * (kx * dkxdky + ky * dkydky) - (1 / abs(sqrt(kx ** 2 + ky ** 2)) ) * (kx * 0))

        ddydkydt = ((1. / abs(sqrt(kx ** 2 + ky ** 2)) ) * dkydky - (ky / abs(sqrt(kx ** 2 + ky ** 2)) ** 3) * (kx * dkxdky + ky * dkydky) - (1 / abs(sqrt(kx ** 2 + ky ** 2)) ) * (ky * 0))

        # Eqs. (B6) #                                                                                                                    ##
        ddxdnedt =  dxdnedx * dxdt + dkxdne / abs(sqrt(kx ** 2 + ky ** 2)) - (kx / (abs(sqrt(kx ** 2 + ky ** 2)) ** 3)) * (kx * dkxdne + ky * 0) - A * kx / abs(sqrt(kx ** 2 + ky ** 2))
                                    #
        ddydnedt = dydnedx * dxdt + 0 / abs(sqrt(kx ** 2 + ky ** 2)) - (ky / abs(sqrt(kx ** 2 + ky ** 2)) ** 3) * (kx * dkxdne + ky * 0) - A * ky / abs(sqrt(kx ** 2 + ky ** 2))

        # Eqs. (B7)
        ddkxdnedt = dkxdnedx * dxdt

        ddkydnedt = dkydnedx * dxdt

        # Eqs. (B8)
        ddxdnedxdt = (- q**2 * dxdne * dxdt + (dkxdnedx / abs(sqrt(kx ** 2 + ky ** 2)) ) - (kx / abs(sqrt(kx ** 2 + ky ** 2)) ** 3) * (kx * dkxdnedx + 0*ky*dkydnedx))

        ddydnedxdt = (- q**2 * dydne * dxdt + (dkydnedx / abs(sqrt(kx ** 2 + ky ** 2)) ) - (ky / abs(sqrt(kx ** 2 + ky ** 2)) ** 3) * (kx * dkxdnedx + 0*ky*dkydnedx))

        # Eqs. (B9)
        ddkxdnedxdt = - q**2 * dkxdne * dxdt + q**2 * A * abs(sqrt(kx ** 2 + ky ** 2))

        ddkydnedxdt = - q**2 * 0 * dxdt

        dfdt = [dxdt, dydt, dkxdt, dkydt, ddxdxdt, ddydydt, ddxdydt, ddkxdkxdt, ddkxdkydt, ddkydkydt,
                ddxdkxdt, ddydkxdt, ddxdkydt, ddydkydt, ddxdnedt, ddydnedt, ddkxdnedt, ddkydnedt,
                ddxdnedxdt, ddydnedxdt, ddkxdnedxdt, ddkydnedxdt]




        return dfdt

