#############################################################################
##
# This file is part of Taurus
##
# http://taurus-scada.org
##
# Copyright 2011 CELLS / ALBA Synchrotron, Bellaterra, Spain
##
# Taurus is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
##
# Taurus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
##
# You should have received a copy of the GNU Lesser General Public License
# along with Taurus.  If not, see <http://www.gnu.org/licenses/>.
##
#############################################################################

"""
This module provides a factory for a generic plot widget
and cli command
"""

__all__ = [
    "EP_GROUP_PLOT",
    "get_plot_entry_points",
    "get_plot_class",
    "get_plot_widget",
    "TaurusPlot",
]


from taurus.core.util.plugin import selectEntryPoints


EP_GROUP_PLOT = "taurus.alt.plot"


def get_plot_entry_points(include=(".*",), exclude=()):
    return selectEntryPoints(EP_GROUP_PLOT, include=include, exclude=exclude)


def get_plot_class(include=(".*",), exclude=()):
    """
    Factory that returns a class that complies with a minimal
    TaurusPlot interface. The selection is done among the classes registered in
    the `taurus.alt.plot` entry-point, prioritized according to the given
    `include` and `exclude` patterns
    (see :function:`taurus.core.util.plugin.selectEntryPoints`)
    """
    eps = selectEntryPoints(EP_GROUP_PLOT, include=include, exclude=exclude)
    for ep in eps:
        try:
            return ep.load()
        except:
            pass
    raise ImportError("Could not load any plot class from {}".format(eps))


def get_plot_widget(*args, **kwargs):
    """
    Factory that returns a widget instance that complies with
    a minimal TaurusPlot interface.

    .. seealso:: :class:`get_plot_class`
    """

    return get_plot_class()(*args, **kwargs)


TaurusPlot = get_plot_widget