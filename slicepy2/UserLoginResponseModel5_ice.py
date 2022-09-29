# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.5
#
# <auto-generated>
#
# Generated from file `UserLoginResponseModel5.ice'
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

if 'UserLoginResponseModel5' not in _M_com.fastonz.fmserver.model.__dict__:
    _M_com.fastonz.fmserver.model.UserLoginResponseModel5 = Ice.createTempClass()
    class UserLoginResponseModel5(object):
        def __init__(self, displayName='', userRight=0, userLevel=0, callRight=0, seatList=0, nodeID=0, urole='', deptID=0, sex='', tel='', mobile='', email='', bindUserID=0, result=0, lastInsertID=0, role='', h323Right=0, deptName=''):
            self.displayName = displayName
            self.userRight = userRight
            self.userLevel = userLevel
            self.callRight = callRight
            self.seatList = seatList
            self.nodeID = nodeID
            self.urole = urole
            self.deptID = deptID
            self.sex = sex
            self.tel = tel
            self.mobile = mobile
            self.email = email
            self.bindUserID = bindUserID
            self.result = result
            self.lastInsertID = lastInsertID
            self.role = role
            self.h323Right = h323Right
            self.deptName = deptName

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.displayName)
            _h = 5 * _h + Ice.getHash(self.userRight)
            _h = 5 * _h + Ice.getHash(self.userLevel)
            _h = 5 * _h + Ice.getHash(self.callRight)
            _h = 5 * _h + Ice.getHash(self.seatList)
            _h = 5 * _h + Ice.getHash(self.nodeID)
            _h = 5 * _h + Ice.getHash(self.urole)
            _h = 5 * _h + Ice.getHash(self.deptID)
            _h = 5 * _h + Ice.getHash(self.sex)
            _h = 5 * _h + Ice.getHash(self.tel)
            _h = 5 * _h + Ice.getHash(self.mobile)
            _h = 5 * _h + Ice.getHash(self.email)
            _h = 5 * _h + Ice.getHash(self.bindUserID)
            _h = 5 * _h + Ice.getHash(self.result)
            _h = 5 * _h + Ice.getHash(self.lastInsertID)
            _h = 5 * _h + Ice.getHash(self.role)
            _h = 5 * _h + Ice.getHash(self.h323Right)
            _h = 5 * _h + Ice.getHash(self.deptName)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_com.fastonz.fmserver.model.UserLoginResponseModel5):
                return NotImplemented
            else:
                if self.displayName is None or other.displayName is None:
                    if self.displayName != other.displayName:
                        return (-1 if self.displayName is None else 1)
                else:
                    if self.displayName < other.displayName:
                        return -1
                    elif self.displayName > other.displayName:
                        return 1
                if self.userRight is None or other.userRight is None:
                    if self.userRight != other.userRight:
                        return (-1 if self.userRight is None else 1)
                else:
                    if self.userRight < other.userRight:
                        return -1
                    elif self.userRight > other.userRight:
                        return 1
                if self.userLevel is None or other.userLevel is None:
                    if self.userLevel != other.userLevel:
                        return (-1 if self.userLevel is None else 1)
                else:
                    if self.userLevel < other.userLevel:
                        return -1
                    elif self.userLevel > other.userLevel:
                        return 1
                if self.callRight is None or other.callRight is None:
                    if self.callRight != other.callRight:
                        return (-1 if self.callRight is None else 1)
                else:
                    if self.callRight < other.callRight:
                        return -1
                    elif self.callRight > other.callRight:
                        return 1
                if self.seatList is None or other.seatList is None:
                    if self.seatList != other.seatList:
                        return (-1 if self.seatList is None else 1)
                else:
                    if self.seatList < other.seatList:
                        return -1
                    elif self.seatList > other.seatList:
                        return 1
                if self.nodeID is None or other.nodeID is None:
                    if self.nodeID != other.nodeID:
                        return (-1 if self.nodeID is None else 1)
                else:
                    if self.nodeID < other.nodeID:
                        return -1
                    elif self.nodeID > other.nodeID:
                        return 1
                if self.urole is None or other.urole is None:
                    if self.urole != other.urole:
                        return (-1 if self.urole is None else 1)
                else:
                    if self.urole < other.urole:
                        return -1
                    elif self.urole > other.urole:
                        return 1
                if self.deptID is None or other.deptID is None:
                    if self.deptID != other.deptID:
                        return (-1 if self.deptID is None else 1)
                else:
                    if self.deptID < other.deptID:
                        return -1
                    elif self.deptID > other.deptID:
                        return 1
                if self.sex is None or other.sex is None:
                    if self.sex != other.sex:
                        return (-1 if self.sex is None else 1)
                else:
                    if self.sex < other.sex:
                        return -1
                    elif self.sex > other.sex:
                        return 1
                if self.tel is None or other.tel is None:
                    if self.tel != other.tel:
                        return (-1 if self.tel is None else 1)
                else:
                    if self.tel < other.tel:
                        return -1
                    elif self.tel > other.tel:
                        return 1
                if self.mobile is None or other.mobile is None:
                    if self.mobile != other.mobile:
                        return (-1 if self.mobile is None else 1)
                else:
                    if self.mobile < other.mobile:
                        return -1
                    elif self.mobile > other.mobile:
                        return 1
                if self.email is None or other.email is None:
                    if self.email != other.email:
                        return (-1 if self.email is None else 1)
                else:
                    if self.email < other.email:
                        return -1
                    elif self.email > other.email:
                        return 1
                if self.bindUserID is None or other.bindUserID is None:
                    if self.bindUserID != other.bindUserID:
                        return (-1 if self.bindUserID is None else 1)
                else:
                    if self.bindUserID < other.bindUserID:
                        return -1
                    elif self.bindUserID > other.bindUserID:
                        return 1
                if self.result is None or other.result is None:
                    if self.result != other.result:
                        return (-1 if self.result is None else 1)
                else:
                    if self.result < other.result:
                        return -1
                    elif self.result > other.result:
                        return 1
                if self.lastInsertID is None or other.lastInsertID is None:
                    if self.lastInsertID != other.lastInsertID:
                        return (-1 if self.lastInsertID is None else 1)
                else:
                    if self.lastInsertID < other.lastInsertID:
                        return -1
                    elif self.lastInsertID > other.lastInsertID:
                        return 1
                if self.role is None or other.role is None:
                    if self.role != other.role:
                        return (-1 if self.role is None else 1)
                else:
                    if self.role < other.role:
                        return -1
                    elif self.role > other.role:
                        return 1
                if self.h323Right is None or other.h323Right is None:
                    if self.h323Right != other.h323Right:
                        return (-1 if self.h323Right is None else 1)
                else:
                    if self.h323Right < other.h323Right:
                        return -1
                    elif self.h323Right > other.h323Right:
                        return 1
                if self.deptName is None or other.deptName is None:
                    if self.deptName != other.deptName:
                        return (-1 if self.deptName is None else 1)
                else:
                    if self.deptName < other.deptName:
                        return -1
                    elif self.deptName > other.deptName:
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
            return IcePy.stringify(self, _M_com.fastonz.fmserver.model._t_UserLoginResponseModel5)

        __repr__ = __str__

    _M_com.fastonz.fmserver.model._t_UserLoginResponseModel5 = IcePy.defineStruct('::com::fastonz::fmserver::model::UserLoginResponseModel5', UserLoginResponseModel5, (), (
        ('displayName', (), IcePy._t_string),
        ('userRight', (), IcePy._t_int),
        ('userLevel', (), IcePy._t_int),
        ('callRight', (), IcePy._t_int),
        ('seatList', (), IcePy._t_int),
        ('nodeID', (), IcePy._t_int),
        ('urole', (), IcePy._t_string),
        ('deptID', (), IcePy._t_int),
        ('sex', (), IcePy._t_string),
        ('tel', (), IcePy._t_string),
        ('mobile', (), IcePy._t_string),
        ('email', (), IcePy._t_string),
        ('bindUserID', (), IcePy._t_int),
        ('result', (), IcePy._t_int),
        ('lastInsertID', (), IcePy._t_int),
        ('role', (), IcePy._t_string),
        ('h323Right', (), IcePy._t_int),
        ('deptName', (), IcePy._t_string)
    ))

    _M_com.fastonz.fmserver.model.UserLoginResponseModel5 = UserLoginResponseModel5
    del UserLoginResponseModel5

# End of module com.fastonz.fmserver.model

__name__ = 'com.fastonz.fmserver'

# End of module com.fastonz.fmserver

__name__ = 'com.fastonz'

# End of module com.fastonz

__name__ = 'com'

# End of module com
