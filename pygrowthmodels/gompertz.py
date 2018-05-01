"""Gompertz exponential growth model"""

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


def gompertz(time, alpha, beta, rate):
    """
    Computes the Gompertz exponential growth model

    Parameters
    ----------
    time : time
    alpha : upper asymptote
    beta : growth displacement
    rate : growth rate

    See Also
    --------
    gompertz_inverse

    References
    ----------
    .. [1] D. Fekedulegn, M. Mac Siurtain, and J. Colbert, "Parameter estimation
           of nonlinear growth models in forestry," Silva Fennica, vol. 33,
           no. 4, pp. 327-336, 1999.
    """

    result = alpha * exp(-beta * exp(-rate * time))

    return result


def gompertz_inverse(size, alpha, beta, rate):
    """
    Computes the inverse of Gompertz exponential growth model

    Parameters
    ----------
    size : size
    alpha : upper asymptote
    beta : growth displacement
    rate : growth rate

    See Also
    --------
    gompertz

    References
    ----------
    .. [1] D. Fekedulegn, M. Mac Siurtain, and J. Colbert, "Parameter estimation
           of nonlinear growth models in forestry," Silva Fennica, vol. 33,
           no. 4, pp. 327-336, 1999.
    """

    if size == 0:
        result = float('nan')
    else:
        result = - log(-log(size / alpha) / beta) / rate

    return result
