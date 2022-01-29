from helpers.ode_solver import OdeSolver
from helpers.visualizer import Visualizer
from single_mode.average_rays import AverageRays
from single_mode.monte_carlo_rays import MonteCarloRays


def run():

    #initialize objects
    average_ray = AverageRays()

    average_ray_ode_solver = OdeSolver(average_ray.aux_integrator_func, average_ray.w,
                        average_ray.stop_time, average_ray.num_points,
                        average_ray.p, average_ray.abs_err, average_ray.rel_err,
                        average_ray.file_name)

    visualizer = Visualizer()

    #run code
    average_ray_ode_solver.integrator()
    visualizer.plot_figure()


if __name__ == '__main__':
    run()