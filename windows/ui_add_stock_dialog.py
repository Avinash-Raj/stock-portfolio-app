# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_stock_dialoglRWZgd.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QGridLayout, QLabel, QLayout,
    QLineEdit, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 400)
        Dialog.setMaximumSize(QSize(400, 400))
        Dialog.setStyleSheet(u"QLineEdit { border-radius: 5px; }")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.addStockFrame = QFrame(Dialog)
        self.addStockFrame.setObjectName(u"addStockFrame")
        self.addStockFrame.setMaximumSize(QSize(500, 700))
        self.addStockFrame.setFrameShape(QFrame.StyledPanel)
        self.addStockFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.addStockFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.sharesLineEdit = QLineEdit(self.addStockFrame)
        self.sharesLineEdit.setObjectName(u"sharesLineEdit")
        self.sharesLineEdit.setMinimumSize(QSize(20, 0))

        self.gridLayout.addWidget(self.sharesLineEdit, 2, 1, 1, 1)

        self.sharesLabel = QLabel(self.addStockFrame)
        self.sharesLabel.setObjectName(u"sharesLabel")

        self.gridLayout.addWidget(self.sharesLabel, 2, 0, 1, 1, Qt.AlignRight)

        self.nameLineEdit = QLineEdit(self.addStockFrame)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.gridLayout.addWidget(self.nameLineEdit, 0, 1, 1, 1)

        self.priceLabel = QLabel(self.addStockFrame)
        self.priceLabel.setObjectName(u"priceLabel")

        self.gridLayout.addWidget(self.priceLabel, 1, 0, 1, 1, Qt.AlignRight)

        self.nameLabel = QLabel(self.addStockFrame)
        self.nameLabel.setObjectName(u"nameLabel")

        self.gridLayout.addWidget(self.nameLabel, 0, 0, 1, 1, Qt.AlignRight)

        self.priceLineEdit = QLineEdit(self.addStockFrame)
        self.priceLineEdit.setObjectName(u"priceLineEdit")

        self.gridLayout.addWidget(self.priceLineEdit, 1, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 10)
        self.gridLayout.setColumnStretch(1, 10)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.buttonFrame = QFrame(self.addStockFrame)
        self.buttonFrame.setObjectName(u"buttonFrame")
        self.buttonFrame.setMinimumSize(QSize(0, 0))
        self.buttonFrame.setMaximumSize(QSize(700, 50))
        self.buttonFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.buttonFrame)
#ifndef Q_OS_MAC
        self.verticalLayout_3.setSpacing(-1)
#endif
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.buttonBox = QDialogButtonBox(self.buttonFrame)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setAutoFillBackground(True)
        self.buttonBox.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: #008B8B;\n"
"       border: 1px solid #c9c9c9;\n"
"       border-radius: 3px;\n"
"       padding: 5px;\n"
"       margin-right: 5px;\n"
"}")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout_3.addWidget(self.buttonBox)


        self.verticalLayout_2.addWidget(self.buttonFrame)


        self.verticalLayout.addWidget(self.addStockFrame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.sharesLabel.setText(QCoreApplication.translate("Dialog", u"Shares", None))
        self.priceLabel.setText(QCoreApplication.translate("Dialog", u"Price", None))
        self.nameLabel.setText(QCoreApplication.translate("Dialog", u"Name", None))
    # retranslateUi

