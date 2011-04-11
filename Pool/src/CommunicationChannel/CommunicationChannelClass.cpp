static const char *RcsId     = "$Header$";
static const char *TagName   = "$Name$";
static const char *HttpServer= "http://www.esrf.fr/computing/cs/tango/tango_doc/ds_doc/";
//+=============================================================================
//
// file :        CommunicationChannelClass.cpp
//
// description : C++ source for the CommunicationChannelClass. A singleton
//               class derived from DeviceClass. It implements the
//               command list and all properties and methods required
//               by the CommunicationChannel once per process.
//
// project :     TANGO Device Server
//
// $Author$
//
// $Revision$
//
// $Log$
// Revision 1.2  2007/07/16 12:19:39  tcoutinho
// Changed Comunication to Communication
//
// Revision 1.1  2007/07/16 12:12:23  tcoutinho
// Unfortunately I made a syntax error and named 'Comunication' instead of 'Communication'. The old directory was ComunicationChannel
//
// Revision 1.5  2007/07/12 13:09:25  tcoutinho
// - added Open, Close, ReadLine methods
//
// Revision 1.4  2007/07/09 14:03:25  tcoutinho
// added open and close methods
//
// Revision 1.3  2007/06/28 16:22:37  tcoutinho
// safety commit during comunication channels development
//
// Revision 1.2  2007/06/28 07:15:34  tcoutinho
// safety commit during comunication channels development
//
// Revision 1.1  2007/06/27 08:54:55  tcoutinho
// first commit for comuncation channels
//
//
// copyleft :   European Synchrotron Radiation Facility
//              BP 220, Grenoble 38043
//              FRANCE
//
//-=============================================================================
//
//  		This file is generated by POGO
//	(Program Obviously used to Generate tango Object)
//
//         (c) - Software Engineering Group - ESRF
//=============================================================================


#include "CommunicationChannel.h"
#include "CommunicationChannelClass.h"
#include <tango.h>



//+----------------------------------------------------------------------------
/**
 *	Create CommunicationChannelClass singleton and return it in a C function for Python usage
 */
//+----------------------------------------------------------------------------
extern "C" {
#ifdef WIN32

__declspec(dllexport)

#endif

    Tango::DeviceClass *_create_CommunicationChannel_class(const char *name) {
        return CommunicationChannel_ns::CommunicationChannelClass::init(name);
    }
}


