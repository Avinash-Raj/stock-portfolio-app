# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_stock_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(708, 635)
        Dialog.setStyleSheet(u"QLineEdit { border-radius: 5px; }")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.addStockFrame = QFrame(Dialog)
        self.addStockFrame.setObjectName(u"addStockFrame")
        self.addStockFrame.setFrameShape(QFrame.StyledPanel)
        self.addStockFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.addStockFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(-1, 20, -1, -1)
        self.marketValueLineEdit = QLineEdit(self.addStockFrame)
        self.marketValueLineEdit.setObjectName(u"marketValueLineEdit")

        self.gridLayout.addWidget(self.marketValueLineEdit, 4, 1, 1, 1)

        self.priceLabel = QLabel(self.addStockFrame)
        self.priceLabel.setObjectName(u"priceLabel")

        self.gridLayout.addWidget(self.priceLabel, 1, 0, 1, 1, Qt.AlignRight)

        self.nameLabel = QLabel(self.addStockFrame)
        self.nameLabel.setObjectName(u"nameLabel")

        self.gridLayout.addWidget(self.nameLabel, 0, 0, 1, 1, Qt.AlignRight)

        self.sharesLabel = QLabel(self.addStockFrame)
        self.sharesLabel.setObjectName(u"sharesLabel")

        self.gridLayout.addWidget(self.sharesLabel, 2, 0, 1, 1, Qt.AlignRight)

        self.costBasisLabel = QLabel(self.addStockFrame)
        self.costBasisLabel.setObjectName(u"costBasisLabel")

        self.gridLayout.addWidget(self.costBasisLabel, 3, 0, 1, 1, Qt.AlignRight)

        self.priceLineEdit = QLineEdit(self.addStockFrame)
        self.priceLineEdit.setObjectName(u"priceLineEdit")

        self.gridLayout.addWidget(self.priceLineEdit, 1, 1, 1, 1)

        self.nameLineEdit = QLineEdit(self.addStockFrame)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.gridLayout.addWidget(self.nameLineEdit, 0, 1, 1, 1)

        self.gainLabel = QLabel(self.addStockFrame)
        self.gainLabel.setObjectName(u"gainLabel")

        self.gridLayout.addWidget(self.gainLabel, 5, 0, 1, 1, Qt.AlignRight)

        self.marketValueLabel = QLabel(self.addStockFrame)
        self.marketValueLabel.setObjectName(u"marketValueLabel")

        self.gridLayout.addWidget(self.marketValueLabel, 4, 0, 1, 1, Qt.AlignRight)

        self.sharesLineEdit = QLineEdit(self.addStockFrame)
        self.sharesLineEdit.setObjectName(u"sharesLineEdit")
        self.sharesLineEdit.setMinimumSize(QSize(20, 0))

        self.gridLayout.addWidget(self.sharesLineEdit, 2, 1, 1, 1)

        self.costBasisLineEdit = QLineEdit(self.addStockFrame)
        self.costBasisLineEdit.setObjectName(u"costBasisLineEdit")

        self.gridLayout.addWidget(self.costBasisLineEdit, 3, 1, 1, 1)

        self.gainLineEdit = QLineEdit(self.addStockFrame)
        self.gainLineEdit.setObjectName(u"gainLineEdit")

        self.gridLayout.addWidget(self.gainLineEdit, 5, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 10)
        self.gridLayout.setRowStretch(1, 10)
        self.gridLayout.setRowStretch(2, 10)
        self.gridLayout.setRowStretch(3, 10)
        self.gridLayout.setRowStretch(4, 10)
        self.gridLayout.setRowStretch(5, 10)
        self.gridLayout.setColumnStretch(0, 30)
        self.gridLayout.setColumnStretch(1, 30)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.buttonFrame = QFrame(self.addStockFrame)
        self.buttonFrame.setObjectName(u"buttonFrame")
        self.buttonFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.buttonFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
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

        self.horizontalLayout.addWidget(self.buttonBox)


        self.verticalLayout_2.addWidget(self.buttonFrame)


        self.verticalLayout.addWidget(self.addStockFrame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.priceLabel.setText(QCoreApplication.translate("Dialog", u"Price", None))
        self.nameLabel.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.sharesLabel.setText(QCoreApplication.translate("Dialog", u"Shares", None))
        self.costBasisLabel.setText(QCoreApplication.translate("Dialog", u"Cost Basis", None))
        self.gainLabel.setText(QCoreApplication.translate("Dialog", u"Gain", None))
        self.marketValueLabel.setText(QCoreApplication.translate("Dialog", u"Market Value", None))
    # retranslateUi

