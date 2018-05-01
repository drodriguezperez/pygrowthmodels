"""Tests for the Logistic growth model"""

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

from pygrowthmodels import generalised_logistic
from pygrowthmodels import generalised_logistic_inverse
from pygrowthmodels import logistic
from pygrowthmodels import logistic_inverse


def test_logistic():
    """Logistic growth model test"""
    time = [-2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0]

    # Evaluate (1, 2, 3) parameters
    value = [1.237842e-003, 5.523816e-003, 2.428890e-002, 1.003676e-001, 3.333333e-001, 6.914385e-001, 9.094430e-001,
             9.782649e-001, 9.950670e-001]

    for step in range(len(time)):
        assert logistic(time[step], 1, 2, 3) == approx(value[step])

    # Evaluate (12, 1, 2) parameters
    value = [2.158345e-001, 5.691105e-001, 1.430435e+000, 3.227297e+000, 6, 8.772703e+000, 1.056956e+001, 1.143089e+001,
             1.178417e+001]

    for step in range(len(time)):
        assert logistic(time[step], 12, 1, 2) == approx(value[step])


def test_logistic_inverse():
    """Logistic inverse growth model test"""
    time = [-2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5]

    # Evaluate (1, 2, 3) parameters
    value = [1.237842e-003, 5.523816e-003, 2.428890e-002, 1.003676e-001, 3.333333e-001, 6.914385e-001, 9.094430e-001,
             9.782649e-001, 9.950670e-001]

    for step in range(len(time)):
        assert logistic_inverse(value[step], 1, 2, 3) == approx(time[step], abs=1e-6)

    # Evaluate (12, 1, 2) parameters
    value = [2.158345e-001, 5.691105e-001, 1.430435e+000, 3.227297e+000, 6, 8.772703e+000, 1.056956e+001, 1.143089e+001]

    for step in range(len(time)):
        assert logistic_inverse(value[step], 12, 1, 2) == approx(time[step], abs=1e-5)


def test_logistic_inverse_nan():
    """NaN in Logistic inverse growth model test"""
    assert logistic_inverse(0, 1, 2, 3) == approx(float('nan'), nan_ok=True)


def test_generalised_logistic():
    """Generalised Logistic inverse growth model test"""
    time = [-2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0]

    # Evaluate (1, 3, 5, 2, 0) parameters
    value = [1.000045e+000, 1.000553e+000, 1.006715e+000, 1.078849e+000, 1.666667e+000, 2.717962e+000, 2.973407e+000,
             2.997790e+000, 2.999818e+000]

    for step in range(len(time)):
        assert generalised_logistic(time[step], 1, 3, 5, 2, 0) == approx(value[step])

    # Evaluate (12, 3, 5, 2, 1) parameters
    value = [1.200000e+001, 1.199998e+001, 1.199980e+001, 1.199751e+001, 1.196978e+001, 1.164518e+001, 9, 4.269170e+000,
             3.119670e+000]

    for step in range(len(time)):
        assert generalised_logistic(time[step], 12, 3, 5, 2, 1) == approx(value[step])


def test_generalised_logistic_inverse():
    """Generalised Logistic inverse growth model test"""
    # Evaluate (1, 3, 5, 2, 0) parameters
    assert generalised_logistic_inverse(1.078849e+000, 1, 3, 5, 2, 0) == approx(-0.5)
    assert generalised_logistic_inverse(2.717962e+000, 1, 3, 5, 2, 0) == approx(0.5)

    # Evaluate (12, 3, 5, 2, 1) parameters
    assert generalised_logistic_inverse(1.164518e+001, 12, 3, 5, 2, 1) == approx(0.5)
    assert generalised_logistic_inverse(9, 12, 3, 5, 2, 1) == approx(1.0)
    assert generalised_logistic_inverse(4.269170e+000, 12, 3, 5, 2, 1) == approx(1.5)
    assert generalised_logistic_inverse(3.119670e+000, 12, 3, 5, 2, 1) == approx(2.0)
