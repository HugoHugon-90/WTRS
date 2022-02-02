from helpers import constants
from input_handlers.single_mode_input_handler import SingleModeInputHandler
from single_mode.single_mode_turbulence_profile import SingleModeTurbulenceProfile


class Setup(SingleModeTurbulenceProfile):

    def __init__(self, input_params: SingleModeInputHandler):

        super().__init__(input_params.amp, [input_params.q0x, input_params.q0y])

        self.plot_trajectory = input_params.plot_trajectory

        self.stop_time = input_params.stop_time
        self.num_points = input_params.num_points

        self.amplitude = input_params.amp
        self.q0_vector = [input_params.q0x, input_params.q0y]

        self.mc_file_name = input_params.file_name_mc
        self.mc_is_active = input_params.monte_carlo_is_active
        self.mc_num_realizations = input_params.monte_carlo_num_realizations

        self.k0_angle = input_params.k0_angle
        self.kx0 = input_params.k0x
        self.ky0 = input_params.k0y
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

        self.turbulence_profile = SingleModeTurbulenceProfile(input_params.amp, [input_params.q0x, input_params.q0y])
        self.dnedne = self.turbulence_profile.dnedne()
        self.dnednedx = self.dnednedx()
        self.dnedxdnedx = self.dnedxdnedx()

        self.w = self.x0, self.y0, self.kx0, self.ky0, self.dxdx0, \
                 self.dxdy0, self.dydy0, self.dxdkx0, self.dxdky0, self.dydkx0, \
                 self.dydky0, self.dkxdkx0, self.dkxdky0, self.dkydky0, self.dxdne, self.dydne, \
                 self.dkxdne, self.dkydne, self.dxdnedx, self.dydnedx, self.dkxdnedx, self.dkydnedx

        self.w_mc = self.x0, self.y0, self.kx0, self.ky0

        self.num_points = input_params.num_points
        self.abs_err = input_params.abs_err
        self.rel_err = input_params.rel_err
        self.stop_time = input_params.stop_time

        self.file_name = input_params.file_name

        self.plot_params = input_params.plot_params