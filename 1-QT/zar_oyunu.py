# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'zar_oyunu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ZarOyunu(object):
    def setupUi(self, ZarOyunu):
        if not ZarOyunu.objectName():
            ZarOyunu.setObjectName(u"ZarOyunu")
        ZarOyunu.resize(289, 163)
        self.verticalLayout = QVBoxLayout(ZarOyunu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txtZar = QLineEdit(ZarOyunu)
        self.txtZar.setObjectName(u"txtZar")
        font = QFont()
        font.setPointSize(20)
        self.txtZar.setFont(font)

        self.verticalLayout.addWidget(self.txtZar)

        self.btnAt = QPushButton(ZarOyunu)
        self.btnAt.setObjectName(u"btnAt")
        self.btnAt.setEnabled(False)

        self.verticalLayout.addWidget(self.btnAt)

        self.lblSonuc = QLabel(ZarOyunu)
        self.lblSonuc.setObjectName(u"lblSonuc")
        self.lblSonuc.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lblSonuc)


        self.retranslateUi(ZarOyunu)

        QMetaObject.connectSlotsByName(ZarOyunu)
    # setupUi

    def retranslateUi(self, ZarOyunu):
        ZarOyunu.setWindowTitle(QCoreApplication.translate("ZarOyunu", u"Zar Oyunu V1.0", None))
        self.txtZar.setInputMask(QCoreApplication.translate("ZarOyunu", u"0", None))
        self.btnAt.setText(QCoreApplication.translate("ZarOyunu", u"Zar At", None))
        self.lblSonuc.setText(QCoreApplication.translate("ZarOyunu", u"-", None))
    # retranslateUi

