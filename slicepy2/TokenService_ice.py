# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.5
#
# <auto-generated>
#
# Generated from file `TokenService.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy
import TryAddTokenModel_ice
import TryAddTokenModel2_ice
import TryAddTokenModel3_ice
import TryActiveTokenModel_ice

# Included module com
_M_com = Ice.openModule('com')

# Included module com.fastonz
_M_com.fastonz = Ice.openModule('com.fastonz')

# Included module com.fastonz.fmserver
_M_com.fastonz.fmserver = Ice.openModule('com.fastonz.fmserver')

# Included module com.fastonz.fmserver.model
_M_com.fastonz.fmserver.model = Ice.openModule('com.fastonz.fmserver.model')

# Start of module com
__name__ = 'com'

# Start of module com.fastonz
__name__ = 'com.fastonz'

# Start of module com.fastonz.fmserver
__name__ = 'com.fastonz.fmserver'

# Start of module com.fastonz.fmserver.tokenMgr
_M_com.fastonz.fmserver.tokenMgr = Ice.openModule('com.fastonz.fmserver.tokenMgr')
__name__ = 'com.fastonz.fmserver.tokenMgr'

if '_t_TokenList' not in _M_com.fastonz.fmserver.tokenMgr.__dict__:
    _M_com.fastonz.fmserver.tokenMgr._t_TokenList = IcePy.defineSequence('::com::fastonz::fmserver::tokenMgr::TokenList', (), IcePy._t_string)

_M_com.fastonz.fmserver.tokenMgr._t_TokenService = IcePy.defineValue('::com::fastonz::fmserver::tokenMgr::TokenService', Ice.Value, -1, (), False, True, None, ())

