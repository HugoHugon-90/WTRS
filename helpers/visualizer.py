from math import pi, cos

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
                 title="Average ray evolution"):

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
            plt.rcParams['text.usetex'] = True
            loaded_data = loadtxt(self.setup.file_name, unpack=True)
            x_max = max(int(loaded_data[4][len(loaded_data[4])-1]),int(loaded_data[2][len(loaded_data[2])-1]))
            y_max = max(int(loaded_data[5][len(loaded_data[3])-1]),int(loaded_data[3][len(loaded_data[3])-1]))
            x_max = int(1.2*x_max)
            y_max = int(1.2*y_max)

            x = np.ones(y_max)
            y = np.linspace(0, 2*pi, x_max)
            z = np.array([cos(self.setup.q0_vector[0]*800*i)
                          for j in x for i in y])
            Z = z.reshape(y_max, x_max)

            plt.text(x_max/2.5, y_max*0.9, r"\textbf{$\delta n_e = A \cos(q_x \cdot x + \phi)$}",
                     fontsize=14, fontweight = "extra bold")
            plt.xlabel(r'$x$')
            plt.ylabel(r'$y$')
            plt.grid(self.has_grid)

            title = self.title + f" and RMS aperture for k0 = {self.setup.k0_angle}º,\n qx = {self.setup.q0_vector[0]} " \
                                 f"and A = {self.setup.amplitude}"
            if self.setup.mc_is_active:
                plt.grid(False)
                loaded_data_mc = loadtxt(self.setup.mc_file_name, unpack=True)
                plt.plot(loaded_data_mc[0], loaded_data_mc[1], c="darkturquoise", linewidth=self.lw,
                         linestyle='dotted',
                         alpha = .5, label= "Monte Carlo rays" )
                title = title + " / Comparison with Monte Carlo"

            ll=0
            for l in int(loaded_data[4][len(loaded_data[4])-1]), int(loaded_data[2][len(loaded_data[2])-1]):
                if l<0:
                    ll=l
                    plt.imshow(Z,origin="lower", cmap= 'Oranges',interpolation='bilinear',
                               aspect='auto', alpha=0.3, extent=[-x_max, x_max, 0, y_max])

            if ll==0:
                plt.imshow(Z,origin="lower", cmap= 'Oranges',interpolation='bilinear',
                            aspect='auto', alpha=0.3)




            plt.plot(loaded_data[0], loaded_data[1], c="black", linewidth=self.lw+1, label= "Average ray" )
            plt.plot(loaded_data[2], loaded_data[3], c="red", linewidth=self.lw+1, label= "RMS aperture")
            plt.plot(loaded_data[4], loaded_data[5], c="red", linewidth=self.lw+1)

            plt.title(rf'{title}')

            plt.legend(loc="lower right")

            fig = const.output_location + "/" + self.figname + "." + self.figformat
            plt.savefig(fig, dpi=self.dpi)



        else:

            loaded_data = loadtxt(self.setup.file_name, unpack=True)
            plt.xlabel(self.xlabel)
            plt.ylabel(self.ylabel)
            plt.grid(self.has_grid)

            plt.figure(1, figsize=(self.figsizel, self.figsizew))

            if len(self.setup.plot_params)>1:
                color = iter(plt.cm.rainbow(np.linspace(0, 1, len(self.setup.plot_params))))
                plt_param = iter(self.setup.plot_params)
                for plt_num in range(1, len(self.setup.plot_params) + 1):
                    c = next(color)
                    pp = next(plt_param)
                    plt.plot(loaded_data[0], loaded_data[plt_num], c=c,
                             label=f"Formalism:  {pp}", linewidth=self.lw)
            else:
                plt.plot(loaded_data[0], loaded_data[1], c='red', label="Formalism",
                         linewidth=self.lw)

            plt.legend(loc="lower right")

            title = "Average evolution of"
            for pp in self.setup.plot_params:
                title = title + " " + pp+","
            title = title[:-1] + f"\n for k0 = {self.setup.k0_angle}º, qx = {self.setup.q0_vector[0]} " \
                                 f"and A = {self.setup.amplitude}"
            plt.title(title)

            if self.setup.mc_is_active:
                loaded_data_mc = loadtxt(self.setup.mc_file_name, unpack=True)

                if self.setup.plot_params[0] in ['dxdx','dydy','dkxdkx','dkydky']:
                    plt.plot(loaded_data_mc[0], loaded_data_mc[2], c="blue",
                             label= "Monte Carlo", linewidth=self.lw)
                else:
                    plt.plot(loaded_data_mc[0], loaded_data_mc[1], c="blue",
                             label= "Monte Carlo", linewidth=self.lw)

                fig = const.output_location + "/" + "MC_" + self.figname + "." + self.figformat
                plt.legend(loc="lower right")
                plt.savefig(fig, dpi=self.dpi)
                return 0

            else:
                fig = const.output_location + "/" + self.figname + "." + self.figformat
                plt.savefig(fig, dpi=self.dpi)
