# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.5
#
# <auto-generated>
#
# Generated from file `LiveRoomExpandModel.ice'
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

# Start of module com.fastonz.live
_M_com.fastonz.live = Ice.openModule('com.fastonz.live')
__name__ = 'com.fastonz.live'

# Start of module com.fastonz.live.sliceprotocol
_M_com.fastonz.live.sliceprotocol = Ice.openModule('com.fastonz.live.sliceprotocol')
__name__ = 'com.fastonz.live.sliceprotocol'

# Start of module com.fastonz.live.sliceprotocol.model
_M_com.fastonz.live.sliceprotocol.model = Ice.openModule('com.fastonz.live.sliceprotocol.model')
__name__ = 'com.fastonz.live.sliceprotocol.model'

if '_t_KickList' not in _M_com.fastonz.live.sliceprotocol.model.__dict__:
    _M_com.fastonz.live.sliceprotocol.model._t_KickList = IcePy.defineSequence('::com::fastonz::live::sliceprotocol::model::KickList', (), IcePy._t_string)

if '_t_MuteList' not in _M_com.fastonz.live.sliceprotocol.model.__dict__:
    _M_com.fastonz.live.sliceprotocol.model._t_MuteList = IcePy.defineSequence('::com::fastonz::live::sliceprotocol::model::MuteList', (), IcePy._t_string)

if '_t_SensitiveWordList' not in _M_com.fastonz.live.sliceprotocol.model.__dict__:
    _M_com.fastonz.live.sliceprotocol.model._t_SensitiveWordList = IcePy.defineSequence('::com::fastonz::live::sliceprotocol::model::SensitiveWordList', (), IcePy._t_string)

