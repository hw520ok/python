# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(276, 153)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../emotion/bishi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.lblID = QtWidgets.QLabel(Form)
        self.lblID.setGeometry(QtCore.QRect(30, 20, 41, 16))
        self.lblID.setObjectName("lblID")
        self.lblPwd = QtWidgets.QLabel(Form)
        self.lblPwd.setGeometry(QtCore.QRect(30, 60, 41, 16))
        self.lblPwd.setObjectName("lblPwd")
        self.btnLogin = QtWidgets.QPushButton(Form)
        self.btnLogin.setGeometry(QtCore.QRect(170, 100, 81, 31))
        self.btnLogin.setObjectName("btnLogin")
        self.btnRegister = QtWidgets.QPushButton(Form)
        self.btnRegister.setGeometry(QtCore.QRect(30, 100, 81, 31))
        self.btnRegister.setObjectName("btnRegister")
        self.edtID = QtWidgets.QLineEdit(Form)
        self.edtID.setGeometry(QtCore.QRect(70, 20, 181, 20))
        self.edtID.setObjectName("edtID")
        self.edtPwd = QtWidgets.QLineEdit(Form)
        self.edtPwd.setGeometry(QtCore.QRect(70, 60, 181, 20))
        self.edtPwd.setObjectName("edtPwd")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "用户登录"))
        self.lblID.setText(_translate("Form", "帐号："))
        self.lblPwd.setText(_translate("Form", "密码："))
        self.btnLogin.setText(_translate("Form", "登录"))
        self.btnRegister.setText(_translate("Form", "注册"))

import res_rc
