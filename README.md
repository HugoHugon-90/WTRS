# WTRS
A ray tracing code in 2D - slab geometry based on the work of J.P. Bizarro, H. Hugon and R. Jorge, 2018 (https://journals.aps.org/pra/abstract/10.1103/PhysRevA.98.023847)

# Single-mode, homogeneous random media case: physical description

## Physical quantities (SI): 
- r1, r2 (2D - positions [m])
- k = ||k|| (scalar wavevector [m^(-1)])
- k1, k2 (2D - wavenumbers [m^(-1)])
- k_0 (unperturbed wavenumber [m^(-1)])
- c (speed of light [m.s^(-1)]) 
- q (wavenumber of turbulence [m^(-1)]
- n0 (unperturbed refractive index)
- n (refractive index)
- < n_e > (ensemble averaged density [m^(-3)])
- \phi (random phase [0, 2 Pi])
- \delta n_e (r) = \delta n_e0 cos(q r1 + \phi)  (density fluctuations << < ne > [m^(-3)])
- n(r)/n0 = 1 + \delta n_e (r) / <ne> (turbulence profile through the effects of density fluctuations in the refractive index)
- t (time [s])
- w(r) = c k /n(r) 

## Normalized quantites used in the code
- x[y] = (k_0 / 2 Pi) r1[2] (position)
- \kappa_x[y] = k_1[2] / k_0
- \delta n_e (r) = \delta n_e0 cos(q x + \phi)
- q --> q/k_0 (in this normalized system, wavenumber of turbulence becomes adimensional)
- \tau = (c k_0 / 2 Pi n_0) t
- < ne > === 1 ---> \delta n_e0 (r) becomes a percentage 
- \kappa_x[y]_0, x[y]_0 refer to initial conditions for normalized wavevectors and position, respectively 


