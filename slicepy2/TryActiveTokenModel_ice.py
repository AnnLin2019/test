# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.5
#
# <auto-generated>
#
# Generated from file `TryActiveTokenModel.ice'
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

if 'TryActiveTokenModel' not in _M_com.fastonz.fmserver.model.__dict__:
    _M_com.fastonz.fmserver.model.TryActiveTokenModel = Ice.createTempClass()
    class TryActiveTokenModel(object):
        def __init__(self, tokenID='', nodeID='', roomID=0, userID=0, termianlType=0, activeID=0):
            self.tokenID = tokenID
            self.nodeID = nodeID
            self.roomID = roomID
            self.userID = userID
            self.termianlType = termianlType
            self.activeID = activeID

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.tokenID)
            _h = 5 * _h + Ice.getHash(self.nodeID)
            _h = 5 * _h + Ice.getHash(self.roomID)
            _h = 5 * _h + Ice.getHash(self.userID)
            _h = 5 * _h + Ice.getHash(self.termianlType)
            _h = 5 * _h + Ice.getHash(self.activeID)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_com.fastonz.fmserver.model.TryActiveTokenModel):
                return NotImplemented
            else:
                if self.tokenID is None or other.tokenID is None:
                    if self.tokenID != other.tokenID:
                        return (-1 if self.tokenID is None else 1)
                else:
                    if self.tokenID < other.tokenID:
                        return -1
                    elif self.tokenID > other.tokenID:
                        return 1
                if self.nodeID is None or other.nodeID is None:
                    if self.nodeID != other.nodeID:
                        return (-1 if self.nodeID is None else 1)
                else:
                    if self.nodeID < other.nodeID:
                        return -1
                    elif self.nodeID > other.nodeID:
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
                if self.termianlType is None or other.termianlType is None:
                    if self.termianlType != other.termianlType:
                        return (-1 if self.termianlType is None else 1)
                else:
                    if self.termianlType < other.termianlType:
                        return -1
                    elif self.termianlType > other.termianlType:
                        return 1
                if self.activeID is None or other.activeID is None:
                    if self.activeID != other.activeID:
                        return (-1 if self.activeID is None else 1)
                else:
                    if self.activeID < other.activeID:
                        return -1
                    elif self.activeID > other.activeID:
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
            return IcePy.stringify(self, _M_com.fastonz.fmserver.model._t_TryActiveTokenModel)

        __repr__ = __str__

    _M_com.fastonz.fmserver.model._t_TryActiveTokenModel = IcePy.defineStruct('::com::fastonz::fmserver::model::TryActiveTokenModel', TryActiveTokenModel, (), (
        ('tokenID', (), IcePy._t_string),
        ('nodeID', (), IcePy._t_string),
        ('roomID', (), IcePy._t_int),
        ('userID', (), IcePy._t_int),
        ('termianlType', (), IcePy._t_int),
        ('activeID', (), IcePy._t_int)
    ))

    _M_com.fastonz.fmserver.model.TryActiveTokenModel = TryActiveTokenModel
    del TryActiveTokenModel

# End of module com.fastonz.fmserver.model

__name__ = 'com.fastonz.fmserver'

# End of module com.fastonz.fmserver

__name__ = 'com.fastonz'

# End of module com.fastonz

__name__ = 'com'

# End of module com
