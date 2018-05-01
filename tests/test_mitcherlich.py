"""Tests for the Mitcherlich growth model"""

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

from pygrowthmodels import mitcherlich
from pygrowthmodels import mitcherlich_inverse


def test_mitcherlich():
    """Mitcherlich growth model test"""
    time = [-2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0]

    # Evaluate (1, 2, 3) parameters
    value = [7.777778e-001, 6.150998e-001, 3.333333e-001, -1.547005e-001, -1, -2.464102e+000, -5, -9.392305e+000, -17]

    for step in range(len(time)):
        assert mitcherlich(time[step], 1, 2, 3) == approx(value[step])

    # Evaluate (12, 1, 2) parameters
    value = [1.175000e+001, 1.164645e+001, 1.150000e+001, 1.129289e+001, 11, 1.058579e+001, 10, 9.171573e+000, 8]

    for step in range(len(time)):
        assert mitcherlich(time[step], 12, 1, 2) == approx(value[step])


def test_mitcherlich_inverse():
    """Mitcherlich inverse growth model test"""
    time = [-2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0]

    # Evaluate (1, 2, 3) parameters
    value = [7.777778e-001, 6.150998e-001, 3.333333e-001, -1.547005e-001, -1, -2.464102e+000, -5, -9.392305e+000, -17]

    for step in range(len(time)):
        assert mitcherlich_inverse(value[step], 1, 2, 3) == approx(time[step])


def test_mitcherlich_inverse_nan():
    """NaN in Mitcherlich inverse growth model test"""
    assert mitcherlich_inverse(10, 1, 2, 3) == approx(float('nan'), nan_ok=True)
