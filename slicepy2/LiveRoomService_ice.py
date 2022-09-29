# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.5
#
# <auto-generated>
#
# Generated from file `LiveRoomService.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy
import LiveRoomModel_ice
import LiveRoomInfoModel_ice
import LiveRoomCDNModel_ice
import GetChatRecordModel_ice
import ChatRecordModel_ice
import LiveRoomExpandModel_ice
import LiveRoomThirdpartyPushRunModel_ice

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

if '_t_CDNList' not in _M_com.fastonz.live.sliceprotocol.controller.__dict__:
    _M_com.fastonz.live.sliceprotocol.controller._t_CDNList = IcePy.defineSequence('::com::fastonz::live::sliceprotocol::controller::CDNList', (), _M_com.fastonz.live.sliceprotocol.model._t_LiveRoomCDNModel)

if '_t_ChatRecordList' not in _M_com.fastonz.live.sliceprotocol.controller.__dict__:
    _M_com.fastonz.live.sliceprotocol.controller._t_ChatRecordList = IcePy.defineSequence('::com::fastonz::live::sliceprotocol::controller::ChatRecordList', (), _M_com.fastonz.live.sliceprotocol.model._t_ChatRecordModel)

if '_t_LiveRoomInfoList' not in _M_com.fastonz.live.sliceprotocol.controller.__dict__:
    _M_com.fastonz.live.sliceprotocol.controller._t_LiveRoomInfoList = IcePy.defineSequence('::com::fastonz::live::sliceprotocol::controller::LiveRoomInfoList', (), _M_com.fastonz.live.sliceprotocol.model._t_LiveRoomInfoModel)

if '_t_LiveRoomThirdpartyPushRunInfoList' not in _M_com.fastonz.live.sliceprotocol.controller.__dict__:
    _M_com.fastonz.live.sliceprotocol.controller._t_LiveRoomThirdpartyPushRunInfoList = IcePy.defineSequence('::com::fastonz::live::sliceprotocol::controller::LiveRoomThirdpartyPushRunInfoList', (), _M_com.fastonz.live.sliceprotocol.model._t_LiveRoomThirdpartyPushRunModel)

_M_com.fastonz.live.sliceprotocol.controller._t_LiveRoomService = IcePy.defineValue('::com::fastonz::live::sliceprotocol::controller::LiveRoomService', Ice.Value, -1, (), False, True, None, ())

