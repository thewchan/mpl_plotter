import unittest
import numpy as np


class TestAll(unittest.TestCase):

    def test_two_d(self):
        from mpl_plotter.two_d import line, scatter, heatmap, quiver, streamline, fill_area

        line(show=True)

        scatter(show=True)

        heatmap(show=True)

        quiver(show=True)

        streamline(show=True)

        fill_area(show=True)

        # Input
        x = np.linspace(0, 2*np.pi, 100)
        y = np.sin(x)
        line(x=x, y=y, show=True, aspect=1)

    def test_three_d(self):
        from mpl_plotter.three_d import line, scatter, surface

        line(show=True)

        scatter(show=True)

        surface(show=True)

        # Wireframe
        surface(show=True, alpha=0, line_width=0.5, edge_color="red", cstride=12, rstride=12)
