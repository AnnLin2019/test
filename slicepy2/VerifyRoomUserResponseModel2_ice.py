# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.5
#
# <auto-generated>
#
# Generated from file `VerifyRoomUserResponseModel2.ice'
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

if 'VerifyRoomUserResponseModel2' not in _M_com.fastonz.fmserver.model.__dict__:
    _M_com.fastonz.fmserver.model.VerifyRoomUserResponseModel2 = Ice.createTempClass()
    class VerifyRoomUserResponseModel2(object):
        def __init__(self, roomID=0, verifyMode=0, userRight=0, result=0):
            self.roomID = roomID
            self.verifyMode = verifyMode
            self.userRight = userRight
            self.result = result

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.roomID)
            _h = 5 * _h + Ice.getHash(self.verifyMode)
            _h = 5 * _h + Ice.getHash(self.userRight)
            _h = 5 * _h + Ice.getHash(self.result)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_com.fastonz.fmserver.model.VerifyRoomUserResponseModel2):
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
            return IcePy.stringify(self, _M_com.fastonz.fmserver.model._t_VerifyRoomUserResponseModel2)

        __repr__ = __str__

    _M_com.fastonz.fmserver.model._t_VerifyRoomUserResponseModel2 = IcePy.defineStruct('::com::fastonz::fmserver::model::VerifyRoomUserResponseModel2', VerifyRoomUserResponseModel2, (), (
        ('roomID', (), IcePy._t_int),
        ('verifyMode', (), IcePy._t_int),
        ('userRight', (), IcePy._t_int),
        ('result', (), IcePy._t_int)
    ))

    _M_com.fastonz.fmserver.model.VerifyRoomUserResponseModel2 = VerifyRoomUserResponseModel2
    del VerifyRoomUserResponseModel2

# End of module com.fastonz.fmserver.model

__name__ = 'com.fastonz.fmserver'

# End of module com.fastonz.fmserver

__name__ = 'com.fastonz'

# End of module com.fastonz

__name__ = 'com'

# End of module com
