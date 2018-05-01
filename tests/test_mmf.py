"""Tests for the Morgan-Mercer-Flodin growth model"""

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

from pygrowthmodels import mmf
from pygrowthmodels import mmf_inverse


def test_mmf():
    """Morgan-Mercer-Flodin growth model test"""
    time = [-2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 3.0]

    # Evaluate (1, 2, 3, 4) parameters
    value = [1.157895, 1.372093, 1.750000, 1.979592, 2.000000, 1.979592, 1.750000, 1.372093, 1.157895, 1.035714]

    for step in range(len(time)):
        assert mmf(time[step], 1, 2, 3, 4) == approx(value[step])

    # Evaluate (12, 2, 3, 1) parameters
    value = [-18, -8, -3, 0, 2, 3.428571, 4.5, 5.333333, 6, 7]

    for step in range(len(time)):
        assert mmf(time[step], 12, 2, 3, 1) == approx(value[step])


def test_mmf_inverse():
    """Morgan-Mercer-Flodin invserse growth model test"""
    time = [-2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 3.0]

    # Evaluate (1, 2, 3,4) parameters
    assert mmf_inverse(2.000000, 1, 2, 3, 4) == approx(0.0)
    assert mmf_inverse(1.750000, 1, 2, 3, 4) == approx(1.0)
    assert mmf_inverse(1.372093, 1, 2, 3, 4) == approx(1.5)
    assert mmf_inverse(1.157895, 1, 2, 3, 4) == approx(2.0)

    # Evaluate (12, 2, 3, 1) parameters
    value = [-18, -8, -3, 0, 2, 3.428571, 4.5, 5.333333, 6, 7]

    for step in range(len(time)):
        assert mmf_inverse(value[step], 12, 2, 3, 1) == approx(time[step])
