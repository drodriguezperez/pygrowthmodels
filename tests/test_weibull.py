"""Tests for the von Weibull growth model"""

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

from pygrowthmodels import weibull
from pygrowthmodels import weibull_inverse


def test_weibull():
    """Weibull growth model test"""
    time = [-2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0]

    # Evaluate (1, 2, 3, 4) parameters
    value = [1, 9.999995e-001, 9.004259e-001, -6.580582e-001, -1, -6.580582e-001, 9.004259e-001, 9.999995e-001, 1]

    for step in range(len(time)):
        assert weibull(time[step], 1, 2, 3, 4) == approx(value[step])

    # Evaluate (1, 2, 3, 4) parameters
    value = [-7.948576e+002, -1.680343e+002, -2.817107e+001, 3.036622e+000, 10, 1.155374e+001, 1.190043e+001,
             1.197778e+001, 1.199504e+001]

    for step in range(len(time)):
        assert weibull(time[step], 12, 2, 3, 1) == approx(value[step])


def test_weibull_inverse():
    """Weibull inverse growth model test"""
    assert weibull_inverse(1, 1, 2, 3, 4) == approx(float('inf'))
    assert weibull_inverse(-1, 1, 2, 3, 4) == approx(0.0)
    assert weibull_inverse(-6.580582e-001, 1, 2, 3, 4) == approx(0.5)
    assert weibull_inverse(9.004259e-001, 1, 2, 3, 4) == approx(1.0)

    assert weibull_inverse(-7.948576e+002, 12, 2, 3, 1) == approx(-2.0)
    assert weibull_inverse(-1.680343e+002, 12, 2, 3, 1) == approx(-1.5)
    assert weibull_inverse(-2.817107e+001, 12, 2, 3, 1) == approx(-1.0)
    assert weibull_inverse(3.036622e+000, 12, 2, 3, 1) == approx(-0.5)
    assert weibull_inverse(10, 12, 2, 3, 1) == approx(0.0)
    assert weibull_inverse(1.155374e+001, 12, 2, 3, 1) == approx(0.5)
