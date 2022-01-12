#2-D evolution eqs for the average rays

class Average_Ray_Equations:

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




