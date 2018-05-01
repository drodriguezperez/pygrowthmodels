"""Stannard growth model"""

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


def stannard(time, alpha, beta, rate, slope):
    """
    Computes the Stannard growth model

    Parameters
    ----------
    time : time
    alpha : upper asymptote
    beta : growth displacement
    rate : growth rate
    slope : slope of growth

    See Also
    --------
    stannard_inverse

    References
    ----------
    .. [1] A. Khamiz, Z. Ismail, and A. T. Muhammad, "Nonlinear growth models
           for modeling oil palm yield growth," Journal of Mathematics and
           Statistics, vol. 1, no. 3, p. 225, 2005.
    """

    result = alpha * (1 + exp(-(beta + rate * time) / slope)) ** (-slope)

    return result


def stannard_inverse(size, alpha, beta, rate, slope):
    """
    Computes the inverse of Stannard growth model

    Parameters
    ----------
    size : size
    alpha : upper asymptote
    beta : growth displacement
    rate : growth rate
    slope : slope of growth

    See Also
    --------
    stannard

    References
    ----------
    .. [1] A. Khamiz, Z. Ismail, and A. T. Muhammad, "Nonlinear growth models
           for modeling oil palm yield growth," Journal of Mathematics and
           Statistics, vol. 1, no. 3, p. 225, 2005.
    """

    if (alpha / size) ** (1 / slope) == 1:
        return float('inf')
    else:
        result = - (beta + slope * log((alpha / size) ** (1 / slope) - 1)) / rate

    return result
