from cmath import cos,acos, asin, sin, pi

from helpers.json_handler import JsonHandler


class InputParameters(JsonHandler):

    # input type
    input_type = "sad"

    # unperturbed wavenumber (mute if input type is set to "oblique", "parallel" or "perpendicular"
    k0 = [abs(cos(pi/3)), abs(sin(pi/3.))]

    # turbulence amplitude as a percentage; [0,1], << 1
    dne0 = 0.04

    # turbulence wavenumber normalized to the unperturbed wavevector k_0; belongs in [0,1], << 1
    #  qx, qy, qz
    q0 = 0.04, 0, 0

    # integrator configs
    num_points = 10000
    stop_time = 1000.0
    abs_err = 1.0e-8
    rel_err = 1.0e-6

    # output configs
    if input_type not in ["perpendicular", "parallel", "oblique"] :
        file_name = f"kx0_{float(abs(acos(k0[0])*180/pi)).__round__(2)}_deg__ky0_{float(abs(asin(k0[1]))*180/pi).__round__(2)}_deg.txt"
    else:
        file_name = input_type + ".txt"
