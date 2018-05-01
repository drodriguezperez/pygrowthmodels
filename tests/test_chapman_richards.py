"""Tests for the Chapman-Richards growth model"""

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

from pygrowthmodels import chapman_richards
from pygrowthmodels import chapman_richards_inverse


def test_chapman_richards():
    """Chapman-Richards growth model test"""
    time = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]

    # Evaluate (1, 2, 3, 4) parameters
    value = [1.217769, 1.035581, 1.007518, 1.001658, 1.000369, 1.000082, 1.000018, 1.000004, 1.000001]

    for step in range(len(time)):
        assert chapman_richards(time[step], 1, 2, 3, 4) == approx(value[step])


def test_chapman_richards_inverse():
    """Chapman-Richards inverse growth model test"""
    # Evaluate (1, 2, 3, 4) parameters
    assert chapman_richards_inverse(1.217769, 1, 2, 3, 4) == approx(0.5)
