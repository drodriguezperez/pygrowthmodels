"""Tests for the Brody growth model"""

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

from pygrowthmodels import brody
from pygrowthmodels import brody_inverse


def test_brody():
    """Brody growth model test"""
    time = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]

    # Evaluate (1, 2, 3) parameters
    value = [2, 1.223130, 1.049787, 1.011109, 1.002479, 1.000553, 1.000123, 1.000028, 1.000006, 1.000001]

    for step in range(len(time)):
        assert brody(time[step], 1, 2, 3) == approx(value[step])

    # Evaluate (10, 5, 0.43) parameters
    value = [5, 5.967293, 6.747455, 7.376687, 7.884190, 8.293511, 8.623646, 8.889914, 9.104669, 9.277879]

    for step in range(len(time)):
        assert brody(time[step], 10, 5, 0.43) == approx(value[step])


def test_brody_inverse():
    """Brody inverse growth model test"""
    time = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]

    # Evaluate (1, 2, 3) parameters
    value = [2, 1.223130, 1.049787, 1.011109, 1.002479, 1.000553, 1.000123, 1.000028, 1.000006, 1.000001]

    for step in range(len(time)):
        assert brody_inverse(value[step], 1, 2, 3) == approx(time[step], rel=1e-1)

    # Evaluate (10, 5, 0.43) parameters
    value = [5, 5.967293, 6.747455, 7.376687, 7.884190, 8.293511, 8.623646, 8.889914, 9.104669, 9.277879]

    for step in range(len(time)):
        assert brody_inverse(value[step], 10, 5, 0.43) == approx(time[step])
