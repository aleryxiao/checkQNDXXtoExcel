# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledDwOOqm.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject,QRect)
from PySide6.QtWidgets import (QLabel, QLineEdit, QPushButton, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(636, 203)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.iB = QPushButton(self.centralwidget)
        self.iB.setObjectName(u"iB")
        self.iB.setGeometry(QRect(380, 50, 221, 31))
        self.oB = QPushButton(self.centralwidget)
        self.oB.setObjectName(u"oB")
        self.oB.setGeometry(QRect(380, 95, 221, 31))
        self.iT = QTextBrowser(self.centralwidget)
        self.iT.setObjectName(u"iT")
        self.iT.setGeometry(QRect(30, 50, 331, 31))
        self.oT = QTextBrowser(self.centralwidget)
        self.oT.setObjectName(u"oT")
        self.oT.setGeometry(QRect(30, 95, 331, 31))
        self.rB = QPushButton(self.centralwidget)
        self.rB.setObjectName(u"rB")
        self.rB.setGeometry(QRect(30, 144, 101, 31))
        self.rT = QTextBrowser(self.centralwidget)
        self.rT.setObjectName(u"rT")
        self.rT.setGeometry(QRect(150, 144, 451, 31))
        self.cT = QLineEdit(self.centralwidget)
        self.cT.setObjectName(u"cT")
        self.cT.setGeometry(QRect(129, 16, 113, 21))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 11, 121, 31))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u9752\u5e74\u5927\u5b66\u4e60Check @AleryXiao", None))
        self.iB.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8f93\u5165\u6587\u4ef6\uff08\u53ef\u591a\u9009\uff09", None))
        self.oB.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8f93\u51fa\u6587\u4ef6", None))
        self.iT.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u70b9\u51fb\u53f3\u4fa7\u6309\u94ae\u9009\u62e9Input\u6587\u4ef6\uff08\u540e\u53f0\u5bfc\u51fa\u7684\u8bb0\u5f55\uff09</p></body></html>", None))
        self.oT.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u70b9\u51fb\u53f3\u4fa7\u6309\u94ae\u9009\u62e9Output\u6587\u4ef6\uff08\u540d\u5355\uff09</p></body></html>", None))
        self.rB.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c", None))
        self.rT.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u6b64\u5904\u663e\u793a\u7a0b\u5e8f\u7684\u5f53\u524d\u72b6\u6001</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u73ed\u7ea7\u7f16\u53f7:", None))
    # retranslateUi

