"""Tests for the Negative exponential growth model"""

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

from pygrowthmodels import negative_exponential
from pygrowthmodels import negative_exponential_inverse


def test_negative_exponential():
    """Negative exponential growth model test"""
    time = [-2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0]

    # Evaluate (1, 2) parameters
    value = [-5.359815e+001, -1.908554e+001, -6.389056e+000, -1.718282e+000, 0, 6.321206e-001, 8.646647e-001,
             9.502129e-001, 9.816844e-001]

    for step in range(len(time)):
        assert negative_exponential(time[step], 1, 2) == approx(value[step])

    # Evaluate (12, 1) parameters
    value = [-7.666867e+001, -4.178027e+001, -2.061938e+001, -7.784655e+000, 0, 4.721632e+000, 7.585447e+000,
             9.322438e+000, 1.037598e+001]

    for step in range(len(time)):
        assert negative_exponential(time[step], 12, 1) == approx(value[step])


def test_negative_exponential_inverse():
    """Negative exponential inverse growth model test"""
    time = [-2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5]

    # Evaluate (1, 2) parameters
    value = [-5.359815e+001, -1.908554e+001, -6.389056e+000, -1.718282e+000, 0, 6.321206e-001, 8.646647e-001,
             9.502129e-001]

    for step in range(len(time)):
        assert negative_exponential_inverse(value[step], 1, 2) == approx(time[step])

    # Evaluate (12, 1) parameters
    value = [-7.666867e+001, -4.178027e+001, -2.061938e+001, -7.784655e+000, 0, 4.721632e+000, 7.585447e+000,
             9.322438e+000]

    for step in range(len(time)):
        assert negative_exponential_inverse(value[step], 12, 1) == approx(time[step])


def test_negative_exponential_inverse_nan():
    """NaN in Negative exponential inverse growth model test"""
    assert negative_exponential_inverse(10, 0, 2) == approx(float('nan'), nan_ok=True)
    assert negative_exponential_inverse(10, 1, 0) == approx(float('nan'), nan_ok=True)
