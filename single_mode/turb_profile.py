from cmath import cos
from cmath import pi
from scipy import rand


# single mode density fluctuation turbulence profile in the x direction
# dne = dne0 Cos (q.x + phi)

class Turb_Profile:

    def __init__(self, dne0, q):
        self.dne0 = dne0
        self.q = q

    # profile
    def dne_profile(self, x):
        return self.dne0 * cos(self.q * x + rand(0, 2 * pi))

    # source terms
    # Eq.(42)
    # literal integration of <dnedne>, <dnednedx> and <ddnedx ddnedx> over [0,2Pi] using the single mode profile

    def dnedne(self):
        return self.dne0 ** 2 / 2

    def dnednedx(self):
        return 0

    def dnedxdnedx(self):
        return self.q ** 2 * self.dnedne()
