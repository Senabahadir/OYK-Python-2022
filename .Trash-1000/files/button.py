# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'button.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(205, 110)
        self.label = QLabel(Form)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(60, 20, 54, 17))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QRect(10, 60, 80, 25))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setGeometry(QRect(100, 60, 80, 25))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.label.setText(QCoreApplication.translate("Form", "TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("Form", "Artir", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", "Azalt", None))

    # retranslateUi
