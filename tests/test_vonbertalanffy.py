"""Tests for the von Bertalanffy growth model"""

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

from pygrowthmodels import vonbertalanffy
from pygrowthmodels import vonbertalanffy_inverse


def test_vonbertalanffy():
    """von Bertalanffy growth model test"""
    time = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]

    # Evaluate (1, 2, 3, 4) parameters
    value = [1.217769e+000, 1.035581e+000, 1.007518e+000, 1.001658e+000, 1.000369e+000, 1.000082e+000, 1.000018e+000,
             1.000004e+000, 1.000001e+000]

    for step in range(len(time)):
        assert vonbertalanffy(time[step], 1, 2, 3, 4) == approx(value[step])

    # Evaluate (12, 2, 3, -2) parameters
    value = [1.199897e+001, 1.199977e+001, 1.199995e+001, 1.199999e+001, 1.200000e+001, 1.200000e+001, 1.200000e+001,
             1.200000e+001, 1.200000e+001]

    for step in range(len(time)):
        assert vonbertalanffy(time[step], 12, 2, 3, -2) == approx(value[step])


def test_vonbertalanffy_inverse():
    """von Bertalanffy invserse growth model test"""
    assert vonbertalanffy_inverse(1.217769e+000, 1, 2, 3, 4) == approx(0.5)

    assert vonbertalanffy_inverse(1.200000e+001, 12, 2, 3, -2) == approx(float('inf'))
