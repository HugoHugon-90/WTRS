from helpers.dsolver import Dsolver
from helpers.visualizer import Visualizer


def run():
    dsolver = Dsolver()
    visualizer = Visualizer()
    dsolver.integrator()
    visualizer.plot_figure()


if __name__ == '__main__':
    run()