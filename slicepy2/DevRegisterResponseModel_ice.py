# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.5
#
# <auto-generated>
#
# Generated from file `DevRegisterResponseModel.ice'
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

if 'DevRegisterResponseModel' not in _M_com.fastonz.fmserver.model.__dict__:
    _M_com.fastonz.fmserver.model.DevRegisterResponseModel = Ice.createTempClass()
    class DevRegisterResponseModel(object):
        def __init__(self, devNodeID='', backDev='', priority=0, maxOnline=0, maxBandWidth=0, roomMaxUserCount=0, result=0):
            self.devNodeID = devNodeID
            self.backDev = backDev
            self.priority = priority
            self.maxOnline = maxOnline
            self.maxBandWidth = maxBandWidth
            self.roomMaxUserCount = roomMaxUserCount
            self.result = result

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.devNodeID)
            _h = 5 * _h + Ice.getHash(self.backDev)
            _h = 5 * _h + Ice.getHash(self.priority)
            _h = 5 * _h + Ice.getHash(self.maxOnline)
            _h = 5 * _h + Ice.getHash(self.maxBandWidth)
            _h = 5 * _h + Ice.getHash(self.roomMaxUserCount)
            _h = 5 * _h + Ice.getHash(self.result)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_com.fastonz.fmserver.model.DevRegisterResponseModel):
                return NotImplemented
            else:
                if self.devNodeID is None or other.devNodeID is None:
                    if self.devNodeID != other.devNodeID:
                        return (-1 if self.devNodeID is None else 1)
                else:
                    if self.devNodeID < other.devNodeID:
                        return -1
                    elif self.devNodeID > other.devNodeID:
                        return 1
                if self.backDev is None or other.backDev is None:
                    if self.backDev != other.backDev:
                        return (-1 if self.backDev is None else 1)
                else:
                    if self.backDev < other.backDev:
                        return -1
                    elif self.backDev > other.backDev:
                        return 1
                if self.priority is None or other.priority is None:
                    if self.priority != other.priority:
                        return (-1 if self.priority is None else 1)
                else:
                    if self.priority < other.priority:
                        return -1
                    elif self.priority > other.priority:
                        return 1
                if self.maxOnline is None or other.maxOnline is None:
                    if self.maxOnline != other.maxOnline:
                        return (-1 if self.maxOnline is None else 1)
                else:
                    if self.maxOnline < other.maxOnline:
                        return -1
                    elif self.maxOnline > other.maxOnline:
                        return 1
                if self.maxBandWidth is None or other.maxBandWidth is None:
                    if self.maxBandWidth != other.maxBandWidth:
                        return (-1 if self.maxBandWidth is None else 1)
                else:
                    if self.maxBandWidth < other.maxBandWidth:
                        return -1
                    elif self.maxBandWidth > other.maxBandWidth:
                        return 1
                if self.roomMaxUserCount is None or other.roomMaxUserCount is None:
                    if self.roomMaxUserCount != other.roomMaxUserCount:
                        return (-1 if self.roomMaxUserCount is None else 1)
                else:
                    if self.roomMaxUserCount < other.roomMaxUserCount:
                        return -1
                    elif self.roomMaxUserCount > other.roomMaxUserCount:
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
            return IcePy.stringify(self, _M_com.fastonz.fmserver.model._t_DevRegisterResponseModel)

        __repr__ = __str__

    _M_com.fastonz.fmserver.model._t_DevRegisterResponseModel = IcePy.defineStruct('::com::fastonz::fmserver::model::DevRegisterResponseModel', DevRegisterResponseModel, (), (
        ('devNodeID', (), IcePy._t_string),
        ('backDev', (), IcePy._t_string),
        ('priority', (), IcePy._t_int),
        ('maxOnline', (), IcePy._t_int),
        ('maxBandWidth', (), IcePy._t_int),
        ('roomMaxUserCount', (), IcePy._t_int),
        ('result', (), IcePy._t_int)
    ))

    _M_com.fastonz.fmserver.model.DevRegisterResponseModel = DevRegisterResponseModel
    del DevRegisterResponseModel

# End of module com.fastonz.fmserver.model

__name__ = 'com.fastonz.fmserver'

# End of module com.fastonz.fmserver

__name__ = 'com.fastonz'

# End of module com.fastonz

__name__ = 'com'

# End of module com
