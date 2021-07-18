from PyQt5 import QtCore, QtGui, QtWidgets
from ftplib import FTP
import os
import datetime
import tik_tool_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(520, 767)
        MainWindow.setWindowOpacity(0.98)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.fw_line = QtWidgets.QLineEdit(self.centralwidget)
        self.fw_line.setMinimumSize(QtCore.QSize(200, 20))
        self.fw_line.setMaximumSize(QtCore.QSize(275, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fw_line.setFont(font)
        self.fw_line.setStyleSheet("border-radius:10px;\n"
                                    "border: 1px solid rgb(86, 86, 86);")
        self.fw_line.setAlignment(QtCore.Qt.AlignCenter)
        self.fw_line.setObjectName("fw_line")
        self.horizontalLayout_6.addWidget(self.fw_line)
        self.selectfw_button = QtWidgets.QPushButton(self.centralwidget)
        self.selectfw_button.setMinimumSize(QtCore.QSize(120, 0))
        self.selectfw_button.setMaximumSize(QtCore.QSize(5000, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selectfw_button.setFont(font)
        self.selectfw_button.setStyleSheet("QPushButton#selectfw_button::hover{\n"
                                            "background-color: rgb(53, 195, 255);\n"
                                            "border-left: 1.5px solid gray;\n"
                                            "border-bottom: 1.5px solid gray;\n"
                                            "border-top: 1px solid gray;\n"
                                            "border-right: 1px solid gray;}\n"
                                            "QPushButton#selectfw_button::pressed{\n"
                                            "border: 1px solid gray;\n"
                                            "background-color: rgb(57, 136, 255);\n"
                                            "font-size: 12.5px;}\n"
                                            "QPushButton#selectfw_button{\n"
                                            "border-radius: 5px;\n"
                                            "border-left: 1.5px solid gray;\n"
                                            "border-bottom: 1.5px solid gray;\n"
                                            "border-top: 1px solid gray;\n"
                                            "border-right: 1px solid gray;\n"
                                            "background-color: rgb(198, 198, 198,100);}")
        self.selectfw_button.setObjectName("selectfw_button")
        self.horizontalLayout_6.addWidget(self.selectfw_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 19, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(400, 120))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 16777203))
        self.widget.setStyleSheet("background-image: url(:/newPrefix/Users/JackHammer/Downloads/mikrotik_logo/mt.png);\n"
                                    "background-repeat: no-repeat;")
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 4, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem5, 24, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem6 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem6, 9, 2, 1, 1)
        self.name_line = QtWidgets.QLineEdit(self.centralwidget)
        self.name_line.setMinimumSize(QtCore.QSize(200, 25))
        self.name_line.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.name_line.setFont(font)
        self.name_line.setStyleSheet("border-radius:10px;\n"
                                        "border: 1px solid rgb(86, 86, 86);")
        self.name_line.setAlignment(QtCore.Qt.AlignCenter)
        self.name_line.setObjectName("name_line")
        self.gridLayout.addWidget(self.name_line, 8, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem7, 11, 2, 1, 1)
        self.account_line = QtWidgets.QLineEdit(self.centralwidget)
        self.account_line.setMinimumSize(QtCore.QSize(200, 25))
        self.account_line.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.account_line.setFont(font)
        self.account_line.setStyleSheet("border-radius:10px;\n"
                                        "border: 1px solid rgb(86, 86, 86);")
        self.account_line.setInputMethodHints(QtCore.Qt.ImhNone)
        self.account_line.setInputMask("")
        self.account_line.setAlignment(QtCore.Qt.AlignCenter)
        self.account_line.setObjectName("account_line")
        self.gridLayout.addWidget(self.account_line, 6, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 6, 3, 1, 1)
        self.package_select = QtWidgets.QComboBox(self.centralwidget)
        self.package_select.setMinimumSize(QtCore.QSize(200, 27))
        self.package_select.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.package_select.setFont(font)
        self.package_select.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.package_select.setStyleSheet("QComboBox\n"
                                            "{border-top-left-radius:10px;\n"
                                            "border-bottom-left-radius:10px;\n"
                                            "border: 1px solid rgb(86, 86, 86);}")
        self.package_select.setCurrentText("")
        self.package_select.setObjectName("package_select")
        self.package_select.addItem("")
        self.package_select.setItemText(0, "")
        self.package_select.addItem("")
        self.package_select.addItem("")
        self.package_select.addItem("")
        self.package_select.addItem("")
        self.package_select.addItem("")
        self.package_select.addItem("")
        self.package_select.addItem("")
        self.gridLayout.addWidget(self.package_select, 10, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 10, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 8, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem9, 7, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)
        self.ssid_line = QtWidgets.QLineEdit(self.centralwidget)
        self.ssid_line.setMinimumSize(QtCore.QSize(200, 25))
        self.ssid_line.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ssid_line.setFont(font)
        self.ssid_line.setStyleSheet("border-radius:10px;\n"
                                        "border: 1px solid rgb(86, 86, 86);\n"
                                        "")
        self.ssid_line.setAlignment(QtCore.Qt.AlignCenter)
        self.ssid_line.setObjectName("ssid_line")
        self.gridLayout.addWidget(self.ssid_line, 2, 2, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem10, 5, 2, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 6, 0, 1, 1)
        self.password_line = QtWidgets.QLineEdit(self.centralwidget)
        self.password_line.setMinimumSize(QtCore.QSize(200, 25))
        self.password_line.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.password_line.setFont(font)
        self.password_line.setStyleSheet("border-radius:10px;\n"
                                            "border: 1px solid rgb(86, 86, 86);")
        self.password_line.setAlignment(QtCore.Qt.AlignCenter)
        self.password_line.setObjectName("password_line")
        self.gridLayout.addWidget(self.password_line, 4, 2, 1, 1)
        self.device_select = QtWidgets.QComboBox(self.centralwidget)
        self.device_select.setMinimumSize(QtCore.QSize(200, 27))
        self.device_select.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.device_select.setFont(font)
        self.device_select.setStyleSheet("QComboBox\n"
                                            "{border-top-left-radius:10px;\n"
                                            "border-bottom-left-radius:10px;\n"
                                            "border: 1px solid rgb(86, 86, 86);}")
        self.device_select.setObjectName("device_select")
        self.device_select.addItem("")
        self.device_select.setItemText(0, "")
        self.device_select.addItem("")
        self.device_select.addItem("")
        self.device_select.addItem("")
        self.gridLayout.addWidget(self.device_select, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem12, 3, 2, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem13, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 4, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.configb_button = QtWidgets.QPushButton(self.centralwidget)
        self.configb_button.setMinimumSize(QtCore.QSize(66, 30))
        self.configb_button.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.configb_button.setFont(font)
        self.configb_button.setStyleSheet("QPushButton#configb_button::hover{\n"
                                            "background-color: rgb(254, 255, 144);\n"
                                            "border-left: 1.5px solid gray;\n"
                                            "border-bottom: 1.5px solid gray;\n"
                                            "border-top: 1px solid gray;\n"
                                            "border-right: 1px solid gray;}\n"
                                            "QPushButton#configb_button::pressed{\n"
                                            "border: 1px solid gray;\n"
                                            "background-color: rgb(255, 251, 106);\n"
                                            "font-size: 12.5px;}\n"
                                            "QPushButton#configb_button{\n"
                                            "border-radius: 10px;\n"
                                            "border-left: 1.5px solid gray;\n"
                                            "border-bottom: 1.5px solid gray;\n"
                                            "border-top: 1px solid gray;\n"
                                            "border-right: 1px solid gray;\n"
                                            "background-color: rgb(198, 198, 198,100);}")
        self.configb_button.setObjectName("configb_button")
        self.horizontalLayout_2.addWidget(self.configb_button)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 8, 1, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.fw_button = QtWidgets.QPushButton(self.centralwidget)
        self.fw_button.setMinimumSize(QtCore.QSize(66, 30))
        self.fw_button.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fw_button.setFont(font)
        self.fw_button.setStyleSheet("QPushButton#fw_button::hover{\n"
                                        "background-color: rgb(53, 195, 255);\n"
                                        "border-left: 1.5px solid gray;\n"
                                        "border-bottom: 1.5px solid gray;\n"
                                        "border-top: 1px solid gray;\n"
                                        "border-right: 1px solid gray;}\n"
                                        "QPushButton#fw_button::pressed{\n"
                                        "border: 1px solid gray;\n"
                                        "background-color: rgb(57, 136, 255);\n"
                                        "font-size: 12.5px;}\n"
                                        "QPushButton#fw_button{\n"
                                        "border-radius: 10px;\n"
                                        "border-left: 1.5px solid gray;\n"
                                        "border-bottom: 1.5px solid gray;\n"
                                        "border-top: 1px solid gray;\n"
                                        "border-right: 1px solid gray;\n"
                                        "background-color: rgb(198, 198, 198,100);}")
        self.fw_button.setObjectName("fw_button")
        self.horizontalLayout_7.addWidget(self.fw_button)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 21, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem14, 28, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 23, 1, 1, 1)
        self.msg_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.msg_label.setFont(font)
        self.msg_label.setStyleSheet("color:green")
        self.msg_label.setAlignment(QtCore.Qt.AlignCenter)
        self.msg_label.setObjectName("msg_label")
        self.gridLayout_2.addWidget(self.msg_label, 1, 1, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 16, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 2, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem15, 17, 1, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem16, 4, 0, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem17, 7, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.configr_button = QtWidgets.QPushButton(self.centralwidget)
        self.configr_button.setMinimumSize(QtCore.QSize(66, 30))
        self.configr_button.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.configr_button.setFont(font)
        self.configr_button.setStyleSheet("QPushButton#configr_button::hover{\n"
                                            "background-color: rgb(113, 255, 111);\n"
                                            "border-left: 1.5px solid gray;\n"
                                            "border-bottom: 1.5px solid gray;\n"
                                            "border-top: 1px solid gray;\n"
                                            "border-right: 1px solid gray;}\n"
                                            "QPushButton#configr_button::pressed{\n"
                                            "border: 1px solid gray;\n"
                                            "background-color: rgb(5, 206, 2);\n"
                                            "font-size: 12.5px;}\n"
                                            "QPushButton#configr_button{\n"
                                            "border-radius: 10px;\n"
                                            "border-left: 1.5px solid gray;\n"
                                            "border-bottom: 1.5px solid gray;\n"
                                            "border-top: 1px solid gray;\n"
                                            "border-right: 1px solid gray;\n"
                                            "background-color: rgb(198, 198, 198,100);}")
        self.configr_button.setObjectName("configr_button")
        self.horizontalLayout_4.addWidget(self.configr_button)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 6, 1, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem18, 9, 1, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem19, 22, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.reset_button = QtWidgets.QPushButton(self.centralwidget)
        self.reset_button.setMinimumSize(QtCore.QSize(66, 30))
        self.reset_button.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.reset_button.setFont(font)
        self.reset_button.setStyleSheet("QPushButton#reset_button::hover{\n"
                                        "background-color: rgb(255, 134, 134);\n"
                                        "border-left: 1.5px solid gray;\n"
                                        "border-bottom: 1.5px solid gray;\n"
                                        "border-top: 1px solid gray;\n"
                                        "border-right: 1px solid gray;}\n"
                                        "QPushButton#reset_button::pressed{\n"
                                        "border: 1px solid gray;\n"
                                        "background-color: rgb(255, 85, 85);\n"
                                        "font-size: 12.5px;}\n"
                                        "QPushButton#reset_button{\n"
                                        "border-radius: 10px;\n"
                                        "border-left: 1.5px solid gray;\n"
                                        "border-bottom: 1.5px solid gray;\n"
                                        "border-top: 1px solid gray;\n"
                                        "border-right: 1px solid gray;\n"
                                        "background-color: rgb(198, 198, 198,100);}")
        self.reset_button.setObjectName("reset_button")
        self.horizontalLayout_5.addWidget(self.reset_button)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 25, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.device_select, self.ssid_line)
        MainWindow.setTabOrder(self.ssid_line, self.password_line)
        MainWindow.setTabOrder(self.password_line, self.account_line)
        MainWindow.setTabOrder(self.account_line, self.name_line)
        MainWindow.setTabOrder(self.name_line, self.package_select)
        MainWindow.setTabOrder(self.package_select, self.configr_button)
        MainWindow.setTabOrder(self.configr_button, self.configb_button)
        MainWindow.setTabOrder(self.configb_button, self.fw_line)
        MainWindow.setTabOrder(self.fw_line, self.selectfw_button)
        MainWindow.setTabOrder(self.selectfw_button, self.fw_button)
        MainWindow.setTabOrder(self.fw_button, self.reset_button)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tik-Tool"))
        self.selectfw_button.setText(_translate("MainWindow", "Select Firmware"))
        self.package_select.setItemText(1, _translate("MainWindow", "RES25"))
        self.package_select.setItemText(2, _translate("MainWindow", "RES100"))
        self.package_select.setItemText(3, _translate("MainWindow", "BUS25"))
        self.package_select.setItemText(4, _translate("MainWindow", "BUS100"))
        self.package_select.setItemText(5, _translate("MainWindow", "TOWERHOST"))
        self.package_select.setItemText(6, _translate("MainWindow", "EMPLOYEE"))
        self.package_select.setItemText(7, _translate("MainWindow", "FREE"))
        self.label_2.setText(_translate("MainWindow", "Wireless Password"))
        self.label_5.setText(_translate("MainWindow", "Package"))
        self.label_4.setText(_translate("MainWindow", "Customer Name"))
        self.label_6.setText(_translate("MainWindow", "Select Device"))
        self.device_select.setItemText(1, _translate("MainWindow", "HAP ac3"))
        self.device_select.setItemText(2, _translate("MainWindow", "RB2011"))
        self.device_select.setItemText(3, _translate("MainWindow", "RB4011"))
        self.label.setText(_translate("MainWindow", "SSID"))
        self.label_3.setText(_translate("MainWindow", "Account Number"))
        self.configb_button.setText(_translate("MainWindow", "Configure Bridge Mode"))
        self.fw_button.setText(_translate("MainWindow", "Update Firmware"))
        self.msg_label.setText(_translate("MainWindow", "Message"))
        self.configr_button.setText(_translate("MainWindow", "Configure Router Mode"))
        self.reset_button.setText(_translate("MainWindow", "Factory Reset Router"))


### Custom Actions and Settings ###
        self.timer = QtCore.QTimer()
        self.account_line.setValidator(QtGui.QIntValidator(0,999999999))
        ssidChars = QtCore.QRegExp("[a-zA-Z0-9\!\@\#\%\^\&\*\_\-\+\s]{0,30}")
        ssidValidator = QtGui.QRegExpValidator(ssidChars, self.ssid_line)
        self.ssid_line.setValidator(ssidValidator)
        passChars = QtCore.QRegExp("[a-zA-Z0-9\!\@\#\%\^\&\*\_\-\+]{0,30}")
        passValidator = QtGui.QRegExpValidator(passChars, self.password_line)
        self.password_line.setValidator(passValidator)
        nameChars = QtCore.QRegExp("[a-zA-Z\s]{0,30}")
        nameValidator = QtGui.QRegExpValidator(nameChars, self.name_line)
        self.name_line.setValidator(nameValidator)
        self.msg_label.hide()
        self.configr_button.clicked.connect(lambda:self.config_device(self.ssid_line.text(), self.password_line.text(), self.account_line.text(), self.name_line.text().upper().replace(" ","_"), self.package_select.currentText()))
        self.configb_button.clicked.connect(lambda:self.config_bridg(self.account_line.text(), self.name_line.text().upper().replace(" ","_"), self.package_select.currentText()))
        self.reset_button.clicked.connect(lambda:self.reset_router())
        self.selectfw_button.clicked.connect(lambda:self.select_file())
        self.fw_button.clicked.connect(lambda:self.upgrade_fw())
        self.timer.timeout.connect(self.hide_msg)
        self.device_select.currentTextChanged.connect(lambda:self.device_select.setStyleSheet("border-top-left-radius:10px;\nborder-bottom-left-radius:10px;\nborder: 1px solid rgb(86, 86, 86);"))
        self.ssid_line.textChanged.connect(lambda:self.ssid_line.setStyleSheet("border-radius:10px;\nborder: 1px solid rgb(86, 86, 86);"))
        self.password_line.textChanged.connect(lambda:self.password_line.setStyleSheet("border-radius:10px;\nborder: 1px solid rgb(86, 86, 86);"))
        self.account_line.textChanged.connect(lambda:self.account_line.setStyleSheet("border-radius:10px;\nborder: 1px solid rgb(86, 86, 86);"))
        self.name_line.textChanged.connect(lambda:self.name_line.setStyleSheet("border-radius:10px;\nborder: 1px solid rgb(86, 86, 86);"))
        self.package_select.currentTextChanged.connect(lambda:self.package_select.setStyleSheet("border-top-left-radius:10px;\nborder-bottom-left-radius:10px;\nborder: 1px solid rgb(86, 86, 86);"))
        self.fw_line.textChanged.connect(lambda:self.fw_line.setStyleSheet("border-radius:10px;\nborder: 1px solid rgb(86, 86, 86);"))
        self.device_select.setEditable(True)
        device_LEdit = self.device_select.lineEdit()
        device_LEdit.setAlignment(QtCore.Qt.AlignCenter)
        device_LEdit.setStyleSheet("border-radius:10px;\n"
                                    "border: 1px solid rgb(255,255,255,0);\n"
                                    "background-color: rgb(255,255,255,0)")
        device_LEdit.setReadOnly(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(65)
        device_LEdit.setFont(font)
        
        self.package_select.setEditable(True)
        device_PEdit = self.package_select.lineEdit()
        device_PEdit.setAlignment(QtCore.Qt.AlignCenter)
        device_PEdit.setStyleSheet("border-radius:10px;\n"
                                    "border: 1px solid rgb(255,255,255,0);\n"
                                    "background-color: rgb(255,255,255,0)")
        device_PEdit.setReadOnly(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(65)
        device_PEdit.setFont(font)
        self.device_password = 'YOUR_PASSWORD'
        self.romon_secret = 'YOURSECRET'

    
    def hide_msg(self):
        self.msg_label.hide()
        self.confirm_reset = 0
        self.timer.stop()
        
    def show_msg(self, color, msg):
        self.msg_label.setText(msg)
        self.msg_label.setStyleSheet(f"color:{color}")
        self.msg_label.show()
        self.timer.start(5000)
        
    def reset_style(self):
        self.msg_label.hide()
        self.ssid_line.setStyleSheet("border-radius:10px;\nborder: 1px solid rgb(86, 86, 86);")
        self.password_line.setStyleSheet("border-radius:10px;\nborder: 1px solid rgb(86, 86, 86);")
        self.account_line.setStyleSheet("border-radius:10px;\nborder: 1px solid rgb(86, 86, 86);")
        self.name_line.setStyleSheet("border-radius:10px;\nborder: 1px solid rgb(86, 86, 86);")
        self.device_select.setStyleSheet("border-top-left-radius:10px;\nborder-bottom-left-radius:10px;\nborder: 1px solid rgb(86, 86, 86);")
        self.package_select.setStyleSheet("border-top-left-radius:10px;\nborder-bottom-left-radius:10px;\nborder: 1px solid rgb(86, 86, 86);")
        self.fw_line.setStyleSheet("border-radius:10px;\nborder: 1px solid rgb(86, 86, 86);")
        
    def highlight_fields(self, *args):
        if self.ssid_line in args and self.ssid_line.text() == '':
            self.ssid_line.setStyleSheet("border-radius:10px;\nborder: 2px solid rgb(255, 0, 0, 175);")
        if self.password_line in args and self.password_line.text() == '':
            self.password_line.setStyleSheet("border-radius:10px;\nborder: 2px solid rgb(255, 0, 0, 175);")
        if self.account_line in args and self.account_line.text() == '':
            self.account_line.setStyleSheet("border-radius:10px;\nborder: 2px solid rgb(255, 0, 0, 175);")
        if self.name_line in args and self.name_line.text() == '':
            self.name_line.setStyleSheet("border-radius:10px;\nborder: 2px solid rgb(255, 0, 0, 175);")
        if self.device_select in args and self.device_select.currentText() == '':
            self.device_select.setStyleSheet("border-top-left-radius:10px;\nborder-bottom-left-radius:10px;\nborder: 2px solid rgb(255, 0, 0, 175);")
        if self.package_select in args and self.package_select.currentText() == '':
            self.package_select.setStyleSheet("border-top-left-radius:10px;\nborder-bottom-left-radius:10px;\nborder: 2px solid rgb(255, 0, 0, 175);")
        if self.fw_line in args and self.fw_line.text() == '':
            self.fw_line.setStyleSheet("border-radius:10px;\nborder: 2px solid rgb(255, 0, 0, 175);")
        
    def send_config(self, timestamp, path, version, password):
        if not os.path.exists('C:\\Tik_Configs\\'):
            os.makedirs('C:\\Tik_Configs\\')
        with FTP('192.168.88.1', 'admin', password,timeout=3) as ftp:
            with open(f'{path}', 'rb') as file:
                if version == 1:
                    ftp.storlines(f'STOR {self.name_line.text().upper().replace(" ","_")}_CONFIG_{timestamp}.rsc', file)
                elif version == 2:
                    ftp.storlines(f'STOR {self.name_line.text().upper().replace(" ","_")}_CONFIG_{timestamp}.auto.rsc', file)
                elif version == 3:
                    ftp.storlines(f'STOR RESET_{timestamp}.auto.rsc', file)
                elif version == 4:
                    fw_file = path.split("/")
                    fw_file = fw_file[-1]
                    ftp.storbinary(f'STOR {fw_file}', file)
                    
    def config_device(self, ssid, wireless_pass, account_num, name, package):
        self.confirm_reset = 0
        timestamp = datetime.datetime.now().strftime("%b-%d-%Y_%H:%M:%S")
        self.reset_style()
        
        self.highlight_fields(self.ssid_line, self.password_line, self.account_line, self.name_line, self.device_select, self.package_select)   

        if ssid != '' and wireless_pass != '' and len(wireless_pass) >= 8 and account_num != '' and name != '' and self.device_select.currentText() != '' and self.package_select.currentText() != '':
            try:
                if self.device_select.currentText() == 'RB2011':
                    config = f"""
                    # {timestamp}
                    # model = RB2011UiAS-2HnD
                    /interface bridge
                    add name=bridge1
                    /interface wireless
                    set [ find default-name=wlan1 ] disabled=no mode=ap-bridge ssid="{ssid}" \\
                        wireless-protocol=802.11
                    /interface list
                    add name=WAN
                    add name=LAN
                    /interface wireless security-profiles
                    set [ find default=yes ] authentication-types=wpa-psk,wpa2-psk mode=\\
                        dynamic-keys supplicant-identity=MikroTik wpa-pre-shared-key=\\
                        {wireless_pass} wpa2-pre-shared-key={wireless_pass}
                    /ip pool
                    add name=dhcp ranges=192.168.88.3-192.168.88.254
                    /ip dhcp-server
                    add address-pool=dhcp disabled=no interface=bridge1 name=dhcp1
                    /interface bridge port
                    add bridge=bridge1 interface=ether2
                    add bridge=bridge1 interface=ether3
                    add bridge=bridge1 interface=ether4
                    add bridge=bridge1 interface=ether5
                    add bridge=bridge1 interface=ether6
                    add bridge=bridge1 interface=ether7
                    add bridge=bridge1 interface=ether8
                    add bridge=bridge1 interface=ether9
                    add bridge=bridge1 interface=ether10
                    add bridge=bridge1 interface=sfp1
                    add bridge=bridge1 interface=wlan1
                    /interface list member
                    add interface=ether1 list=WAN
                    add interface=bridge1 list=LAN
                    /ip address
                    add address=192.168.88.1/24 interface=ether2 network=192.168.88.0
                    /ip dhcp-client
                    add disabled=no interface=ether1
                    /ip dhcp-server network
                    add address=192.168.88.0/24 gateway=192.168.88.1 netmask=24
                    /ip firewall nat
                    add action=masquerade chain=srcnat out-interface-list=WAN
                    /system identity
                    set name="{account_num} | {name.upper()} | {package} | R"
                    /tool romon
                    set enabled=yes secrets={self.romon_secret}
                    /user set [ find where name="admin" ] password="{self.device_password}"
                    """
                if self.device_select.currentText() == 'RB4011':
                    config = """"""
                    
                if self.device_select.currentText() == 'HAP ac3':
                    config = """"""
                    
                    
                if config != "":   
                    config_folder = f'C:\\Tik_Configs\\{name}'
                    if not os.path.exists(config_folder):
                        os.makedirs(config_folder)
                    

                    f = open(f"{config_folder}\\{timestamp.replace(':','')}.rsc", "w")
                    f.write(config)
                    f.close()
                        

                    path = f"{config_folder}\\{timestamp.replace(':','')}.rsc"
                    auto_rsc = f"system reset-configuration no-defaults=yes run-after-reset={name}_CONFIG_{timestamp}.rsc"

                    f2 = open(f"{config_folder}\\{timestamp.replace(':','')}.auto.rsc", "w")
                    f2.write(auto_rsc)
                    f2.close()

                    path2 = f"{config_folder}\\{timestamp.replace(':','')}.auto.rsc"

                    self.show_msg('green', "Device is being configured")
                    try:
                        self.send_config(timestamp=timestamp, path=path, version=1, password='')
                        self.send_config(timestamp=timestamp, path = path2, version=2, password='')
                    except:
                        self.send_config(timestamp=timestamp, path=path, version=1, password=self.device_password)
                        self.send_config(timestamp=timestamp, path = path2, version=2, password=self.device_password)
                else:
                    self.show_msg('red',f"Configuring a {self.device_select.currentText()} is not available at this time")
            except:
                self.show_msg('red', "Could not connect to the device")
        else:
            if len(wireless_pass) < 8 and wireless_pass !="":
                self.password_line.setStyleSheet("border-radius:10px;\nborder: 1px solid rgb(86, 86, 86);\nbackground-color: rgb(255, 0, 0, 50);")
                self.show_msg('red', "Password must be at least 8 characters long")
            else:
                self.show_msg('red', "Please fill out all highlighted fields")
            
    def config_bridg(self, account_num, name, package):
        try:
            self.confirm_reset = 0
            timestamp = datetime.datetime.now().strftime("%b-%d-%Y_%H:%M:%S")
            self.reset_style()
            self.highlight_fields(self.account_line, self.name_line, self.device_select, self.package_select)
            
            if account_num != '' and name != '' and self.device_select.currentText() != '' and package != '':
                if self.device_select.currentText() == 'RB2011':
                        config = f"""
                                    # {timestamp}
                                    # model = RB2011UiAS-2HnD
                                    /interface bridge
                                    add name=bridge1
                                    /interface wireless
                                    set [ find default-name=wlan1 ] disabled=yes mode=ap-bridge ssid=CUSTOMER_SSID \\
                                        wireless-protocol=802.11
                                    /interface list
                                    add name=WAN
                                    add name=LAN
                                    /interface wireless security-profiles
                                    set [ find default=yes ] authentication-types=wpa-psk,wpa2-psk mode=\\
                                        dynamic-keys supplicant-identity=MikroTik wpa-pre-shared-key=\\
                                        WIFI_PASSWORD wpa2-pre-shared-key=WIFI_PASSWORD
                                    /interface bridge port
                                    add bridge=bridge1 interface=ether1
                                    add bridge=bridge1 interface=ether2
                                    add bridge=bridge1 interface=ether3
                                    add bridge=bridge1 interface=ether4
                                    add bridge=bridge1 interface=ether5
                                    add bridge=bridge1 interface=ether6
                                    add bridge=bridge1 interface=ether7
                                    add bridge=bridge1 interface=ether8
                                    add bridge=bridge1 interface=ether9
                                    add bridge=bridge1 interface=ether10
                                    add bridge=bridge1 interface=sfp1
                                    add bridge=bridge1 interface=wlan1
                                    /interface list member
                                    add interface=bridge1 list=LAN
                                    /ip address
                                    add address=192.168.88.1/24 interface=bridge1 network=192.168.88.0
                                    /ip dhcp-client
                                    add disabled=no interface=bridge1
                                    /system identity
                                    set name="{account_num} | {name.upper()} | {package} | B"
                                    /tool romon
                                    set enabled=yes secrets={self.romon_secret}
                                    /user set [ find where name="admin" ] password="{self.device_password}"
                                    """
                        
                if self.device_select.currentText() == 'RB4011':
                        config = """"""
                        
                if self.device_select.currentText() == 'HAP ac3':
                    config = """"""

                
                if config != "":   
                    config_folder = f'C:\\Tik_Configs\\{name}'
                    if not os.path.exists(config_folder):
                        os.makedirs(config_folder)
                    

                    f = open(f"{config_folder}\\{timestamp.replace(':','')}.rsc", "w")
                    f.write(config)
                    f.close()
                        

                    path = f"{config_folder}\\{timestamp.replace(':','')}.rsc"
                    auto_rsc = f"system reset-configuration no-defaults=yes run-after-reset={name}_CONFIG_{timestamp}.rsc"

                    f2 = open(f"{config_folder}\\{timestamp.replace(':','')}.auto.rsc", "w")
                    f2.write(auto_rsc)
                    f2.close()

                    path2 = f"{config_folder}\\{timestamp.replace(':','')}.auto.rsc"

                
                    self.show_msg('green', "Device is being configured")
                    try:
                        self.send_config(timestamp=timestamp, path=path, version=1, password='')
                        self.send_config(timestamp=timestamp, path=path2, version=2, password='')
                    except:
                        self.send_config(timestamp=timestamp, path=path, version=1, password=self.device_password)
                        self.send_config(timestamp=timestamp, path=path2, version=2, password=self.device_password)
                else:
                    self.show_msg('red',f"Configuring a {self.device_select.currentText()} is not available at this time")
                
            else:
                self.show_msg('red', "Please fill out all highlighted fields")
        except:
            self.show_msg('red', 'Something went wrong')
        
    confirm_reset = 0
    def reset_router(self):
        self.reset_style()
        
        if self.confirm_reset == 0:
            self.show_msg('red', "Are you sure that you want to factory reset the device? If so, click the reset button again")
            self.confirm_reset = 1
        else:
            timestamp = datetime.datetime.now().strftime("%b-%d-%Y_%H:%M:%S")
            self.show_msg('green', "Factory resetting the device")

            config_folder = f'C:\\Tik_Configs\\temp'
            if not os.path.exists(config_folder):
                os.makedirs(config_folder)

            auto_rsc = f"system reset-configuration"
            path = f"{config_folder}\\{timestamp.replace(':','')}.auto.rsc"
            f = open(f"{config_folder}\\{timestamp.replace(':','')}.auto.rsc", "w")
            f.write(auto_rsc)
            f.close()
            
            try:
                self.send_config(timestamp=timestamp, path = path, version=3, password=self.device_password)
                self.show_msg('green','Resetting device')
            except:
                try:
                    self.send_config(timestamp=timestamp, path = path, version=3, password='')
                    self.show_msg('green','Resetting device')
                except:
                    self.show_msg('red', "Something went wrong")


            self.confirm_reset = 0

    def select_file(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(None,"getOpenFileName","C:\\","All Files (*.npk);;Mikrotik Firmware (*.npk)")
        print(filename)
        self.fw_line.setText(filename[0])

    def upgrade_fw(self):
        self.reset_style()
        if self.fw_line.text() != '':
            self.show_msg('green', "Upgrading device firmware")
            self.ssid_line.setStyleSheet("border-radius:10px;\nborder: 1px solid rgb(86, 86, 86);")
            self.password_line.setStyleSheet("border-radius:10px;\nborder: 1px solid rgb(86, 86, 86);")
            self.account_line.setStyleSheet("border-radius:10px;\nborder: 1px solid rgb(86, 86, 86);")
            self.name_line.setStyleSheet("border-radius:10px;\nborder: 1px solid rgb(86, 86, 86);")
            self.device_select.setStyleSheet("border-top-left-radius:10px;\nborder-bottom-left-radius:10px;\nborder: 1px solid rgb(86, 86, 86);")
            self.package_select.setStyleSheet("border-top-left-radius:10px;\nborder-bottom-left-radius:10px;\nborder: 1px solid rgb(86, 86, 86);")
            try:
                timestamp = datetime.datetime.now().strftime("%b-%d-%Y_%H:%M:%S")
                self.send_config(timestamp=timestamp, path = self.fw_line.text(), version=4, password='')
                config_folder = f'C:\\Tik_Configs\\temp'
                if not os.path.exists(config_folder):
                    os.makedirs(config_folder)
                auto_rsc = f"""system routerboard upgrade
                                system reboot"""
                path = f"{config_folder}\\{timestamp.replace(':','')}.auto.rsc"
                f = open(path, "w")
                f.write(auto_rsc)
                f.close()
                self.show_msg('green','Upgrading device firmware')
                self.send_config(timestamp=timestamp, path = path, version=3, password='')
            except:
                try:
                    timestamp = datetime.datetime.now().strftime("%b-%d-%Y_%H:%M:%S")
                    self.send_config(timestamp=timestamp, path = self.fw_line.text(), version=4, password=self.device_password)
                    config_folder = f'C:\\Tik_Configs\\temp'
                    if not os.path.exists(config_folder):
                        os.makedirs(config_folder)
                    auto_rsc = f"""system routerboard upgrade
                                    system reboot"""
                    path = f"{config_folder}\\{timestamp.replace(':','')}.auto.rsc"
                    f = open(path, "w")
                    f.write(auto_rsc)
                    f.close()
                    self.show_msg('green','Upgrading device firmware')
                    self.send_config(timestamp=timestamp, path = path, version=3, password=self.device_password)
                except:
                    self.show_msg('red', "Something went wrong")
        else:
            self.show_msg('red', "Please select firmware file")
            self.highlight_fields(self.fw_line)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
