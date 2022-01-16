from helpers import constants
from single_mode.input_parameters import InputParameters
from single_mode.single_mode_turbulence_profile import SingleModeTurbulenceProfile


class Setup(SingleModeTurbulenceProfile):

    def __init__(self):
        super().__init__(InputParameters.dne0, InputParameters.q0)

        self.input_type = InputParameters.input_type

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
            self.kx0 = InputParameters.k0[0]
            self.ky0 = InputParameters.k0[1]

        self.x0 = constants.r0[0]
        self.y0 = constants.r0[1]
        self.dx0 = constants.dx0
        self.dy0 = constants.dy0
        self.dkx0 = constants.dkx0
        self.dky0 = constants.dky0
        self.dxdx0 = constants.dxdx0
        self.dxdy0 = constants.dxdy0
        self.dydy0 = constants.dydy0
        self.dxdkx0 = constants.dxdkx0
        self.dxdky0 = constants.dxdky0
        self.dydkx0 = constants.dydkx0
        self.dydky0 = constants.dydky0
        self.dkxdkx0 = constants.dkxdkx0
        self.dkxdky0 = constants.dkxdky0
        self.dkydky0 = constants.dkydky0
        self.dxdne = constants.dxdne
        self.dydne = constants.dydne
        self.dkxdne = constants.dkxdne
        self.dkydne = constants.dkydne
        self.dxdnedx = constants.dxdnedx
        self.dydnedx = constants.dydnedx
        self.dkxdnedx = constants.dkxdnedx
        self.dkydnedx = constants.dkydnedx

        self.turbulence_profile = SingleModeTurbulenceProfile(InputParameters.dne0, InputParameters.q0)
        self.dnedne = self.turbulence_profile.dnedne()
        self.dnednedx = self.dnednedx()
        self.dnedxdnedx = self.dnedxdnedx()

        self.w = self.x0, self.y0, self.kx0, self.ky0, self.dxdx0, self.dxdy0, self.dydy0, self.dxdkx0, self.dxdky0, self.dydkx0, \
                 self.dydky0, self.dkxdkx0, self.dkxdky0, self.dkydky0, self.dxdne, self.dydne, \
                 self.dkxdne, self.dkydne, self.dxdnedx, self.dydnedx, self.dkxdnedx, self.dkydnedx

        self.num_points = InputParameters.num_points
        self.abs_err = InputParameters.abs_err
        self.rel_err = InputParameters.rel_err
        self.stop_time = InputParameters.stop_time
        self.file_name = InputParameters.file_name
