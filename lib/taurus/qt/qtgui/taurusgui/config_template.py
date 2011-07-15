#!/usr/bin/env python

#############################################################################
##
## This file is part of Taurus, a Tango User Interface Library
## 
## http://www.tango-controls.org/static/taurus/latest/doc/html/index.html
##
## Copyright 2011 CELLS / ALBA Synchrotron, Bellaterra, Spain
## 
## Taurus is free software: you can redistribute it and/or modify
## it under the terms of the GNU Lesser General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## 
## Taurus is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Lesser General Public License for more details.
## 
## You should have received a copy of the GNU Lesser General Public License
## along with Taurus.  If not, see <http://www.gnu.org/licenses/>.
##
###########################################################################

"""
configuration file for an example of how to construct a GUI based on TaurusGUI  

This configuration file determines the default, permanent, pre-defined
contents of the GUI. While the user may add/remove more elements at run
time and those customizations will also be stored, this file defines what a
user will find when launching the GUI for the first time.
"""

##==============================================================================
## Import section. You probably want to keep this line. Don't edit this block 
## unless you know what you are doing
from taurus.qt.qtgui.taurusgui.utils import PanelDescription, ExternalApp, Qt_Qt
## (end of import section)
##==============================================================================

##===============================================================================
## Xml configuration. 
##
## Most of the configurations can be defined using the Application Settings
## Wizard (which can be launched by invoking "taurusgui --new-gui"). The wizard
## will create an xml file containing the configurations which can be imported
## here. 
## If the same variable is present both in the configuration file and in
## this file, the one in this file will be used.
##===============================================================================
#XML_CONFIG = 'config.xml'

##===============================================================================
## General info.
##===============================================================================
#GUI_NAME = 'MyGui'
#ORGANIZATION = 'Taurus'
#CUSTOM_LOGO = <full path to GUI-specific logo>

##===============================================================================
## Create synoptic panels by providing a list of Jdraw file names. If relative
## paths are given, the directory containing this configuration file will be used
## as root. 
## (comment out or make SYNOPTIC=None to skip creating synoptic panels)
##===============================================================================
#SYNOPTIC = ['foo.jdw','mypath/bar.jdw']

##===============================================================================
## Set INSTRUMENTS_FROM_POOL to True for enabling auto-creation of
## instrument panels based on the Pool Instrument info
##===============================================================================
#INSTRUMENTS_FROM_POOL = True

##===============================================================================
## You can define panels to be shown.  
## To define a panel, instantiate a PanelDescription object (see documentation
## for the gblgui_utils module)
## Note: The panels defined here will be created *in addition* to those
## defined in the XML configuration file.
##===============================================================================
#
#nxbrowser = PanelDescription('NeXus Browser',
#                       classname = 'TaurusNeXusBrowser',
#                       area = None)
#
#i0 = PanelDescription('BigInstrument',
#                       classname = 'TaurusAttrForm',
#                       area = Qt_Qt.TopDockWidgetArea,
#                       model = 'sys/tg_test/1')
#
#i1 = PanelDescription('instrument1',
#                       classname = 'TaurusForm',
#                       area = Qt_Qt.TopDockWidgetArea,
#                       model = ['sys/tg_test/1/double_scalar',
#                                'sys/tg_test/1/short_scalar_ro',
#                                'sys/tg_test/1/float_spectrum_ro',
#                                'sys/tg_test/1/double_spectrum'])
#
#i2 = PanelDescription('instrument2',
#                       classname = 'TaurusForm',
#                       area = Qt_Qt.TopDockWidgetArea,
#                       model = ['sys/tg_test/1/wave',
#                                'sys/tg_test/1/boolean_scalar'])
#
#trend = PanelDescription('Trend',
#                        classname = 'TaurusTrend',
#                        area = Qt_Qt.TopDockWidgetArea,
#                        model = ['sys/tg_test/1/double_scalar'])

##===============================================================================
## Define which external application launchers are to be inserted.
## To define an external application, instantiate an ExternalApp object
## See TaurusMainWindow.addExternalAppLauncher for valid values of ExternalApp
## Note: The launchers defined here will be created *in addition* to those
## defined in the XML configuration file.
##===============================================================================
#xterm = ExternalApp(cmdargs=['xterm','spock'], text="Spock", icon='utilities-terminal')
#hdfview = ExternalApp(["hdfview"])
#pymca = ExternalApp(['pymca'])

##===============================================================================
## Macro execution configuration
## (comment out or make MACRO_SERVER=None to skip creating a macro execution 
## infrastructure)
##===============================================================================
#MACROSERVER_NAME = 
#DOOR_NAME = 
#MACROEDITORS_PATH = 

##===============================================================================
## Monitor widget
##You can provide a list models (taurus attributes) that will be monitored in a
##small trend always visible
##===============================================================================
#MONITOR = ['sys/tg_test/1/double_scalar_rww']
