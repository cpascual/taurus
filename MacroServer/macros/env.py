from macro import *

################################################################################
#
# Environment related macros
#
################################################################################

try:
    from lxml import etree
except ImportError:
    try:
        # Python 2.5
        import xml.etree.cElementTree as etree
        print "Using python native cElemenTree XML library"
    except ImportError:
        try:
            # Python 2.5
            import xml.etree.ElementTree as etree
            print "Using python native ElemenTree XML library"
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree
                print "Using python normal cElemenTree XML library"
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree
                    print "Using python normal ElemenTree XML library"
                except ImportError:
                    print "Could not find any suitable XML library"
                    sys.exit(1)


class dumpenv(Macro):
    """Dumps the complete environment"""
    
    def run(self):
        m = self.getManager()
        env = m.getEnv()
        out = List(['Name','Value'])
        for k,v in env.iteritems():
            out.appendRow([str(k), str(v)])

        for line in out.genOutput():
            self.output(line)

class lsenv(Macro):
    """Lists the environment"""
    
    param_def = [
        ['macro_list',
         ParamRepeat(['macro', Type.Macro, None, 'macro name'], min=0),
         None, 'List of macros to show environment'],
    ]
    
    def prepare(self, *macro_list, **opts):
        self.table_opts = opts
        
    def run(self, *macro_list):
        # we cannot use the macro.getEnv because by default it uses the 
        # current macro name so we use the manager API directly
        m = self.getManager()
        door_name = self.getDoorName()
        
        # list the environment for the current door
        if len(macro_list) == 0:
            # list All the environment for the current door
            out = List(['Name','Value','Type'])
            env = m.getAllDoorEnv(door_name)
            for k,v in env.iteritems():
                str_val = self.reprValue(v)
                out.appendRow([str(k), str_val, str(type(v))])
        else:
            # list the environment for the current door for the given macros
            out = List(['Macro', 'Name', 'Value', 'Type'])
            for macro_name in macro_list:
                macro_env = m.getMacroClass(macro_name).env
                env = m.getDoorMacroEnv(door_name, macro_name, macro_env)
                for k, v in env.iteritems():
                    out.appendRow([ macro_name, k, self.reprValue(v), str(type(v)) ])

        for line in out.genOutput():
            self.output(line)

    def reprValue(self, v, max=54):
        # cut long strings
        v = str(v)
        if len(v) > max: v = '%s [...]' % v[:max]
        return v

class senv(Macro):
    """Sets the given environment variable to the given value"""

    param_def = [['name', Type.Env, None, 'Environment variable name'],
                 ['value_list',
                  ParamRepeat(['value', Type.String, None, 'environment value item'], min=1),
                  None, 'value(s). one item will eval to a single element. More than one item will eval to a tuple of elements'],
                ]

    def run(self, env, *value):
        if len(value) == 1: 
            value = value[0]
        else:
            value = '(%s)' % ', '.join(value)
        k,v = self.setEnv(env, value)
        line = '%s = %s' % (k, str(v))
        self.output(line)

class usenv(Macro):
    """Unsets the given environment variable"""
    param_def = [
        ['environment_list',
         ParamRepeat(['env', Type.Env, None, 'Environment variable name'], min=1),
         None, 'List of environment items to be removed'],
    ]    
    
    def run(self, *env):
        self.unsetEnv(env)
        self.output("Success!")
        
