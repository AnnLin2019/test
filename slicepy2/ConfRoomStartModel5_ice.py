# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.5
#
# <auto-generated>
#
# Generated from file `ConfRoomStartModel5.ice'
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

if 'ConfRoomStartModel5' not in _M_com.fastonz.fmserver.model.__dict__:
    _M_com.fastonz.fmserver.model.ConfRoomStartModel5 = Ice.createTempClass()
    class ConfRoomStartModel5(object):
        def __init__(self, roomName='', maxUserCount=0, defaultMode='', useDefaultFlag=0, defaultVideoCodec='', defaultVideoWind='', defaultVideoQOS='', defaultVideoBitrate=0, defaultVideoQuality=0, enableUserList=0, result=0, layout='', companyID=0, super=0, presenter=0, videoPushType=0, videoNum=0, enableScreenSharing=0, deptID=0, deptName='', companyName=''):
            self.roomName = roomName
            self.maxUserCount = maxUserCount
            self.defaultMode = defaultMode
            self.useDefaultFlag = useDefaultFlag
            self.defaultVideoCodec = defaultVideoCodec
            self.defaultVideoWind = defaultVideoWind
            self.defaultVideoQOS = defaultVideoQOS
            self.defaultVideoBitrate = defaultVideoBitrate
            self.defaultVideoQuality = defaultVideoQuality
            self.enableUserList = enableUserList
            self.result = result
            self.layout = layout
            self.companyID = companyID
            self.super = super
            self.presenter = presenter
            self.videoPushType = videoPushType
            self.videoNum = videoNum
            self.enableScreenSharing = enableScreenSharing
            self.deptID = deptID
            self.deptName = deptName
            self.companyName = companyName

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.roomName)
            _h = 5 * _h + Ice.getHash(self.maxUserCount)
            _h = 5 * _h + Ice.getHash(self.defaultMode)
            _h = 5 * _h + Ice.getHash(self.useDefaultFlag)
            _h = 5 * _h + Ice.getHash(self.defaultVideoCodec)
            _h = 5 * _h + Ice.getHash(self.defaultVideoWind)
            _h = 5 * _h + Ice.getHash(self.defaultVideoQOS)
            _h = 5 * _h + Ice.getHash(self.defaultVideoBitrate)
            _h = 5 * _h + Ice.getHash(self.defaultVideoQuality)
            _h = 5 * _h + Ice.getHash(self.enableUserList)
            _h = 5 * _h + Ice.getHash(self.result)
            _h = 5 * _h + Ice.getHash(self.layout)
            _h = 5 * _h + Ice.getHash(self.companyID)
            _h = 5 * _h + Ice.getHash(self.super)
            _h = 5 * _h + Ice.getHash(self.presenter)
            _h = 5 * _h + Ice.getHash(self.videoPushType)
            _h = 5 * _h + Ice.getHash(self.videoNum)
            _h = 5 * _h + Ice.getHash(self.enableScreenSharing)
            _h = 5 * _h + Ice.getHash(self.deptID)
            _h = 5 * _h + Ice.getHash(self.deptName)
            _h = 5 * _h + Ice.getHash(self.companyName)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_com.fastonz.fmserver.model.ConfRoomStartModel5):
                return NotImplemented
            else:
                if self.roomName is None or other.roomName is None:
                    if self.roomName != other.roomName:
                        return (-1 if self.roomName is None else 1)
                else:
                    if self.roomName < other.roomName:
                        return -1
                    elif self.roomName > other.roomName:
                        return 1
                if self.maxUserCount is None or other.maxUserCount is None:
                    if self.maxUserCount != other.maxUserCount:
                        return (-1 if self.maxUserCount is None else 1)
                else:
                    if self.maxUserCount < other.maxUserCount:
                        return -1
                    elif self.maxUserCount > other.maxUserCount:
                        return 1
                if self.defaultMode is None or other.defaultMode is None:
                    if self.defaultMode != other.defaultMode:
                        return (-1 if self.defaultMode is None else 1)
                else:
                    if self.defaultMode < other.defaultMode:
                        return -1
                    elif self.defaultMode > other.defaultMode:
                        return 1
                if self.useDefaultFlag is None or other.useDefaultFlag is None:
                    if self.useDefaultFlag != other.useDefaultFlag:
                        return (-1 if self.useDefaultFlag is None else 1)
                else:
                    if self.useDefaultFlag < other.useDefaultFlag:
                        return -1
                    elif self.useDefaultFlag > other.useDefaultFlag:
                        return 1
                if self.defaultVideoCodec is None or other.defaultVideoCodec is None:
                    if self.defaultVideoCodec != other.defaultVideoCodec:
                        return (-1 if self.defaultVideoCodec is None else 1)
                else:
                    if self.defaultVideoCodec < other.defaultVideoCodec:
                        return -1
                    elif self.defaultVideoCodec > other.defaultVideoCodec:
                        return 1
                if self.defaultVideoWind is None or other.defaultVideoWind is None:
                    if self.defaultVideoWind != other.defaultVideoWind:
                        return (-1 if self.defaultVideoWind is None else 1)
                else:
                    if self.defaultVideoWind < other.defaultVideoWind:
                        return -1
                    elif self.defaultVideoWind > other.defaultVideoWind:
                        return 1
                if self.defaultVideoQOS is None or other.defaultVideoQOS is None:
                    if self.defaultVideoQOS != other.defaultVideoQOS:
                        return (-1 if self.defaultVideoQOS is None else 1)
                else:
                    if self.defaultVideoQOS < other.defaultVideoQOS:
                        return -1
                    elif self.defaultVideoQOS > other.defaultVideoQOS:
                        return 1
                if self.defaultVideoBitrate is None or other.defaultVideoBitrate is None:
                    if self.defaultVideoBitrate != other.defaultVideoBitrate:
                        return (-1 if self.defaultVideoBitrate is None else 1)
                else:
                    if self.defaultVideoBitrate < other.defaultVideoBitrate:
                        return -1
                    elif self.defaultVideoBitrate > other.defaultVideoBitrate:
                        return 1
                if self.defaultVideoQuality is None or other.defaultVideoQuality is None:
                    if self.defaultVideoQuality != other.defaultVideoQuality:
                        return (-1 if self.defaultVideoQuality is None else 1)
                else:
                    if self.defaultVideoQuality < other.defaultVideoQuality:
                        return -1
                    elif self.defaultVideoQuality > other.defaultVideoQuality:
                        return 1
                if self.enableUserList is None or other.enableUserList is None:
                    if self.enableUserList != other.enableUserList:
                        return (-1 if self.enableUserList is None else 1)
                else:
                    if self.enableUserList < other.enableUserList:
                        return -1
                    elif self.enableUserList > other.enableUserList:
                        return 1
                if self.result is None or other.result is None:
                    if self.result != other.result:
                        return (-1 if self.result is None else 1)
                else:
                    if self.result < other.result:
                        return -1
                    elif self.result > other.result:
                        return 1
                if self.layout is None or other.layout is None:
                    if self.layout != other.layout:
                        return (-1 if self.layout is None else 1)
                else:
                    if self.layout < other.layout:
                        return -1
                    elif self.layout > other.layout:
                        return 1
                if self.companyID is None or other.companyID is None:
                    if self.companyID != other.companyID:
                        return (-1 if self.companyID is None else 1)
                else:
                    if self.companyID < other.companyID:
                        return -1
                    elif self.companyID > other.companyID:
                        return 1
                if self.super is None or other.super is None:
                    if self.super != other.super:
                        return (-1 if self.super is None else 1)
                else:
                    if self.super < other.super:
                        return -1
                    elif self.super > other.super:
                        return 1
                if self.presenter is None or other.presenter is None:
                    if self.presenter != other.presenter:
                        return (-1 if self.presenter is None else 1)
                else:
                    if self.presenter < other.presenter:
                        return -1
                    elif self.presenter > other.presenter:
                        return 1
                if self.videoPushType is None or other.videoPushType is None:
                    if self.videoPushType != other.videoPushType:
                        return (-1 if self.videoPushType is None else 1)
                else:
                    if self.videoPushType < other.videoPushType:
                        return -1
                    elif self.videoPushType > other.videoPushType:
                        return 1
                if self.videoNum is None or other.videoNum is None:
                    if self.videoNum != other.videoNum:
                        return (-1 if self.videoNum is None else 1)
                else:
                    if self.videoNum < other.videoNum:
                        return -1
                    elif self.videoNum > other.videoNum:
                        return 1
                if self.enableScreenSharing is None or other.enableScreenSharing is None:
                    if self.enableScreenSharing != other.enableScreenSharing:
                        return (-1 if self.enableScreenSharing is None else 1)
                else:
                    if self.enableScreenSharing < other.enableScreenSharing:
                        return -1
                    elif self.enableScreenSharing > other.enableScreenSharing:
                        return 1
                if self.deptID is None or other.deptID is None:
                    if self.deptID != other.deptID:
                        return (-1 if self.deptID is None else 1)
                else:
                    if self.deptID < other.deptID:
                        return -1
                    elif self.deptID > other.deptID:
                        return 1
                if self.deptName is None or other.deptName is None:
                    if self.deptName != other.deptName:
                        return (-1 if self.deptName is None else 1)
                else:
                    if self.deptName < other.deptName:
                        return -1
                    elif self.deptName > other.deptName:
                        return 1
                if self.companyName is None or other.companyName is None:
                    if self.companyName != other.companyName:
                        return (-1 if self.companyName is None else 1)
                else:
                    if self.companyName < other.companyName:
                        return -1
                    elif self.companyName > other.companyName:
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
            return IcePy.stringify(self, _M_com.fastonz.fmserver.model._t_ConfRoomStartModel5)

        __repr__ = __str__

    _M_com.fastonz.fmserver.model._t_ConfRoomStartModel5 = IcePy.defineStruct('::com::fastonz::fmserver::model::ConfRoomStartModel5', ConfRoomStartModel5, (), (
        ('roomName', (), IcePy._t_string),
        ('maxUserCount', (), IcePy._t_int),
        ('defaultMode', (), IcePy._t_string),
        ('useDefaultFlag', (), IcePy._t_int),
        ('defaultVideoCodec', (), IcePy._t_string),
        ('defaultVideoWind', (), IcePy._t_string),
        ('defaultVideoQOS', (), IcePy._t_string),
        ('defaultVideoBitrate', (), IcePy._t_int),
        ('defaultVideoQuality', (), IcePy._t_int),
        ('enableUserList', (), IcePy._t_int),
        ('result', (), IcePy._t_int),
        ('layout', (), IcePy._t_string),
        ('companyID', (), IcePy._t_int),
        ('super', (), IcePy._t_int),
        ('presenter', (), IcePy._t_int),
        ('videoPushType', (), IcePy._t_int),
        ('videoNum', (), IcePy._t_int),
        ('enableScreenSharing', (), IcePy._t_int),
        ('deptID', (), IcePy._t_int),
        ('deptName', (), IcePy._t_string),
        ('companyName', (), IcePy._t_string)
    ))

    _M_com.fastonz.fmserver.model.ConfRoomStartModel5 = ConfRoomStartModel5
    del ConfRoomStartModel5

# End of module com.fastonz.fmserver.model

__name__ = 'com.fastonz.fmserver'

# End of module com.fastonz.fmserver

__name__ = 'com.fastonz'

# End of module com.fastonz

__name__ = 'com'

# End of module com
