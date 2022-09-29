# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.5
#
# <auto-generated>
#
# Generated from file `RegisterServiceModel.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module com
_M_com = Ice.openModule('com')
__name__ = 'com'

# Start of module com.fastonz
_M_com.fastonz = Ice.openModule('com.fastonz')
__name__ = 'com.fastonz'

# Start of module com.fastonz.fmserver
_M_com.fastonz.fmserver = Ice.openModule('com.fastonz.fmserver')
__name__ = 'com.fastonz.fmserver'

# Start of module com.fastonz.fmserver.model
_M_com.fastonz.fmserver.model = Ice.openModule('com.fastonz.fmserver.model')
__name__ = 'com.fastonz.fmserver.model'

if 'RegisterServiceModel' not in _M_com.fastonz.fmserver.model.__dict__:
    _M_com.fastonz.fmserver.model.RegisterServiceModel = Ice.createTempClass()
    class RegisterServiceModel(object):
        def __init__(self, serviceID=0, result=0):
            self.serviceID = serviceID
            self.result = result

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.serviceID)
            _h = 5 * _h + Ice.getHash(self.result)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_com.fastonz.fmserver.model.RegisterServiceModel):
                return NotImplemented
            else:
                if self.serviceID is None or other.serviceID is None:
                    if self.serviceID != other.serviceID:
                        return (-1 if self.serviceID is None else 1)
                else:
                    if self.serviceID < other.serviceID:
                        return -1
                    elif self.serviceID > other.serviceID:
                        return 1
                if self.result is None or other.result is None:
                    if self.result != other.result:
                        return (-1 if self.result is None else 1)
                else:
                    if self.result < other.result:
                        return -1
                    elif self.result > other.result:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_com.fastonz.fmserver.model._t_RegisterServiceModel)

        __repr__ = __str__

    _M_com.fastonz.fmserver.model._t_RegisterServiceModel = IcePy.defineStruct('::com::fastonz::fmserver::model::RegisterServiceModel', RegisterServiceModel, (), (
        ('serviceID', (), IcePy._t_int),
        ('result', (), IcePy._t_int)
    ))

    _M_com.fastonz.fmserver.model.RegisterServiceModel = RegisterServiceModel
    del RegisterServiceModel

# End of module com.fastonz.fmserver.model

__name__ = 'com.fastonz.fmserver'

# End of module com.fastonz.fmserver

__name__ = 'com.fastonz'

# End of module com.fastonz

__name__ = 'com'

# End of module com
