"""Tests for the Blumberg growth model"""

#
#  Created by Daniel Rodriguez Perez.
#
#  Copyright (c) 2018 Daniel Rodriguez Perez.
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>
#


from pytest import approx

from pygrowthmodels import blumberg
from pygrowthmodels import blumberg_inverse


def test_blumberg():
    """Blumberg tests"""
    time = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]

    # Evaluate (1, 2, 3) parameters
    value = [0, 0.05882353, 0.33333333, 0.62790698, 0.8, 0.88652482, 0.93103448, 0.95543175, 0.96969697, 0.97852349]

    for step in range(len(time)):
        assert blumberg(time[step], 1, 2, 3) == approx(value[step])

    # Evaluate (10, 5, 0.43) parameters
    value = [0, 1.292630, 1.666667, 1.923072, 2.122552, 2.287412, 2.428652, 2.552605, 2.663284, 2.763410]

    for step in range(len(time)):
        assert blumberg(time[step], 10, 5, 0.43) == approx(value[step])

    # Evaluate (1, 2, 3, 2) parameters
    value = [0.8, 0.8865248, 0.9310345, 0.9554318, 0.9696970, 0.9785235, 0.9842520, 0.9881218, 0.9908257, 0.9927700]

    for step in range(len(time)):
        assert blumberg(time[step], 1, 2, 3, 2) == approx(value[step])

    # Evaluate (10, 5, 0.43, 2) parameters
    value = [2.122552, 2.287412, 2.428652, 2.552605, 2.663284, 2.763410, 2.854921, 2.939251, 3.017494, 3.090503]

    for step in range(len(time)):
        assert blumberg(time[step], 10, 5, 0.43, 2) == approx(value[step])


def test_blumberg_inverse():
    """Blumberg inverse tests"""
    time = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]

    # Evaluate (1, 2, 3) parameters
    value = [0, 0.05882353, 0.33333333, 0.62790698, 0.8, 0.88652482, 0.93103448, 0.95543175, 0.96969697, 0.97852349]

    for step in range(len(time)):
        assert blumberg_inverse(value[step], 1, 2, 3) == approx(time[step])

    # Evaluate (10, 5, 0.43) parameters
    value = [0, 1.292630, 1.666667, 1.923072, 2.122552, 2.287412, 2.428652, 2.552605, 2.663284, 2.763410]

    for step in range(len(time)):
        assert blumberg_inverse(value[step], 10, 5, 0.43) == approx(time[step])

    # Evaluate (1, 2, 3, 2) parameters
    value = [0.8, 0.8865248, 0.9310345, 0.9554318, 0.9696970, 0.9785235, 0.9842520, 0.9881218, 0.9908257, 0.9927700]

    for step in range(len(time)):
        assert blumberg_inverse(value[step], 1, 2, 3, 2) == approx(time[step], rel=1e-5)
