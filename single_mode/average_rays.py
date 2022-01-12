#2-D evolution eqs for the average rays
from cmath import sqrt


class Average_Rays:

    def __init__(self, x0, y0, kx0, ky0, dx0, dy0, dkx0, dky0, dxdx0, dxdy0, dydy0, dkxdkx0, dkxdky0, dkydky0, dxdne, dydne, dkxdne, dkydne, dxdnedr, dydnedr, dnedne, t):

        self.x0 = x0
        self.y0 = x0
        self.kx0 = kx0
        self.ky0 = ky0
        self.dx0 = dx0
        self.dy0 = dy0
        self.dkx0 = dkx0
        self.dky0 = dky0
        self.dxdx0 = dxdx0
        self.dxdy0 = dxdy0
        self.dydy0 = dydy0
        self.dkxdkx0 = dkxdkx0
        self.dkxdky0 = dkxdky0
        self.dkydky0 = dkydky0
        self.dxdne = dxdne
        self.dydne = dydne
        self.dkxdne = dkxdne
        self.dkydne = dkydne
        self.dxdnedr = dxdnedr
        self.dydnedr = dydnedr
        self.dnedne = dnedne
        self.t = t
        self.w = x0, y0, kx0, ky0, dx0, dy0, dkx0, dky0, dxdx0, dxdy0, dydy0, dkxdkx0, dkxdky0, dkydky0, dxdne, dydne, dkxdne, dkydne, dxdnedr, dydnedr, dnedne



    def dxdt(self, w):

        x, y, kx, ky, dx, dy, dkx, dky,  dxdx, dxdy, dydy, dkxdkx, dkxdky, dkydky, dxdne, dydne, dkxdne, dkydne, dxdnedr, dydnedr, dnedne = w

        k = sqrt(kx ** 2 + ky ** 2)
        k3 = k ** 3
        k5 = k ** 5
        ky2 = ky ** 2
        ky3 = ky ** 3
        kx2 = kx ** 2
        kx3 = kx ** 3

        #Eq. A1 with <ne> = 1
        dxdt = kx / k \
               + (3/2) * ( kx * ky2 * dkydky + 2* kx * ky * dkxdky + kx3 * dkxdkx ) / k5 \
               - ( (3/2)*( kx * dkxdkx ) + (1/2) * ( kx * dkydky + 2 * ky * dkxdky ) ) / k3 \
               - dkxdne / k \
               + (kx2 * dkxdne + kx * ky * dkydne) / k3 \
               - (kx / k) (dxdnedr + dydnedr) \
               - kx * dnedne / k

        return dxdt

        #TODO: Finish writing all the partial equations
