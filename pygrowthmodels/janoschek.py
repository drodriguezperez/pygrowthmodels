"""Tests for the Janoschek growth model"""

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

from math import exp
from math import log


def janoschek(time, lower, alpha, rate, delta):
    """
        Computes the Janoschek growth model

        Parameters
        ----------
        time : time
        lower : lower asymptote
        alpha : upper asymptote
        rate : growth rate
        delta : the point of inflection.
    """

    result = lower - (lower - alpha) * exp(-rate * time ** delta)

    return result


def janoschek_inverse(size, lower, alpha, rate, delta):
    result = (log((lower - alpha) / (lower - size)) / rate) ** (1 / delta)

    return result
