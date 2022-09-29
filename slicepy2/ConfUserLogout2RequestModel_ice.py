# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.5
#
# <auto-generated>
#
# Generated from file `ConfUserLogout2RequestModel.ice'
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

if 'ConfUserLogout2RequestModel' not in _M_com.fastonz.fmserver.model.__dict__:
    _M_com.fastonz.fmserver.model.ConfUserLogout2RequestModel = Ice.createTempClass()
    class ConfUserLogout2RequestModel(object):
        def __init__(self, serviceID=0, roomID=0, userID=0, userName='', logID=0):
            self.serviceID = serviceID
            self.roomID = roomID
            self.userID = userID
            self.userName = userName
            self.logID = logID

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.serviceID)
            _h = 5 * _h + Ice.getHash(self.roomID)
            _h = 5 * _h + Ice.getHash(self.userID)
            _h = 5 * _h + Ice.getHash(self.userName)
            _h = 5 * _h + Ice.getHash(self.logID)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_com.fastonz.fmserver.model.ConfUserLogout2RequestModel):
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
                if self.roomID is None or other.roomID is None:
                    if self.roomID != other.roomID:
                        return (-1 if self.roomID is None else 1)
                else:
                    if self.roomID < other.roomID:
                        return -1
                    elif self.roomID > other.roomID:
                        return 1
                if self.userID is None or other.userID is None:
                    if self.userID != other.userID:
                        return (-1 if self.userID is None else 1)
                else:
                    if self.userID < other.userID:
                        return -1
                    elif self.userID > other.userID:
                        return 1
                if self.userName is None or other.userName is None:
                    if self.userName != other.userName:
                        return (-1 if self.userName is None else 1)
                else:
                    if self.userName < other.userName:
                        return -1
                    elif self.userName > other.userName:
                        return 1
                if self.logID is None or other.logID is None:
                    if self.logID != other.logID:
                        return (-1 if self.logID is None else 1)
                else:
                    if self.logID < other.logID:
                        return -1
                    elif self.logID > other.logID:
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
            return IcePy.stringify(self, _M_com.fastonz.fmserver.model._t_ConfUserLogout2RequestModel)

        __repr__ = __str__

    _M_com.fastonz.fmserver.model._t_ConfUserLogout2RequestModel = IcePy.defineStruct('::com::fastonz::fmserver::model::ConfUserLogout2RequestModel', ConfUserLogout2RequestModel, (), (
        ('serviceID', (), IcePy._t_int),
        ('roomID', (), IcePy._t_int),
        ('userID', (), IcePy._t_int),
        ('userName', (), IcePy._t_string),
        ('logID', (), IcePy._t_int)
    ))

    _M_com.fastonz.fmserver.model.ConfUserLogout2RequestModel = ConfUserLogout2RequestModel
    del ConfUserLogout2RequestModel

# End of module com.fastonz.fmserver.model

__name__ = 'com.fastonz.fmserver'

# End of module com.fastonz.fmserver

__name__ = 'com.fastonz'

# End of module com.fastonz

__name__ = 'com'

# End of module com