import math as math

import errors.helpers as err_h
import errors.input_json_errors as input_err
import helpers.constants as const
from helpers.json_handler import JsonHandler


class SingleModeInputHandler(JsonHandler):

    def __init__(self, json_file):

        self.input_configuration = None
        self.k0_angle = None
        self.k0x = None
        self.k0y = None
        self.amp = None
        self.q0x = None
        self.q0y = None
        self.file_name = f'{const.output_location}/file.txt'
        self.num_points = 10000
        self.stop_time = 1000.0
        self.abs_err = 1.0e-8
        self.rel_err = 1.0e-6
        self.plot_params = []

        super().__init__(json_file)

        for k in const.single_mode_json_input_mandatory_key_list:
            if k not in self.keys:
                raise input_err.FieldNotFoundError(k)

            if k == 'ray_params':

                if 'input_configuration' in list(dict(self.json_data['ray_params']).keys()) \
                        and str(self.json_data['ray_params']['input_configuration']).replace(" ", "") != '':

                    input_configuration = self.json_data['ray_params']['input_configuration']

                    err_h.ErrorHelpers.check_type_error(input_configuration, str)

                    if str(input_configuration).replace(" ", "").lower() not in \
                            const.single_mode_input_configuration_reserved_words:
                        raise input_err.WrongInputConfigurationError(input_configuration)

                    self.input_configuration = str(input_configuration).replace(" ", "").lower()

                    if self.input_configuration == "parallel":
                        self.k0x = 1
                        self.k0y = 0
                        self.k0_angle = 0.0
                    elif self.input_configuration == "oblique":
                        self.k0x = 1 / abs(math.sqrt(2))
                        self.k0y = 1 / abs(math.sqrt(2))
                        self.k0_angle = 45.0
                    elif self.input_configuration == "perpendicular":
                        self.k0x = 0
                        self.k0y = 1
                        self.k0_angle = 90.0

                elif 'k0_angle_degrees' in list(dict(self.json_data['ray_params']).keys()):

                    self.k0_angle = self.json_data['ray_params']['k0_angle_degrees']
                    err_h.ErrorHelpers.check_type_error(self.k0_angle, float)

                    self.k0x = math.cos(self.k0_angle * math.pi / 180)
                    self.k0y = math.sin(self.k0_angle * math.pi / 180)

                else:
                    raise input_err.WrongRayParamsError()

                self.file_name = f"{const.output_location}/k0_angle_{self.k0_angle}_deg.txt"

                if 'turbulence_amplitude' in list(dict(self.json_data['ray_params']).keys()):

                    turb_amp = self.json_data['ray_params']['turbulence_amplitude']

                    err_h.ErrorHelpers.check_type_error(turb_amp, float)

                    if turb_amp < 0 or turb_amp > 0.15:
                        raise input_err.TurbAmpIllDefinedError()

                    self.amp = turb_amp

                else:
                    input_err.FieldNotFoundError('turbulence_amplitude', 'ray_params')

                if 'turbulence_wavenumber' in list(dict(self.json_data['ray_params']).keys()):

                    q0_list = list(dict(self.json_data['ray_params']['turbulence_wavenumber']).keys())

                    if "q0x" not in q0_list:
                        raise input_err.FieldNotFoundError("q0x", "turbulence_wavenumber")

                    if "q0y" not in q0_list:
                        raise input_err.FieldNotFoundError("q0y", "turbulence_wavenumber")

                    for q0 in self.json_data['ray_params']['turbulence_wavenumber'].values():
                        err_h.ErrorHelpers.check_type_error(q0, float)

                    self.q0x = self.json_data['ray_params']['turbulence_wavenumber']['q0x']
                    self.q0y = self.json_data['ray_params']['turbulence_wavenumber']['q0y']

                else:
                    input_err.FieldNotFoundError('turbulence_wavenumber', 'ray_params')

            if k == 'integrator_params':
                integ_keys = list(dict(self.json_data['integrator_params']).keys())

                if 'num_points' in integ_keys:
                    np = self.json_data['integrator_params']['num_points']
                    err_h.ErrorHelpers.check_type_error(np, int)
                    self.num_points = np

                if 'stop_time' in integ_keys:
                    st = self.json_data['integrator_params']['stop_time']
                    err_h.ErrorHelpers.check_type_error(st, float)
                    self.stop_time = st

                if 'abs_err' in integ_keys:
                    ae = self.json_data['integrator_params']['abs_err']
                    err_h.ErrorHelpers.check_type_error(ae, float)
                    self.abs_err = ae

                if 'rel_err' in integ_keys:
                    re = self.json_data['integrator_params']['rel_err']
                    err_h.ErrorHelpers.check_type_error(re, float)
                    self.rel_err = re

            if k == 'quantities_to_plot':
                plot_keys = list(dict(self.json_data['quantities_to_plot']).keys())

                if 'x' in plot_keys:
                    xp = self.json_data['quantities_to_plot']['x']
                    err_h.ErrorHelpers.check_type_error(xp, bool)
                    if xp:
                        self.plot_params.append('x')

                if 'y' in plot_keys:
                    yp = self.json_data['quantities_to_plot']['y']
                    err_h.ErrorHelpers.check_type_error(yp, bool)
                    if yp:
                        self.plot_params.append('y')

                if 'kx' in plot_keys:
                    kxp = self.json_data['quantities_to_plot']['kx']
                    err_h.ErrorHelpers.check_type_error(kxp, bool)
                    if kxp:
                        self.plot_params.append('kx')

                if 'ky' in plot_keys:
                    kyp = self.json_data['quantities_to_plot']['ky']
                    err_h.ErrorHelpers.check_type_error(kyp, bool)
                    if kyp == True:
                        self.plot_params.append('ky')

                if 'dxdx' in plot_keys:
                    dxdxp = self.json_data['quantities_to_plot']['dxdx']
                    err_h.ErrorHelpers.check_type_error(dxdxp, bool)
                    if dxdxp == True:
                        self.plot_params.append('dxdx')

                if 'dxdy' in plot_keys:
                    dxdyp = self.json_data['quantities_to_plot']['dxdy']
                    err_h.ErrorHelpers.check_type_error(dxdyp, bool)
                    if dxdyp == True:
                        self.plot_params.append('dxdy')

                if 'dydy' in plot_keys:
                    dydyp = self.json_data['quantities_to_plot']['dydy']
                    err_h.ErrorHelpers.check_type_error(dydyp, bool)
                    if dydyp == True:
                        self.plot_params.append('dydy')

                if len(self.plot_params) == 0:
                    raise input_err.AtLeastOnePLotQuantitieError()




