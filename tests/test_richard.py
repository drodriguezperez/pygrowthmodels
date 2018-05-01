"""Tests for the Richard growth model"""

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

from pygrowthmodels import generalised_richard
from pygrowthmodels import generalised_richard_inverse
from pygrowthmodels import richard
from pygrowthmodels import richard_inverse


def test_richard():
    """Richard growth model test"""
    assert richard(-2.0, 12, 2, 3, 1) == approx(1.485410e-002)
    assert richard(-1.5, 12, 2, 3, 1) == approx(6.628579e-002)
    assert richard(-1.0, 12, 2, 3, 1) == approx(2.914668e-001)
    assert richard(-0.5, 12, 2, 3, 1) == approx(1.204411e+000)
    assert richard(0.0, 12, 2, 3, 1) == approx(4)
    assert richard(0.5, 12, 2, 3, 1) == approx(8.297261e+000)
    assert richard(1.0, 12, 2, 3, 1) == approx(1.091332e+001)
    assert richard(1.5, 12, 2, 3, 1) == approx(1.173918e+001)
    assert richard(2.0, 12, 2, 3, 1) == approx(1.194080e+001)


def test_richard_inverse():
    """Richard inverse growth model test"""
    assert richard_inverse(1.485410e-002, 12, 2, 3, 1) == approx(-2.0)
    assert richard_inverse(6.628579e-002, 12, 2, 3, 1) == approx(-1.5)
    assert richard_inverse(2.914668e-001, 12, 2, 3, 1) == approx(-1.0)
    assert richard_inverse(1.204411e+000, 12, 2, 3, 1) == approx(-0.5)
    assert richard_inverse(4, 12, 2, 3, 1) == approx(0.0)
    assert richard_inverse(8.297261e+000, 12, 2, 3, 1) == approx(0.5)
    assert richard_inverse(1.173918e+001, 12, 2, 3, 1) == approx(1.5)


def test_richard_nan():
    """NaN in Richard inverse growth model test"""
    assert richard(-2.0, 1, -2, 3, 4) == approx(float('nan'), nan_ok=True)
    assert richard(-1.5, 1, -2, 3, 4) == approx(float('nan'), nan_ok=True)
    assert richard(-1.0, 1, -2, 3, 4) == approx(float('nan'), nan_ok=True)
    assert richard(-0.5, 1, -2, 3, 4) == approx(float('nan'), nan_ok=True)
    assert richard(0.0, 1, -2, 3, 4) == approx(float('nan'), nan_ok=True)


def test_generalised_richard():
    """Generalised Richard growth model test"""
    assert generalised_richard(-2.0, 1, 3, 5, 4, 2, 0) == approx(1.13804918)
    assert generalised_richard(-1.5, 1, 3, 5, 4, 2, 0) == approx(1.25789346)
    assert generalised_richard(-1.0, 1, 3, 5, 4, 2, 0) == approx(1.48143674)
    assert generalised_richard(-0.5, 1, 3, 5, 4, 2, 0) == approx(1.89119211)
    assert generalised_richard(0.0, 1, 3, 5, 4, 2, 0) == approx(2.51967137)
    assert generalised_richard(0.5, 1, 3, 5, 4, 2, 0) == approx(2.92542185)
    assert generalised_richard(1.0, 1, 3, 5, 4, 2, 0) == approx(2.99331824)
    assert generalised_richard(1.5, 1, 3, 5, 4, 2, 0) == approx(2.99944730)
    assert generalised_richard(2.0, 1, 3, 5, 4, 2, 0) == approx(2.99995460)

    assert generalised_richard(-2.0, 12, 4, 5, 1, 2, 1) == approx(11.99999878)
    assert generalised_richard(-1.5, 12, 4, 5, 1, 2, 1) == approx(11.99998509)
    assert generalised_richard(-1.0, 12, 4, 5, 1, 2, 1) == approx(11.99981840)
    assert generalised_richard(-0.5, 12, 4, 5, 1, 2, 1) == approx(11.99778827)
    assert generalised_richard(0.0, 12, 4, 5, 1, 2, 1) == approx(11.97313871)
    assert generalised_richard(0.5, 12, 4, 5, 1, 2, 1) == approx(11.68460462)
    assert generalised_richard(1.0, 12, 4, 5, 1, 2, 1) == approx(9.33333333)
    assert generalised_richard(1.5, 12, 4, 5, 1, 2, 1) == approx(5.12815137)
    assert generalised_richard(2.0, 12, 4, 5, 1, 2, 1) == approx(4.10637367)


def test_generalised_richard_invserse():
    """Generalised Richard inverse growth model test"""
    assert generalised_richard_inverse(1.13804918, 1, 3, 5, 4, 2, 0) == approx(-2.0)
    assert generalised_richard_inverse(1.25789346, 1, 3, 5, 4, 2, 0) == approx(-1.5)
    assert generalised_richard_inverse(1.48143674, 1, 3, 5, 4, 2, 0) == approx(-1.0)
    assert generalised_richard_inverse(1.89119211, 1, 3, 5, 4, 2, 0) == approx(-0.5)
    assert generalised_richard_inverse(2.92542185, 1, 3, 5, 4, 2, 0) == approx(0.5)
    assert generalised_richard_inverse(2.99331824, 1, 3, 5, 4, 2, 0) == approx(1.0)
    assert generalised_richard_inverse(2.99944730, 1, 3, 5, 4, 2, 0) == approx(1.5)

    assert generalised_richard_inverse(11.99778827, 12, 4, 5, 1, 2, 1) == approx(-0.5)
    assert generalised_richard_inverse(11.68460462, 12, 4, 5, 1, 2, 1) == approx(0.5)
    assert generalised_richard_inverse(9.33333333, 12, 4, 5, 1, 2, 1) == approx(1.0)
    assert generalised_richard_inverse(5.12815137, 12, 4, 5, 1, 2, 1) == approx(1.5)
    assert generalised_richard_inverse(4.10637367, 12, 4, 5, 1, 2, 1) == approx(2.0)