if 'TokenServicePrx' not in _M_com.fastonz.fmserver.tokenMgr.__dict__:
    _M_com.fastonz.fmserver.tokenMgr.TokenServicePrx = Ice.createTempClass()
    class TokenServicePrx(Ice.ObjectPrx):

        def TryAddToken(self, requestModel, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_TryAddToken.invoke(self, ((requestModel, ), context))

        def TryAddTokenAsync(self, requestModel, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_TryAddToken.invokeAsync(self, ((requestModel, ), context))

        def begin_TryAddToken(self, requestModel, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_TryAddToken.begin(self, ((requestModel, ), _response, _ex, _sent, context))

        def end_TryAddToken(self, _r):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_TryAddToken.end(self, _r)

        def TryAddToken2(self, requestModel, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_TryAddToken2.invoke(self, ((requestModel, ), context))

        def TryAddToken2Async(self, requestModel, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_TryAddToken2.invokeAsync(self, ((requestModel, ), context))

        def begin_TryAddToken2(self, requestModel, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_TryAddToken2.begin(self, ((requestModel, ), _response, _ex, _sent, context))

        def end_TryAddToken2(self, _r):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_TryAddToken2.end(self, _r)

        def TryAddToken3(self, requestModel, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_TryAddToken3.invoke(self, ((requestModel, ), context))

        def TryAddToken3Async(self, requestModel, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_TryAddToken3.invokeAsync(self, ((requestModel, ), context))

        def begin_TryAddToken3(self, requestModel, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_TryAddToken3.begin(self, ((requestModel, ), _response, _ex, _sent, context))

        def end_TryAddToken3(self, _r):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_TryAddToken3.end(self, _r)

        def TryActiveToken(self, requestModel, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_TryActiveToken.invoke(self, ((requestModel, ), context))

        def TryActiveTokenAsync(self, requestModel, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_TryActiveToken.invokeAsync(self, ((requestModel, ), context))

        def begin_TryActiveToken(self, requestModel, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_TryActiveToken.begin(self, ((requestModel, ), _response, _ex, _sent, context))

        def end_TryActiveToken(self, _r):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_TryActiveToken.end(self, _r)

        def ActiveOneToken(self, tokenID, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_ActiveOneToken.invoke(self, ((tokenID, ), context))

        def ActiveOneTokenAsync(self, tokenID, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_ActiveOneToken.invokeAsync(self, ((tokenID, ), context))

        def begin_ActiveOneToken(self, tokenID, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_ActiveOneToken.begin(self, ((tokenID, ), _response, _ex, _sent, context))

        def end_ActiveOneToken(self, _r):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_ActiveOneToken.end(self, _r)

        def ActiveTokens(self, activeID, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_ActiveTokens.invoke(self, ((activeID, ), context))

        def ActiveTokensAsync(self, activeID, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_ActiveTokens.invokeAsync(self, ((activeID, ), context))

        def begin_ActiveTokens(self, activeID, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_ActiveTokens.begin(self, ((activeID, ), _response, _ex, _sent, context))

        def end_ActiveTokens(self, _r):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_ActiveTokens.end(self, _r)

        def CheckToken(self, ownerID, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_CheckToken.invoke(self, ((ownerID, ), context))

        def CheckTokenAsync(self, ownerID, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_CheckToken.invokeAsync(self, ((ownerID, ), context))

        def begin_CheckToken(self, ownerID, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_CheckToken.begin(self, ((ownerID, ), _response, _ex, _sent, context))

        def end_CheckToken(self, _r):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_CheckToken.end(self, _r)

        def ReleaseOneToken(self, tokenID, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_ReleaseOneToken.invoke(self, ((tokenID, ), context))

        def ReleaseOneTokenAsync(self, tokenID, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_ReleaseOneToken.invokeAsync(self, ((tokenID, ), context))

        def begin_ReleaseOneToken(self, tokenID, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_ReleaseOneToken.begin(self, ((tokenID, ), _response, _ex, _sent, context))

        def end_ReleaseOneToken(self, _r):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_ReleaseOneToken.end(self, _r)

        def ReleaseTokens(self, activeID, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_ReleaseTokens.invoke(self, ((activeID, ), context))

        def ReleaseTokensAsync(self, activeID, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_ReleaseTokens.invokeAsync(self, ((activeID, ), context))

        def begin_ReleaseTokens(self, activeID, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_ReleaseTokens.begin(self, ((activeID, ), _response, _ex, _sent, context))

        def end_ReleaseTokens(self, _r):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_ReleaseTokens.end(self, _r)

        def ReleaseTokensByList(self, tokens, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_ReleaseTokensByList.invoke(self, ((tokens, ), context))

        def ReleaseTokensByListAsync(self, tokens, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_ReleaseTokensByList.invokeAsync(self, ((tokens, ), context))

        def begin_ReleaseTokensByList(self, tokens, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_ReleaseTokensByList.begin(self, ((tokens, ), _response, _ex, _sent, context))

        def end_ReleaseTokensByList(self, _r):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_ReleaseTokensByList.end(self, _r)

        def TryActiveToken2(self, requestModel, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_TryActiveToken2.invoke(self, ((requestModel, ), context))

        def TryActiveToken2Async(self, requestModel, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_TryActiveToken2.invokeAsync(self, ((requestModel, ), context))

        def begin_TryActiveToken2(self, requestModel, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_TryActiveToken2.begin(self, ((requestModel, ), _response, _ex, _sent, context))

        def end_TryActiveToken2(self, _r):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_TryActiveToken2.end(self, _r)

        def TryReleaseToken(self, nodeID, roomID, userID, tokenID, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_TryReleaseToken.invoke(self, ((nodeID, roomID, userID, tokenID), context))

        def TryReleaseTokenAsync(self, nodeID, roomID, userID, tokenID, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_TryReleaseToken.invokeAsync(self, ((nodeID, roomID, userID, tokenID), context))

        def begin_TryReleaseToken(self, nodeID, roomID, userID, tokenID, _response=None, _ex=None, _sent=None, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_TryReleaseToken.begin(self, ((nodeID, roomID, userID, tokenID), _response, _ex, _sent, context))

        def end_TryReleaseToken(self, _r):
            return _M_com.fastonz.fmserver.tokenMgr.TokenService._op_TryReleaseToken.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenServicePrx.ice_checkedCast(proxy, '::com::fastonz::fmserver::tokenMgr::TokenService', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_com.fastonz.fmserver.tokenMgr.TokenServicePrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::com::fastonz::fmserver::tokenMgr::TokenService'
    _M_com.fastonz.fmserver.tokenMgr._t_TokenServicePrx = IcePy.defineProxy('::com::fastonz::fmserver::tokenMgr::TokenService', TokenServicePrx)

    _M_com.fastonz.fmserver.tokenMgr.TokenServicePrx = TokenServicePrx
    del TokenServicePrx

    _M_com.fastonz.fmserver.tokenMgr.TokenService = Ice.createTempClass()
    class TokenService(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::com::fastonz::fmserver::tokenMgr::TokenService')

        def ice_id(self, current=None):
            return '::com::fastonz::fmserver::tokenMgr::TokenService'

        @staticmethod
        def ice_staticId():
            return '::com::fastonz::fmserver::tokenMgr::TokenService'

        def TryAddToken(self, requestModel, current=None):
            raise NotImplementedError("servant method 'TryAddToken' not implemented")

        def TryAddToken2(self, requestModel, current=None):
            raise NotImplementedError("servant method 'TryAddToken2' not implemented")

        def TryAddToken3(self, requestModel, current=None):
            raise NotImplementedError("servant method 'TryAddToken3' not implemented")

        def TryActiveToken(self, requestModel, current=None):
            raise NotImplementedError("servant method 'TryActiveToken' not implemented")

        def ActiveOneToken(self, tokenID, current=None):
            raise NotImplementedError("servant method 'ActiveOneToken' not implemented")

        def ActiveTokens(self, activeID, current=None):
            raise NotImplementedError("servant method 'ActiveTokens' not implemented")

        def CheckToken(self, ownerID, current=None):
            raise NotImplementedError("servant method 'CheckToken' not implemented")

        def ReleaseOneToken(self, tokenID, current=None):
            raise NotImplementedError("servant method 'ReleaseOneToken' not implemented")

        def ReleaseTokens(self, activeID, current=None):
            raise NotImplementedError("servant method 'ReleaseTokens' not implemented")

        def ReleaseTokensByList(self, tokens, current=None):
            raise NotImplementedError("servant method 'ReleaseTokensByList' not implemented")

        def TryActiveToken2(self, requestModel, current=None):
            raise NotImplementedError("servant method 'TryActiveToken2' not implemented")

        def TryReleaseToken(self, nodeID, roomID, userID, tokenID, current=None):
            raise NotImplementedError("servant method 'TryReleaseToken' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_com.fastonz.fmserver.tokenMgr._t_TokenServiceDisp)

        __repr__ = __str__

    _M_com.fastonz.fmserver.tokenMgr._t_TokenServiceDisp = IcePy.defineClass('::com::fastonz::fmserver::tokenMgr::TokenService', TokenService, (), None, ())
    TokenService._ice_type = _M_com.fastonz.fmserver.tokenMgr._t_TokenServiceDisp

    TokenService._op_TryAddToken = IcePy.Operation('TryAddToken', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), _M_com.fastonz.fmserver.model._t_TryAddTokenModel, False, 0),), (((), IcePy._t_int, False, 0),), ((), IcePy._t_int, False, 0), ())
    TokenService._op_TryAddToken2 = IcePy.Operation('TryAddToken2', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), _M_com.fastonz.fmserver.model._t_TryAddTokenModel2, False, 0),), (((), IcePy._t_int, False, 0),), ((), IcePy._t_int, False, 0), ())
    TokenService._op_TryAddToken3 = IcePy.Operation('TryAddToken3', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), _M_com.fastonz.fmserver.model._t_TryAddTokenModel3, False, 0),), (((), IcePy._t_int, False, 0),), ((), IcePy._t_int, False, 0), ())
    TokenService._op_TryActiveToken = IcePy.Operation('TryActiveToken', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), _M_com.fastonz.fmserver.model._t_TryActiveTokenModel, False, 0),), (((), IcePy._t_int, False, 0),), ((), IcePy._t_int, False, 0), ())
    TokenService._op_ActiveOneToken = IcePy.Operation('ActiveOneToken', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), IcePy._t_string, False, 0),), (), ((), IcePy._t_int, False, 0), ())
    TokenService._op_ActiveTokens = IcePy.Operation('ActiveTokens', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), IcePy._t_int, False, 0),), (), ((), IcePy._t_int, False, 0), ())
    TokenService._op_CheckToken = IcePy.Operation('CheckToken', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), IcePy._t_int, False, 0),), (), ((), IcePy._t_int, False, 0), ())
    TokenService._op_ReleaseOneToken = IcePy.Operation('ReleaseOneToken', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), IcePy._t_string, False, 0),), (), ((), IcePy._t_int, False, 0), ())
    TokenService._op_ReleaseTokens = IcePy.Operation('ReleaseTokens', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), IcePy._t_int, False, 0),), (), ((), IcePy._t_int, False, 0), ())
    TokenService._op_ReleaseTokensByList = IcePy.Operation('ReleaseTokensByList', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), _M_com.fastonz.fmserver.tokenMgr._t_TokenList, False, 0),), (), ((), IcePy._t_int, False, 0), ())
    TokenService._op_TryActiveToken2 = IcePy.Operation('TryActiveToken2', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), _M_com.fastonz.fmserver.model._t_TryActiveTokenModel, False, 0),), (((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0)), ((), IcePy._t_int, False, 0), ())
    TokenService._op_TryReleaseToken = IcePy.Operation('TryReleaseToken', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), IcePy._t_string, False, 0), ((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0), ((), IcePy._t_string, False, 0)), (((), IcePy._t_int, False, 0),), ((), IcePy._t_int, False, 0), ())

    _M_com.fastonz.fmserver.tokenMgr.TokenService = TokenService
    del TokenService

# End of module com.fastonz.fmserver.tokenMgr

__name__ = 'com.fastonz.fmserver'

# End of module com.fastonz.fmserver

__name__ = 'com.fastonz'

# End of module com.fastonz

__name__ = 'com'

# End of module com
