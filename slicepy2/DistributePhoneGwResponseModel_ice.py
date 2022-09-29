# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.5
#
# <auto-generated>
#
# Generated from file `DistributePhoneGwResponseModel.ice'
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

if 'CallOutPhoneGwInfo' not in _M_com.fastonz.fmserver.model.__dict__:
    _M_com.fastonz.fmserver.model.CallOutPhoneGwInfo = Ice.createTempClass()
    class CallOutPhoneGwInfo(object):
        def __init__(self, phoneNum='', phoneGwAddr='', phoneGwCheckCode='', PhoneGwDevID='', callNum='', inviteCode=''):
            self.phoneNum = phoneNum
            self.phoneGwAddr = phoneGwAddr
            self.phoneGwCheckCode = phoneGwCheckCode
            self.PhoneGwDevID = PhoneGwDevID
            self.callNum = callNum
            self.inviteCode = inviteCode

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.phoneNum)
            _h = 5 * _h + Ice.getHash(self.phoneGwAddr)
            _h = 5 * _h + Ice.getHash(self.phoneGwCheckCode)
            _h = 5 * _h + Ice.getHash(self.PhoneGwDevID)
            _h = 5 * _h + Ice.getHash(self.callNum)
            _h = 5 * _h + Ice.getHash(self.inviteCode)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_com.fastonz.fmserver.model.CallOutPhoneGwInfo):
                return NotImplemented
            else:
                if self.phoneNum is None or other.phoneNum is None:
                    if self.phoneNum != other.phoneNum:
                        return (-1 if self.phoneNum is None else 1)
                else:
                    if self.phoneNum < other.phoneNum:
                        return -1
                    elif self.phoneNum > other.phoneNum:
                        return 1
                if self.phoneGwAddr is None or other.phoneGwAddr is None:
                    if self.phoneGwAddr != other.phoneGwAddr:
                        return (-1 if self.phoneGwAddr is None else 1)
                else:
                    if self.phoneGwAddr < other.phoneGwAddr:
                        return -1
                    elif self.phoneGwAddr > other.phoneGwAddr:
                        return 1
                if self.phoneGwCheckCode is None or other.phoneGwCheckCode is None:
                    if self.phoneGwCheckCode != other.phoneGwCheckCode:
                        return (-1 if self.phoneGwCheckCode is None else 1)
                else:
                    if self.phoneGwCheckCode < other.phoneGwCheckCode:
                        return -1
                    elif self.phoneGwCheckCode > other.phoneGwCheckCode:
                        return 1
                if self.PhoneGwDevID is None or other.PhoneGwDevID is None:
                    if self.PhoneGwDevID != other.PhoneGwDevID:
                        return (-1 if self.PhoneGwDevID is None else 1)
                else:
                    if self.PhoneGwDevID < other.PhoneGwDevID:
                        return -1
                    elif self.PhoneGwDevID > other.PhoneGwDevID:
                        return 1
                if self.callNum is None or other.callNum is None:
                    if self.callNum != other.callNum:
                        return (-1 if self.callNum is None else 1)
                else:
                    if self.callNum < other.callNum:
                        return -1
                    elif self.callNum > other.callNum:
                        return 1
                if self.inviteCode is None or other.inviteCode is None:
                    if self.inviteCode != other.inviteCode:
                        return (-1 if self.inviteCode is None else 1)
                else:
                    if self.inviteCode < other.inviteCode:
                        return -1
                    elif self.inviteCode > other.inviteCode:
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
            return IcePy.stringify(self, _M_com.fastonz.fmserver.model._t_CallOutPhoneGwInfo)

        __repr__ = __str__

    _M_com.fastonz.fmserver.model._t_CallOutPhoneGwInfo = IcePy.defineStruct('::com::fastonz::fmserver::model::CallOutPhoneGwInfo', CallOutPhoneGwInfo, (), (
        ('phoneNum', (), IcePy._t_string),
        ('phoneGwAddr', (), IcePy._t_string),
        ('phoneGwCheckCode', (), IcePy._t_string),
        ('PhoneGwDevID', (), IcePy._t_string),
        ('callNum', (), IcePy._t_string),
        ('inviteCode', (), IcePy._t_string)
    ))

    _M_com.fastonz.fmserver.model.CallOutPhoneGwInfo = CallOutPhoneGwInfo
    del CallOutPhoneGwInfo

if '_t_CallOutPhoneGwInfoList' not in _M_com.fastonz.fmserver.model.__dict__:
    _M_com.fastonz.fmserver.model._t_CallOutPhoneGwInfoList = IcePy.defineSequence('::com::fastonz::fmserver::model::CallOutPhoneGwInfoList', (), _M_com.fastonz.fmserver.model._t_CallOutPhoneGwInfo)

if 'DistributePhoneGwResponseModel' not in _M_com.fastonz.fmserver.model.__dict__:
    _M_com.fastonz.fmserver.model.DistributePhoneGwResponseModel = Ice.createTempClass()
    class DistributePhoneGwResponseModel(object):
        def __init__(self, result=0, remainCallCount=0, roomID=0, userID=0, callOutGwInfo=None):
            self.result = result
            self.remainCallCount = remainCallCount
            self.roomID = roomID
            self.userID = userID
            self.callOutGwInfo = callOutGwInfo

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.result)
            _h = 5 * _h + Ice.getHash(self.remainCallCount)
            _h = 5 * _h + Ice.getHash(self.roomID)
            _h = 5 * _h + Ice.getHash(self.userID)
            if self.callOutGwInfo:
                for _i0 in self.callOutGwInfo:
                    _h = 5 * _h + Ice.getHash(_i0)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_com.fastonz.fmserver.model.DistributePhoneGwResponseModel):
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
                if self.remainCallCount is None or other.remainCallCount is None:
                    if self.remainCallCount != other.remainCallCount:
                        return (-1 if self.remainCallCount is None else 1)
                else:
                    if self.remainCallCount < other.remainCallCount:
                        return -1
                    elif self.remainCallCount > other.remainCallCount:
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
                if self.callOutGwInfo is None or other.callOutGwInfo is None:
                    if self.callOutGwInfo != other.callOutGwInfo:
                        return (-1 if self.callOutGwInfo is None else 1)
                else:
                    if self.callOutGwInfo < other.callOutGwInfo:
                        return -1
                    elif self.callOutGwInfo > other.callOutGwInfo:
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
            return IcePy.stringify(self, _M_com.fastonz.fmserver.model._t_DistributePhoneGwResponseModel)

        __repr__ = __str__

    _M_com.fastonz.fmserver.model._t_DistributePhoneGwResponseModel = IcePy.defineStruct('::com::fastonz::fmserver::model::DistributePhoneGwResponseModel', DistributePhoneGwResponseModel, (), (
        ('result', (), IcePy._t_int),
        ('remainCallCount', (), IcePy._t_int),
        ('roomID', (), IcePy._t_int),
        ('userID', (), IcePy._t_int),
        ('callOutGwInfo', (), _M_com.fastonz.fmserver.model._t_CallOutPhoneGwInfoList)
    ))

    _M_com.fastonz.fmserver.model.DistributePhoneGwResponseModel = DistributePhoneGwResponseModel
    del DistributePhoneGwResponseModel

# End of module com.fastonz.fmserver.model

__name__ = 'com.fastonz.fmserver'

# End of module com.fastonz.fmserver

__name__ = 'com.fastonz'

# End of module com.fastonz

__name__ = 'com'

# End of module com