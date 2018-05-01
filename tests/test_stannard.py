"""Tests for the Stannard growth model"""

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

from pygrowthmodels import stannard
from pygrowthmodels import stannard_inverse


def test_stannard():
    """Stannard growth model test"""
    time = [-2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 4.0]

    # Evaluate (1, 2, 3, 0.5) parameters
    value = [0.01831257, 0.08180985, 0.34525776, 0.85501964, 0.99096609, 0.99954437, 0.9999773, 0.99999887, 0.99999994,
             1]

    for step in range(len(time)):
        assert stannard(time[step], 1, 2, 3, 0.5) == approx(value[step])

    # Evaluate (12, 2, 3, 0.7) parameters
    value = [0.2192816, 0.9660857, 3.7981941, 9.0791332, 11.5399613, 11.9437234, 11.9933643, 11.9992210, 11.9999086, 12]

    for step in range(len(time)):
        assert stannard(time[step], 12, 2, 3, 0.7) == approx(value[step])


def test_stannard_inverse():
    """Stannard inverse growth model test"""
    time = [-2.0, -1.5, -1.0, -0.5, 0.5, float('inf')]

    # Evaluate (1, 2, 3, 0.5) parameters
    value = [0.01831257, 0.08180985, 0.34525776, 0.85501964, 0.99954437, 1]

    for step in range(len(time)):
        assert stannard_inverse(value[step], 1, 2, 3, 0.5) == approx(time[step])

    # Evaluate (12, 2, 3, 0.7) parameters
    value = [0.2192816, 0.9660857, 3.7981941, 9.0791332, 11.9437234, 12]

    for step in range(len(time)):
        assert stannard_inverse(value[step], 12, 2, 3, 0.7) == approx(time[step])
