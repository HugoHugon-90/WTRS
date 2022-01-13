from cmath import sqrt

# input type
input_type = "oblique"

# turbulence amplitude as a percentage; [0,1], << 1
dne0 = 0.04

# turbulence wavenumber normalized to the unperturbed wavevector k_0; [0,1], <<1
q0 = 0.05

# initial position (please don't change)
r0 = [0, 0]

# unperturbed wavenumber
k0_obl = [1. / abs(sqrt(2)), 1. / abs(sqrt(2))]
k0_par = [1., 0.]
k0_perp = [0., 1.]

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
dxdne = 0.
dydne = 0.
dkxdne = 0.
dkydne = 0.
dxdnedx = 0.
dydnedx = 0.
dkxdnedx = 0.
dkydnedx = 0.


# integrator configs
num_points = 10000
window = [-100.0, 100.0]
abserr = 1.0e-8
relerr = 1.0e-6
stop_time = 1000.0

# output configs
file_name = "x_average_ray.txt"
