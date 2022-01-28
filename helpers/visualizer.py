import matplotlib.pyplot as plt
from numpy import loadtxt
import numpy as np

from helpers import constants as const
from single_mode.average_rays import AverageRays


class Visualizer(AverageRays):

    def __init__(self, figsizel = 6, figsizew = 4.5,
                 xlabel = "t", ylabel = "", linewidth = 1, has_grid = True,
                 colour = 'b', legend = '', figname = 'figure',
                 figformat = 'png', dpi = 600, fontsize = 16,
                 title = "average ray evolution"):

        super().__init__()

        self.figsizel = figsizel
        self.figsizew = figsizew
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.lw = linewidth
        self.colour = colour
        self.figname = figname
        self.figformat = figformat
        self.dpi = dpi
        self.fontsize = fontsize
        self.legend = legend
        self.title = title
        self.has_grid = has_grid

    def plot_figure(self):

        loaded_data = loadtxt(self.file_name, unpack=True)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.grid(self.has_grid)

        fg = plt.figure(1, figsize=(self.figsizel, self.figsizew))
        color = iter(plt.cm.rainbow(np.linspace(0, 1, len(self.plot_params))))
        plt_param = iter(self.plot_params)
        for plt_num in range(1, len(self.plot_params)+1):
            c = next(color)
            pp = next(plt_param)
            plt.plot(loaded_data[0], loaded_data[plt_num], c = c, label = pp, linewidth = self.lw)

        fg.legend( loc = "upper right")

        plt.title(self.title)

        fig = const.output_location + "/" + self.figname + "." + self.figformat
        plt.savefig(fig, dpi=self.dpi)
