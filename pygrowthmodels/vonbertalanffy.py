"""von Bertalanffy growth model"""

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


def vonbertalanffy(time, alpha, beta, rate, slope):
    """
    Computes the von Bertalanffy growth model

    Parameters
    ----------
    time : time
    alpha : upper asymptote
    beta : growth displacement
    rate : growth rate
    slope : slope of growth

    See Also
    --------
    vonbertalanffy_inverse

    References
    ----------
    .. [1] D. Fekedulegn, M. Mac Siurtain, and J. Colbert, "Parameter estimation
           of nonlinear growth models in forestry," Silva Fennica, vol. 33,
           no. 4, pp. 327-336, 1999.
    """

    result = alpha ** (1 - slope) - beta * exp(-rate * time)
    result = result ** (1 / (1 - slope))

    return result


def vonbertalanffy_inverse(size, alpha, beta, rate, slope):
    """
    Computes the inverse of von Bertalanffy growth model

    Parameters
    ----------
    size : size
    alpha : upper asymptote
    beta : growth displacement
    rate : growth rate
    slope : slope of growth

    See Also
    --------
    vonbertalanffy

    References
    ----------
    .. [1] D. Fekedulegn, M. Mac Siurtain, and J. Colbert, "Parameter estimation
           of nonlinear growth models in forestry," Silva Fennica, vol. 33,
           no. 4, pp. 327-336, 1999.
    """

    if (alpha ** (1 - slope) - size ** (1 - slope)) == 0:
        result = float('inf')
    else:
        result = -log((alpha ** (1 - slope) - size ** (1 - slope)) / beta) / rate

    return result
