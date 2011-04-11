//+=============================================================================
//
// file :        main.cpp
//
// description : C++ source for a TANGO device server main.
//               The main rule is to initialise (and create) the Tango
//               system and to create the DServerClass singleton.
//               The main should be the same for every Tango device server.
//
// project :     TANGO Device Server
//
// $Author$
//
// $Revision$ $
//
// $Log$
// Revision 1.3  2006/07/07 12:38:44  etaurel
// - Some changes in file header
// - Commit after implementing the group multi motor read
//
// Revision 1.2  2006/06/12 10:28:58  etaurel
// - Many changes dur to bug fixes found when writing test units...
//
// Revision 1.1.1.1  2006/03/10 13:40:57  etaurel
// Initial import
//
//
// copyleft :     CELLS/ALBA
//				  Edifici Ciències Nord. Mòdul C-3 central.
//  			  Campus Universitari de Bellaterra. Universitat Autònoma de Barcelona
//  			  08193 Bellaterra, Barcelona
//  			  Spain
//
//-============================================================================
//
//  		This file is generated by POGO
//	(Program Obviously used to Generate tango Object)
//
//         (c) - Software Engineering Group - ESRF
//=============================================================================

#include <tango.h>
#include <CPoolExcept.h>

int main(int argc,char *argv[])
{
    Tango::Util *tg = NULL;
    try
    {
        // Initialise the device server
        //----------------------------------------
        tg = Tango::Util::init(argc,argv);

        // Create the device server singleton 
        //	which will create everything
        //----------------------------------------
        tg->server_init(false);

        // Run the endless loop
        //----------------------------------------
        cout << "Ready to accept request" << endl;
        tg->server_run();
    }
    catch (bad_alloc)
    {
        cout << "Can't allocate memory to store device object !!!" << endl;
    }
    catch (Pool_ns::PoolFailed &pf)
    {
        Pool_ns::PoolThrower::print_exception(pf);
        
        cout << "Received a PoolFailed_Exception" << endl;
    }
    catch (CORBA::Exception &e)
    {
        Tango::Except::print_exception(e);
        
        cout << "Received a CORBA_Exception" << endl;
    }
    catch (...)
    {
        cout << "Received an unknown exception" << endl;
    }
    cout << "Exiting" << endl;
    tg->server_cleanup();
    cout << "Exited" << endl;
    return(0);
}