if 'LiveRoomServicePrx' not in _M_com.fastonz.live.sliceprotocol.controller.__dict__:
    _M_com.fastonz.live.sliceprotocol.controller.LiveRoomServicePrx = Ice.createTempClass()
    class LiveRoomServicePrx(Ice.ObjectPrx):

        def getLiveRoom(self, liveRoomId, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_getLiveRoom.invoke(self, ((liveRoomId, ), context))

        def getLiveRoomAsync(self, liveRoomId, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_getLiveRoom.invokeAsync(self, ((liveRoomId, ), context))

        def begin_getLiveRoom(self, liveRoomId, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_getLiveRoom.begin(self, ((liveRoomId, ), _response, _ex, _sent, context))

        def end_getLiveRoom(self, _r):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_getLiveRoom.end(self, _r)

        def getLiveRoomV2(self, liveRoomId, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_getLiveRoomV2.invoke(self, ((liveRoomId, ), context))

        def getLiveRoomV2Async(self, liveRoomId, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_getLiveRoomV2.invokeAsync(self, ((liveRoomId, ), context))

        def begin_getLiveRoomV2(self, liveRoomId, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_getLiveRoomV2.begin(self, ((liveRoomId, ), _response, _ex, _sent, context))

        def end_getLiveRoomV2(self, _r):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_getLiveRoomV2.end(self, _r)

        def getLiveRoomInfoList(self, appId, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_getLiveRoomInfoList.invoke(self, ((appId, ), context))

        def getLiveRoomInfoListAsync(self, appId, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_getLiveRoomInfoList.invokeAsync(self, ((appId, ), context))

        def begin_getLiveRoomInfoList(self, appId, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_getLiveRoomInfoList.begin(self, ((appId, ), _response, _ex, _sent, context))

        def end_getLiveRoomInfoList(self, _r):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_getLiveRoomInfoList.end(self, _r)

        def activeLiveRoom(self, liveRoomId, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_activeLiveRoom.invoke(self, ((liveRoomId, ), context))

        def activeLiveRoomAsync(self, liveRoomId, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_activeLiveRoom.invokeAsync(self, ((liveRoomId, ), context))

        def begin_activeLiveRoom(self, liveRoomId, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_activeLiveRoom.begin(self, ((liveRoomId, ), _response, _ex, _sent, context))

        def end_activeLiveRoom(self, _r):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_activeLiveRoom.end(self, _r)

        def releaseLiveRoom(self, liveRoomId, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_releaseLiveRoom.invoke(self, ((liveRoomId, ), context))

        def releaseLiveRoomAsync(self, liveRoomId, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_releaseLiveRoom.invokeAsync(self, ((liveRoomId, ), context))

        def begin_releaseLiveRoom(self, liveRoomId, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_releaseLiveRoom.begin(self, ((liveRoomId, ), _response, _ex, _sent, context))

        def end_releaseLiveRoom(self, _r):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_releaseLiveRoom.end(self, _r)

        def getLiveRoomCDNInfo(self, liveRoomId, appId, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_getLiveRoomCDNInfo.invoke(self, ((liveRoomId, appId), context))

        def getLiveRoomCDNInfoAsync(self, liveRoomId, appId, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_getLiveRoomCDNInfo.invokeAsync(self, ((liveRoomId, appId), context))

        def begin_getLiveRoomCDNInfo(self, liveRoomId, appId, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_getLiveRoomCDNInfo.begin(self, ((liveRoomId, appId), _response, _ex, _sent, context))

        def end_getLiveRoomCDNInfo(self, _r):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_getLiveRoomCDNInfo.end(self, _r)

        def getChatRecordList(self, getChatRecordModel, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_getChatRecordList.invoke(self, ((getChatRecordModel, ), context))

        def getChatRecordListAsync(self, getChatRecordModel, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_getChatRecordList.invokeAsync(self, ((getChatRecordModel, ), context))

        def begin_getChatRecordList(self, getChatRecordModel, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_getChatRecordList.begin(self, ((getChatRecordModel, ), _response, _ex, _sent, context))

        def end_getChatRecordList(self, _r):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_getChatRecordList.end(self, _r)

        def getLiveRoomExpandModel(self, liveRoomId, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_getLiveRoomExpandModel.invoke(self, ((liveRoomId, ), context))

        def getLiveRoomExpandModelAsync(self, liveRoomId, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_getLiveRoomExpandModel.invokeAsync(self, ((liveRoomId, ), context))

        def begin_getLiveRoomExpandModel(self, liveRoomId, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_getLiveRoomExpandModel.begin(self, ((liveRoomId, ), _response, _ex, _sent, context))

        def end_getLiveRoomExpandModel(self, _r):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_getLiveRoomExpandModel.end(self, _r)

        def getLiveRoomThirdpartyPushRunModelList(self, liveRoomId, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_getLiveRoomThirdpartyPushRunModelList.invoke(self, ((liveRoomId, ), context))

        def getLiveRoomThirdpartyPushRunModelListAsync(self, liveRoomId, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_getLiveRoomThirdpartyPushRunModelList.invokeAsync(self, ((liveRoomId, ), context))

        def begin_getLiveRoomThirdpartyPushRunModelList(self, liveRoomId, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_getLiveRoomThirdpartyPushRunModelList.begin(self, ((liveRoomId, ), _response, _ex, _sent, context))

        def end_getLiveRoomThirdpartyPushRunModelList(self, _r):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService._op_getLiveRoomThirdpartyPushRunModelList.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomServicePrx.ice_checkedCast(proxy, '::com::fastonz::live::sliceprotocol::controller::LiveRoomService', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_com.fastonz.live.sliceprotocol.controller.LiveRoomServicePrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::com::fastonz::live::sliceprotocol::controller::LiveRoomService'
    _M_com.fastonz.live.sliceprotocol.controller._t_LiveRoomServicePrx = IcePy.defineProxy('::com::fastonz::live::sliceprotocol::controller::LiveRoomService', LiveRoomServicePrx)

    _M_com.fastonz.live.sliceprotocol.controller.LiveRoomServicePrx = LiveRoomServicePrx
    del LiveRoomServicePrx

    _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService = Ice.createTempClass()
    class LiveRoomService(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::com::fastonz::live::sliceprotocol::controller::LiveRoomService')

        def ice_id(self, current=None):
            return '::com::fastonz::live::sliceprotocol::controller::LiveRoomService'

        @staticmethod
        def ice_staticId():
            return '::com::fastonz::live::sliceprotocol::controller::LiveRoomService'

        def getLiveRoom(self, liveRoomId, current=None):
            raise NotImplementedError("servant method 'getLiveRoom' not implemented")

        def getLiveRoomV2(self, liveRoomId, current=None):
            raise NotImplementedError("servant method 'getLiveRoomV2' not implemented")

        def getLiveRoomInfoList(self, appId, current=None):
            raise NotImplementedError("servant method 'getLiveRoomInfoList' not implemented")

        def activeLiveRoom(self, liveRoomId, current=None):
            raise NotImplementedError("servant method 'activeLiveRoom' not implemented")

        def releaseLiveRoom(self, liveRoomId, current=None):
            raise NotImplementedError("servant method 'releaseLiveRoom' not implemented")

        def getLiveRoomCDNInfo(self, liveRoomId, appId, current=None):
            raise NotImplementedError("servant method 'getLiveRoomCDNInfo' not implemented")

        def getChatRecordList(self, getChatRecordModel, current=None):
            raise NotImplementedError("servant method 'getChatRecordList' not implemented")

        def getLiveRoomExpandModel(self, liveRoomId, current=None):
            raise NotImplementedError("servant method 'getLiveRoomExpandModel' not implemented")

        def getLiveRoomThirdpartyPushRunModelList(self, liveRoomId, current=None):
            raise NotImplementedError("servant method 'getLiveRoomThirdpartyPushRunModelList' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_com.fastonz.live.sliceprotocol.controller._t_LiveRoomServiceDisp)

        __repr__ = __str__

    _M_com.fastonz.live.sliceprotocol.controller._t_LiveRoomServiceDisp = IcePy.defineClass('::com::fastonz::live::sliceprotocol::controller::LiveRoomService', LiveRoomService, (), None, ())
    LiveRoomService._ice_type = _M_com.fastonz.live.sliceprotocol.controller._t_LiveRoomServiceDisp

    LiveRoomService._op_getLiveRoom = IcePy.Operation('getLiveRoom', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), IcePy._t_int, False, 0),), (((), _M_com.fastonz.live.sliceprotocol.model._t_LiveRoomModel, False, 0),), ((), IcePy._t_int, False, 0), ())
    LiveRoomService._op_getLiveRoomV2 = IcePy.Operation('getLiveRoomV2', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), IcePy._t_int, False, 0),), (((), _M_com.fastonz.live.sliceprotocol.model._t_LiveRoomInfoModel, False, 0),), ((), IcePy._t_int, False, 0), ())
    LiveRoomService._op_getLiveRoomInfoList = IcePy.Operation('getLiveRoomInfoList', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), IcePy._t_string, False, 0),), (((), _M_com.fastonz.live.sliceprotocol.controller._t_LiveRoomInfoList, False, 0),), ((), IcePy._t_int, False, 0), ())
    LiveRoomService._op_activeLiveRoom = IcePy.Operation('activeLiveRoom', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), IcePy._t_int, False, 0),), (), ((), IcePy._t_int, False, 0), ())
    LiveRoomService._op_releaseLiveRoom = IcePy.Operation('releaseLiveRoom', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), IcePy._t_int, False, 0),), (), ((), IcePy._t_int, False, 0), ())
    LiveRoomService._op_getLiveRoomCDNInfo = IcePy.Operation('getLiveRoomCDNInfo', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), IcePy._t_int, False, 0), ((), IcePy._t_string, False, 0)), (((), _M_com.fastonz.live.sliceprotocol.controller._t_CDNList, False, 0),), ((), IcePy._t_int, False, 0), ())
    LiveRoomService._op_getChatRecordList = IcePy.Operation('getChatRecordList', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), _M_com.fastonz.live.sliceprotocol.model._t_GetChatRecordModel, False, 0),), (((), _M_com.fastonz.live.sliceprotocol.controller._t_ChatRecordList, False, 0),), ((), IcePy._t_int, False, 0), ())
    LiveRoomService._op_getLiveRoomExpandModel = IcePy.Operation('getLiveRoomExpandModel', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), IcePy._t_int, False, 0),), (((), _M_com.fastonz.live.sliceprotocol.model._t_LiveRoomExpandModel, False, 0),), ((), IcePy._t_int, False, 0), ())
    LiveRoomService._op_getLiveRoomThirdpartyPushRunModelList = IcePy.Operation('getLiveRoomThirdpartyPushRunModelList', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), IcePy._t_int, False, 0),), (((), _M_com.fastonz.live.sliceprotocol.controller._t_LiveRoomThirdpartyPushRunInfoList, False, 0),), ((), IcePy._t_int, False, 0), ())

    _M_com.fastonz.live.sliceprotocol.controller.LiveRoomService = LiveRoomService
    del LiveRoomService

# End of module com.fastonz.live.sliceprotocol.controller

__name__ = 'com.fastonz.live.sliceprotocol'

# End of module com.fastonz.live.sliceprotocol

__name__ = 'com.fastonz.live'

# End of module com.fastonz.live

__name__ = 'com.fastonz'

# End of module com.fastonz

__name__ = 'com'

# End of module com
