from scipy.integrate import odeint
from helpers.constants import plot_vs_integrator_dict, input_location
from input_handlers.single_mode_input_handler import SingleModeInputHandler


class OdeSolver(SingleModeInputHandler):

    def __init__(self, derivative_func_list, w, stop_time, num_points, param_list, abserr, relerr, file_name,
                 json_file = input_location + "/" + 'single_mode_input.json'):

        super().__init__(json_file)

        self.derivative_func_list = derivative_func_list
        self.stop_time = stop_time
        self.num_points = num_points
        self.param_list = param_list
        self.w0 = w
        self.abserr = abserr
        self.relerr = relerr
        self.file_name = file_name

    def integrator(self):

        t = [ self.stop_time * float(i) / (self.num_points - 1) for i in range(self.num_points) ]

        wsol = odeint(self.derivative_func_list, self.w0, t, args = (self.param_list,), atol = self.abserr, rtol = self.relerr)



        with open(self.file_name, 'w') as f:
            # Print & save the solution.
            for t1, w1 in zip(t, wsol):
                print(f'{t1}', file=f, end='')

                for p in self.plot_params:
                    print(f'\t {w1[plot_vs_integrator_dict[p]]}', file=f, end='')

                print('\n', file=f, end='')

        return wsol
