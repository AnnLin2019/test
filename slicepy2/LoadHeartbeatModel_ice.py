# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.5
#
# <auto-generated>
#
# Generated from file `LoadHeartbeatModel.ice'
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

# Start of module com.fastonz.loadSrv
_M_com.fastonz.loadSrv = Ice.openModule('com.fastonz.loadSrv')
__name__ = 'com.fastonz.loadSrv'

# Start of module com.fastonz.loadSrv.model
_M_com.fastonz.loadSrv.model = Ice.openModule('com.fastonz.loadSrv.model')
__name__ = 'com.fastonz.loadSrv.model'

if 'ServiceHeartbeatModel' not in _M_com.fastonz.loadSrv.model.__dict__:
    _M_com.fastonz.loadSrv.model.ServiceHeartbeatModel = Ice.createTempClass()
    class ServiceHeartbeatModel(object):
        def __init__(self, appId='', appType=0, curLoad=0):
            self.appId = appId
            self.appType = appType
            self.curLoad = curLoad

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.appId)
            _h = 5 * _h + Ice.getHash(self.appType)
            _h = 5 * _h + Ice.getHash(self.curLoad)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_com.fastonz.loadSrv.model.ServiceHeartbeatModel):
                return NotImplemented
            else:
                if self.appId is None or other.appId is None:
                    if self.appId != other.appId:
                        return (-1 if self.appId is None else 1)
                else:
                    if self.appId < other.appId:
                        return -1
                    elif self.appId > other.appId:
                        return 1
                if self.appType is None or other.appType is None:
                    if self.appType != other.appType:
                        return (-1 if self.appType is None else 1)
                else:
                    if self.appType < other.appType:
                        return -1
                    elif self.appType > other.appType:
                        return 1
                if self.curLoad is None or other.curLoad is None:
                    if self.curLoad != other.curLoad:
                        return (-1 if self.curLoad is None else 1)
                else:
                    if self.curLoad < other.curLoad:
                        return -1
                    elif self.curLoad > other.curLoad:
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
            return IcePy.stringify(self, _M_com.fastonz.loadSrv.model._t_ServiceHeartbeatModel)

        __repr__ = __str__

    _M_com.fastonz.loadSrv.model._t_ServiceHeartbeatModel = IcePy.defineStruct('::com::fastonz::loadSrv::model::ServiceHeartbeatModel', ServiceHeartbeatModel, (), (
        ('appId', (), IcePy._t_string),
        ('appType', (), IcePy._t_int),
        ('curLoad', (), IcePy._t_int)
    ))

    _M_com.fastonz.loadSrv.model.ServiceHeartbeatModel = ServiceHeartbeatModel
    del ServiceHeartbeatModel

# End of module com.fastonz.loadSrv.model

__name__ = 'com.fastonz.loadSrv'

# End of module com.fastonz.loadSrv

__name__ = 'com.fastonz'

# End of module com.fastonz

__name__ = 'com'

# End of module com
