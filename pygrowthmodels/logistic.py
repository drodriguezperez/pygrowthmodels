"""Logistic growth model"""

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


def logistic(time, alpha, beta, rate):
    """
    Computes the Logistic growth model

    Parameters
    ----------
    time : time
    alpha : upper asymptote
    beta : growth range
    rate : growth rate

    See Also
    --------
    logistic_inverse, generalised_logistic, generalised_logistic_inverse

    References
    ----------
    .. [1] D. Fekedulegn, M. Mac Siurtain, and J. Colbert, "Parameter estimation
           of nonlinear growth models in forestry," Silva Fennica, vol. 33,
           no. 4, pp. 327-336, 1999.
    """

    result = alpha / (1 + beta * exp(-rate * time))

    return (result)


def logistic_inverse(size, alpha, beta, rate):
    """
    Computes the inverse of Logistic growth model

    Parameters
    ----------
    size : size
    alpha : upper asymptote
    beta : growth range
    rate : growth rate

    See Also
    --------
    logistic, generalised_logistic, generalised_logistic_inverse

    References
    ----------
    .. [1] D. Fekedulegn, M. Mac Siurtain, and J. Colbert, "Parameter estimation
           of nonlinear growth models in forestry," Silva Fennica, vol. 33,
           no. 4, pp. 327-336, 1999.
    """

    if size == 0:
        result = float('nan');
    else:
        result = - log((alpha - size) / (beta * size)) / rate

    return (result)


def generalised_logistic(time, A, U, k, beta, time_0=0):
    """
    Computes the Generalised Logistic growth model

    Parameters
    ----------
    time : time
    A : the lower asymptote
    U : the upper asymptote
    k : growth range
    beta : growth range
    time_0 : time shift (default 0)

    See Also
    --------
    logistic, logistic_inverse, generalised_logistic_inverse
    """

    result = A + logistic(time - time_0, U - A, beta, k)

    return result


def generalised_logistic_inverse(size, A, U, k, beta, time_0=0):
    """
    Computes the inverse of Generalised Logistic growth model

    Parameters
    ----------
    size: size
    A : the lower asymptote
    U : the upper asymptote
    k : growth range
    beta : growth range
    time_0 : time shift (default 0)

    See Also
    --------
    logistic, logistic_inverse, generalised_logistic
    """

    result = logistic_inverse(size - A, U - A, beta, k) + time_0

    return result
