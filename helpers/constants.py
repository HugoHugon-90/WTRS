from cmath import sqrt

# inputs
single_mode_input_configuration_reserved_words = {'parallel', 'perpendicular', 'oblique', ''}
single_mode_json_input_mandatory_key_list = {'ray_params', 'integrator_params','plot_trajectory',
                                             'quantities_to_plot', 'monte_carlo'}
single_mode_json_ray_xor_params_key_list = {'input_type', 'k0_angle_degrees'}
single_mode_json_ray_mandatory_params_key_list = {'turbulence_amplitude', 'turbulence_wavenumber'}

single_mode_json_turb_wavenumb_params_key_list = {'q0x', 'q0y', 'q0z'}

single_mode_json_integrator_params_key_list = {'num_points', 'stop_time', 'abs_err', 'rel_err'}

plot_vs_integrator_dict = {'x': 0, 'y': 1, 'kx': 2, 'ky': 3, 'dxdx': 4, 'dydy':5, 'dxdy':6, 'dkxdkx':7, 'dkxdky':8, 'dkydky':9,
                           'dxdkx':10, 'dydkx':11, 'dxdky':12, 'dydky':13,'dxdne': 14, 'dydne':15, 'dkxdne':16, 'dkydne':17,
                           'dxdnedx':18, 'dydnedx':19, 'dkxnedx':20, 'dkydnedx':21}

monte_carlo_param_list =['x','y','kx','ky','dxdx','dydy','dkxdkx','dkydky']
# files
input_location = "WTRS/input_files"
single_mode_input_json = "single_mode_input.json"
output_location = "WTRS/output_files"
output_location_mc = "WTRS/output_files/monte_carlo"

# unperturbed wavenumber
k0_obl = [1. / abs(sqrt(2)), 1. / abs(sqrt(2))]
k0_par = [1., 0.]
k0_perp = [0., 1.]

# initial position (please don't change)
r0 = [0, 0]

# initial first-order fluctuations
dx0 = 0.
dy0 = 0.
dkx0 = 0.
dky0 = 0.

# initial second-order fluctuations
dxdx0 = 0.
dydy0 = 0.
dxdy0 = 0.
dkxdkx0 = 0.
dkydky0 = 0.
dkxdky0 = 0.
dxdkx0 = 0.
dxdky0 = 0.
dydkx0 = 0.
dydky0 = 0.

# initial density-dependent fluctuations
dxdne = 0
dydne = 0.
dkxdne = 0.
dkydne = 0.
dxdnedx = 0.
dydnedx = 0.
dkxdnedx = 0.
dkydnedx = 0.
