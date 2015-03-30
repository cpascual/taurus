#!/usr/bin/env python

#############################################################################
##
## This file is part of Taurus
## 
## http://taurus-scada.org
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
#############################################################################

"""This module contains the base taurus name validator classes"""

__all__ = ["TangoAuthorityNameValidator", "TangoDeviceNameValidator", 
"TangoAttributeNameValidator", "TangoConfigurationNameValidator"]

__docformat__ = "restructuredtext"


from taurus.core.taurusvalidator import (TaurusAttributeNameValidator, 
                                         TaurusDeviceNameValidator, 
                                         TaurusAuthorityNameValidator, 
                                         TaurusConfigurationNameValidator) 


#todo: I do not understand the behaviour of getNames for Auth, Dev and Attr in
#      the case when the fullname does not match the regexp. For Auth it returns
#      a 3-tuple, for devs a 2-tuple and for attrs and conf a single None.
#      This is not coherent to what the method returns when it matches the 
#      regexp (always a 3-tuple) 

class TangoAuthorityNameValidator(TaurusAuthorityNameValidator):
    '''Validator for Tango authority names. Apart from the standard named 
    groups (scheme, authority, path, query and fragment), the following named 
    groups are created:
    
     - host: tango host name, without port.
     - port: port number
    '''

    scheme = 'tango'
    authority = '//(?P<host>([\w\-_]+\.)*[\w\-_]+):(?P<port>\d{1,5})'
    path = '(?!)'
    query = '(?!)'
    fragment = '(?!)'


class TangoDeviceNameValidator(TaurusDeviceNameValidator):    
    '''Validator for Tango device names. Apart from the standard named 
    groups (scheme, authority, path, query and fragment), the following named 
    groups are created:
    
     - devname: device name (either alias or slashed name)
     - [_devalias]: device alias
     - [_devslashname]: device name in slashed (a/b/c) form 
     - [host] as in :class:`TangoAuthorityNameValidator`
     - [port] as in :class:`TangoAuthorityNameValidator`
     
    Note: brackets on the group name indicate that this group will only contain
    a string if the URI contains it.
    '''

    scheme = 'tango'
    authority = TangoAuthorityNameValidator.authority
    path = r'/?(?P<devname>((?P<_devalias>[^/?#:]+)|' + \
           r'(?P<_devslashname>[^/?#:]+/[^/?#:]+/[^/?#:]+)))'
    query = '(?!)'
    fragment = '(?!)' 

    def getNames(self, fullname, factory=None, queryAuth=True):
        '''reimplemented from :class:`TaurusDeviceNameValidator`. It accepts an
        extra keyword arg `queryAuth` which, if set to False, will prevent the 
        validator from trying to query a TaurusAuthority to obtain missing info
        such as the devslashname <--> devalias correspondence. 
        '''
        groups = self.getUriGroups(fullname)
        if groups is None:
            return None
    
        import PyTango
        default_authority = '//' + PyTango.ApiUtil.get_env_var('TANGO_HOST')        

        authority = groups.get('authority')
        if authority is None:
            groups['authority'] = authority = default_authority       
        
        db = None
        if queryAuth:
            # attempt to get an Authority object    
            if factory is None:
                from taurus import Factory
                factory = Factory(scheme=self.scheme)
            try:
                db = factory.getAuthority('tango:%s' % authority)
            except:
                pass
        
        #note, since we validated, we either have alias or slashname (not both)
        _devalias = groups.get('_devalias')    
        _devslashname = groups.get('_devslashname')
        
        if _devslashname is None and db is not None:
            #get _devslashname from the alias using the DB
            _devslashname = db.getElementFullName(_devalias)
            groups['_devslashname'] = _devslashname
        
        if _devslashname is None:
            # if we still do not have a slashname, we can only give the short
            return None, None, _devalias
        
        # we can now construct everything. First the complete:
        complete = 'tango:%(authority)s/%(_devslashname)s' % groups
        
        # then the normal
        if authority.lower() == default_authority.lower():
            normal = '%(_devslashname)s' % groups
        else:
            normal = '%(authority)s/%(_devslashname)s' % groups
        
        #and finally the short
        if _devalias is not None:
            short = _devalias
        else:
            if db is not None:
                # get the alias from the DB (if it is defined)
                short = db.getElementAlias(_devslashname) or _devslashname
            else:
                short = _devslashname
        
        return complete, normal, short  
            
    
    @property
    def nonStrictNamePattern(self):
        '''In non-strict mode, allow double-slash even if there is no Authority.
        (e.g., "tango://a/b/c" passes this non-strict form)
        '''
        return self.namePattern.replace('tango):(', 'tango)://(')


