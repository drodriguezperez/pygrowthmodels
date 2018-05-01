"""Tests for the Gompertz exponential growth model"""

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

from pygrowthmodels import gompertz
from pygrowthmodels import gompertz_inverse


def test_gompertz():
    """Gompertz growth model test"""
    time = [-2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0]

    # Evaluate (1, 2, 3) parameters
    value = [0, 6.488035e-079, 3.580340e-018, 1.280131e-004, 1.353353e-001, 6.400171e-001, 9.052228e-001, 9.780270e-001,
             9.950548e-001]

    for step in range(len(time)):
        assert gompertz(time[step], 1, 2, 3) == approx(value[step])

    # Evaluate (1, 2, 3) parameters
    value = [2.330805e-023, 2.270614e-008, 7.415748e-003, 7.918564e-001, 4.414553e+000, 8.306408e+000, 1.048108e+001,
             1.141718e+001, 1.178221e+001]

    for step in range(len(time)):
        assert gompertz(time[step], 12, 1, 2) == approx(value[step])


def test_gompertz_inverse():
    """Gompertz inverse growth model test"""
    time = [-1.5, -1.0, -0.5, 0.5, 1.0, 1.5]

    # Evaluate (1, 2, 3) parameters
    value = [6.488035e-079, 3.580340e-018, 1.280131e-004, 6.400171e-001, 9.052228e-001, 9.780270e-001]

    for step in range(len(time)):
        assert gompertz_inverse(value[step], 1, 2, 3) == approx(time[step])


def test_gompertz_inverse_nan():
    """NaN in Gompertz inverse growth model test"""
    assert gompertz_inverse(0, 1, 2, 3) == approx(float('nan'), nan_ok=True)
