# SPDX-FileCopyrightText: © 2021 Antonio López Rivera <antonlopezr99@gmail.com>
# SPDX-License-Identifier: GPL-3.0-only

import unittest
import numpy as np

from mpl_plotter.color.schemes import colorscheme_one
from mpl_plotter.presets.custom import two_d
from mpl_plotter.presets.data.publication import preset2
from mpl_plotter.two_d.panes import panes


x = np.linspace(0, np.pi/4, 100)
u = np.sin(x); uu = np.sinh(x)
v = np.cos(x); vv = np.cosh(x)
y = np.tan(x); yy = np.tanh(x)


from tests.setup import show, backend


class TestsInput(unittest.TestCase):

    def test_panes_1(self):
        f = two_d(preset=preset2).line
        panes(x,                                    # Horizontal vector
              u,                                    # List of pairs of curves to be compared
              f,                                    # Plotting functions
              y_labels=["u"],                       # List of vertical axis labels
              plot_labels=["a"],                    # List of legend labels
              show=show, backend=backend)

    def test_panes_2(self):
        f = two_d(preset=preset2).line
        panes([x],                                  # Horizontal vector
              [u],                                  # List of pairs of curves to be compared
              [f],                                  # Plotting functions
              y_labels=["u"],                       # List of vertical axis labels
              plot_labels=["a"],                    # List of legend labels
              show=show, backend=backend)

    def test_panes_3(self):
        f = two_d(preset=preset2).line
        panes(x,                                    # Horizontal vector
              [u, v, y],                            # List of pairs of curves to be compared
              [f, f, f],                            # Plotting functions
              y_labels=["u", "v", "y"],             # List of vertical axis labels
              plot_labels=["a", "b", 'c'],          # List of legend labels
              colors=colorscheme_one()[:3],
              show=show, backend=backend)

    def test_panes_4(self):
        f = two_d(preset=preset2).line
        panes([x],                                  # Horizontal vector
              [u, v, y],                            # List of pairs of curves to be compared
              [f, f, f],                            # Plotting functions
              y_labels=["u", "v", "y"],             # List of vertical axis labels
              plot_labels=["a", "b", 'c'],          # List of legend labels
              colors=colorscheme_one()[:3],
              show=show, backend=backend)

    def test_panes_5(self):
        f = two_d(preset=preset2).line
        panes([x, x, x],                            # Horizontal vector
              [u, v, y],                            # List of pairs of curves to be compared
              [f, f, f],                            # Plotting functions
              y_labels=["u", "v", "y"],             # List of vertical axis labels
              plot_labels=["a", "b", 'c'],          # List of legend labels
              colors=colorscheme_one()[:3],
              show=show, backend=backend)

    def test_panes_6(self):
        f = two_d(preset=preset2).line
        panes(x,                                    # Horizontal vector
              [[u, uu], [v, vv], [y, yy]],          # List of pairs of curves to be compared
              [[f, f], [f, f], [f, f]],             # Plotting functions
              y_labels=["u", "v", "y"],             # List of vertical axis labels
              plot_labels=["a", "b"],               # List of legend labels
              show=show, backend=backend)

    def test_panes_7(self):
        f = two_d(preset=preset2).line
        panes([x],                                  # Horizontal vector
              [[u, uu], [v, vv], [y, yy]],          # List of pairs of curves to be compared
              [[f, f], [f, f], [f, f]],             # Plotting functions
              y_labels=["u", "v", "y"],             # List of vertical axis labels
              plot_labels=["a", "b"],               # List of legend labels
              show=show, backend=backend)

    def test_panes_8(self):
        f = two_d(preset=preset2).line
        panes([x, x, x],                            # Horizontal vector
              [[u, uu], [v, vv], [y, yy]],          # List of pairs of curves to be compared
              [[f, f], [f, f], [f, f]],             # Plotting functions
              y_labels=["u", "v", "y"],             # List of vertical axis labels
              plot_labels=["a", "b"],               # List of legend labels
              show=show, backend=backend)

    def test_panes_9(self):
        f = two_d(preset=preset2).line
        panes([[x, x], [x, x], [x, x]],             # Horizontal vector
              [[u, uu], [v, vv], [y, yy]],          # List of pairs of curves to be compared
              [[f, f], [f, f], [f, f]],             # Plotting functions
              y_labels=["u", "v", "y"],             # List of vertical axis labels
              plot_labels=["a", "b"],               # List of legend labels
              show=show, backend=backend)


