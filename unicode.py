# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unicode.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 209)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(320, 30, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 120, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 29, 281, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 120, 281, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.unicode_str)
        self.pushButton_2.clicked.connect(self.str_unicode)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "游魂制作-unicode互转 V1.0 QQ:657970252"))
        self.pushButton.setText(_translate("Form", "转汉字"))
        self.pushButton_2.setText(_translate("Form", "转unicode"))

    def unicode_str(self):
        # unicode = input("请输入unicode编码：").encode('utf-8').decode('unicode_escape')
        unicode=self.lineEdit.text()
        unicode=str(unicode).encode('utf-8').decode('unicode_escape')
        print(unicode)

    def str_unicode(self):
        # text = input("请输入字符：").encode("unicode_escape")
        text=self.lineEdit_2.text().encode("unicode_escape")
        print(str(text).encode('utf-8').decode('unicode_escape').replace(r"b'", '', ).replace("'", ""))
