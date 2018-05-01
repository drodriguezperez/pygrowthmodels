"""Brody growth model"""

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


def brody(time, alpha, w0, rate):
    """
    Computes the Brody growth model

    Parameters
    ----------
    time : time
    alpha : upper asymptote
    w0 : a reference value at time = 0
    rate : growth rate

    See Also
    --------
    brody_inverse

    References
    ----------
    .. [1] M. M. Kaps, W. O. W. Herring, and W. R. W. Lamberson, "Genetic and
           environmental parameters for traits derived from the Brody growth
           curve and their relationships with weaning weight in Angus cattle.,"
           Journal of Animal Science, vol. 78, no. 6, pp. 1436-1442, May 2000.
    """

    result = alpha - (alpha - w0) * exp(- rate * time)

    return result


def brody_inverse(size, alpha, w0, rate):
    """
    Computes the inverse Brody growth model

    Parameters
    ----------
    size : size
    alpha : upper asymptote
    w0 : a reference value at time = 0
    rate : growth rate

    See Also
    --------
    brody

    References
    ----------
    .. [1] M. M. Kaps, W. O. W. Herring, and W. R. W. Lamberson, "Genetic and
           environmental parameters for traits derived from the Brody growth
           curve and their relationships with weaning weight in Angus cattle.,"
           Journal of Animal Science, vol. 78, no. 6, pp. 1436-1442, May 2000.
    """

    result = - log((alpha - size) / (alpha - w0)) / rate

    return result
