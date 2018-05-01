"""Schnute growth model"""

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


def schnute(time, r0, beta, k, m):
    """
    Computes the Schnute growth model

    Parameters
    ----------
    time : time
    r0 : reference value
    beta : growth displacement
    k : growth rate
    m : slope of growth

    See Also
    --------
    schnute_inverse

    References
    ----------
    .. [1] A. Khamiz, Z. Ismail, and A. T. Muhammad, "Nonlinear growth models
           for modeling oil palm yield growth," Journal of Mathematics and
           Statistics, vol. 1, no. 3, p. 225, 2005.
    """

    result = (r0 + beta * exp(k * time)) ** m

    return result


def schnute_inverse(size, r0, beta, k, m):
    """
    Computes the inverse of Schnute growth model

    Parameters
    ----------
    size : size
    r0 : reference value
    beta : growth displacement
    k : growth rate
    m : slope of growth

    See Also
    --------
    schnute

    References
    ----------
    .. [1] A. Khamiz, Z. Ismail, and A. T. Muhammad, "Nonlinear growth models
           for modeling oil palm yield growth," Journal of Mathematics and
           Statistics, vol. 1, no. 3, p. 225, 2005.
    """

    result = log((size ** (1 / m) - r0) / beta) / k

    return result