if 'LiveRoomExpandModel' not in _M_com.fastonz.live.sliceprotocol.model.__dict__:
    _M_com.fastonz.live.sliceprotocol.model.LiveRoomExpandModel = Ice.createTempClass()
    class LiveRoomExpandModel(object):
        def __init__(self, privateChatSwitch=False, groupChatSwitch=False, giftSwitch=False, meetingReceiveGroupChatSwitch=False, multiLanguageSwitch=False, kickList=None, muteList=None, sensitiveWordList=None, chatBufferSize=0, autoCloseTime=0):
            self.privateChatSwitch = privateChatSwitch
            self.groupChatSwitch = groupChatSwitch
            self.giftSwitch = giftSwitch
            self.meetingReceiveGroupChatSwitch = meetingReceiveGroupChatSwitch
            self.multiLanguageSwitch = multiLanguageSwitch
            self.kickList = kickList
            self.muteList = muteList
            self.sensitiveWordList = sensitiveWordList
            self.chatBufferSize = chatBufferSize
            self.autoCloseTime = autoCloseTime

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.privateChatSwitch)
            _h = 5 * _h + Ice.getHash(self.groupChatSwitch)
            _h = 5 * _h + Ice.getHash(self.giftSwitch)
            _h = 5 * _h + Ice.getHash(self.meetingReceiveGroupChatSwitch)
            _h = 5 * _h + Ice.getHash(self.multiLanguageSwitch)
            if self.kickList:
                for _i0 in self.kickList:
                    _h = 5 * _h + Ice.getHash(_i0)
            if self.muteList:
                for _i1 in self.muteList:
                    _h = 5 * _h + Ice.getHash(_i1)
            if self.sensitiveWordList:
                for _i2 in self.sensitiveWordList:
                    _h = 5 * _h + Ice.getHash(_i2)
            _h = 5 * _h + Ice.getHash(self.chatBufferSize)
            _h = 5 * _h + Ice.getHash(self.autoCloseTime)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_com.fastonz.live.sliceprotocol.model.LiveRoomExpandModel):
                return NotImplemented
            else:
                if self.privateChatSwitch is None or other.privateChatSwitch is None:
                    if self.privateChatSwitch != other.privateChatSwitch:
                        return (-1 if self.privateChatSwitch is None else 1)
                else:
                    if self.privateChatSwitch < other.privateChatSwitch:
                        return -1
                    elif self.privateChatSwitch > other.privateChatSwitch:
                        return 1
                if self.groupChatSwitch is None or other.groupChatSwitch is None:
                    if self.groupChatSwitch != other.groupChatSwitch:
                        return (-1 if self.groupChatSwitch is None else 1)
                else:
                    if self.groupChatSwitch < other.groupChatSwitch:
                        return -1
                    elif self.groupChatSwitch > other.groupChatSwitch:
                        return 1
                if self.giftSwitch is None or other.giftSwitch is None:
                    if self.giftSwitch != other.giftSwitch:
                        return (-1 if self.giftSwitch is None else 1)
                else:
                    if self.giftSwitch < other.giftSwitch:
                        return -1
                    elif self.giftSwitch > other.giftSwitch:
                        return 1
                if self.meetingReceiveGroupChatSwitch is None or other.meetingReceiveGroupChatSwitch is None:
                    if self.meetingReceiveGroupChatSwitch != other.meetingReceiveGroupChatSwitch:
                        return (-1 if self.meetingReceiveGroupChatSwitch is None else 1)
                else:
                    if self.meetingReceiveGroupChatSwitch < other.meetingReceiveGroupChatSwitch:
                        return -1
                    elif self.meetingReceiveGroupChatSwitch > other.meetingReceiveGroupChatSwitch:
                        return 1
                if self.multiLanguageSwitch is None or other.multiLanguageSwitch is None:
                    if self.multiLanguageSwitch != other.multiLanguageSwitch:
                        return (-1 if self.multiLanguageSwitch is None else 1)
                else:
                    if self.multiLanguageSwitch < other.multiLanguageSwitch:
                        return -1
                    elif self.multiLanguageSwitch > other.multiLanguageSwitch:
                        return 1
                if self.kickList is None or other.kickList is None:
                    if self.kickList != other.kickList:
                        return (-1 if self.kickList is None else 1)
                else:
                    if self.kickList < other.kickList:
                        return -1
                    elif self.kickList > other.kickList:
                        return 1
                if self.muteList is None or other.muteList is None:
                    if self.muteList != other.muteList:
                        return (-1 if self.muteList is None else 1)
                else:
                    if self.muteList < other.muteList:
                        return -1
                    elif self.muteList > other.muteList:
                        return 1
                if self.sensitiveWordList is None or other.sensitiveWordList is None:
                    if self.sensitiveWordList != other.sensitiveWordList:
                        return (-1 if self.sensitiveWordList is None else 1)
                else:
                    if self.sensitiveWordList < other.sensitiveWordList:
                        return -1
                    elif self.sensitiveWordList > other.sensitiveWordList:
                        return 1
                if self.chatBufferSize is None or other.chatBufferSize is None:
                    if self.chatBufferSize != other.chatBufferSize:
                        return (-1 if self.chatBufferSize is None else 1)
                else:
                    if self.chatBufferSize < other.chatBufferSize:
                        return -1
                    elif self.chatBufferSize > other.chatBufferSize:
                        return 1
                if self.autoCloseTime is None or other.autoCloseTime is None:
                    if self.autoCloseTime != other.autoCloseTime:
                        return (-1 if self.autoCloseTime is None else 1)
                else:
                    if self.autoCloseTime < other.autoCloseTime:
                        return -1
                    elif self.autoCloseTime > other.autoCloseTime:
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
            return IcePy.stringify(self, _M_com.fastonz.live.sliceprotocol.model._t_LiveRoomExpandModel)

        __repr__ = __str__

    _M_com.fastonz.live.sliceprotocol.model._t_LiveRoomExpandModel = IcePy.defineStruct('::com::fastonz::live::sliceprotocol::model::LiveRoomExpandModel', LiveRoomExpandModel, (), (
        ('privateChatSwitch', (), IcePy._t_bool),
        ('groupChatSwitch', (), IcePy._t_bool),
        ('giftSwitch', (), IcePy._t_bool),
        ('meetingReceiveGroupChatSwitch', (), IcePy._t_bool),
        ('multiLanguageSwitch', (), IcePy._t_bool),
        ('kickList', (), _M_com.fastonz.live.sliceprotocol.model._t_KickList),
        ('muteList', (), _M_com.fastonz.live.sliceprotocol.model._t_MuteList),
        ('sensitiveWordList', (), _M_com.fastonz.live.sliceprotocol.model._t_SensitiveWordList),
        ('chatBufferSize', (), IcePy._t_int),
        ('autoCloseTime', (), IcePy._t_int)
    ))

    _M_com.fastonz.live.sliceprotocol.model.LiveRoomExpandModel = LiveRoomExpandModel
    del LiveRoomExpandModel

# End of module com.fastonz.live.sliceprotocol.model

__name__ = 'com.fastonz.live.sliceprotocol'

# End of module com.fastonz.live.sliceprotocol

__name__ = 'com.fastonz.live'

# End of module com.fastonz.live

__name__ = 'com.fastonz'

# End of module com.fastonz

__name__ = 'com'

# End of module com