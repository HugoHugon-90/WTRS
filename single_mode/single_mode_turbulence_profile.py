from math import cos, sin
from profiles.turbulence_profile import TurbulenceProfile


# single mode density fluctuation turbulence profile in the x direction
# dne = dne0 Cos (q.x + phi)
class SingleModeTurbulenceProfile(TurbulenceProfile):

    # turbulence profile ( 0 < = phi < = 2Pi )
    def profile(self, x, y, phi):
        return self.amplitude * cos(self.q_vector[0] * x + phi)

    def d_profile_dx(self, x, y, phi):
        return - self.amplitude * self.q_vector[0]* sin(self.q_vector[0] * x + phi)

    # source terms
    # Eq.(42)
    # literal integration of <dnedne>, <dnednedx> and <ddnedx ddnedx> over [0,2Pi] using the single mode profile
    def dnedne(self):
        return (self.amplitude ** 2) / 2

    def dnednedx(self):
        return 0

    def dnedxdnedx(self):
        return (self.q_vector[0] ** 2) * (self.amplitude ** 2) / 2
