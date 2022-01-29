from helpers.ode_solver import OdeSolver
from helpers.visualizer import Visualizer
from input_handlers.single_mode_input_handler import SingleModeInputHandler
from single_mode.average_rays import AverageRays
from helpers import constants
from single_mode.monte_carlo_rays import MonteCarloRays
from single_mode.setup import Setup


def run():

    # Initialize and setup vars from input file
    _init = SingleModeInputHandler(f"{constants.input_location}/{constants.single_mode_input_json}")
    _setup = Setup(_init)

    # Instatiate ray-objects (our formalism and Monte Carlo)
    _average_ray = AverageRays(_setup)
    _mc_ray = None

    if _init.activate_monte_carlo:
        _mc_ray = MonteCarloRays(_setup)

    # Instantiate and execute ODE solver
    _solver = OdeSolver(_setup, _average_ray, _mc_ray)
    _solver.integrator()

    # Instantiate visualizer and plot figure
    visualizer = Visualizer(_setup)
    visualizer.plot_figure()


if __name__ == '__main__':
    run()
