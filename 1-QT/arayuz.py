# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'progress_with_button.ui'
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
            Form.setObjectName(u"Form")
        Form.resize(409, 190)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.btnStart = QPushButton(Form)
        self.btnStart.setObjectName(u"btnStart")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnStart.sizePolicy().hasHeightForWidth())
        self.btnStart.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(20)
        self.btnStart.setFont(font)

        self.horizontalLayout.addWidget(self.btnStart)

        self.btnStop = QPushButton(Form)
        self.btnStop.setObjectName(u"btnStop")
        self.btnStop.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btnStop.sizePolicy().hasHeightForWidth())
        self.btnStop.setSizePolicy(sizePolicy)
        self.btnStop.setFont(font)

        self.horizontalLayout.addWidget(self.btnStop)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblUser = QLabel(Form)
        self.lblUser.setObjectName(u"lblUser")
        self.lblUser.setFont(font)

        self.horizontalLayout_2.addWidget(self.lblUser)

        self.lblStatus = QLabel(Form)
        self.lblStatus.setObjectName(u"lblStatus")
        self.lblStatus.setFont(font)
        self.lblStatus.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lblStatus)

        self.lblComputer = QLabel(Form)
        self.lblComputer.setObjectName(u"lblComputer")
        self.lblComputer.setFont(font)
        self.lblComputer.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lblComputer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btnStart.setText(QCoreApplication.translate("Form", u"Start", None))
        self.btnStop.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.lblUser.setText(QCoreApplication.translate("Form", u"0", None))
        self.lblStatus.setText(QCoreApplication.translate("Form", u"-", None))
        self.lblComputer.setText(QCoreApplication.translate("Form", u"0", None))
    # retranslateUi

