# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceVwrrmu.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QAbstractButton,
    QAbstractScrollArea,
    QApplication,
    QDialogButtonBox,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLayout,
    QLineEdit,
    QMainWindow,
    QMenu,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStackedWidget,
    QStatusBar,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from mystocks import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1145, 803)
        MainWindow.setStyleSheet(
            "*{\n"
            "  border: none;\n"
            "  background-color: transparent;\n"
            "  background: none;\n"
            "  padding: 0;\n"
            "  margin: 0;\n"
            "  color: #fff;\n"
            "}\n"
            "\n"
            "#MainBodyContainer {\n"
            "   background-color: #2E2E2E;\n"
            "}\n"
            "#LeftMenuContainer {\n"
            "background-color: #2E2E2E;\n"
            "}\n"
            "#LeftMenuSubContainer  QPushButton {\n"
            "	text-align: left;\n"
            "   padding: 5px 10px;\n"
            "	border-top-left-radius: 10px;\n"
            "	border-bottom-left-radius: 10px;\n"
            "}\n"
            "#LeftMenuSubContainer  QPushButton:hover{\n"
            "	background-color: #008B8B;\n"
            "}\n"
            "#menuFrame {\n"
            "  border-bottom: 3px solid #fff;\n"
            "}\n"
            "\n"
            "#setting_frame,#help_frame {\n"
            "border: 1px solid #fff;\n"
            "}\n"
            "\n"
            "#topBarLeftFrame, #topBarRightFrame, #addBtn {\n"
            "padding: 0px;\n"
            "margin: 0px;\n"
            "}\n"
            "\n"
            "#topBarFrame {\n"
            "/*border-bottom: 1px solid #fff;*/\n"
            "background-color:  #008B8B;\n"
            "}\n"
            "\n"
            "\n"
            "#LeftMenuSubContainer  #menuClose:hover{\n"
            "	background-color: red;\n"
            "}\n"
            "\n"
            "#tableWidget::item { padding: 20px }\n"
            "\n"
            "\n"
            "QLineEdit:focus {"
            "\n"
            "            border: 1px solid #008B8B;\n"
            "            border-radius: 5px;\n"
            "            padding: 2px;\n"
            "            outline: none;\n"
            "          \n"
            "        }\n"
            ""
        )
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 1, 0, 0)
        self.LeftMenuContainer = QWidget(self.centralwidget)
        self.LeftMenuContainer.setObjectName("LeftMenuContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LeftMenuContainer.sizePolicy().hasHeightForWidth())
        self.LeftMenuContainer.setSizePolicy(sizePolicy)
        self.LeftMenuContainer.setMaximumSize(QSize(160, 16777215))
        self.horizontalLayout_3 = QHBoxLayout(self.LeftMenuContainer)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuSubContainer = QWidget(self.LeftMenuContainer)
        self.LeftMenuSubContainer.setObjectName("LeftMenuSubContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LeftMenuSubContainer.sizePolicy().hasHeightForWidth())
        self.LeftMenuSubContainer.setSizePolicy(sizePolicy1)
        self.LeftMenuSubContainer.setMaximumSize(QSize(160, 16777215))
        self.LeftMenuSubContainer.setSizeIncrement(QSize(0, 0))
        self.LeftMenuSubContainer.setBaseSize(QSize(0, -1))
        self.verticalLayout_2 = QVBoxLayout(self.LeftMenuSubContainer)
        # ifndef Q_OS_MAC
        self.verticalLayout_2.setSpacing(-1)
        # endif
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 12, 0, 0)
        self.closeFrame = QFrame(self.LeftMenuSubContainer)
        self.closeFrame.setObjectName("closeFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.closeFrame.sizePolicy().hasHeightForWidth())
        self.closeFrame.setSizePolicy(sizePolicy2)
        self.closeFrame.setFrameShape(QFrame.StyledPanel)
        self.closeFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.closeFrame)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.menuClose = QPushButton(self.closeFrame)
        self.menuClose.setObjectName("menuClose")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.menuClose.sizePolicy().hasHeightForWidth())
        self.menuClose.setSizePolicy(sizePolicy3)
        icon = QIcon()
        icon.addFile(":/icons/sample-qt/icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuClose.setIcon(icon)
        self.menuClose.setIconSize(QSize(24, 24))

        self.verticalLayout_13.addWidget(self.menuClose, 0, Qt.AlignLeft)

        self.verticalLayout_2.addWidget(self.closeFrame, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.menuFrame = QFrame(self.LeftMenuSubContainer)
        self.menuFrame.setObjectName("menuFrame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.menuFrame.sizePolicy().hasHeightForWidth())
        self.menuFrame.setSizePolicy(sizePolicy4)
        self.menuFrame.setFrameShape(QFrame.StyledPanel)
        self.menuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.menuFrame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.menuFrame)

        self.portFolioBtnFrame = QFrame(self.LeftMenuSubContainer)
        self.portFolioBtnFrame.setObjectName("portFolioBtnFrame")
        self.portFolioBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.portFolioBtnFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.portFolioBtnFrame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(30, 5, 30, -1)
        self.portfolioBtn = QPushButton(self.portFolioBtnFrame)
        self.portfolioBtn.setObjectName("portfolioBtn")
        icon1 = QIcon()
        icon1.addFile(":/icons/sample-qt/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.portfolioBtn.setIcon(icon1)
        self.portfolioBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.portfolioBtn)

        self.verticalLayout_2.addWidget(self.portFolioBtnFrame, 0, Qt.AlignHCenter)

        self.frame_3 = QFrame(self.LeftMenuSubContainer)
        self.frame_3.setObjectName("frame_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy5)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.LeftMenuSubContainer)
        self.frame_4.setObjectName("frame_4")
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(30, 12, 30, 12)
        self.settingsBtn = QPushButton(self.frame_4)
        self.settingsBtn.setObjectName("settingsBtn")
        icon2 = QIcon()
        icon2.addFile(":/icons/sample-qt/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon2)
        self.settingsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_6.addWidget(self.settingsBtn)

        self.helpBtn = QPushButton(self.frame_4)
        self.helpBtn.setObjectName("helpBtn")
        icon3 = QIcon()
        icon3.addFile(":/icons/sample-qt/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon3)
        self.helpBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_6.addWidget(self.helpBtn)

        self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignHCenter)

        self.horizontalLayout_3.addWidget(self.LeftMenuSubContainer)

        self.horizontalLayout_2.addWidget(self.LeftMenuContainer)

        self.MainBodyContainer = QWidget(self.centralwidget)
        self.MainBodyContainer.setObjectName("MainBodyContainer")
        sizePolicy.setHeightForWidth(self.MainBodyContainer.sizePolicy().hasHeightForWidth())
        self.MainBodyContainer.setSizePolicy(sizePolicy)
        self.MainBodyContainer.setStyleSheet(
            "#tableContainer {\n"
            "background-color: #2E2E2E;\n"
            "border: none;\n"
            "}\n"
            "\n"
            "#tableWidget {\n"
            "background-color: #2E2E2E;\n"
            "border: 1px solid #aaa;\n"
            " border-top-color: #aaa; \n"
            "}\n"
            "\n"
            "QScrollBar:horizontal {\n"
            "    border: 1px solid #aaa;\n"
            "    background: #aaa;\n"
            "    height: 12px;\n"
            "    margin: 0 20px 0 20px;\n"
            "}"
        )
        self.horizontalLayout = QHBoxLayout(self.MainBodyContainer)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tableContainer = QWidget(self.MainBodyContainer)
        self.tableContainer.setObjectName("tableContainer")
        self.tableContainer.setStyleSheet("QTableWidget::item { height: 40px; }")
        self.verticalLayout_7 = QVBoxLayout(self.tableContainer)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.topBarFrame = QFrame(self.tableContainer)
        self.topBarFrame.setObjectName("topBarFrame")
        sizePolicy4.setHeightForWidth(self.topBarFrame.sizePolicy().hasHeightForWidth())
        self.topBarFrame.setSizePolicy(sizePolicy4)
        self.topBarFrame.setMaximumSize(QSize(16777215, 16777215))
        self.topBarFrame.setFrameShape(QFrame.StyledPanel)
        self.topBarFrame.setFrameShadow(QFrame.Raised)
        self.topBarFrame.setLineWidth(1)
        self.topBarFrame.setMidLineWidth(0)
        self.horizontalLayout_4 = QHBoxLayout(self.topBarFrame)
        # ifndef Q_OS_MAC
        self.horizontalLayout_4.setSpacing(-1)
        # endif
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(12, 12, 12, 12)
        self.topBarRightFrame = QFrame(self.topBarFrame)
        self.topBarRightFrame.setObjectName("topBarRightFrame")
        self.topBarRightFrame.setFrameShape(QFrame.StyledPanel)
        self.topBarRightFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.topBarRightFrame)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.menuOpenBtn = QPushButton(self.topBarRightFrame)
        self.menuOpenBtn.setObjectName("menuOpenBtn")
        self.menuOpenBtn.setAutoFillBackground(False)
        icon4 = QIcon()
        icon4.addFile(":/icons/sample-qt/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuOpenBtn.setIcon(icon4)
        self.menuOpenBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.menuOpenBtn)

        self.horizontalLayout_4.addWidget(self.topBarRightFrame, 0, Qt.AlignLeft)

        self.topBarLeftFrame = QFrame(self.topBarFrame)
        self.topBarLeftFrame.setObjectName("topBarLeftFrame")
        self.topBarLeftFrame.setEnabled(True)
        self.topBarLeftFrame.setFrameShape(QFrame.StyledPanel)
        self.topBarLeftFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.topBarLeftFrame)
        self.horizontalLayout_5.setSpacing(25)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.addBtn = QPushButton(self.topBarLeftFrame)
        self.addBtn.setObjectName("addBtn")
        icon5 = QIcon()
        icon5.addFile(":/icons/sample-qt/icons/plus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addBtn.setIcon(icon5)
        self.addBtn.setIconSize(QSize(18, 18))

        self.horizontalLayout_5.addWidget(self.addBtn)

        self.refreshBtn = QPushButton(self.topBarLeftFrame)
        self.refreshBtn.setObjectName("refreshBtn")
        icon6 = QIcon()
        icon6.addFile(":/icons/sample-qt/icons/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshBtn.setIcon(icon6)
        self.refreshBtn.setIconSize(QSize(18, 18))

        self.horizontalLayout_5.addWidget(self.refreshBtn)

        self.horizontalLayout_4.addWidget(self.topBarLeftFrame, 0, Qt.AlignRight)

        self.verticalLayout_7.addWidget(self.topBarFrame)

        self.frame_pages = QFrame(self.tableContainer)
        self.frame_pages.setObjectName("frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 5, 0)
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName("stackedWidget")
        self.portfolio_page = QWidget()
        self.portfolio_page.setObjectName("portfolio_page")
        self.verticalLayout_10 = QVBoxLayout(self.portfolio_page)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.tableFrame = QFrame(self.portfolio_page)
        self.tableFrame.setObjectName("tableFrame")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(1)
        sizePolicy6.setVerticalStretch(1)
        sizePolicy6.setHeightForWidth(self.tableFrame.sizePolicy().hasHeightForWidth())
        self.tableFrame.setSizePolicy(sizePolicy6)
        self.tableFrame.setFrameShape(QFrame.StyledPanel)
        self.tableFrame.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_9 = QVBoxLayout(self.tableFrame)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.tableFrame)
        if self.tableWidget.columnCount() < 6:
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if self.tableWidget.rowCount() < 1:
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(0, 4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(0, 5, __qtablewidgetitem12)
        self.tableWidget.setObjectName("tableWidget")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy7)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setFrameShadow(QFrame.Raised)
        self.tableWidget.setMidLineWidth(1)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setIconSize(QSize(12, 12))
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_9.addWidget(self.tableWidget)

        self.verticalLayout_10.addWidget(self.tableFrame)

        self.stackedWidget.addWidget(self.portfolio_page)
        self.setting_page = QWidget()
        self.setting_page.setObjectName("setting_page")
        sizePolicy7.setHeightForWidth(self.setting_page.sizePolicy().hasHeightForWidth())
        self.setting_page.setSizePolicy(sizePolicy7)
        self.setting_page.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_15 = QVBoxLayout(self.setting_page)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.setting_frame = QFrame(self.setting_page)
        self.setting_frame.setObjectName("setting_frame")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(1)
        sizePolicy8.setVerticalStretch(1)
        sizePolicy8.setHeightForWidth(self.setting_frame.sizePolicy().hasHeightForWidth())
        self.setting_frame.setSizePolicy(sizePolicy8)
        self.setting_frame.setMinimumSize(QSize(0, 0))
        self.setting_frame.setMaximumSize(QSize(16777215, 16777215))
        self.setting_frame.setFrameShape(QFrame.StyledPanel)
        self.setting_frame.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_11 = QVBoxLayout(self.setting_frame)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridFrame = QFrame(self.setting_frame)
        self.gridFrame.setObjectName("gridFrame")
        self.gridFrame.setStyleSheet(
            "QLineEdit { border-radius: 5px; }\n"
            "\n"
            "QPushButton{\n"
            "background-color: #008B8B;\n"
            "border: 1px solid #c9c9c9;\n"
            " border-radius: 3px;\n"
            "padding: 5px;\n"
            " margin-right: 5px;}"
        )
        self.gridFrame.setFrameShape(QFrame.StyledPanel)
        self.gridFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.gridFrame)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label = QLabel(self.gridFrame)
        self.label.setObjectName("label")
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)

        self.verticalLayout_14.addWidget(self.label, 0, Qt.AlignHCenter)

        self.frame = QFrame(self.gridFrame)
        self.frame.setObjectName("frame")
        sizePolicy7.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy7)
        self.frame.setMaximumSize(QSize(1000, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")

        self.verticalLayout_14.addWidget(self.frame, 0, Qt.AlignVCenter)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(10, 20, 10, 10)
        self.sumUpColumnsLineEdit = QLineEdit(self.gridFrame)
        self.sumUpColumnsLineEdit.setObjectName("sumUpColumnsLineEdit")
        self.sumUpColumnsLineEdit.setMaximumSize(QSize(500, 16777215))

        self.gridLayout.addWidget(self.sumUpColumnsLineEdit, 2, 1, 1, 1)

        self.localCurrencyLabel = QLabel(self.gridFrame)
        self.localCurrencyLabel.setObjectName("localCurrencyLabel")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.localCurrencyLabel.setFont(font1)

        self.gridLayout.addWidget(self.localCurrencyLabel, 0, 0, 1, 1, Qt.AlignRight)

        self.columnsToConvertLabel = QLabel(self.gridFrame)
        self.columnsToConvertLabel.setObjectName("columnsToConvertLabel")
        self.columnsToConvertLabel.setFont(font1)

        self.gridLayout.addWidget(self.columnsToConvertLabel, 1, 0, 1, 1, Qt.AlignRight)

        self.localCurrencyLineEdit = QLineEdit(self.gridFrame)
        self.localCurrencyLineEdit.setObjectName("localCurrencyLineEdit")
        sizePolicy2.setHeightForWidth(self.localCurrencyLineEdit.sizePolicy().hasHeightForWidth())
        self.localCurrencyLineEdit.setSizePolicy(sizePolicy2)
        self.localCurrencyLineEdit.setMaximumSize(QSize(500, 18))

        self.gridLayout.addWidget(self.localCurrencyLineEdit, 0, 1, 1, 1)

        self.columnsToConvertLineEdit = QLineEdit(self.gridFrame)
        self.columnsToConvertLineEdit.setObjectName("columnsToConvertLineEdit")
        self.columnsToConvertLineEdit.setMaximumSize(QSize(500, 16777215))

        self.gridLayout.addWidget(self.columnsToConvertLineEdit, 1, 1, 1, 1)

        self.label_2 = QLabel(self.gridFrame)
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1, Qt.AlignRight)

        self.verticalLayout_14.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(self.gridFrame)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setStyleSheet("\n" "\n" "* { button-layout: 1 }")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout_14.addWidget(self.buttonBox, 0, Qt.AlignHCenter)

        self.verticalLayout_14.setStretch(2, 1)
        self.verticalLayout_14.setStretch(3, 1)
        self.verticalLayout_14.setStretch(4, 1)

        self.verticalLayout_11.addWidget(self.gridFrame)

        self.verticalLayout_15.addWidget(self.setting_frame)

        self.stackedWidget.addWidget(self.setting_page)
        self.help_page = QWidget()
        self.help_page.setObjectName("help_page")
        sizePolicy7.setHeightForWidth(self.help_page.sizePolicy().hasHeightForWidth())
        self.help_page.setSizePolicy(sizePolicy7)
        self.verticalLayout = QVBoxLayout(self.help_page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.help_frame = QFrame(self.help_page)
        self.help_frame.setObjectName("help_frame")
        sizePolicy6.setHeightForWidth(self.help_frame.sizePolicy().hasHeightForWidth())
        self.help_frame.setSizePolicy(sizePolicy6)
        self.help_frame.setFrameShape(QFrame.StyledPanel)
        self.help_frame.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_12 = QVBoxLayout(self.help_frame)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.help_frame)
        self.pushButton_2.setObjectName("pushButton_2")

        self.verticalLayout_12.addWidget(self.pushButton_2)

        self.verticalLayout.addWidget(self.help_frame)

        self.stackedWidget.addWidget(self.help_page)

        self.verticalLayout_8.addWidget(self.stackedWidget)

        self.verticalLayout_7.addWidget(self.frame_pages)

        self.horizontalLayout.addWidget(self.tableContainer)

        self.horizontalLayout_2.addWidget(self.MainBodyContainer)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1145, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.menuClose.setText("")
        self.portfolioBtn.setText(QCoreApplication.translate("MainWindow", "Portfolio", None))
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", "Settings", None))
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", "Help", None))
        # if QT_CONFIG(tooltip)
        self.menuOpenBtn.setToolTip(QCoreApplication.translate("MainWindow", "Menus", None))
        # endif // QT_CONFIG(tooltip)
        self.menuOpenBtn.setText("")
        # if QT_CONFIG(tooltip)
        self.addBtn.setToolTip(QCoreApplication.translate("MainWindow", "Add", None))
        # endif // QT_CONFIG(tooltip)
        self.addBtn.setText("")
        # if QT_CONFIG(tooltip)
        self.refreshBtn.setToolTip(QCoreApplication.translate("MainWindow", "Refresh", None))
        # endif // QT_CONFIG(tooltip)
        self.refreshBtn.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", "Name", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", "Price", None))
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", "Shares", None))
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", "Cost Basis", None))
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", "Market Value", None))
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", "Gain", None))
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", "1", None))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", "TESLA", None))
        ___qtablewidgetitem8 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", "124", None))
        ___qtablewidgetitem9 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", "3", None))
        ___qtablewidgetitem10 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", "122334", None))
        ___qtablewidgetitem11 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", "1231324", None))
        ___qtablewidgetitem12 = self.tableWidget.item(0, 5)
        ___qtablewidgetitem12.setText(
            QCoreApplication.translate("MainWindow", "1324erdfsdafdsvfvafdvdfv fd vdf ", None)
        )
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("MainWindow", "Settings", None))
        self.localCurrencyLabel.setText(QCoreApplication.translate("MainWindow", "Local Currency", None))
        self.columnsToConvertLabel.setText(QCoreApplication.translate("MainWindow", "Columns to Convert", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", "SumUp Columns", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", "help push button", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", "File", None))

    # retranslateUi
