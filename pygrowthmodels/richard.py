"""Richard growth model"""

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


def richard(time, alpha, beta, rate, slope):
    """
    Computes the Richard growth model

    Parameters
    ----------
    time : time
    alpha : upper asymptote
    beta : growth range
    rate : growth rate
    slope : slope of growth

    See Also
    --------
    richard_inverse

    References
    ----------
    .. [1] D. Fekedulegn, M. Mac Siurtain, and J. Colbert, "Parameter estimation
           of nonlinear growth models in forestry," Silva Fennica, vol. 33, no.
           4, pp. 327-336, 1999.
    """

    result = (1 + beta * exp(-rate * time))

    if result < 0 and slope > 1:
        result = float('nan')
    else:
        result = result ** (1 / slope)
        result = alpha / result

    return result


def richard_inverse(size, alpha, beta, rate, slope):
    """
    Computes the inverse of Richard growth model

    Parameters
    ----------
    size : size
    alpha : upper asymptote
    beta : growth range
    rate : growth rate
    slope : slope of growth

    See Also
    --------
    richard

    References
    ----------
    .. [1] A. Khamiz, Z. Ismail, and A. T. Muhammad, "Nonlinear growth models
           for modeling oil palm yield growth," Journal of Mathematics and
           Statistics, vol. 1, no. 3, p. 225, 2005.
    """

    result = -log(((alpha / size) ** slope - 1) / beta) / rate

    return result


def generalised_richard(time, A, U, k, m, beta, t0=0):
    """
    Computes the Generalised Richard growth model

    Parameters
    ----------
    time : time
    A : the lower asymptote
    U : the upper asymptote
    k : growth range
    m : slope of growth
    beta : growth range
    t0 : time shift (default 0)

    See Also
    --------
    generalised_richard_inverse

    References
    ----------
    .. [1] D. Fekedulegn, M. Mac Siurtain, and J. Colbert, "Parameter estimation
           of nonlinear growth models in forestry," Silva Fennica, vol. 33, no.
           4, pp. 327-336, 1999.
    """

    result = A + richard(time - t0, U - A, beta, k, m)

    return result


def generalised_richard_inverse(size, A, U, k, m, beta, t0=0):
    """
    Computes the inverse of Generalised Richard growth model

    Parameters
    ----------
    size : size
    A : the lower asymptote
    U : the upper asymptote
    k : growth range
    m : slope of growth
    beta : growth range
    t0 : time shift (default 0)

    See Also
    --------
    generalised_richard

    References
    ----------
    .. [1] A. Khamiz, Z. Ismail, and A. T. Muhammad, "Nonlinear growth models
           for modeling oil palm yield growth," Journal of Mathematics and
           Statistics, vol. 1, no. 3, p. 225, 2005.
    """

    result = richard_inverse(size - A, U - A, beta, k, m) + t0

    return result
