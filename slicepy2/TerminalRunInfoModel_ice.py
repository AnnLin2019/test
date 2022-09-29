# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.5
#
# <auto-generated>
#
# Generated from file `TerminalRunInfoModel.ice'
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

if 'TerminalRunInfoModel' not in _M_com.fastonz.fmserver.model.__dict__:
    _M_com.fastonz.fmserver.model.TerminalRunInfoModel = Ice.createTempClass()
    class TerminalRunInfoModel(object):
        def __init__(self, terminalID='', terminalName='', roomID=0, userID=0, onlineState=0, bindCode='', activeSrvID=0):
            self.terminalID = terminalID
            self.terminalName = terminalName
            self.roomID = roomID
            self.userID = userID
            self.onlineState = onlineState
            self.bindCode = bindCode
            self.activeSrvID = activeSrvID

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.terminalID)
            _h = 5 * _h + Ice.getHash(self.terminalName)
            _h = 5 * _h + Ice.getHash(self.roomID)
            _h = 5 * _h + Ice.getHash(self.userID)
            _h = 5 * _h + Ice.getHash(self.onlineState)
            _h = 5 * _h + Ice.getHash(self.bindCode)
            _h = 5 * _h + Ice.getHash(self.activeSrvID)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_com.fastonz.fmserver.model.TerminalRunInfoModel):
                return NotImplemented
            else:
                if self.terminalID is None or other.terminalID is None:
                    if self.terminalID != other.terminalID:
                        return (-1 if self.terminalID is None else 1)
                else:
                    if self.terminalID < other.terminalID:
                        return -1
                    elif self.terminalID > other.terminalID:
                        return 1
                if self.terminalName is None or other.terminalName is None:
                    if self.terminalName != other.terminalName:
                        return (-1 if self.terminalName is None else 1)
                else:
                    if self.terminalName < other.terminalName:
                        return -1
                    elif self.terminalName > other.terminalName:
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
                if self.onlineState is None or other.onlineState is None:
                    if self.onlineState != other.onlineState:
                        return (-1 if self.onlineState is None else 1)
                else:
                    if self.onlineState < other.onlineState:
                        return -1
                    elif self.onlineState > other.onlineState:
                        return 1
                if self.bindCode is None or other.bindCode is None:
                    if self.bindCode != other.bindCode:
                        return (-1 if self.bindCode is None else 1)
                else:
                    if self.bindCode < other.bindCode:
                        return -1
                    elif self.bindCode > other.bindCode:
                        return 1
                if self.activeSrvID is None or other.activeSrvID is None:
                    if self.activeSrvID != other.activeSrvID:
                        return (-1 if self.activeSrvID is None else 1)
                else:
                    if self.activeSrvID < other.activeSrvID:
                        return -1
                    elif self.activeSrvID > other.activeSrvID:
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
            return IcePy.stringify(self, _M_com.fastonz.fmserver.model._t_TerminalRunInfoModel)

        __repr__ = __str__

    _M_com.fastonz.fmserver.model._t_TerminalRunInfoModel = IcePy.defineStruct('::com::fastonz::fmserver::model::TerminalRunInfoModel', TerminalRunInfoModel, (), (
        ('terminalID', (), IcePy._t_string),
        ('terminalName', (), IcePy._t_string),
        ('roomID', (), IcePy._t_int),
        ('userID', (), IcePy._t_int),
        ('onlineState', (), IcePy._t_int),
        ('bindCode', (), IcePy._t_string),
        ('activeSrvID', (), IcePy._t_int)
    ))

    _M_com.fastonz.fmserver.model.TerminalRunInfoModel = TerminalRunInfoModel
    del TerminalRunInfoModel

# End of module com.fastonz.fmserver.model

__name__ = 'com.fastonz.fmserver'

# End of module com.fastonz.fmserver

__name__ = 'com.fastonz'

# End of module com.fastonz

__name__ = 'com'

# End of module com