class load_env(Macro):
    """ Read environment variables from config_env.xml file"""
    
    def run(self):
        doc = etree.parse("config_env.xml")       
        root = doc.getroot()
        for element in root:
            if element.find("./name").text == "auto_filter":
                self.output("Loading auto_filter variables:")
                filter_max_elem = element.find(".//FilterMax")
                if filter_max_elem is not None:
                    filter_max = filter_max_elem.text
                    self.setEnv("FilterMax", filter_max)
                    self.output("FilterMax loaded")
                else:
                    self.output("FilterMax not found")
                filter_min_elem = element.find(".//FilterMin")
                if filter_min_elem is not None:
                    filter_min = filter_max_elem.text
                    self.setEnv("FilterMin", filter_min)
                    self.output("FilterMin loaded")
                else:
                    self.output("FilterMin not found")
                filter_delta_elem = element.find(".//FilterDelta")
                if filter_delta_elem is not None:
                    filter_delta = filter_delta_elem.text
                    self.setEnv("FilterDelta", filter_delta)
                    self.output("FilterDelta loaded")
                else:
                    self.output("FilterDelta not found")
                filter_signal_elem = element.find(".//FilterSignal")
                if filter_signal_elem is not None:
                    filter_signal = filter_signal_elem.text
                    self.setEnv("FilterSignal", filter_signal)
                    self.output("FilterSignal loaded")
                else:
                    self.output("FilterSignal not found")
                filter_absorber_elem = element.find(".//FilterAbsorber")
                if filter_absorber_elem is not None:
                    filter_absorber = filter_absorber_elem.text
                    self.setEnv("FilterAbsorber", filter_absorber)
                    self.output("FilterAbsorber loaded")
                else:
                    self.output("FilterAbsorber not found")
                auto_filter_elem = element.find(".//AutoFilter")
                if auto_filter_elem is not None:
                    auto_filter = auto_filter_elem.text
                    self.setEnv("AutoFilter", auto_filter)
                    self.output("AutoFilter loaded")
                else:
                    self.output("AutoFilter not found")
            if element.find("./name").text == "auto_beamshutter":
                self.output("Loading auto_beamshutter variables:")
                auto_beamshutter_elem = element.find(".//AutoBeamshutter")
                if auto_beamshutter_elem is not None:
                    auto_beamshutter = auto_beamshutter_elem.text
                    self.setEnv("AutoBeamshutter", auto_beamshutter)
                    self.output("AutoBeamshutter loaded")
                else:
                    self.output("AutoBeamshutter not found")
                beamshutter_limit_elem = element.find(".//BeamshutterLimit")
                if beamshutter_limit_elem is not None:
                    beamshutter_limit = beamshutter_limit_elem.text
                    self.setEnv("BeamshutterLimit", beamshutter_limit)
                    self.output("BeamshutterLimit loaded")
                else:
                    self.output("BeamshutterLimit not found")
                beamshutter_signal_elem = element.find(".//BeamshutterSignal")
                if beamshutter_signal_elem is not None:
                    beamshutter_signal = beamshutter_signal_elem.text
                    self.setEnv("BeamshutterSignal", beamshutter_signal)
                    self.output("BeamshutterSignal loaded")
                else:
                    self.output("BeamshutterSignal not found")
                beamshutter_time_elem = element.find(".//BeamshutterTime")
                if beamshutter_time_elem is not None:
                    beamshutter_time = beamshutter_time_elem.text
                    self.setEnv("BeamshutterTime", beamshutter_time)
                    self.output("BeamshutterTime loaded")
                else:
                    self.output("BeamshutterTime not found")
            if element.find("./name").text == "exafs":
                self.output("Loading exafs variables:")
                exafs_int_times_elem = element.find(".//ExafsIntTimes")
                if exafs_int_times_elem is not None:
                    exafs_int_times = exafs_int_times_elem.text
                    self.setEnv("ExafsIntTimes", exafs_int_times)
                    self.output("ExafsIntTimes loaded")
                else:
                    self.output("ExafsIntTimes not found")
                exafs_nb_intervals_elem = element.find(".//ExafsNbIntervals")
                if exafs_nb_intervals_elem is not None:
                    exafs_nb_intervals = exafs_nb_intervals_elem.text
                    self.setEnv("ExafsNbIntervals", exafs_nb_intervals)
                    self.output("ExafsNbIntervals loaded")
                else:
                    self.output("ExafsNbIntervals not found")
                exafs_regions_elem = element.find(".//ExafsRegions")
                if exafs_regions_elem is not None:
                    exafs_regions = exafs_regions_elem.text
                    self.setEnv("ExafsRegions", exafs_regions)
                    self.output("ExafsRegions loaded")
                else:
                    self.output("ExafsRegions not found")  
        misc_tree = root.find("./miscellaneous")
        if misc_tree is not None:
            for parameter in misc_tree:
                if parameter.tag != "name":
                    self.setEnv(parameter.tag, parameter.text) 
            