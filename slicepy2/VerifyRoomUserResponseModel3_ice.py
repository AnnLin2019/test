# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.5
#
# <auto-generated>
#
# Generated from file `VerifyRoomUserResponseModel3.ice'
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

if 'VerifyRoomUserResponseModel3' not in _M_com.fastonz.fmserver.model.__dict__:
    _M_com.fastonz.fmserver.model.VerifyRoomUserResponseModel3 = Ice.createTempClass()
    class VerifyRoomUserResponseModel3(object):
        def __init__(self, roomID=0, verifyMode=0, userRight=0, result=0, role=''):
            self.roomID = roomID
            self.verifyMode = verifyMode
            self.userRight = userRight
            self.result = result
            self.role = role

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.roomID)
            _h = 5 * _h + Ice.getHash(self.verifyMode)
            _h = 5 * _h + Ice.getHash(self.userRight)
            _h = 5 * _h + Ice.getHash(self.result)
            _h = 5 * _h + Ice.getHash(self.role)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_com.fastonz.fmserver.model.VerifyRoomUserResponseModel3):
                return NotImplemented
            else:
                if self.roomID is None or other.roomID is None:
                    if self.roomID != other.roomID:
                        return (-1 if self.roomID is None else 1)
                else:
                    if self.roomID < other.roomID:
                        return -1
                    elif self.roomID > other.roomID:
                        return 1
                if self.verifyMode is None or other.verifyMode is None:
                    if self.verifyMode != other.verifyMode:
                        return (-1 if self.verifyMode is None else 1)
                else:
                    if self.verifyMode < other.verifyMode:
                        return -1
                    elif self.verifyMode > other.verifyMode:
                        return 1
                if self.userRight is None or other.userRight is None:
                    if self.userRight != other.userRight:
                        return (-1 if self.userRight is None else 1)
                else:
                    if self.userRight < other.userRight:
                        return -1
                    elif self.userRight > other.userRight:
                        return 1
                if self.result is None or other.result is None:
                    if self.result != other.result:
                        return (-1 if self.result is None else 1)
                else:
                    if self.result < other.result:
                        return -1
                    elif self.result > other.result:
                        return 1
                if self.role is None or other.role is None:
                    if self.role != other.role:
                        return (-1 if self.role is None else 1)
                else:
                    if self.role < other.role:
                        return -1
                    elif self.role > other.role:
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
            return IcePy.stringify(self, _M_com.fastonz.fmserver.model._t_VerifyRoomUserResponseModel3)

        __repr__ = __str__

    _M_com.fastonz.fmserver.model._t_VerifyRoomUserResponseModel3 = IcePy.defineStruct('::com::fastonz::fmserver::model::VerifyRoomUserResponseModel3', VerifyRoomUserResponseModel3, (), (
        ('roomID', (), IcePy._t_int),
        ('verifyMode', (), IcePy._t_int),
        ('userRight', (), IcePy._t_int),
        ('result', (), IcePy._t_int),
        ('role', (), IcePy._t_string)
    ))

    _M_com.fastonz.fmserver.model.VerifyRoomUserResponseModel3 = VerifyRoomUserResponseModel3
    del VerifyRoomUserResponseModel3

# End of module com.fastonz.fmserver.model

__name__ = 'com.fastonz.fmserver'

# End of module com.fastonz.fmserver

__name__ = 'com.fastonz'

# End of module com.fastonz

__name__ = 'com'

# End of module com