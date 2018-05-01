"""Tests for the Monomolecular growth model"""

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

from pygrowthmodels import monomolecular
from pygrowthmodels import monomolecular_inverse


def test_monomolecular():
    """Monomolecular growth model test"""
    time = [-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0]

    # Evaluate (1, 2, 3) parameters
    value = [-1.790343e+002, -3.917107e+001, -7.963378e+000, -1, 5.537397e-001, 9.004259e-001, 9.777820e-001,
             9.950425e-001]

    for step in range(len(time)):
        assert monomolecular(time[step], 1, 2, 3) == approx(value[step])

    # Evaluate (12, 1, 2) parameters
    value = [-2.290264e+002, -7.666867e+001, -2.061938e+001, 0, 7.585447e+000, 1.037598e+001, 1.140256e+001,
             1.178021e+001]

    for step in range(len(time)):
        assert monomolecular(time[step], 12, 1, 2) == approx(value[step])


def test_monomolecular_inverse():
    """Monomolecular invserse growth model test"""
    time = [-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0]

    # Evaluate (1, 2, 3) parameters
    value = [-1.790343e+002, -3.917107e+001, -7.963378e+000, -1, 5.537397e-001, 9.004259e-001, 9.777820e-001,
             9.950425e-001]

    for step in range(len(time)):
        assert monomolecular_inverse(value[step], 1, 2, 3) == approx(time[step])


def test_monomolecular_inverse_nan():
    """NaN in Monomolecular invserse growth model test"""
    assert monomolecular_inverse(10, 1, 2, 3) == approx(float('nan'), nan_ok=True)