class TestsPlotters(unittest.TestCase):

    def test_panes_10(self):
        f = two_d(preset=preset2).line
        panes(x,                                    # Horizontal vector
              [[u, uu], [v, vv], [y, yy]],          # List of pairs of curves to be compared
              f,                                    # Plotting functions
              y_labels=["u", "v", "y"],             # List of vertical axis labels
              plot_labels=["a", "b"],               # List of legend labels
              show=show, backend=backend)

    def test_panes_11(self):
        f = two_d(preset=preset2).line
        panes(x,                                    # Horizontal vector
              [[u, uu], [v, vv], [y, yy]],          # List of pairs of curves to be compared
              [f, f, f],                            # Plotting functions
              y_labels=["u", "v", "y"],             # List of vertical axis labels
              plot_labels=["a", "b"],               # List of legend labels
              show=show, backend=backend)

    def test_panes_12(self):
        f = two_d(preset=preset2).line
        panes(x,                                    # Horizontal vector
              [[u, uu], [v, vv], [y, yy]],          # List of pairs of curves to be compared
              [[f, f], [f, f], [f, f]],             # Plotting functions
              y_labels=["u", "v", "y"],             # List of vertical axis labels
              plot_labels=["a", "b"],               # List of legend labels
              show=show, backend=backend)

    def test_pane_13(self):
        plotter = lambda x, y, **kwargs: two_d(preset=preset2).line(x, y, **{**kwargs, **{'x_tick_label_size': 5,
                                                                                          'y_tick_label_size': 5,
                                                                                          'line_width': 1}})
        f = lambda n, x: np.sin(n**2*x)
        panes(x,                                    # Horizontal vector
              [f(1, x),
               f(2, x),
               f(3, x),
               f(4, x),
               f(5, x),
               f(6, x),
               f(7, x),
               f(8, x),
               f(9, x),
               f(10, x),
               f(11, x),
               f(12, x)],                               # List of curves to be plotted
              plotter,                                  # Plotting function
              show=show, backend=backend)

    def test_pane_14(self):
        plotter = lambda x, y, **kwargs: two_d(preset=preset2).line(x, y, **{**kwargs, **{'x_tick_label_size': 5,
                                                                                          'y_tick_label_size': 5,
                                                                                          'line_width': 1}})
        f = lambda n, x: np.sin(n ** 2 * x)
        g = lambda n, x: np.cos(n*x)
        h = lambda n, x: np.cos((20-n)*x)
        panes(x,                                        # Horizontal vector
              [[f(1,  x), g(1,  x), h(1,  x)],
               [f(2,  x), g(2,  x), h(2,  x)],
               [f(3,  x), g(3,  x), h(3,  x)],
               [f(4,  x), g(4,  x), h(4,  x)],
               [f(5,  x), g(5,  x), h(5,  x)],
               [f(6,  x), g(6,  x), h(6,  x)],
               [f(7,  x), g(7,  x), h(7,  x)],
               [f(8,  x), g(8,  x), h(8,  x)],
               [f(9,  x), g(9,  x), h(9,  x)],
               [f(10, x), g(10, x), h(10, x)],
               [f(11, x), g(11, x), h(11, x)],
               [f(12, x), g(12, x), h(12, x)]],         # List of curves to be plotted
              plotter,                                  # Plotting function
              zorders=[0, 2, 1],
              alphas=[0.5, 1, 0.75],
              colors=colorscheme_one()[2:6],
              show=show, backend=backend
              )


class TestsPlurals(unittest.TestCase):

    def test_panes_15(self):
        f = two_d(preset=preset2).line
        panes(x,                                    # Horizontal vector
              [[u, uu], [v, vv], [y, yy]],          # List of pairs of curves to be compared
              [[f, f], [f, f], [f, f]],             # Plotting functions
              y_labels=["u", "v", "y"],             # List of vertical axis labels
              plot_labels=["a", "b"],               # List of legend labels
              show=show, backend=backend)

    def test_panes_16(self):
        f = two_d(preset=preset2).line
        panes(x,                                    # Horizontal vector
              [[u, uu], [v, vv], [y, yy]],          # List of pairs of curves to be compared
              [[f, f], [f, f], [f, f]],             # Plotting functions
              y_labels=["u", "v", "y"],             # List of vertical axis labels
              plot_labels=["a", "b", "c"],          # List of legend labels. Expected behavior: legend[a, a, b, b, c, c]
              show=show, backend=backend)

    def test_panes_17(self):
        f = two_d(preset=preset2).line
        panes(x,                                    # Horizontal vector
              [[u, uu], [v, vv], [y, yy]],          # List of pairs of curves to be compared
              [[f, f], [f, f], [f, f]],             # Plotting functions
              y_labels=["u", "v", "y"],             # List of vertical axis labels
              plot_labels=[["a", "b"],              # List of legend labels
                           ["c", "d"],
                           ["e", "f"]],
              colors=[[colorscheme_one()[0], colorscheme_one()[1]],
                      [colorscheme_one()[2], colorscheme_one()[3]],
                      [colorscheme_one()[4], colorscheme_one()[5]]],
              show=show, backend=backend)