namespace CommunicationChannel_ns
{
//+----------------------------------------------------------------------------
//
// method : 		ReadLineClass::execute()
// 
// description : 	method to trigger the execution of the command.
//                PLEASE DO NOT MODIFY this method core without pogo   
//
// in : - device : The device on which the command must be excuted
//		- in_any : The command input data
//
// returns : The command output data (packed in the Any object)
//
//-----------------------------------------------------------------------------
CORBA::Any *ReadLineClass::execute(Tango::DeviceImpl *device,const CORBA::Any &in_any)
{

    cout2 << "ReadLineClass::execute(): arrived" << endl;

    return insert((static_cast<CommunicationChannel *>(device))->read_line());
}

//+----------------------------------------------------------------------------
//
// method : 		CloseClass::execute()
// 
// description : 	method to trigger the execution of the command.
//                PLEASE DO NOT MODIFY this method core without pogo   
//
// in : - device : The device on which the command must be excuted
//		- in_any : The command input data
//
// returns : The command output data (packed in the Any object)
//
//-----------------------------------------------------------------------------
CORBA::Any *CloseClass::execute(Tango::DeviceImpl *device,const CORBA::Any &in_any)
{

    cout2 << "CloseClass::execute(): arrived" << endl;

    ((static_cast<CommunicationChannel *>(device))->close());
    return new CORBA::Any();
}

//+----------------------------------------------------------------------------
//
// method : 		OpenClass::execute()
// 
// description : 	method to trigger the execution of the command.
//                PLEASE DO NOT MODIFY this method core without pogo   
//
// in : - device : The device on which the command must be excuted
//		- in_any : The command input data
//
// returns : The command output data (packed in the Any object)
//
//-----------------------------------------------------------------------------
CORBA::Any *OpenClass::execute(Tango::DeviceImpl *device,const CORBA::Any &in_any)
{

    cout2 << "OpenClass::execute(): arrived" << endl;

    ((static_cast<CommunicationChannel *>(device))->open());
    return new CORBA::Any();
}

//+----------------------------------------------------------------------------
//
// method : 		WriteReadCmd::execute()
// 
// description : 	method to trigger the execution of the command.
//                PLEASE DO NOT MODIFY this method core without pogo   
//
// in : - device : The device on which the command must be excuted
//		- in_any : The command input data
//
// returns : The command output data (packed in the Any object)
//
//-----------------------------------------------------------------------------
CORBA::Any *WriteReadCmd::execute(Tango::DeviceImpl *device,const CORBA::Any &in_any)
{

    cout2 << "WriteReadCmd::execute(): arrived" << endl;

    const Tango::DevVarCharArray	*argin;
    extract(in_any, argin);

    return insert((static_cast<CommunicationChannel *>(device))->write_read(argin));
}

//+----------------------------------------------------------------------------
//
// method : 		WriteCmd::execute()
// 
// description : 	method to trigger the execution of the command.
//                PLEASE DO NOT MODIFY this method core without pogo   
//
// in : - device : The device on which the command must be excuted
//		- in_any : The command input data
//
// returns : The command output data (packed in the Any object)
//
//-----------------------------------------------------------------------------
CORBA::Any *WriteCmd::execute(Tango::DeviceImpl *device,const CORBA::Any &in_any)
{

    cout2 << "WriteCmd::execute(): arrived" << endl;

    const Tango::DevVarCharArray	*argin;
    extract(in_any, argin);

    return insert((static_cast<CommunicationChannel *>(device))->write(argin));
}

//+----------------------------------------------------------------------------
//
// method : 		ReadCmd::execute()
// 
// description : 	method to trigger the execution of the command.
//                PLEASE DO NOT MODIFY this method core without pogo   
//
// in : - device : The device on which the command must be excuted
//		- in_any : The command input data
//
// returns : The command output data (packed in the Any object)
//
//-----------------------------------------------------------------------------
CORBA::Any *ReadCmd::execute(Tango::DeviceImpl *device,const CORBA::Any &in_any)
{

    cout2 << "ReadCmd::execute(): arrived" << endl;

    Tango::DevLong	argin;
    extract(in_any, argin);

    return insert((static_cast<CommunicationChannel *>(device))->read(argin));
}






//
//----------------------------------------------------------------
//	Initialize pointer for singleton pattern
//----------------------------------------------------------------
//
CommunicationChannelClass *CommunicationChannelClass::_instance = NULL;

//+----------------------------------------------------------------------------
//
// method : 		CommunicationChannelClass::CommunicationChannelClass(string &s)
// 
// description : 	constructor for the CommunicationChannelClass
//
// in : - s : The class name
//
//-----------------------------------------------------------------------------
CommunicationChannelClass::CommunicationChannelClass(string &s):DeviceClass(s)
{

    cout2 << "Entering CommunicationChannelClass constructor" << endl;
    set_default_property();
    get_class_property();
    write_class_property();
    
    nb_static_attr = 0;
    first_call_to_device_factory = true;

    cout2 << "Leaving CommunicationChannelClass constructor" << endl;

}
//+----------------------------------------------------------------------------
//
// method : 		CommunicationChannelClass::~CommunicationChannelClass()
// 
// description : 	destructor for the CommunicationChannelClass
//
//-----------------------------------------------------------------------------
CommunicationChannelClass::~CommunicationChannelClass()
{
    _instance = NULL;
}

//+----------------------------------------------------------------------------
//
// method : 		CommunicationChannelClass::instance
// 
// description : 	Create the object if not already done. Otherwise, just
//			return a pointer to the object
//
// in : - name : The class name
//
//-----------------------------------------------------------------------------
CommunicationChannelClass *CommunicationChannelClass::init(const char *name)
{
    if (_instance == NULL)
    {
        try
        {
            string s(name);
            _instance = new CommunicationChannelClass(s);
        }
        catch (bad_alloc)
        {
            throw;
        }		
    }		
    return _instance;
}

CommunicationChannelClass *CommunicationChannelClass::instance()
{
    if (_instance == NULL)
    {
        cerr << "Class is not initialised !!" << endl;
        exit(-1);
    }
    return _instance;
}

//+----------------------------------------------------------------------------
//
// method : 		CommunicationChannelClass::command_factory
// 
// description : 	Create the command object(s) and store them in the 
//			command list
//
//-----------------------------------------------------------------------------
void CommunicationChannelClass::command_factory()
{
    command_list.push_back(new ReadCmd("Read",
        Tango::DEV_LONG, Tango::DEVVAR_CHARARRAY,
        "Number of bytes to read from the Communication channel. 0 will return an empty array. -1 will read all available data",
        "The data stream read from the channel",
        Tango::OPERATOR));
    command_list.push_back(new WriteCmd("Write",
        Tango::DEVVAR_CHARARRAY, Tango::DEV_LONG,
        "The data stream to be sent to the Communication channel",
        "The number of bytes actually sent to the channel",
        Tango::OPERATOR));
    command_list.push_back(new WriteReadCmd("WriteRead",
        Tango::DEVVAR_CHARARRAY, Tango::DEVVAR_CHARARRAY,
        "The data stream to be sent to the Communication channel",
        "The data stream read from the channel",
        Tango::OPERATOR));
    command_list.push_back(new OpenClass("Open",
        Tango::DEV_VOID, Tango::DEV_VOID,
        "",
        "",
        Tango::OPERATOR));
    command_list.push_back(new CloseClass("Close",
        Tango::DEV_VOID, Tango::DEV_VOID,
        "",
        "",
        Tango::OPERATOR));
    command_list.push_back(new ReadLineClass("ReadLine",
        Tango::DEV_VOID, Tango::DEVVAR_CHARARRAY,
        "",
        "The character read from the communication channel",
        Tango::OPERATOR));

    //	add polling if any
    for (unsigned int i=0 ; i<command_list.size(); i++)
    {
    }
}

//+----------------------------------------------------------------------------
//
// method : 		CommunicationChannelClass::get_class_property
// 
// description : 	Get the class property for specified name.
//
// in :		string	name : The property name
//
//+----------------------------------------------------------------------------
Tango::DbDatum CommunicationChannelClass::get_class_property(string &prop_name)
{
    for (unsigned int i=0 ; i<cl_prop.size() ; i++)
        if (cl_prop[i].name == prop_name)
            return cl_prop[i];
    //	if not found, return  an empty DbDatum
    return Tango::DbDatum(prop_name);
}
//+----------------------------------------------------------------------------
//
// method : 		CommunicationChannelClass::get_default_device_property()
// 
// description : 	Return the default value for device property.
//
//-----------------------------------------------------------------------------
Tango::DbDatum CommunicationChannelClass::get_default_device_property(string &prop_name)
{
    for (unsigned int i=0 ; i<dev_def_prop.size() ; i++)
        if (dev_def_prop[i].name == prop_name)
            return dev_def_prop[i];
    //	if not found, return  an empty DbDatum
    return Tango::DbDatum(prop_name);
}

//+----------------------------------------------------------------------------
//
// method : 		CommunicationChannelClass::get_default_class_property()
// 
// description : 	Return the default value for class property.
//
//-----------------------------------------------------------------------------
Tango::DbDatum CommunicationChannelClass::get_default_class_property(string &prop_name)
{
    for (unsigned int i=0 ; i<cl_def_prop.size() ; i++)
        if (cl_def_prop[i].name == prop_name)
            return cl_def_prop[i];
    //	if not found, return  an empty DbDatum
    return Tango::DbDatum(prop_name);
}
//+----------------------------------------------------------------------------
//
// method : 		CommunicationChannelClass::device_factory
// 
// description : 	Create the device object(s) and store them in the 
//			device list
//
// in :		Tango::DevVarStringArray *devlist_ptr : The device name list
//
//-----------------------------------------------------------------------------
void CommunicationChannelClass::device_factory(const Tango::DevVarStringArray *devlist_ptr)
{

    //	Create all devices.(Automatic code generation)
    //-------------------------------------------------------------
    for (unsigned long i=0 ; i < devlist_ptr->length() ; i++)
    {
        cout4 << "Device name : " << (*devlist_ptr)[i].in() << endl;
                        
        // Create devices and add it into the device list
        //----------------------------------------------------
        device_list.push_back(new CommunicationChannel(this, (*devlist_ptr)[i]));							 

        // Export device to the outside world
        // Check before if database used.
        //---------------------------------------------
        if ((Tango::Util::_UseDb == true) && (Tango::Util::_FileDb == false))
            export_device(device_list.back());
        else
            export_device(device_list.back(), (*devlist_ptr)[i]);
    }
    //	End of Automatic code generation
    //-------------------------------------------------------------

    long nb_dev = device_list.size();

//
// Get the number of static attribute before any dynamic one is added
//
    
    if ((nb_dev != 0) && (first_call_to_device_factory == true))
    {
        nb_static_attr = device_list.back()->get_device_attr()->get_attr_nb();
        first_call_to_device_factory = false;
    }

//
// Create dynamic attribute but remove the unwanted ones
//
    
    long nb_new_device = devlist_ptr->length();
    long start_index;
    
    if (nb_dev != 0)
        start_index = nb_dev - nb_new_device;
    else
        start_index = 0;
        
    for (long i=0 ; i < nb_new_device ; i++)
    {
        if (static_cast<CommunicationChannel *>(device_list[start_index + i])->is_add_device_done() == true)
        {
            static_cast<CommunicationChannel *>(device_list[start_index + i])->create_dyn_attr();
            static_cast<CommunicationChannel *>(device_list[start_index + i])->remove_unwanted_dyn_attr_from_device();
        }	
    }	
}
//+----------------------------------------------------------------------------
//	Method: CommunicationChannelClass::attribute_factory(vector<Tango::Attr *> &att_list)
//-----------------------------------------------------------------------------
void CommunicationChannelClass::attribute_factory(vector<Tango::Attr *> &att_list)
{
    //	Attribute : SimulationMode
    SimulationModeAttrib	*simulation_mode = new SimulationModeAttrib();
    att_list.push_back(simulation_mode);

	//	Attribute : Instrument
	InstrumentAttrib	*instrument = new InstrumentAttrib();
	instrument->set_disp_level(Tango::EXPERT);
	att_list.push_back(instrument);
    
    //	End of Automatic code generation
    //-------------------------------------------------------------
}

//+----------------------------------------------------------------------------
//
// method : 		CommunicationChannelClass::get_class_property()
// 
// description : 	Read the class properties from database.
//
//-----------------------------------------------------------------------------
void CommunicationChannelClass::get_class_property()
{
    //	Initialize your default values here (if not done with  POGO).
    //------------------------------------------------------------------

    //	Read class properties from database.(Automatic code generation)
    //------------------------------------------------------------------

    //	Call database and extract values
    //--------------------------------------------
    if (Tango::Util::instance()->_UseDb==true)
        get_db_class()->get_property(cl_prop);
    Tango::DbDatum	def_prop;

    //	End of Automatic code generation
    //------------------------------------------------------------------

}

//+----------------------------------------------------------------------------
//
// method : 	CommunicationChannelClass::set_default_property
// 
// description: Set default property (class and device) for wizard.
//              For each property, add to wizard property name and description
//              If default value has been set, add it to wizard property and
//              store it in a DbDatum.
//
//-----------------------------------------------------------------------------
void CommunicationChannelClass::set_default_property()
{
    string	prop_name;
    string	prop_desc;
    string	prop_def;

    vector<string>	vect_data;
    //	Set Default Class Properties
    //	Set Default Device Properties
    prop_name = "id";
    prop_desc = "The communication channel identifier";
    prop_def  = "";
    if (prop_def.length()>0)
    {
        Tango::DbDatum	data(prop_name);
        data << vect_data ;
        dev_def_prop.push_back(data);
        add_wiz_dev_prop(prop_name, prop_desc,  prop_def);
    }
    else
        add_wiz_dev_prop(prop_name, prop_desc);

}
//+----------------------------------------------------------------------------
//
// method : 		CommunicationChannelClass::write_class_property
// 
// description : 	Set class description as property in database
//
//-----------------------------------------------------------------------------
void CommunicationChannelClass::write_class_property()
{
    //	First time, check if database used
    //--------------------------------------------
    if (Tango::Util::_UseDb == false)
        return;

    Tango::DbData	data;
    string	classname = get_name();
    string	header;
    string::size_type	start, end;

    //	Put title
    Tango::DbDatum	title("ProjectTitle");
    string	str_title("CommunicationChannel");
    title << str_title;
    data.push_back(title);

    //	Put Description
    Tango::DbDatum	description("Description");
    vector<string>	str_desc;
    str_desc.push_back("Communication Channel Device used by the Sardana project device pool");
    description << str_desc;
    data.push_back(description);
        
    //	put cvs location
    string	rcsId(RcsId);
    string	filename(classname);
    start = rcsId.find("/");
    if (start!=string::npos)
    {
        filename += "Class.cpp";
        end   = rcsId.find(filename);
        if (end>start)
        {
            string	strloc = rcsId.substr(start, end-start);
            //	Check if specific repository
            start = strloc.find("/cvsroot/");
            if (start!=string::npos && start>0)
            {
                string	repository = strloc.substr(0, start);
                if (repository.find("/segfs/")!=string::npos)
                    strloc = "ESRF:" + strloc.substr(start, strloc.length()-start);
            }
            Tango::DbDatum	cvs_loc("cvs_location");
            cvs_loc << strloc;
            data.push_back(cvs_loc);
        }
    }

    //	Get CVS tag revision
    string	tagname(TagName);
    header = "$Name: ";
    start = header.length();
    string	endstr(" $");
    end   = tagname.find(endstr);
    if (end!=string::npos && end>start)
    {
        string	strtag = tagname.substr(start, end-start);
        Tango::DbDatum	cvs_tag("cvs_tag");
        cvs_tag << strtag;
        data.push_back(cvs_tag);
    }

    //	Get URL location
    string	httpServ(HttpServer);
    if (httpServ.length()>0)
    {
        Tango::DbDatum	db_doc_url("doc_url");
        db_doc_url << httpServ;
        data.push_back(db_doc_url);
    }

    //  Put inheritance
    Tango::DbDatum	inher_datum("InheritedFrom");
    vector<string> inheritance;
    inheritance.push_back("Device_4Impl");
    inher_datum << inheritance;
    data.push_back(inher_datum);

    //	Call database and and values
    //--------------------------------------------
    get_db_class()->put_property(data);
}

}	// namespace