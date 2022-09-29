# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.5
#
# <auto-generated>
#
# Generated from file `UserService.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy
import TokenModel_ice

# Included module com
_M_com = Ice.openModule('com')

# Included module com.fastonz
_M_com.fastonz = Ice.openModule('com.fastonz')

# Included module com.fastonz.live
_M_com.fastonz.live = Ice.openModule('com.fastonz.live')

# Included module com.fastonz.live.sliceprotocol
_M_com.fastonz.live.sliceprotocol = Ice.openModule('com.fastonz.live.sliceprotocol')

# Included module com.fastonz.live.sliceprotocol.model
_M_com.fastonz.live.sliceprotocol.model = Ice.openModule('com.fastonz.live.sliceprotocol.model')

# Start of module com
__name__ = 'com'

# Start of module com.fastonz
__name__ = 'com.fastonz'

# Start of module com.fastonz.live
__name__ = 'com.fastonz.live'

# Start of module com.fastonz.live.sliceprotocol
__name__ = 'com.fastonz.live.sliceprotocol'

# Start of module com.fastonz.live.sliceprotocol.controller
_M_com.fastonz.live.sliceprotocol.controller = Ice.openModule('com.fastonz.live.sliceprotocol.controller')
__name__ = 'com.fastonz.live.sliceprotocol.controller'

if '_t_TokenList' not in _M_com.fastonz.live.sliceprotocol.controller.__dict__:
    _M_com.fastonz.live.sliceprotocol.controller._t_TokenList = IcePy.defineSequence('::com::fastonz::live::sliceprotocol::controller::TokenList', (), _M_com.fastonz.live.sliceprotocol.model._t_TokenModel)

_M_com.fastonz.live.sliceprotocol.controller._t_UserService = IcePy.defineValue('::com::fastonz::live::sliceprotocol::controller::UserService', Ice.Value, -1, (), False, True, None, ())

