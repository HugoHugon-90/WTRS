from cmath import cos
from cmath import pi
from scipy import rand
from profiles.turbulence_profile import TurbulenceProfile


# single mode density fluctuation turbulence profile in the x direction
# dne = dne0 Cos (q.x + phi)
class SingleModeTurbulenceProfile(TurbulenceProfile):

    def __init__(self, dne0, q_vector):
        self.dne0 = dne0
        self.q_vector = q_vector

        super().__init__(self.dne0, self.q_vector)

    # turbulence profile ( 0 < = phi < = 2Pi )
    def profile(self, x, y, phi):
        return self.dne0 * cos(self.q_vector[0] * x + rand(0, 2 * pi))

    # source terms
    # Eq.(42)
    # literal integration of <dnedne>, <dnednedx> and <ddnedx ddnedx> over [0,2Pi] using the single mode profile
    def dnedne(self):
        return (self.dne0 ** 2) / 2

    def dnednedx(self):
        return 0

    def dnedxdnedx(self):
        return (self.q_vector[0] ** 2) * (self.dne0 ** 2) / 2
