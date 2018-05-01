"""Morgan-Mercer-Flodin growth model"""


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


def mmf(time, alpha, w0, gamma, rate):
    """
    Computes the Morgan-Mercer-Flodin growth model

    Parameters
    ----------
    time : time
    alpha : upper asymptote
    w0 : the value at time = 0
    gamma : parameter that controls the point of inflection
    rate : growth rate

    See Also
    --------
    mmf_inverse

    References
    ----------
    .. [1] A. Khamiz, Z. Ismail, and A. T. Muhammad, "Nonlinear growth models
           for modeling oil palm yield growth," Journal of Mathematics and
           Statistics, vol. 1, no. 3, p. 225, 2005.
    """

    result = (w0 * gamma + alpha * time ** rate) / (gamma + time ** rate)

    return result


def mmf_inverse(size, alpha, w0, gamma, rate):
    """
    Computes the inverse of Morgan-Mercer-Flodin growth model

    Parameters
    ----------
    size : size
    alpha : upper asymptote
    w0 : the value at time = 0
    gamma : parameter that controls the point of inflection
    rate : growth rate

    See Also
    --------
    mmf

    References
    ----------
    .. [1] A. Khamiz, Z. Ismail, and A. T. Muhammad, "Nonlinear growth models
           for modeling oil palm yield growth," Journal of Mathematics and
           Statistics, vol. 1, no. 3, p. 225, 2005.
    """

    result = (gamma * (w0 - size) / (size - alpha)) ** (1 / rate)

    return result
