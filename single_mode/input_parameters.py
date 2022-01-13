from cmath import cos, sin, pi

# input type
input_type = ""

# unperturbed wavenumber (mute if input type is set to "oblique", "parallel" or "perpendicular"
k0 = [abs(cos(pi/3.)), abs(sin(pi/3.))]

# turbulence amplitude as a percentage; [0,1], << 1
dne0 = 0.04

# turbulence wavenumber normalized to the unperturbed wavevector k_0; [0,1], << 1
q0 = 0.04

# integrator configs
num_points = 10000
window = [-100.0, 100.0]
abserr = 1.0e-8
relerr = 1.0e-6
stop_time = 1000.0

# output configs
file_name = "x_average_ray.txt"
