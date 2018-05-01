"""Mitcherlich growth model"""

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

from math import log


def mitcherlich(time, alpha, beta, rate):
    """
    Computes the Mitcherlich growth model

    Parameters
    ----------
    time : time
    alpha : upper asymptote
    beta : growth range
    rate : growth rate

    See Also
    --------
    mitcherlich_inverse

    References
    ----------
    .. [1] D. Fekedulegn, M. Mac Siurtain, and J. Colbert, "Parameter estimation
           of nonlinear growth models in forestry," Silva Fennica, vol. 33,
           no. 4, pp. 327-336, 1999.
    """

    result = alpha - beta * rate ** time

    return result


def mitcherlich_inverse(size, alpha, beta, rate):
    """
    Computes the inverse of Mitcherlich growth model

    Parameters
    ----------
    size : size
    alpha : upper asymptote
    beta : growth range
    rate : growth rate

    See Also
    --------
    mitcherlich

    References
    ----------
    .. [1] D. Fekedulegn, M. Mac Siurtain, and J. Colbert, "Parameter estimation
           of nonlinear growth models in forestry," Silva Fennica, vol. 33,
           no. 4, pp. 327-336, 1999.
    """

    if alpha > size:
        result = log((alpha - size) / beta) / log(rate)
    else:
        result = float('nan')

    return result
