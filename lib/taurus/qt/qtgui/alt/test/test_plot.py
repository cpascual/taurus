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

import pytest
from pkg_resources import parse_version
import taurus.qt.qtgui.alt.plot as altplot
from taurus.core.util.test.test_plugin import mock_entry_point

try:
    import taurus_pyqtgraph as tpg
    tpg_version = parse_version(tpg.__version__)
except:
    tpg_version = parse_version("0")


class _MockPlot(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.model = None

    def setModel(self, model):
        self.model = model


@pytest.mark.skipif(tpg_version < parse_version("0.3.4"),
                    reason="taurus_pyqtgraph >= 0.3.4 required"
                    )
def test_get_plot_entry_points():
    """Check that, if taurus_pyqtgraph is installed, it provides a plot"""
    assert "tpg" in [ep.name for ep in altplot.get_plot_entry_points()]
    klass = altplot.get_plot_entry_points(include=("tpg",))[0].load()
    assert "taurus_pyqtgraph." in klass.__module__


def test_alt_plot_class(monkeypatch):
    lines = ["mock{}={}:_MockPlot".format(i, __name__) for i in range(3)]
    mapping = mock_entry_point(lines)
    group_name = list(mapping.keys())[0]
    monkeypatch.setattr(altplot, "EP_GROUP_PLOT", group_name)
    assert altplot.get_plot_class() == _MockPlot


def test_onebad_alt_plot_class(monkeypatch):
    lines = ["bad=_unimportablemod:Bad", "good={}:_MockPlot".format(__name__)]
    mapping = mock_entry_point(lines)
    group_name = list(mapping.keys())[0]
    monkeypatch.setattr(altplot, "EP_GROUP_PLOT", group_name)
    assert altplot.get_plot_class() == _MockPlot


def test_onlybad_alt_plot_class(monkeypatch):
    lines = ["bad=_unimportablemod:Bad"]
    mapping = mock_entry_point(lines)
    group_name = list(mapping.keys())[0]
    monkeypatch.setattr(altplot, "EP_GROUP_PLOT", group_name)
    with pytest.raises(ImportError) as exc_info:
        altplot.get_plot_class()
    assert "bad = _unimportablemod:Bad" in str(exc_info.value)


def test_alt_plot_widget(qtbot, monkeypatch):
    from taurus.qt.qtgui.alt import TaurusPlot

    def mock_get_plot_class():
        return _MockPlot

    monkeypatch.setattr(altplot, "get_plot_class", mock_get_plot_class)
    w = TaurusPlot("foo", bar=1)
    assert isinstance(w, _MockPlot)
    assert w.args == ("foo",)
    assert w.kwargs == {"bar": 1}

