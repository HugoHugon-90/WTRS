from helpers.ode_solver import OdeSolver
from helpers.visualizer import Visualizer
from single_mode.average_rays import AverageRays


def run():

    #
    average_ray = AverageRays()

    ode_solver = OdeSolver(average_ray.aux_integrator_func, average_ray.w,
                        average_ray.stop_time, average_ray.num_points,
                        average_ray.p, average_ray.abs_err, average_ray.rel_err,
                        average_ray.file_name)

    visualizer = Visualizer()

    ode_solver.integrator()
    visualizer.plot_figure()


if __name__ == '__main__':
    run()