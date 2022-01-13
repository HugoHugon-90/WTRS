from helpers.dsolver import Dsolver
from numpy import loadtxt
import matplotlib.pyplot as plt
from matplotlib.font_manager import *


class Visualizer(Dsolver):

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

        t, x1 = loadtxt(self.file_name, unpack=True)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.grid(self.has_grid)

        plt.figure(1, figsize=(self.figsizel, self.figsizew))

        plt.plot(t, x1, self.colour, linewidth=self.lw)

        plt.legend([r'$\left< \delta x \delta x \right>$'], prop=FontProperties(size=self.fontsize))
        plt.title(self.title)

        fig = self.figname + "." + self.figformat
        plt.savefig(fig, dpi=self.dpi)
