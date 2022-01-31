import math

from scipy.integrate import odeint
from helpers.constants import plot_vs_integrator_dict
from single_mode.average_rays import AverageRays
from single_mode.monte_carlo_rays import MonteCarloRays
from single_mode.setup import Setup

import numpy as np


class OdeSolver:

    def __init__(self, setup: Setup, average_ray: AverageRays, monte_carlo_ray: MonteCarloRays = None):
        self.setup = setup
        self.average_ray = average_ray
        self.monte_carlo_ray = monte_carlo_ray

    def integrator(self):

        t = [self.setup.stop_time * float(i) / (self.setup.num_points - 1) for i in range(self.setup.num_points)]

        wsol = odeint(self.average_ray.aux_integrator_func, self.setup.w, t, args=(self.average_ray.p,),
                      atol=self.setup.abs_err, rtol=self.setup.rel_err)

        if not self.setup.plot_trajectory:
            with open(self.setup.file_name, 'w') as f:
                # Print & save the solution.
                for t1, w1 in zip(t, wsol):
                    print(f'{t1}', file=f, end='')

                    for p in self.setup.plot_params:
                        print(f'\t {w1[plot_vs_integrator_dict[p]]}', file=f, end='')

                    print('\n', file=f, end='')
        else:
            with open(self.setup.file_name, 'w') as f:
                for time in range(len(t)):
                    dxdx = wsol[time][plot_vs_integrator_dict['dxdx']]
                    dkxdkx = wsol[time][plot_vs_integrator_dict['dkxdkx']]
                    dkxdky = wsol[time][plot_vs_integrator_dict['dkxdky']]
                    dkydky = wsol[time][plot_vs_integrator_dict['dkydky']]
                    dkxdne = wsol[time][plot_vs_integrator_dict['dkxdne']]
                    dkydne = wsol[time][plot_vs_integrator_dict['dkydne']]
                    dxdnedx = wsol[time][plot_vs_integrator_dict['dxdnedx']]
                    dydy = wsol[time][plot_vs_integrator_dict['dydy']]

                    dxdkx = wsol[time][plot_vs_integrator_dict['dxdkx']]


                    x = wsol[time][plot_vs_integrator_dict['x']]
                    y = wsol[time][plot_vs_integrator_dict['y']]
                    kx = wsol[time][plot_vs_integrator_dict['kx']]
                    ky = wsol[time][plot_vs_integrator_dict['ky']]
                    k = math.sqrt(kx**2 + ky**2)
                    A = self.setup.amplitude
                    q = self.setup.q0_vector[0]

                    #if time == 0:
                     #   time = 1

                    dxdt = (kx /k)* (1+A**2/2) + \
                           (3 * kx/(2*k**5)) * (kx**2 * dkxdkx + ky**2 * dkydky + 2*kx*ky*dkxdky) \
                           - (1/(2*k**3))*(kx*(dkxdkx+dkydky)+2*(kx*dkxdkx+ky*dkxdky)) \
                           - dkxdne/k \
                           + (kx/k**3) * (kx * dkxdne + 0 * ky * dkydne) - \
                           (kx/k)*dxdnedx

                    dydt = (ky /k)* (1+A**2/2) + (3 * ky/(2*k**5)) * (kx**2 * dkxdkx + ky**2 * dkydky + 2*kx*ky*dkxdky) \
                           - (1/(2*k**3))*(ky*(dkxdkx+dkydky)+2*(kx*dkxdky+ky*dkydky)) \
                           - dkydne/k \
                           + (ky/k**3) * (kx * dkxdne +  ky * dkydne) -\
                           (ky/k)*dxdnedx

                    #dxdt = (wsol[time][plot_vs_integrator_dict[self.setup.plot_params[0]]]
                          #  - wsol[time - 1][plot_vs_integrator_dict[self.setup.plot_params[0]]]) / 2.0
                    #dydt = (wsol[time][plot_vs_integrator_dict[self.setup.plot_params[1]]]
                           # - wsol[time - 1][plot_vs_integrator_dict[self.setup.plot_params[1]]]) / 2.0

                    sigma_perp = -(math.sqrt(dxdx) * abs(dydt) + math.sqrt(dydy) * abs(dxdt)) / math.sqrt(dxdt ** 2 + dydt ** 2)
                    sigma_perp_x = - sigma_perp * dydt / math.sqrt(dxdt ** 2 + dydt ** 2)
                    sigma_perp_y = sigma_perp * dxdt / math.sqrt(dxdt ** 2 + dydt ** 2)

                    x_upper = x + sigma_perp_x
                    y_upper = y + sigma_perp_y

                    x_lower = x - sigma_perp_x
                    y_lower = y - sigma_perp_y

                    s = f'{x}\t{y}\t{x_lower}\t{y_lower}\t{x_upper}\t{y_upper}'
                    f.write(s + "\n")

        if self.monte_carlo_ray is not None:

            if not self.setup.plot_trajectory:

                with open(self.setup.mc_file_name, 'w') as f:

                    sol_to_process = np.zeros((len(t), len(self.monte_carlo_ray.phi_realizations)))

                    for phi in range(len(self.monte_carlo_ray.phi_realizations)):
                        self.monte_carlo_ray.set_phi(phi)
                        wsol_mc = odeint(self.monte_carlo_ray.mc_aux_integrator_func, self.setup.w_mc, t,
                                         args=(self.monte_carlo_ray.p,), atol=self.setup.abs_err,
                                         rtol=self.setup.rel_err)

                        for time in range(len(t)):
                            sol_to_process[time][phi] = wsol_mc[time][
                                plot_vs_integrator_dict[self.setup.plot_params[0]]]

                    for time in range(len(t)):
                        s = f'{t[time]}\t{np.average(sol_to_process[time])}\t{np.var(sol_to_process[time])}'
                        f.write(s + "\n")
            else:
                pass

        return wsol
