from scipy.integrate import odeint
from helpers.constants import plot_vs_integrator_dict
from single_mode.average_rays import AverageRays
from single_mode.monte_carlo_rays import MonteCarloRays
from single_mode.setup import Setup


class OdeSolver:

    def __init__(self, setup: Setup, average_ray: AverageRays, monte_carlo_ray: MonteCarloRays = None):
        self.setup = setup
        self.average_ray = average_ray
        self.monte_carlo_ray = monte_carlo_ray

    def integrator(self):

        t = [self.setup.stop_time * float(i) / (self.setup.num_points - 1) for i in range(self.setup.num_points)]

        wsol = odeint(self.average_ray.aux_integrator_func, self.setup.w, t, args=(self.average_ray.p,),
                      atol=self.setup.abs_err, rtol=self.setup.rel_err)

        with open(self.setup.file_name, 'w') as f:
            # Print & save the solution.
            for t1, w1 in zip(t, wsol):
                print(f'{t1}', file=f, end='')

                for p in self.setup.plot_params:
                    print(f'\t {w1[plot_vs_integrator_dict[p]]}', file=f, end='')

                print('\n', file=f, end='')

        if self.monte_carlo_ray is not None:

            for phi in range(len(self.monte_carlo_ray.phi_realizations)):
                self.monte_carlo_ray.set_phi(phi)
                wsol_mc = odeint(self.monte_carlo_ray.mc_aux_integrator_func, self.setup.w_mc, t,
                                 args=(self.monte_carlo_ray.p,), atol=self.setup.abs_err, rtol=self.setup.rel_err)

                with open(self.setup.mc_file_name + f'{phi}.txt', 'w') as f:
                    # Print & save the solution.
                    for t1, w1 in zip(t, wsol_mc):
                        print(f'{t1}', file=f, end='')

                        for p in self.setup.plot_params:
                            print(f'\t {w1[plot_vs_integrator_dict[p]]}', file=f, end='')

                        print('\n', file=f, end='')

        return wsol
