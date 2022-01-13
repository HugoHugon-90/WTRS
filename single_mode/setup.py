from helpers import constants
from single_mode import input_parameters
from single_mode.turbprofile import TurbProfile


class Setup(TurbProfile):

    def __init__(self):
        super().__init__(input_parameters.dne0, input_parameters.q0)

        self.input_type = input_parameters.input_type

        if self.input_type == "parallel":
            self.kx0 = constants.k0_par[0]
            self.ky0 = constants.k0_par[1]

        elif self.input_type == "perpendicular":
            self.kx0 = constants.k0_perp[0]
            self.ky0 = constants.k0_perp[1]

        elif self.input_type == "oblique":
            self.kx0 = constants.k0_obl[0]
            self.ky0 = constants.k0_obl[1]

        else:
            self.kx0 = input_parameters.k0[0]
            self.ky0 = input_parameters.k0[1]

        self.x0 = input_parameters.r0[0]
        self.y0 = input_parameters.r0[1]
        self.dx0 = input_parameters.dx0
        self.dy0 = input_parameters.dy0
        self.dkx0 = input_parameters.dkx0
        self.dky0 = input_parameters.dky0
        self.dxdx0 = input_parameters.dxdx0
        self.dxdy0 = input_parameters.dxdy0
        self.dydy0 = input_parameters.dydy0
        self.dxdkx0 = input_parameters.dxdkx0
        self.dxdky0 = input_parameters.dxdky0
        self.dydkx0 = input_parameters.dydkx0
        self.dydky0 = input_parameters.dydky0
        self.dkxdkx0 = input_parameters.dkxdkx0
        self.dkxdky0 = input_parameters.dkxdky0
        self.dkydky0 = input_parameters.dkydky0
        self.dxdne = input_parameters.dxdne
        self.dydne = input_parameters.dydne
        self.dkxdne = input_parameters.dkxdne
        self.dkydne = input_parameters.dkydne
        self.dxdnedx = input_parameters.dxdnedx
        self.dydnedx = input_parameters.dydnedx
        self.dkxdnedx = input_parameters.dkxdnedx
        self.dkydnedx = input_parameters.dkydnedx

        self.n_profile = TurbProfile(input_parameters.dne0, input_parameters.q0)
        self.dnedne = self.n_profile.dnedne()
        self.dnednedx = self.dnednedx()
        self.dnedxdnedx = self.dnedxdnedx()

        self.w = self.x0, self.y0, self.kx0, self.ky0, self.dxdx0, self.dxdy0, self.dydy0, self.dxdkx0, self.dxdky0, self.dydkx0, \
                 self.dydky0, self.dkxdkx0, self.dkxdky0, self.dkydky0, self.dxdne, self.dydne, \
                 self.dkxdne, self.dkydne, self.dxdnedx, self.dydnedx, self.dkxdnedx, self.dkydnedx


        self.num_points = input_parameters.num_points
        self.window = input_parameters.window
        self.abserr = input_parameters.abserr
        self.relerr = input_parameters.relerr
        self.stop_time = input_parameters.stop_time
        self.file_name = input_parameters.file_name