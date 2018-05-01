"""Blumberg growth model"""


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


def blumberg(time, alpha, w0, slope, time_0=0):
    """
    Computes the Blumberg growth model

    Parameters
    ----------
    time : time
    alpha : upper asymptote
    w0 : a reference value at time = time_0
    slope : slope of growth
    time_0 : time shift (default 0)

    See Also
    --------
    blumberg_inverse

    References
    ----------
    .. [1] A. Tsoularis and J. Wallace, "Analysis of logistic growth models.,"
           Math Biosci, vol. 179, no. 1, pp. 21-55, Jul. 2002.
    """

    result = (alpha * (time + time_0) ** slope) / (w0 + (time + time_0) ** slope)

    return result


def blumberg_inverse(size, alpha, w0, slope, time_0=0):
    """
    Computes the inverse of Blumberg growth model

    Parameters
    ----------
    size : size
    alpha: upper asymptote.
    w0: a reference value at time = time_0
    slope: slope of growth
    time_0 time shift (default 0)

    See Also
    --------
    blumberg

    References
    ----------
    .. [1] A. Tsoularis and J. Wallace, "Analysis of logistic growth models.,"
           Math Biosci, vol. 179, no. 1, pp. 21-55, Jul. 2002.
    """

    result = (size * w0 / (alpha - size)) ** (1 / slope) - time_0

    return result