if 'UserServicePrx' not in _M_com.fastonz.live.sliceprotocol.controller.__dict__:
    _M_com.fastonz.live.sliceprotocol.controller.UserServicePrx = Ice.createTempClass()
    class UserServicePrx(Ice.ObjectPrx):

        def activeToken(self, userId, token, liveRoomId, appId, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.UserService._op_activeToken.invoke(self, ((userId, token, liveRoomId, appId), context))

        def activeTokenAsync(self, userId, token, liveRoomId, appId, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.UserService._op_activeToken.invokeAsync(self, ((userId, token, liveRoomId, appId), context))

        def begin_activeToken(self, userId, token, liveRoomId, appId, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.UserService._op_activeToken.begin(self, ((userId, token, liveRoomId, appId), _response, _ex, _sent, context))

        def end_activeToken(self, _r):
            return _M_com.fastonz.live.sliceprotocol.controller.UserService._op_activeToken.end(self, _r)

        def releaseToken(self, tokens, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.UserService._op_releaseToken.invoke(self, ((tokens, ), context))

        def releaseTokenAsync(self, tokens, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.UserService._op_releaseToken.invokeAsync(self, ((tokens, ), context))

        def begin_releaseToken(self, tokens, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.UserService._op_releaseToken.begin(self, ((tokens, ), _response, _ex, _sent, context))

        def end_releaseToken(self, _r):
            return _M_com.fastonz.live.sliceprotocol.controller.UserService._op_releaseToken.end(self, _r)

        def releaseTokenByLiveRoom(self, liveRoomId, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.UserService._op_releaseTokenByLiveRoom.invoke(self, ((liveRoomId, ), context))

        def releaseTokenByLiveRoomAsync(self, liveRoomId, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.UserService._op_releaseTokenByLiveRoom.invokeAsync(self, ((liveRoomId, ), context))

        def begin_releaseTokenByLiveRoom(self, liveRoomId, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.UserService._op_releaseTokenByLiveRoom.begin(self, ((liveRoomId, ), _response, _ex, _sent, context))

        def end_releaseTokenByLiveRoom(self, _r):
            return _M_com.fastonz.live.sliceprotocol.controller.UserService._op_releaseTokenByLiveRoom.end(self, _r)

        def tokenHeartbeat(self, userId, token, liveRoomId, appId, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.UserService._op_tokenHeartbeat.invoke(self, ((userId, token, liveRoomId, appId), context))

        def tokenHeartbeatAsync(self, userId, token, liveRoomId, appId, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.UserService._op_tokenHeartbeat.invokeAsync(self, ((userId, token, liveRoomId, appId), context))

        def begin_tokenHeartbeat(self, userId, token, liveRoomId, appId, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.UserService._op_tokenHeartbeat.begin(self, ((userId, token, liveRoomId, appId), _response, _ex, _sent, context))

        def end_tokenHeartbeat(self, _r):
            return _M_com.fastonz.live.sliceprotocol.controller.UserService._op_tokenHeartbeat.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.UserServicePrx.ice_checkedCast(proxy, '::com::fastonz::live::sliceprotocol::controller::UserService', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_com.fastonz.live.sliceprotocol.controller.UserServicePrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::com::fastonz::live::sliceprotocol::controller::UserService'
    _M_com.fastonz.live.sliceprotocol.controller._t_UserServicePrx = IcePy.defineProxy('::com::fastonz::live::sliceprotocol::controller::UserService', UserServicePrx)

    _M_com.fastonz.live.sliceprotocol.controller.UserServicePrx = UserServicePrx
    del UserServicePrx

    _M_com.fastonz.live.sliceprotocol.controller.UserService = Ice.createTempClass()
    class UserService(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::com::fastonz::live::sliceprotocol::controller::UserService')

        def ice_id(self, current=None):
            return '::com::fastonz::live::sliceprotocol::controller::UserService'

        @staticmethod
        def ice_staticId():
            return '::com::fastonz::live::sliceprotocol::controller::UserService'

        def activeToken(self, userId, token, liveRoomId, appId, current=None):
            raise NotImplementedError("servant method 'activeToken' not implemented")

        def releaseToken(self, tokens, current=None):
            raise NotImplementedError("servant method 'releaseToken' not implemented")

        def releaseTokenByLiveRoom(self, liveRoomId, current=None):
            raise NotImplementedError("servant method 'releaseTokenByLiveRoom' not implemented")

        def tokenHeartbeat(self, userId, token, liveRoomId, appId, current=None):
            raise NotImplementedError("servant method 'tokenHeartbeat' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_com.fastonz.live.sliceprotocol.controller._t_UserServiceDisp)

        __repr__ = __str__

    _M_com.fastonz.live.sliceprotocol.controller._t_UserServiceDisp = IcePy.defineClass('::com::fastonz::live::sliceprotocol::controller::UserService', UserService, (), None, ())
    UserService._ice_type = _M_com.fastonz.live.sliceprotocol.controller._t_UserServiceDisp

    UserService._op_activeToken = IcePy.Operation('activeToken', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), IcePy._t_int, False, 0), ((), IcePy._t_string, False, 0), ((), IcePy._t_int, False, 0), ((), IcePy._t_string, False, 0)), (), ((), IcePy._t_int, False, 0), ())
    UserService._op_releaseToken = IcePy.Operation('releaseToken', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), _M_com.fastonz.live.sliceprotocol.controller._t_TokenList, False, 0),), (), ((), IcePy._t_int, False, 0), ())
    UserService._op_releaseTokenByLiveRoom = IcePy.Operation('releaseTokenByLiveRoom', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), IcePy._t_int, False, 0),), (), ((), IcePy._t_int, False, 0), ())
    UserService._op_tokenHeartbeat = IcePy.Operation('tokenHeartbeat', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), IcePy._t_int, False, 0), ((), IcePy._t_string, False, 0), ((), IcePy._t_int, False, 0), ((), IcePy._t_string, False, 0)), (), ((), IcePy._t_int, False, 0), ())

    _M_com.fastonz.live.sliceprotocol.controller.UserService = UserService
    del UserService

# End of module com.fastonz.live.sliceprotocol.controller

__name__ = 'com.fastonz.live.sliceprotocol'

# End of module com.fastonz.live.sliceprotocol

__name__ = 'com.fastonz.live'

# End of module com.fastonz.live

__name__ = 'com.fastonz'

# End of module com.fastonz

__name__ = 'com'

# End of module com
