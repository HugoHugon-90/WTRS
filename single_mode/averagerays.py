from cmath import sqrt
from single_mode.setup import Setup


# 2-D evolution eqs for the average rays; single mode in the x-direction

class AverageRays(Setup):

    def __init__(self):
        super().__init__()

    def partial_derivatives(self):

        x, y, kx, ky, dx, dy, dkx, dky, dxdx, dxdy, dydy, dxdkx, dxdky, dydkx, dydky, \
        dkxdkx, dkxdky, dkydky, dxdne, dydne, dkxdne, dkydne, dxdnedx, dydnedx, \
        dkxdnedx, dkydnedx, dnedne, dnedxdnedx = self.w

        k = sqrt(kx ** 2 + ky ** 2)
        k3 = k ** 3
        k5 = k ** 5
        ky2 = ky ** 2
        kx2 = kx ** 2
        A = self.dne0 ** 2 / 2
        q = self.q
        q2 = q ** 2

        # Eqs. (B1)
        dxdt = kx * (1 + A) / k \
               + (3 / 2) * kx * (kx2 * dkxdkx + ky2 * dkydky + 2 * kx * ky * dkxdky) / k5 \
               - (kx * (dkxdkx + dkydky) + 2 * (kx * dkxdkx + ky * dkxdky)) / (2 * k3) \
               - dkxdne / k \
               + kx * (kx * dkxdne + ky * dkydne) / k3 \
               - (kx / k) * dxdnedx

        dydt = ky * (1 + A) / k \
               + (3 / 2) * ky * (kx2 * dkxdkx + ky2 * dkydky + 2 * kx * ky * dkxdky) / k5 \
               + (ky * (dkxdkx + dkydky) + 2 * (kx * dkxdky + ky * dkydky)) / (2 * k3) \
               - dkydne / k \
               + ky * (kx * dkxdne + ky * dkydne) / k3 \
               - (ky / k) * dxdnedx

        # Eqs. (B2)
        dkxdt = (1 / k) * (kx * dkxdnedx + ky * dkydnedx) - q2 * k * dxdne

        dkydt = 0

        # Eqs. (B3)
        ddxdxdt = 2 * dxdkx / k - (2 / k3) * kx2 * dxdkx + ky * kx * dxdky - (2 / k) * kx * dxdne

        ddydydt = 2 * dydky / k - (2 / k3) * kx * ky * dydkx + ky2 * dydky - (2 / k) * ky * dydne

        ddxdydt = (1 / k) * (dxdky + dydkx) - (1 / k3) * (kx2 * dydkx + ky2 * dxdky + kx * ky * (dxdkx + dydky)) \
                  - (1 / k) * (kx * dydne + ky * dxdne)

        # Eqs. (B4)
        ddkxdkxdt = 2 * k * dkxdnedx

        ddkxdkydt = k * dkydnedx

        ddkydkydt = 0

        # Eqs. (B5)
        ddxdkxdt = (1 / k) * dkxdkx - (kx / k3) * (kx * dkxdkx + ky * dkxdky) - (1 / k) * (kx * dkxdne) + k * dxdnedx

        ddydkxdt = (1 / k) * dkxdky - (ky / k3) * (kx * dkxdkx + ky * dkxdky) - (1 / k) * (ky * dkxdne) + k * dydnedx

        ddxdkydt = (1 / k) * dkxdky - (kx / k3) * (kx * dkxdky + ky * dkydky) - (1 / k) * (kx * dkydne)

        ddydkydt = (1 / k) * dkydky - (kx / k3) * (kx * dkxdky + ky * dkydky) - (1 / k) * (ky * dkydne)

        # Eqs. (B6)
        ddxdnedt = dxdnedx * dxdt + dkxdne / k - (kx / k3) * (kx * dkxdne + ky * dkydne) - A * kx / k

        ddydnedt = dydnedx * dxdt + dkydne / k - (ky / k3) * (kx * dkxdne + ky * dkydne) - A * ky / k

        # Eqs. (B7)
        ddkxdnedt = dkxdnedx * dxdt

        ddkydnedt = dkydnedx * dxdt

        # Eqs. (B8)
        ddxdnedxdt = - q2 * dxdne * dxdt + (dkxdnedx / k) - (kx / k3) * (kx * dkxdnedx + ky * dkydnedx)

        ddydnedxdt = - q2 * dydne * dxdt + (dkydnedx / k) - (ky / k3) * (kx * dkxdnedx + ky * dkydnedx)

        # Eqs. (B9)
        ddkxdnedxdt = - q2 * dkxdne * dxdt + q2 * A * k

        ddkydnedxdt = - q2 * dkydne * dxdt

        dfdt = [dxdt, dydt, dkxdt, dkydt, ddxdxdt, ddydydt, ddxdydt, ddkxdkxdt, ddkxdkydt, ddkydkydt,
                ddxdkxdt, ddydkxdt, ddxdkydt, ddydkydt, ddxdnedt, ddydnedt, ddkxdnedt, ddkydnedt,
                ddxdnedxdt, ddydnedxdt, ddkxdnedxdt, ddkydnedxdt]

        return dfdt