class TangoAttributeNameValidator(TaurusAttributeNameValidator):
    '''Validator for Tango attribute names. Apart from the standard named 
    groups (scheme, authority, path, query and fragment), the following named 
    groups are created:
    
     - attrname: attribute name including device name
     - _shortattrname: attribute name excluding device name
     - devname: as in :class:`TangoDeviceNameValidator`
     - [_devalias]: as in :class:`TangoDeviceNameValidator`
     - [_devslashname]: as in :class:`TangoDeviceNameValidator`
     - [host] as in :class:`TangoAuthorityNameValidator`
     - [port] as in :class:`TangoAuthorityNameValidator`
     
    Note: brackets on the group name indicate that this group will only contain
    a string if the URI contains it.
    '''
    scheme = 'tango'
    authority = TangoAuthorityNameValidator.authority
    path = ('(?P<attrname>%s/(?P<_shortattrname>[^/?:#]+))' %
            TangoDeviceNameValidator.path)
    query = '(?!)'
    fragment = '(?!)'  

    def getNames(self, fullname, factory=None, queryAuth=True):
        """Returns the complete and short names"""
                
        groups = self.getUriGroups(fullname)
        if groups is None:
            return None  
        
        complete, normal, short = None, None, groups.get('_shortattrname')
        
        # reuse the getNames from the Device validator...
        devname = fullname.rsplit('/',1)[0]
        v = TangoDeviceNameValidator()
        devcomplete, devnormal, _ = v.getNames(devname, factory=factory,
                                                queryAuth=queryAuth)
        if devcomplete is not None:
            complete = '%s/%s'%(devcomplete, short)
        if devnormal is not None:
            normal = '%s/%s'%(devnormal, short)
        
        return complete, normal, short

    @property
    def nonStrictNamePattern(self):
        '''In non-strict mode, allow double-slash even if there is no Authority.
        (e.g., "tango://a/b/c" passes this non-strict form)
        '''
        return self.namePattern.replace('tango):(', 'tango)://(')
    
    
class TangoConfigurationNameValidator(TaurusConfigurationNameValidator):
    '''Validator for Tango configuration names. Apart from the standard named 
    groups (scheme, authority, path, query and fragment), the following named 
    groups are created:
    
     - [cfgkey]: configuration key (e.g., "label", "units",...)
     - attrname: as in :class:`TangoAttributeNameValidator`
     - _shortattrname: as in :class:`TangoAttributeNameValidator`
     - devname:  as in :class:`TangoDeviceNameValidator`
     - [_devalias]: as in :class:`TangoDeviceNameValidator`
     - [_devslashname]: as in :class:`TangoDeviceNameValidator`
     - [host] as in :class:`TangoAuthorityNameValidator`
     - [port] as in :class:`TangoAuthorityNameValidator`
     
    Note: brackets on the group name indicate that this group will only contain
    a string if the URI contains it.
    '''
    scheme = 'tango'
    authority = TangoAuthorityNameValidator.authority
    path = TangoAttributeNameValidator.path
    query = 'configuration(=(?P<cfgkey>[^# ]+))?'
    fragment = '(?!)'  


    def getNames(self, fullname, factory=None, queryAuth=True):
        """Returns the complete and short names"""
        
        groups = self.getUriGroups(fullname)
        if groups is None:
            return None
        
        query = groups.get('query')
        cfgkey = groups.get('cfgkey')
        
        complete, normal, short = None, None, cfgkey or 'configuration'
        
        # reuse the getNames from the Attribute validator...
        attrname = fullname.split('?',1)[0]
        v = TangoAttributeNameValidator()
        attrcomplete, attrnormal, _ = v.getNames(attrname, factory=factory,
                                                 queryAuth=queryAuth)
        
        if attrcomplete is not None:
            complete = '%s?%s'%(attrcomplete, query)
        if attrnormal is not None:
            normal = '%s?%s'%(attrnormal, query)
        
        return complete, normal, short
        
    
    @property
    def nonStrictNamePattern(self):
        '''In non-strict mode, allow double-slash even if there is no Authority.
        (e.g., "tango://a/b/c" passes this non-strict form)
        '''
        return self.namePattern.replace('tango):(', 'tango)://(')

