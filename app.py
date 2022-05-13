# app.py
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(577, 469)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 120, 391, 241))
        self.groupBox.setObjectName("groupBox")
        self.bnt_add_file = QtWidgets.QPushButton(self.groupBox)
        self.bnt_add_file.setGeometry(QtCore.QRect(290, 30, 75, 23))
        self.bnt_add_file.setObjectName("bnt_add_file")
        self.bnt_translate = QtWidgets.QPushButton(self.groupBox)
        self.bnt_translate.setGeometry(QtCore.QRect(290, 200, 75, 23))
        self.bnt_translate.setObjectName("bnt_translate")
        self.files_listWidget = QtWidgets.QListWidget(self.groupBox)
        self.files_listWidget.setGeometry(QtCore.QRect(10, 30, 256, 192))
        self.files_listWidget.setObjectName("files_listWidget")
        self.bnt_delete_file = QtWidgets.QPushButton(self.groupBox)
        self.bnt_delete_file.setGeometry(QtCore.QRect(290, 70, 75, 23))
        self.bnt_delete_file.setObjectName("bnt_delete_file")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 391, 101))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(30, 30, 54, 12))
        self.label.setObjectName("label")
        # self.account = QtWidgets.QLineEdit(self.groupBox_2)
        # self.account.setGeometry(QtCore.QRect(90, 30, 241, 21))
        # self.account.setObjectName("account")
        # self.password = QtWidgets.QLineEdit(self.groupBox_2)
        # self.password.setGeometry(QtCore.QRect(90, 60, 241, 21))
        # self.password.setObjectName("password")
        # self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        # self.label_2.setGeometry(QtCore.QRect(30, 60, 54, 12))
        # self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Translate"))
        self.groupBox.setTitle(_translate("Form", "选择文件"))
        self.bnt_add_file.setText(_translate("Form", "添加文件"))
        self.bnt_translate.setText(_translate("Form", "全部翻译"))
        self.bnt_delete_file.setText(_translate("Form", "删除文件"))
        self.groupBox_2.setTitle(_translate("Form", ""))
        # self.label.setText(_translate("Form", "帐号"))
        # self.label_2.setText(_translate("Form", "密码"))

