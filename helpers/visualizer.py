import matplotlib.pyplot as plt
from numpy import loadtxt
import numpy as np

from helpers import constants as const
from single_mode.setup import Setup


class Visualizer:

    def __init__(self, setup: Setup, figsizel=6, figsizew=4.5,
                 xlabel="t", ylabel="", linewidth=1, has_grid=True,
                 colour='b', legend='', figname='figure',
                 figformat='png', dpi=600, fontsize=16,
                 title="average ray evolution"):

        self.setup = setup

        self.figsizel = figsizel
        self.figsizew = figsizew
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.lw = linewidth
        self.colour = colour
        self.figformat = figformat
        self.dpi = dpi
        self.fontsize = fontsize
        self.legend = legend
        self.title = title
        self.has_grid = has_grid
        if self.setup.plot_trajectory:
            fn = str(self.setup.k0_angle) + "_trajectory"
        else:
            fn = str(self.setup.k0_angle)
            for p in self.setup.plot_params:
                fn = fn + "_" + p

        self.figname = fn

    def plot_figure(self):

        if self.setup.plot_trajectory:
            loaded_data = loadtxt(self.setup.file_name, unpack=True)

            plt.xlabel('x')
            plt.ylabel('y')
            plt.grid(self.has_grid)

            plt.plot(loaded_data[0], loaded_data[1], c="black", linewidth=self.lw+1, label= "Average ray" )
            plt.plot(loaded_data[2], loaded_data[3], c="red", linewidth=self.lw+1, label= "RMS aperture")
            plt.plot(loaded_data[4], loaded_data[5], c="red", linewidth=self.lw+1)

            plt.title(self.title + f" for a {self.setup.k0_angle} k0 angle")

            plt.legend(loc="lower right")

            fig = const.output_location + "/" + self.figname + "." + self.figformat
            plt.savefig(fig, dpi=self.dpi)

        else:
            if self.setup.mc_is_active:
                loaded_data = loadtxt(self.setup.file_name, unpack=True)
                loaded_data_mc = loadtxt(self.setup.mc_file_name, unpack=True)

                plt.xlabel(self.xlabel)
                plt.ylabel(self.ylabel)
                plt.grid(self.has_grid)

                fg = plt.figure(1, figsize=(self.figsizel, self.figsizew))
                plt.plot(loaded_data[0], loaded_data[1], c="red",
                         label=self.setup.plot_params[0], linewidth=self.lw)
                plt.plot(loaded_data_mc[0], loaded_data_mc[1], c="blue",
                         label= "MC_" + self.setup.plot_params[0], linewidth=self.lw)

                fg.legend(loc="upper right")

                plt.title(self.title)

                fig = const.output_location + "/" + self.figname + "." + self.figformat
                plt.savefig(fig, dpi=self.dpi)

            else:
                loaded_data = loadtxt(self.setup.file_name, unpack=True)
                plt.xlabel(self.xlabel)
                plt.ylabel(self.ylabel)
                plt.grid(self.has_grid)

                fg = plt.figure(1, figsize=(self.figsizel, self.figsizew))
                color = iter(plt.cm.rainbow(np.linspace(0, 1, len(self.setup.plot_params))))
                plt_param = iter(self.setup.plot_params)
                for plt_num in range(1, len(self.setup.plot_params) + 1):
                    c = next(color)
                    pp = next(plt_param)
                    plt.plot(loaded_data[0], loaded_data[plt_num], c=c, label=pp, linewidth=self.lw)

                fg.legend(loc="upper right")

                plt.title(self.title)

                fig = const.output_location + "/" + self.figname + "." + self.figformat
                plt.savefig(fig, dpi=self.dpi)
