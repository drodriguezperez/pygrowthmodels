"""Tests for the Rosso growth model"""

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

from pygrowthmodels import rosso
from pygrowthmodels import rosso_inverse


def test_rosso():
    """Rosso growth model test"""

    time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Evaluate (0.05, 2, 1, 10) parameters
    value = [1, 1, 1, 1.049994, 1.099987, 1.149980, 1.199973, 1.249965, 1.299957, 1.349948, 1.399939]

    for step in range(len(time)):
        assert rosso(time[step], 0.05, 2, 1, 10) == approx(value[step])

    # Evaluate (0.15, 1, 1, 100) parameters
    value = [1, 1, 1.15, 1.30, 1.45, 1.60, 1.75, 1.90, 2.05, 2.20, 2.35]

    for step in range(len(time)):
        assert rosso(time[step], 0.15, 1, 1, 100) == approx(value[step])

    # Evaluate (0.15, 20, 1, 100) parameters
    for step in range(len(time)):
        assert rosso(time[step], 0.15, 20, 1, 100) == approx(1)


def test_rosso_inverse():
    """Rosso inverse growth model test"""

    time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Evaluate (0.05, 0, 1, 10) parameters
    value = [1, 1.0499937, 1.0999870, 1.1499800, 1.1999727, 1.2499649, 1.2999568, 1.3499483, 1.3999393, 1.4499299,
             1.4999199]

    for step in range(len(time)):
        assert rosso_inverse(value[step], 0.05, 0, 1, 10) == approx(time[step])

    # Evaluate (0.15, 0, 1, 100) parameters
    value = [1.00, 1.15, 1.30, 1.45, 1.60, 1.75, 1.90, 2.05, 2.20, 2.35, 2.50]

    for step in range(len(time)):
        assert rosso_inverse(value[step], 0.15, 0, 1, 100) == approx(time[step])

    # Evaluate (0.15, 20, 1, 100) parameters
    assert rosso_inverse(1, 0.15, 20, 1, 100) == approx(20)
