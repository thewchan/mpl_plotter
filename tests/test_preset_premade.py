import unittest
import numpy as np

from mpl_plotter.color.schemes import one


x = np.linspace(0, 4, 1000)
y = np.exp(x)
z = abs(np.sin(x) * np.exp(x))


from tests.setup import show


class Tests(unittest.TestCase):

    def test_publication2(self):
        from mpl_plotter.presets.publication import two_d
        two_d.line(x, z, color=one()[5], show=show)
        two_d.scatter(x, z, norm=z, show=show)
        two_d.heatmap(color=one()[5], show=show)
        two_d.quiver(color=one()[5], show=show)
        two_d.streamline(color=one()[5], show=show)
        two_d.fill_area(color=one()[5], show=show)

    def test_precision2(self):
        from mpl_plotter.presets.precision import two_d
        two_d.line(x, z, color=one()[5], show=show)
        two_d.scatter(x, z, norm=z, show=show)
        two_d.heatmap(color=one()[5], show=show)
        two_d.quiver(color=one()[5], show=show)
        two_d.streamline(color=one()[5], show=show)
        two_d.fill_area(color=one()[5], show=show)


class Tests3(unittest.TestCase):

    def test_publication3(self):
        from mpl_plotter.presets.publication import three_d
        three_d.line(x, y, z, color=one()[5], show=show)
        three_d.scatter(x, y, z, norm=z, color=one()[5], show=show)
        three_d.surface(color=one()[5], show=show, demo_pad_plot=False)

    def test_precision3(self):
        from mpl_plotter.presets.precision import three_d
        three_d.line(x, y, z, color=one()[5], show=show)
        three_d.scatter(x, y, z, norm=z, color=one()[5], show=show)
        three_d.surface(color=one()[5], show=show, demo_pad_plot=False)
