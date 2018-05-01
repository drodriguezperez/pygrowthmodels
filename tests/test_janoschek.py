"""Janoschek growth model"""

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

from pygrowthmodels import janoschek
from pygrowthmodels import janoschek_inverse


def test_janoschek():
    """Janoschek growth model test"""
    time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Evaluate (10, 2, 0.25, 2) parameters
    value = [2, 3.769594, 7.056964, 9.156806, 9.853475, 9.984556, 9.999013, 9.999962, 9.999999, 10]

    for step in range(len(time)):
        assert janoschek(time[step], 10, 2, 0.25, 2) == approx(value[step])


def test_janoschek_inverse():
    """Janoschek invserse growth model test"""
    time = [0, 1, 2, 3, 4]

    # Evaluate (10, 2, 0.25, 2) parameters
    value = [2, 3.769594, 7.056964, 9.156806, 9.853475]

    for step in range(len(time)):
        assert janoschek_inverse(value[step], 10, 2, 0.25, 2) == approx(time[step])
