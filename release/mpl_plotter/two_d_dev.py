import numpy as np

from resources.mock_data import MockData
from two_d_inheritance import fill_area

x = np.arange(-6, 6, .01)
y = MockData().boltzman(x, 0, 1)
z = 1 - MockData().boltzman(x, 0.5, 1)

fill_area()
