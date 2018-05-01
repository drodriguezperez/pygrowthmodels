"""Tests for the Schnute growth model"""

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

from pygrowthmodels import schnute
from pygrowthmodels import schnute_inverse


def test_schnute():
    """Schnute growth model test"""
    time = [-2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 4.0]

    # Evaluate (1, 2, 3, 0.5) parameters
    value = [1.002476, 1.011048, 1.048606, 1.202606, 1.732051, 3.156482, 6.416469, 13.454897, 28.422836, 570.535348]

    for step in range(len(time)):
        assert schnute(time[step], 1, 2, 3, 0.5) == approx(value[step])

    # Evaluate (12, 2, 3, 0.2) parameters
    value = [1.643888, 1.644360, 1.646471, 1.655800, 1.695218, 1.837775, 2.205393, 2.862040, 3.825090, 12.662398]

    for step in range(len(time)):
        assert schnute(time[step], 12, 2, 3, 0.2) == approx(value[step])


def test_schnute_inverse():
    """Schnute inverse growth model test"""
    time = [1.0, 1.5, 2.0, 4.0]

    # Evaluate (1, 2, 3, 0.5) parameters
    value = [6.416469, 13.454897, 28.422836, 570.535348]

    for step in range(len(time)):
        assert schnute_inverse(value[step], 1, 2, 3, 0.5) == approx(time[step])

    # Evaluate (12, 2, 3, 0.2) parameters
    value = [2.205393, 2.862040, 3.825090, 12.662398]

    for step in range(len(time)):
        assert schnute_inverse(value[step], 12, 2, 3, 0.2) == approx(time[step])
