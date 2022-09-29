# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.5
#
# <auto-generated>
#
# Generated from file `CloseRoomResponseModel.ice'
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

# Start of module com.fastonz.fmconfctlserver
_M_com.fastonz.fmconfctlserver = Ice.openModule('com.fastonz.fmconfctlserver')
__name__ = 'com.fastonz.fmconfctlserver'

# Start of module com.fastonz.fmconfctlserver.model
_M_com.fastonz.fmconfctlserver.model = Ice.openModule('com.fastonz.fmconfctlserver.model')
__name__ = 'com.fastonz.fmconfctlserver.model'

if 'CloseRoomResponseModel' not in _M_com.fastonz.fmconfctlserver.model.__dict__:
    _M_com.fastonz.fmconfctlserver.model.CloseRoomResponseModel = Ice.createTempClass()
    class CloseRoomResponseModel(object):
        def __init__(self, result=0, currentOnlines=0):
            self.result = result
            self.currentOnlines = currentOnlines

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.result)
            _h = 5 * _h + Ice.getHash(self.currentOnlines)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_com.fastonz.fmconfctlserver.model.CloseRoomResponseModel):
                return NotImplemented
            else:
                if self.result is None or other.result is None:
                    if self.result != other.result:
                        return (-1 if self.result is None else 1)
                else:
                    if self.result < other.result:
                        return -1
                    elif self.result > other.result:
                        return 1
                if self.currentOnlines is None or other.currentOnlines is None:
                    if self.currentOnlines != other.currentOnlines:
                        return (-1 if self.currentOnlines is None else 1)
                else:
                    if self.currentOnlines < other.currentOnlines:
                        return -1
                    elif self.currentOnlines > other.currentOnlines:
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
            return IcePy.stringify(self, _M_com.fastonz.fmconfctlserver.model._t_CloseRoomResponseModel)

        __repr__ = __str__

    _M_com.fastonz.fmconfctlserver.model._t_CloseRoomResponseModel = IcePy.defineStruct('::com::fastonz::fmconfctlserver::model::CloseRoomResponseModel', CloseRoomResponseModel, (), (
        ('result', (), IcePy._t_int),
        ('currentOnlines', (), IcePy._t_int)
    ))

    _M_com.fastonz.fmconfctlserver.model.CloseRoomResponseModel = CloseRoomResponseModel
    del CloseRoomResponseModel

# End of module com.fastonz.fmconfctlserver.model

__name__ = 'com.fastonz.fmconfctlserver'

# End of module com.fastonz.fmconfctlserver

__name__ = 'com.fastonz'

# End of module com.fastonz

__name__ = 'com'

# End of module com