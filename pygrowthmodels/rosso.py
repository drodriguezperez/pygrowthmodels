"""Rosso growth model"""

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


def rosso(time, mu, lag, lower, alpha):
    """
    Computes the Rosso growth model

    Parameters
    ----------
    time : time
    mu : maximal growth rate
    lag : time lag
    lower : lower asymptote
    alpha : upper asymptote

    See Also
    --------
    rosso_inverse

    References
    ----------
    .. [1] T. Ross, "Indices for performance evaluation of predictive models in
           food microbiology." J. Appl. Bacteriol. vol. 81, no. 5, pp. 501-508.
           Nov. 1996.
    """

    if time <= lag:
        return lower
    else:
        return alpha - log(1 + (exp(alpha - lower) - 1) * exp(-mu * (time - lag)))


def rosso_inverse(size, mu, lag, lower, alpha):
    """
    Computes inverse of the Rosso growth model

    Parameters
    ----------
    size : size
    mu : maximal growth rate
    lag : time lag
    lower : lower asymptote
    alpha : upper asymptote

    See Also
    --------
    rosso

    References
    ----------
    .. [1] T. Ross, "Indices for performance evaluation of predictive models in
           food microbiology." J. Appl. Bacteriol. vol. 81, no. 5, pp. 501-508.
           Nov. 1996.
    """

    return lag - log((exp(alpha - size) - 1) / (exp(alpha - lower) - 1)) / mu
