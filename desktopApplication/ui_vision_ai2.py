# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface_threading_oneGjpGXB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import psutil_rc
import backgroundlogin_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1705, 860)
        font = QFont()
        font.setFamily(u"Terminus")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"*{border:none}\n"
"QProgressBar{\n"
"	background-color:rgb(20, 30, 43);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"	color: rgb(255, 0, 0)\n"
"}\n"
"QProgressBar::chunk{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 136, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border-radius: 10px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"\n"
"background-color: rgb(39, 43, 54);\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMinimumSize(QSize(0, 70))
        self.header_frame.setMaximumSize(QSize(16777215, 70))
        self.header_frame.setStyleSheet(u"border:none;\n"
"\n"
"background-color: rgb(35, 32, 53)")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header_left_frame = QFrame(self.header_frame)
        self.header_left_frame.setObjectName(u"header_left_frame")
        self.header_left_frame.setFrameShape(QFrame.WinPanel)
        self.header_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_left_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header_left_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"color:rgb(255, 255, 255)")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.open_close_side_bar_btn = QPushButton(self.frame)
        self.open_close_side_bar_btn.setObjectName(u"open_close_side_bar_btn")
        icon = QIcon()
        icon.addFile(u":/icons/icons/feather/align-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_close_side_bar_btn.setIcon(icon)
        self.open_close_side_bar_btn.setIconSize(QSize(32, 32))
        self.open_close_side_bar_btn.setFlat(True)

        self.horizontalLayout_9.addWidget(self.open_close_side_bar_btn, 0, Qt.AlignLeft)


        self.horizontalLayout_4.addWidget(self.frame, 0, Qt.AlignLeft)

        self.app_logo = QLabel(self.header_left_frame)
        self.app_logo.setObjectName(u"app_logo")
        self.app_logo.setMaximumSize(QSize(50, 50))
        self.app_logo.setStyleSheet(u"color:rgb(255, 255, 255)")
        self.app_logo.setPixmap(QPixmap(u"icons/feather/app_logo.svg"))
        self.app_logo.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.app_logo, 0, Qt.AlignRight)

        self.label = QLabel(self.header_left_frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Terminus")
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"border:none;\n"
"color:rgb(255, 255, 255)")
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.header_left_frame)

        self.header_right_frame = QFrame(self.header_frame)
        self.header_right_frame.setObjectName(u"header_right_frame")
        self.header_right_frame.setFrameShape(QFrame.NoFrame)
        self.header_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_right_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.minimizeWindowButton = QPushButton(self.header_right_frame)
        self.minimizeWindowButton.setObjectName(u"minimizeWindowButton")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/cil-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeWindowButton.setIcon(icon1)
        self.minimizeWindowButton.setFlat(True)

        self.horizontalLayout_3.addWidget(self.minimizeWindowButton)

        self.restoreWindowButton = QPushButton(self.header_right_frame)
        self.restoreWindowButton.setObjectName(u"restoreWindowButton")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cil-window-restore.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreWindowButton.setIcon(icon2)
        self.restoreWindowButton.setFlat(True)

        self.horizontalLayout_3.addWidget(self.restoreWindowButton)

        self.closeWindowButton = QPushButton(self.header_right_frame)
        self.closeWindowButton.setObjectName(u"closeWindowButton")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeWindowButton.setIcon(icon3)
        self.closeWindowButton.setFlat(True)

        self.horizontalLayout_3.addWidget(self.closeWindowButton)


        self.horizontalLayout_2.addWidget(self.header_right_frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_frame)

        self.main_body_frame = QFrame(self.centralwidget)
        self.main_body_frame.setObjectName(u"main_body_frame")
        self.main_body_frame.setStyleSheet(u"")
        self.main_body_frame.setFrameShape(QFrame.NoFrame)
        self.main_body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_body_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_menu_frame = QFrame(self.main_body_frame)
        self.side_menu_frame.setObjectName(u"side_menu_frame")
        self.side_menu_frame.setMinimumSize(QSize(50, 0))
        self.side_menu_frame.setMaximumSize(QSize(30, 16777215))
        self.side_menu_frame.setStyleSheet(u"border:none;\n"
"background-color: rgb(35, 32, 53)")
        self.side_menu_frame.setFrameShape(QFrame.WinPanel)
        self.side_menu_frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.side_menu_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 0, 0, 0)
        self.left_side_menu = QFrame(self.side_menu_frame)
        self.left_side_menu.setObjectName(u"left_side_menu")
        self.left_side_menu.setMinimumSize(QSize(60, 0))
        self.left_side_menu.setFrameShape(QFrame.NoFrame)
        self.left_side_menu.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.left_side_menu)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.page_login_button = QPushButton(self.left_side_menu)
        self.page_login_button.setObjectName(u"page_login_button")
        self.page_login_button.setMaximumSize(QSize(30, 16777215))
        icon4 = QIcon()
        icon4.addFile(u"icons/feather/login-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.page_login_button.setIcon(icon4)
        self.page_login_button.setIconSize(QSize(32, 32))
        self.page_login_button.setFlat(True)

        self.gridLayout.addWidget(self.page_login_button, 6, 0, 1, 1, Qt.AlignLeft)

        self.label_4 = QLabel(self.left_side_menu)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(30, 0))
        self.label_4.setStyleSheet(u"color: rgb(255,255,255);\n"
"margin-left:14")

        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)

        self.label_7 = QLabel(self.left_side_menu)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(255,255,255);\n"
"margin-left:14")

        self.gridLayout.addWidget(self.label_7, 7, 1, 1, 1)

        self.page_profile_button = QPushButton(self.left_side_menu)
        self.page_profile_button.setObjectName(u"page_profile_button")
        self.page_profile_button.setMaximumSize(QSize(30, 16777215))
        icon5 = QIcon()
        icon5.addFile(u"icons/feather/user-profile-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.page_profile_button.setIcon(icon5)
        self.page_profile_button.setIconSize(QSize(32, 32))
        self.page_profile_button.setFlat(True)

        self.gridLayout.addWidget(self.page_profile_button, 5, 0, 1, 1, Qt.AlignLeft)

        self.label_3 = QLabel(self.left_side_menu)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(30, 0))
        self.label_3.setStyleSheet(u"color: rgb(255,255,255);\n"
"margin-left:10")
        self.label_3.setMargin(5)

        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1, Qt.AlignLeft)

        self.label_5 = QLabel(self.left_side_menu)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(255,255,255);\n"
"margin-left:10")
        self.label_5.setMargin(5)

        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1, Qt.AlignLeft)

        self.page_home_button = QPushButton(self.left_side_menu)
        self.page_home_button.setObjectName(u"page_home_button")
        self.page_home_button.setMinimumSize(QSize(30, 0))
        self.page_home_button.setMaximumSize(QSize(30, 16777215))
        icon6 = QIcon()
        icon6.addFile(u"icons/feather/home-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.page_home_button.setIcon(icon6)
        self.page_home_button.setIconSize(QSize(32, 32))
        self.page_home_button.setFlat(True)

        self.gridLayout.addWidget(self.page_home_button, 0, 0, 1, 1)

        self.page_database_button = QPushButton(self.left_side_menu)
        self.page_database_button.setObjectName(u"page_database_button")
        self.page_database_button.setMaximumSize(QSize(30, 16777215))
        icon7 = QIcon()
        icon7.addFile(u"icons/feather/database-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.page_database_button.setIcon(icon7)
        self.page_database_button.setIconSize(QSize(32, 32))
        self.page_database_button.setFlat(True)

        self.gridLayout.addWidget(self.page_database_button, 3, 0, 1, 1, Qt.AlignLeft)

        self.label_41 = QLabel(self.left_side_menu)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"margin-left:10;\n"
"color: rgb(255,255,255)")
        self.label_41.setMargin(4)

        self.gridLayout.addWidget(self.label_41, 6, 1, 1, 1, Qt.AlignLeft)

        self.page_camera_button = QPushButton(self.left_side_menu)
        self.page_camera_button.setObjectName(u"page_camera_button")
        self.page_camera_button.setMinimumSize(QSize(30, 0))
        self.page_camera_button.setMaximumSize(QSize(30, 16777215))
        self.page_camera_button.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u"icons/feather/camera-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.page_camera_button.setIcon(icon8)
        self.page_camera_button.setIconSize(QSize(32, 32))
        self.page_camera_button.setFlat(True)

        self.gridLayout.addWidget(self.page_camera_button, 1, 0, 1, 1)

        self.label_23 = QLabel(self.left_side_menu)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"color: rgb(255,255,255);\n"
"\n"
"margin-left:10")
        self.label_23.setMargin(5)

        self.gridLayout.addWidget(self.label_23, 5, 1, 1, 1, Qt.AlignLeft)

        self.page_settings_button = QPushButton(self.left_side_menu)
        self.page_settings_button.setObjectName(u"page_settings_button")
        self.page_settings_button.setMaximumSize(QSize(30, 16777215))
        icon9 = QIcon()
        icon9.addFile(u"icons/feather/setting-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.page_settings_button.setIcon(icon9)
        self.page_settings_button.setIconSize(QSize(32, 32))
        self.page_settings_button.setFlat(True)

        self.gridLayout.addWidget(self.page_settings_button, 7, 0, 1, 1)

        self.label_20 = QLabel(self.left_side_menu)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"color: rgb(255,255,255);\n"
"margin-left:10")
        self.label_20.setMargin(5)

        self.gridLayout.addWidget(self.label_20, 4, 1, 1, 1, Qt.AlignLeft)

        self.label_13 = QLabel(self.left_side_menu)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"color: rgb(255,255,255);\n"
"margin-left:10")
        self.label_13.setMargin(5)

        self.gridLayout.addWidget(self.label_13, 3, 1, 1, 1)

        self.page_intrusion_det_button = QPushButton(self.left_side_menu)
        self.page_intrusion_det_button.setObjectName(u"page_intrusion_det_button")
        self.page_intrusion_det_button.setMaximumSize(QSize(30, 16777215))
        self.page_intrusion_det_button.setStyleSheet(u"color:rgb(255, 255, 255)")
        icon10 = QIcon()
        icon10.addFile(u"icons/feather/radar-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.page_intrusion_det_button.setIcon(icon10)
        self.page_intrusion_det_button.setIconSize(QSize(32, 32))
        self.page_intrusion_det_button.setFlat(True)

        self.gridLayout.addWidget(self.page_intrusion_det_button, 2, 0, 1, 1, Qt.AlignLeft)

        self.page_pc_stats_button = QPushButton(self.left_side_menu)
        self.page_pc_stats_button.setObjectName(u"page_pc_stats_button")
        self.page_pc_stats_button.setMaximumSize(QSize(30, 16777215))
        icon11 = QIcon()
        icon11.addFile(u"icons/feather/pc-board-graphics-card-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.page_pc_stats_button.setIcon(icon11)
        self.page_pc_stats_button.setIconSize(QSize(32, 32))
        self.page_pc_stats_button.setFlat(True)

        self.gridLayout.addWidget(self.page_pc_stats_button, 4, 0, 1, 1, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.left_side_menu)


        self.horizontalLayout.addWidget(self.side_menu_frame, 0, Qt.AlignLeft)

        self.stackedWidget = QStackedWidget(self.main_body_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font2 = QFont()
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        font2.setStyleStrategy(QFont.NoAntialias)
        self.stackedWidget.setFont(font2)
        self.stackedWidget.setAutoFillBackground(False)
        self.video_database = QWidget()
        self.video_database.setObjectName(u"video_database")
        self.gridLayout_2 = QGridLayout(self.video_database)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_6 = QFrame(self.video_database)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(6)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.groupBox_2 = QGroupBox(self.frame_6)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 0))
        self.groupBox_2.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_2.setStyleSheet(u"color: rgb(255,255,255)")
        self.verticalLayout_21 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lbl_timer = QLabel(self.groupBox_2)
        self.lbl_timer.setObjectName(u"lbl_timer")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lbl_timer)

        self.spnbx_timer = QSpinBox(self.groupBox_2)
        self.spnbx_timer.setObjectName(u"spnbx_timer")
        self.spnbx_timer.setMinimumSize(QSize(50, 0))
        self.spnbx_timer.setMaximumSize(QSize(50, 16777215))
        self.spnbx_timer.setMinimum(1)
        self.spnbx_timer.setMaximum(100000)
        self.spnbx_timer.setValue(20)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.spnbx_timer)


        self.verticalLayout_21.addLayout(self.formLayout_2)


        self.verticalLayout_20.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer)


        self.verticalLayout_18.addLayout(self.verticalLayout_20)


        self.horizontalLayout_17.addLayout(self.verticalLayout_18)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_5)

        self.btn_open_video = QPushButton(self.frame_6)
        self.btn_open_video.setObjectName(u"btn_open_video")
        self.btn_open_video.setAutoFillBackground(False)
        self.btn_open_video.setStyleSheet(u"")
        icon12 = QIcon()
        icon12.addFile(u"icons/video_player/folder-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_open_video.setIcon(icon12)
        self.btn_open_video.setIconSize(QSize(32, 32))

        self.horizontalLayout_15.addWidget(self.btn_open_video)

        self.btn_rewind = QPushButton(self.frame_6)
        self.btn_rewind.setObjectName(u"btn_rewind")
        icon13 = QIcon()
        icon13.addFile(u"icons/video_player/skip-start-circle-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_rewind.setIcon(icon13)
        self.btn_rewind.setIconSize(QSize(32, 32))

        self.horizontalLayout_15.addWidget(self.btn_rewind)

        self.btn_back = QPushButton(self.frame_6)
        self.btn_back.setObjectName(u"btn_back")
        icon14 = QIcon()
        icon14.addFile(u"icons/video_player/fast-backward-arrows-button-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_back.setIcon(icon14)
        self.btn_back.setIconSize(QSize(32, 32))

        self.horizontalLayout_15.addWidget(self.btn_back)

        self.btn_play_pause = QPushButton(self.frame_6)
        self.btn_play_pause.setObjectName(u"btn_play_pause")
        icon15 = QIcon()
        icon15.addFile(u"icons/video_player/play-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_play_pause.setIcon(icon15)
        self.btn_play_pause.setIconSize(QSize(32, 32))

        self.horizontalLayout_15.addWidget(self.btn_play_pause)

        self.btn_forward = QPushButton(self.frame_6)
        self.btn_forward.setObjectName(u"btn_forward")
        icon16 = QIcon()
        icon16.addFile(u"icons/video_player/fast-forward-svgrepo-com (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_forward.setIcon(icon16)
        self.btn_forward.setIconSize(QSize(32, 32))

        self.horizontalLayout_15.addWidget(self.btn_forward)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_6)


        self.verticalLayout_22.addLayout(self.horizontalLayout_15)

        self.hsldr_timeline = QSlider(self.frame_6)
        self.hsldr_timeline.setObjectName(u"hsldr_timeline")
        self.hsldr_timeline.setMaximum(100)
        self.hsldr_timeline.setOrientation(Qt.Horizontal)

        self.verticalLayout_22.addWidget(self.hsldr_timeline)

        self.lbl_frame = QLabel(self.frame_6)
        self.lbl_frame.setObjectName(u"lbl_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_frame.sizePolicy().hasHeightForWidth())
        self.lbl_frame.setSizePolicy(sizePolicy)
        self.lbl_frame.setMinimumSize(QSize(0, 0))
        self.lbl_frame.setMaximumSize(QSize(16777215, 16777215))
        self.lbl_frame.setStyleSheet(u"color: rgb(255,255,255);\n"
"background-color: rgb(225, 225, 225)")
        self.lbl_frame.setFrameShape(QFrame.Box)
        self.lbl_frame.setFrameShadow(QFrame.Raised)
        self.lbl_frame.setLineWidth(2)
        self.lbl_frame.setScaledContents(True)
        self.lbl_frame.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.lbl_frame)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_7)

        self.btn_take_picture = QPushButton(self.frame_6)
        self.btn_take_picture.setObjectName(u"btn_take_picture")
        icon17 = QIcon()
        icon17.addFile(u"icons/video_player/camera-svgrepo-com (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_take_picture.setIcon(icon17)
        self.btn_take_picture.setIconSize(QSize(32, 32))

        self.horizontalLayout_16.addWidget(self.btn_take_picture)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_8)


        self.verticalLayout_22.addLayout(self.horizontalLayout_16)


        self.verticalLayout_19.addLayout(self.verticalLayout_22)


        self.horizontalLayout_17.addLayout(self.verticalLayout_19)


        self.gridLayout_2.addWidget(self.frame_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.video_database)
        self.intrusion_detection = QWidget()
        self.intrusion_detection.setObjectName(u"intrusion_detection")
        self.intrusion_detection.setStyleSheet(u"color: rgb(255,255,255);\n"
"\n"
"")
        self.gridLayout_4 = QGridLayout(self.intrusion_detection)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.start_time_1 = QDateTimeEdit(self.intrusion_detection)
        self.start_time_1.setObjectName(u"start_time_1")
        self.start_time_1.setMinimumSize(QSize(200, 50))
        self.start_time_1.setMaximumSize(QSize(200, 50))

        self.gridLayout_4.addWidget(self.start_time_1, 5, 2, 1, 1, Qt.AlignRight)

        self.label_11 = QLabel(self.intrusion_detection)
        self.label_11.setObjectName(u"label_11")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_11, 3, 3, 1, 1)

        self.system_sytem = QLabel(self.intrusion_detection)
        self.system_sytem.setObjectName(u"system_sytem")
        self.system_sytem.setFont(font3)
        self.system_sytem.setStyleSheet(u"")
        self.system_sytem.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.system_sytem, 3, 0, 1, 1)

        self.end_time_1 = QDateTimeEdit(self.intrusion_detection)
        self.end_time_1.setObjectName(u"end_time_1")
        self.end_time_1.setMinimumSize(QSize(200, 50))
        self.end_time_1.setMaximumSize(QSize(200, 50))

        self.gridLayout_4.addWidget(self.end_time_1, 5, 3, 1, 1, Qt.AlignRight)

        self.surviellance_op_1 = QLabel(self.intrusion_detection)
        self.surviellance_op_1.setObjectName(u"surviellance_op_1")
        self.surviellance_op_1.setMinimumSize(QSize(600, 500))
        self.surviellance_op_1.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setBold(True)
        font4.setWeight(75)
        self.surviellance_op_1.setFont(font4)
        self.surviellance_op_1.setStyleSheet(u"background-color: rgb(225, 225, 225)")
        self.surviellance_op_1.setFrameShape(QFrame.Box)
        self.surviellance_op_1.setFrameShadow(QFrame.Raised)
        self.surviellance_op_1.setLineWidth(3)
        self.surviellance_op_1.setScaledContents(True)

        self.gridLayout_4.addWidget(self.surviellance_op_1, 5, 0, 1, 1)

        self.label_8 = QLabel(self.intrusion_detection)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 50))
        font5 = QFont()
        font5.setFamily(u"Eras Bold ITC")
        font5.setPointSize(15)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setUnderline(False)
        font5.setWeight(75)
        self.label_8.setFont(font5)
        self.label_8.setStyleSheet(u"")
        self.label_8.setFrameShape(QFrame.NoFrame)
        self.label_8.setFrameShadow(QFrame.Plain)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_8, 1, 2, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.human_det_btn_1 = QPushButton(self.intrusion_detection)
        self.human_det_btn_1.setObjectName(u"human_det_btn_1")
        self.human_det_btn_1.setMinimumSize(QSize(200, 30))
        self.human_det_btn_1.setFont(font4)
        self.human_det_btn_1.setStyleSheet(u"background-color:rgb(85, 100, 109);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5;\n"
"\n"
"")

        self.verticalLayout_3.addWidget(self.human_det_btn_1, 0, Qt.AlignRight)

        self.mov_det_btn_1 = QPushButton(self.intrusion_detection)
        self.mov_det_btn_1.setObjectName(u"mov_det_btn_1")
        self.mov_det_btn_1.setMinimumSize(QSize(200, 30))
        self.mov_det_btn_1.setFont(font4)
        self.mov_det_btn_1.setStyleSheet(u"background-color:rgb(85, 100, 109);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5;\n"
"\n"
"")

        self.verticalLayout_3.addWidget(self.mov_det_btn_1, 0, Qt.AlignRight)


        self.gridLayout_4.addLayout(self.verticalLayout_3, 5, 1, 1, 1)

        self.start_detecting_btn_1 = QPushButton(self.intrusion_detection)
        self.start_detecting_btn_1.setObjectName(u"start_detecting_btn_1")
        self.start_detecting_btn_1.setMinimumSize(QSize(200, 30))
        self.start_detecting_btn_1.setMaximumSize(QSize(200, 30))
        self.start_detecting_btn_1.setStyleSheet(u"background-color:rgb(122, 21, 0);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5;\n"
"\n"
"")

        self.gridLayout_4.addWidget(self.start_detecting_btn_1, 5, 4, 1, 1)

        self.label_10 = QLabel(self.intrusion_detection)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_10, 3, 2, 1, 1)

        self.label_9 = QLabel(self.intrusion_detection)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_9.setWordWrap(False)

        self.gridLayout_4.addWidget(self.label_9, 3, 1, 1, 1)

        self.frame_27 = QFrame(self.intrusion_detection)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.pushButton_14 = QPushButton(self.frame_27)
        self.pushButton_14.setObjectName(u"pushButton_14")
        font6 = QFont()
        font6.setFamily(u"Arial Black")
        font6.setPointSize(20)
        font6.setBold(True)
        font6.setWeight(75)
        self.pushButton_14.setFont(font6)
        icon18 = QIcon()
        icon18.addFile(u"icons/feather/cctv-svgrepo-com (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon18)
        self.pushButton_14.setIconSize(QSize(40, 40))

        self.horizontalLayout_22.addWidget(self.pushButton_14, 0, Qt.AlignHCenter)

        self.pushButton_16 = QPushButton(self.frame_27)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setFont(font6)
        self.pushButton_16.setIcon(icon18)
        self.pushButton_16.setIconSize(QSize(40, 40))

        self.horizontalLayout_22.addWidget(self.pushButton_16)

        self.pushButton_17 = QPushButton(self.frame_27)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setFont(font6)
        self.pushButton_17.setIcon(icon18)
        self.pushButton_17.setIconSize(QSize(40, 40))

        self.horizontalLayout_22.addWidget(self.pushButton_17)

        self.pushButton_15 = QPushButton(self.frame_27)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setFont(font6)
        self.pushButton_15.setIcon(icon18)
        self.pushButton_15.setIconSize(QSize(40, 40))

        self.horizontalLayout_22.addWidget(self.pushButton_15, 0, Qt.AlignHCenter)


        self.gridLayout_4.addWidget(self.frame_27, 4, 0, 1, 1)

        self.textBrowser_2 = QTextBrowser(self.intrusion_detection)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setMaximumSize(QSize(600, 50))
        font7 = QFont()
        font7.setPointSize(15)
        font7.setBold(True)
        font7.setWeight(75)
        self.textBrowser_2.setFont(font7)
        self.textBrowser_2.setStyleSheet(u"background-color:rgb(22, 23, 29)")

        self.gridLayout_4.addWidget(self.textBrowser_2, 6, 0, 1, 1)

        self.pushButton_18 = QPushButton(self.intrusion_detection)
        self.pushButton_18.setObjectName(u"pushButton_18")
        icon19 = QIcon()
        icon19.addFile(u"icons/video_player/pause-svgrepo-com (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_18.setIcon(icon19)
        self.pushButton_18.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.pushButton_18, 6, 1, 1, 1)

        self.stackedWidget.addWidget(self.intrusion_detection)
        self.pc_statistics = QWidget()
        self.pc_statistics.setObjectName(u"pc_statistics")
        self.verticalLayout_4 = QVBoxLayout(self.pc_statistics)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_3 = QFrame(self.pc_statistics)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 40))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_36 = QLabel(self.frame_3)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font3)

        self.horizontalLayout_7.addWidget(self.label_36)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.activity_search = QLineEdit(self.frame_4)
        self.activity_search.setObjectName(u"activity_search")
        self.activity_search.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_8.addWidget(self.activity_search, 0, Qt.AlignRight)

        self.pushButton_5 = QPushButton(self.frame_4)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon20 = QIcon()
        icon20.addFile(u":/icons/icons/feather/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon20)
        self.pushButton_5.setIconSize(QSize(16, 16))

        self.horizontalLayout_8.addWidget(self.pushButton_5, 0, Qt.AlignRight)


        self.horizontalLayout_7.addWidget(self.frame_4, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.tableWidget = QTableWidget(self.pc_statistics)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
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
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)
        self.tableWidget.setSizeIncrement(QSize(1, 1))
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(147)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)

        self.verticalLayout_4.addWidget(self.tableWidget)

        self.frame_2 = QFrame(self.pc_statistics)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_6.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_6.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_6.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_6.addWidget(self.pushButton_4)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.pc_statistics)
        self.analytics = QWidget()
        self.analytics.setObjectName(u"analytics")
        self.stackedWidget.addWidget(self.analytics)
        self.profile = QWidget()
        self.profile.setObjectName(u"profile")
        self.profile.setStyleSheet(u"background-image:  url(:/backgound/icons/5172658.jpg);\n"
"color: white;")
        self.welcome = QLabel(self.profile)
        self.welcome.setObjectName(u"welcome")
        self.welcome.setGeometry(QRect(530, 40, 581, 48))
        font8 = QFont()
        font8.setPointSize(30)
        font8.setBold(True)
        font8.setItalic(True)
        font8.setWeight(75)
        self.welcome.setFont(font8)
        self.welcome.setStyleSheet(u"background: none;")
        self.userlabel = QLabel(self.profile)
        self.userlabel.setObjectName(u"userlabel")
        self.userlabel.setGeometry(QRect(30, 170, 871, 61))
        font9 = QFont()
        font9.setPointSize(15)
        font9.setBold(True)
        font9.setItalic(False)
        font9.setWeight(75)
        font9.setStyleStrategy(QFont.NoAntialias)
        self.userlabel.setFont(font9)
        self.userlabel.setAutoFillBackground(False)
        self.userlabel.setStyleSheet(u"color: white;")
        self.userlabel.setScaledContents(False)
        self.emaillabel = QLabel(self.profile)
        self.emaillabel.setObjectName(u"emaillabel")
        self.emaillabel.setGeometry(QRect(30, 250, 871, 61))
        self.emaillabel.setFont(font9)
        self.phonelabel = QLabel(self.profile)
        self.phonelabel.setObjectName(u"phonelabel")
        self.phonelabel.setGeometry(QRect(30, 330, 871, 61))
        font10 = QFont()
        font10.setPointSize(15)
        font10.setBold(True)
        font10.setItalic(False)
        font10.setUnderline(False)
        font10.setWeight(75)
        font10.setStrikeOut(False)
        font10.setKerning(True)
        font10.setStyleStrategy(QFont.NoAntialias)
        self.phonelabel.setFont(font10)
        self.gohome = QPushButton(self.profile)
        self.gohome.setObjectName(u"gohome")
        self.gohome.setGeometry(QRect(480, 610, 201, 61))
        font11 = QFont()
        font11.setPointSize(10)
        font11.setBold(True)
        font11.setItalic(True)
        font11.setWeight(75)
        self.gohome.setFont(font11)
        self.gohome.setStyleSheet(u"QPushButton#gohome{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#gohome:hover{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#gohome:pressed{	\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105, 118, 132, 200);\n"
"}")
        self.logout = QPushButton(self.profile)
        self.logout.setObjectName(u"logout")
        self.logout.setGeometry(QRect(240, 610, 201, 61))
        self.logout.setFont(font11)
        self.logout.setStyleSheet(u"QPushButton#logout{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#logout:hover{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#logout:pressed{	\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105, 118, 132, 200);\n"
"}")
        self.label_12 = QLabel(self.profile)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 10, 141, 131))
        self.label_12.setStyleSheet(u"border-radius: 50px;\n"
"")
        self.label_12.setPixmap(QPixmap(u"icons/feather/user-profile-svgrepo-com.svg"))
        self.label_12.setScaledContents(True)
        self.welcome_2 = QLabel(self.profile)
        self.welcome_2.setObjectName(u"welcome_2")
        self.welcome_2.setGeometry(QRect(1050, 170, 581, 61))
        font12 = QFont()
        font12.setFamily(u"MS Shell Dlg 2")
        font12.setPointSize(14)
        font12.setBold(False)
        font12.setItalic(False)
        font12.setWeight(50)
        self.welcome_2.setFont(font12)
        self.welcome_2.setStyleSheet(u"background: none;\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.clear = QPushButton(self.profile)
        self.clear.setObjectName(u"clear")
        self.clear.setGeometry(QRect(1300, 390, 201, 61))
        self.clear.setFont(font11)
        self.clear.setStyleSheet(u"QPushButton#clear{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#clear:hover{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#clear:pressed{	\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105, 118, 132, 200);\n"
"}")
        self.submit = QPushButton(self.profile)
        self.submit.setObjectName(u"submit")
        self.submit.setGeometry(QRect(1060, 390, 201, 61))
        self.submit.setFont(font11)
        self.submit.setStyleSheet(u"QPushButton#submit{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#submit:hover{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#submit:pressed{	\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105, 118, 132, 200);\n"
"}")
        self.feedback = QLineEdit(self.profile)
        self.feedback.setObjectName(u"feedback")
        self.feedback.setGeometry(QRect(1060, 230, 441, 141))
        self.feedback.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.stackedWidget.addWidget(self.profile)
        self.t2 = QWidget()
        self.t2.setObjectName(u"t2")
        self.stackedWidget.addWidget(self.t2)
        self.all_cameras_page = QWidget()
        self.all_cameras_page.setObjectName(u"all_cameras_page")
        self.gridLayout_9 = QGridLayout(self.all_cameras_page)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.frame_26 = QFrame(self.all_cameras_page)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_26)
        self.gridLayout_7.setSpacing(10)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.all_cam_op3 = QLabel(self.frame_26)
        self.all_cam_op3.setObjectName(u"all_cam_op3")
        self.all_cam_op3.setMinimumSize(QSize(700, 200))
        self.all_cam_op3.setMaximumSize(QSize(700, 600))
        self.all_cam_op3.setStyleSheet(u"background-color:rgb(161, 170, 182)")

        self.gridLayout_7.addWidget(self.all_cam_op3, 1, 0, 1, 1)

        self.all_cam_op1 = QLabel(self.frame_26)
        self.all_cam_op1.setObjectName(u"all_cam_op1")
        self.all_cam_op1.setMinimumSize(QSize(700, 200))
        self.all_cam_op1.setMaximumSize(QSize(700, 600))
        self.all_cam_op1.setStyleSheet(u"background-color:rgb(161, 170, 182)")

        self.gridLayout_7.addWidget(self.all_cam_op1, 0, 0, 1, 1)

        self.all_cam_op4 = QLabel(self.frame_26)
        self.all_cam_op4.setObjectName(u"all_cam_op4")
        self.all_cam_op4.setMinimumSize(QSize(700, 200))
        self.all_cam_op4.setMaximumSize(QSize(700, 16777215))
        self.all_cam_op4.setStyleSheet(u"background-color:rgb(161, 170, 182)")

        self.gridLayout_7.addWidget(self.all_cam_op4, 1, 1, 1, 1)

        self.all_cam_op2 = QLabel(self.frame_26)
        self.all_cam_op2.setObjectName(u"all_cam_op2")
        self.all_cam_op2.setMinimumSize(QSize(700, 200))
        self.all_cam_op2.setMaximumSize(QSize(700, 600))
        self.all_cam_op2.setStyleSheet(u"background-color:rgb(161, 170, 182)")

        self.gridLayout_7.addWidget(self.all_cam_op2, 0, 1, 1, 1)

        self.all_cam_op_start_btn = QPushButton(self.frame_26)
        self.all_cam_op_start_btn.setObjectName(u"all_cam_op_start_btn")
        self.all_cam_op_start_btn.setMinimumSize(QSize(0, 30))
        self.all_cam_op_start_btn.setFont(font4)
        self.all_cam_op_start_btn.setStyleSheet(u"background-color:rgb(85, 100, 109);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5;\n"
"\n"
"")

        self.gridLayout_7.addWidget(self.all_cam_op_start_btn, 2, 0, 1, 1)

        self.all_cam_op1_stop_btn = QPushButton(self.frame_26)
        self.all_cam_op1_stop_btn.setObjectName(u"all_cam_op1_stop_btn")
        self.all_cam_op1_stop_btn.setMinimumSize(QSize(0, 30))
        self.all_cam_op1_stop_btn.setFont(font4)
        self.all_cam_op1_stop_btn.setStyleSheet(u"background-color:rgb(85, 100, 109);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5;\n"
"\n"
"")

        self.gridLayout_7.addWidget(self.all_cam_op1_stop_btn, 2, 1, 1, 1)


        self.gridLayout_9.addWidget(self.frame_26, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.all_cameras_page)
        self.t3 = QWidget()
        self.t3.setObjectName(u"t3")
        self.t3.setMinimumSize(QSize(600, 600))
        self.stackedWidget.addWidget(self.t3)
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.login.setStyleSheet(u"background-image:url(:/backgound/lockkk.jpg);")
        self.label_39 = QLabel(self.login)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(220, 120, 95, 40))
        font13 = QFont()
        font13.setPointSize(25)
        self.label_39.setFont(font13)
        self.label_39.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background:none;")
        self.label_39.setAlignment(Qt.AlignCenter)
        self.label_40 = QLabel(self.login)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(220, 180, 141, 161))
        font14 = QFont()
        font14.setPointSize(70)
        self.label_40.setFont(font14)
        self.label_40.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background:none;")
        self.tb1 = QLineEdit(self.login)
        self.tb1.setObjectName(u"tb1")
        self.tb1.setGeometry(QRect(120, 350, 311, 41))
        font15 = QFont()
        font15.setPointSize(20)
        self.tb1.setFont(font15)
        self.tb1.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;\n"
"background: transparent;")
        self.tb1.setClearButtonEnabled(True)
        self.tb2 = QLineEdit(self.login)
        self.tb2.setObjectName(u"tb2")
        self.tb2.setGeometry(QRect(120, 420, 311, 41))
        self.tb2.setFont(font15)
        self.tb2.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;\n"
"background: transparent;")
        self.tb2.setEchoMode(QLineEdit.Password)
        self.tb2.setClearButtonEnabled(True)
        self.b1 = QPushButton(self.login)
        self.b1.setObjectName(u"b1")
        self.b1.setGeometry(QRect(170, 499, 200, 41))
        self.b1.setFont(font3)
        self.b1.setStyleSheet(u"QPushButton#b1{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:5px;\n"
"	qproperty-icon : url(:/icons/icons/feather/log-out.svg);\n"
"	qproperty-iconSize: 25px 25px;\n"
"	\n"
"}\n"
"QPushButton#b1:hover{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#b1:pressed{	\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105, 118, 132, 200);\n"
"}")
        self.label_42 = QLabel(self.login)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(900, 110, 241, 81))
        self.label_42.setFont(font13)
        self.label_42.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background:none;\n"
"\n"
"")
        self.label_42.setAlignment(Qt.AlignCenter)
        self.label_43 = QLabel(self.login)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(960, 190, 141, 161))
        self.label_43.setFont(font14)
        self.label_43.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background:none;\n"
"")
        self.username = QLineEdit(self.login)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(870, 400, 311, 41))
        self.username.setFont(font15)
        self.username.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;\n"
"")
        self.username.setClearButtonEnabled(True)
        self.password = QLineEdit(self.login)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(870, 470, 311, 41))
        self.password.setFont(font15)
        self.password.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setClearButtonEnabled(True)
        self.email = QLineEdit(self.login)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(870, 550, 311, 41))
        self.email.setFont(font15)
        self.email.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.email.setClearButtonEnabled(True)
        self.phonenumber = QLineEdit(self.login)
        self.phonenumber.setObjectName(u"phonenumber")
        self.phonenumber.setGeometry(QRect(870, 620, 311, 41))
        self.phonenumber.setFont(font15)
        self.phonenumber.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.phonenumber.setClearButtonEnabled(True)
        self.b2 = QPushButton(self.login)
        self.b2.setObjectName(u"b2")
        self.b2.setGeometry(QRect(920, 680, 200, 40))
        self.b2.setFont(font3)
        self.b2.setStyleSheet(u"QPushButton#b2{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	qproperty-icon : url(:/icons/icons/feather/arrow-right-circle.svg);\n"
"	qproperty-iconSize: 25px 25px;\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#b2:hover{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#b2:pressed{	\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105, 118, 132, 200);\n"
"}")
        self.widget = QWidget(self.login)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(60, 350, 51, 31))
        self.widget.setStyleSheet(u"image: url(:/icons/icons/feather/user-plus.svg);\n"
"background: none;")
        self.widget_2 = QWidget(self.login)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(60, 420, 51, 31))
        self.widget_2.setStyleSheet(u"image: url(:/icons/icons/feather/lock.svg);\n"
"background: none;")
        self.widget_3 = QWidget(self.login)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(810, 400, 51, 31))
        self.widget_3.setStyleSheet(u"image: url(:/icons/icons/feather/user-plus.svg);\n"
"background: none;")
        self.widget_4 = QWidget(self.login)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(810, 470, 51, 31))
        self.widget_4.setStyleSheet(u"image: url(:/icons/icons/feather/lock.svg);\n"
"background: none;")
        self.widget_5 = QWidget(self.login)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(810, 620, 51, 31))
        self.widget_5.setStyleSheet(u"image: url(:/icons/icons/feather/phone-outgoing.svg);\n"
"background: none;")
        self.widget_6 = QWidget(self.login)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(810, 550, 51, 31))
        self.widget_6.setStyleSheet(u"image: url(:/icons/icons/feather/at-sign.svg);\n"
"background: none;")
        self.stackedWidget.addWidget(self.login)
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.settings.setStyleSheet(u"color: rgb(255,255,255)")
        self.horizontalLayout_24 = QHBoxLayout(self.settings)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.frame_28 = QFrame(self.settings)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_28)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_29 = QFrame(self.frame_28)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_29)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_15 = QLabel(self.frame_29)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(200, 50))
        font16 = QFont()
        font16.setFamily(u"Arial Black")
        font16.setPointSize(15)
        font16.setBold(True)
        font16.setWeight(75)
        self.label_15.setFont(font16)

        self.verticalLayout_7.addWidget(self.label_15, 0, Qt.AlignLeft)

        self.pushButton_19 = QPushButton(self.frame_29)
        self.pushButton_19.setObjectName(u"pushButton_19")
        font17 = QFont()
        font17.setFamily(u"Calibri")
        font17.setPointSize(16)
        font17.setBold(True)
        font17.setWeight(75)
        self.pushButton_19.setFont(font17)
        icon21 = QIcon()
        icon21.addFile(u":/icons/icons/feather/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_19.setIcon(icon21)
        self.pushButton_19.setIconSize(QSize(30, 30))

        self.verticalLayout_7.addWidget(self.pushButton_19, 0, Qt.AlignLeft)

        self.pushButton_20 = QPushButton(self.frame_29)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setFont(font17)
        self.pushButton_20.setIcon(icon21)
        self.pushButton_20.setIconSize(QSize(30, 30))

        self.verticalLayout_7.addWidget(self.pushButton_20, 0, Qt.AlignLeft)


        self.verticalLayout_5.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.frame_28)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame_30)


        self.horizontalLayout_24.addWidget(self.frame_28)

        self.stackedWidget.addWidget(self.settings)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"color: rgb(255,255,255);\n"
"border:none\n"
"")
        self.verticalLayout_6 = QVBoxLayout(self.home)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_15 = QFrame(self.home)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(200, 50))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_7 = QPushButton(self.frame_15)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(40, 40))
        self.pushButton_7.setMaximumSize(QSize(16777215, 50))
        icon22 = QIcon()
        icon22.addFile(u"icons/feather/notification-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon22)

        self.gridLayout_5.addWidget(self.pushButton_7, 0, 0, 1, 1, Qt.AlignRight)

        self.pushButton_8 = QPushButton(self.frame_15)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 40))
        self.pushButton_8.setMaximumSize(QSize(16777215, 50))
        self.pushButton_8.setIcon(icon5)

        self.gridLayout_5.addWidget(self.pushButton_8, 0, 1, 1, 1, Qt.AlignRight)


        self.horizontalLayout_11.addLayout(self.gridLayout_5)


        self.verticalLayout_8.addWidget(self.frame_15, 0, Qt.AlignRight)

        self.frame_7 = QFrame(self.home)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_7)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_16)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_18)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_16 = QLabel(self.frame_18)
        self.label_16.setObjectName(u"label_16")
        font18 = QFont()
        font18.setPointSize(33)
        self.label_16.setFont(font18)
        self.label_16.setStyleSheet(u"color: rgb(193, 193, 193)")

        self.verticalLayout_15.addWidget(self.label_16)

        self.label_17 = QLabel(self.frame_18)
        self.label_17.setObjectName(u"label_17")
        font19 = QFont()
        font19.setPointSize(10)
        self.label_17.setFont(font19)

        self.verticalLayout_15.addWidget(self.label_17)


        self.verticalLayout_12.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_16)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_19)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.pushButton_9 = QPushButton(self.frame_19)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(100, 30))
        self.pushButton_9.setMaximumSize(QSize(200, 16777215))
        self.pushButton_9.setStyleSheet(u"background-color:rgb(0, 184, 89);\n"
"border-radius: 4")

        self.verticalLayout_16.addWidget(self.pushButton_9, 0, Qt.AlignLeft)


        self.verticalLayout_12.addWidget(self.frame_19)


        self.horizontalLayout_18.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_7)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(600, 16777215))
        self.frame_17.setStyleSheet(u"border-width:5;\n"
"border-color:rgb(255, 255, 255)")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_17)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(600, 330))
        self.label_14.setStyleSheet(u"border-width:5;\n"
"border-color:rgb(255,255,255)")
        self.label_14.setPixmap(QPixmap(u"images/1_JUBCocLshhnSIoS2MynhjA.jpeg"))
        self.label_14.setScaledContents(True)

        self.horizontalLayout_19.addWidget(self.label_14)


        self.horizontalLayout_18.addWidget(self.frame_17)


        self.verticalLayout_8.addWidget(self.frame_7)

        self.frame_14 = QFrame(self.home)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"background-color:rgb(79, 81, 107)")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.frame_20 = QFrame(self.frame_14)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_20)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pushButton_10 = QPushButton(self.frame_20)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(100, 0))
        self.pushButton_10.setFont(font19)
        self.pushButton_10.setStyleSheet(u"background-color: rgb(96, 150, 73);\n"
"border-radius: 4")

        self.gridLayout_6.addWidget(self.pushButton_10, 1, 0, 1, 1, Qt.AlignHCenter)

        self.frame_22 = QFrame(self.frame_20)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(300, 16777215))
        self.frame_22.setStyleSheet(u"background-color:rgb(66, 70, 94)")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_22)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_22)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(200, 200))
        self.label_18.setPixmap(QPixmap(u"icons/feather/cctv-svgrepo-com (2).svg"))
        self.label_18.setScaledContents(True)

        self.verticalLayout_17.addWidget(self.label_18, 0, Qt.AlignHCenter)

        self.label_21 = QLabel(self.frame_22)
        self.label_21.setObjectName(u"label_21")
        font20 = QFont()
        font20.setPointSize(13)
        font20.setBold(True)
        font20.setWeight(75)
        self.label_21.setFont(font20)

        self.verticalLayout_17.addWidget(self.label_21, 0, Qt.AlignHCenter)

        self.label_22 = QLabel(self.frame_22)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font20)

        self.verticalLayout_17.addWidget(self.label_22, 0, Qt.AlignHCenter)


        self.gridLayout_6.addWidget(self.frame_22, 0, 0, 1, 1)

        self.frame_23 = QFrame(self.frame_20)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMaximumSize(QSize(300, 16777215))
        self.frame_23.setStyleSheet(u"background-color:rgb(66, 70, 94)")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_23)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.frame_23)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(200, 200))
        self.label_24.setPixmap(QPixmap(u"icons/feather/cctv-svgrepo-com (2).svg"))
        self.label_24.setScaledContents(True)

        self.verticalLayout_23.addWidget(self.label_24, 0, Qt.AlignHCenter)

        self.label_26 = QLabel(self.frame_23)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font20)

        self.verticalLayout_23.addWidget(self.label_26, 0, Qt.AlignHCenter)

        self.label_27 = QLabel(self.frame_23)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font20)

        self.verticalLayout_23.addWidget(self.label_27, 0, Qt.AlignHCenter)


        self.gridLayout_6.addWidget(self.frame_23, 0, 1, 1, 1)

        self.pushButton_11 = QPushButton(self.frame_20)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(100, 0))
        self.pushButton_11.setFont(font19)
        self.pushButton_11.setStyleSheet(u"background-color: rgb(96, 150, 73);\n"
"border-radius: 4")

        self.gridLayout_6.addWidget(self.pushButton_11, 1, 1, 1, 1, Qt.AlignHCenter)

        self.frame_24 = QFrame(self.frame_20)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(300, 16777215))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_24)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMaximumSize(QSize(300, 16777215))
        self.frame_25.setStyleSheet(u"background-color:rgb(66, 70, 94)")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_25)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.frame_25)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(200, 200))
        self.label_28.setPixmap(QPixmap(u"icons/feather/cctv-svgrepo-com (2).svg"))
        self.label_28.setScaledContents(True)

        self.verticalLayout_24.addWidget(self.label_28, 0, Qt.AlignHCenter)

        self.label_29 = QLabel(self.frame_25)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font20)

        self.verticalLayout_24.addWidget(self.label_29, 0, Qt.AlignHCenter)

        self.label_31 = QLabel(self.frame_25)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font20)

        self.verticalLayout_24.addWidget(self.label_31, 0, Qt.AlignHCenter)


        self.verticalLayout_25.addWidget(self.frame_25)


        self.gridLayout_6.addWidget(self.frame_24, 0, 2, 1, 1)

        self.pushButton_12 = QPushButton(self.frame_20)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(100, 0))
        self.pushButton_12.setFont(font19)
        self.pushButton_12.setStyleSheet(u"background-color: rgb(96, 150, 73);\n"
"border-radius: 4")

        self.gridLayout_6.addWidget(self.pushButton_12, 1, 2, 1, 1, Qt.AlignHCenter)


        self.horizontalLayout_20.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_14)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(600, 16777215))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.calendarWidget = QCalendarWidget(self.frame_21)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setMinimumSize(QSize(500, 280))
        self.calendarWidget.setMaximumSize(QSize(99999, 99999))
        self.calendarWidget.setStyleSheet(u"background-color:rgb(87, 83, 144);\n"
"color: rgb(0, 0, 0)")
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.ISOWeekNumbers)

        self.horizontalLayout_21.addWidget(self.calendarWidget)


        self.horizontalLayout_20.addWidget(self.frame_21)


        self.verticalLayout_8.addWidget(self.frame_14)


        self.verticalLayout_6.addLayout(self.verticalLayout_8)

        self.stackedWidget.addWidget(self.home)
        self.t1 = QWidget()
        self.t1.setObjectName(u"t1")
        self.stackedWidget.addWidget(self.t1)
        self.cameras = QWidget()
        self.cameras.setObjectName(u"cameras")
        self.cameras.setStyleSheet(u"")
        self.gridLayout_8 = QGridLayout(self.cameras)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(20, 20, 20, 20)
        self.frame_5 = QFrame(self.cameras)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 700))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(150, 400))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.cam_button_1 = QPushButton(self.frame_9)
        self.cam_button_1.setObjectName(u"cam_button_1")
        self.cam_button_1.setMinimumSize(QSize(170, 0))
        font21 = QFont()
        font21.setFamily(u"Arial Black")
        font21.setPointSize(10)
        font21.setBold(True)
        font21.setWeight(75)
        self.cam_button_1.setFont(font21)
        self.cam_button_1.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3;\n"
"border-width:2;\n"
"border-color:rgb(0, 0, 0)")
        icon23 = QIcon()
        icon23.addFile(u"icons/feather/cctv-svgrepo-com (2).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cam_button_1.setIcon(icon23)
        self.cam_button_1.setIconSize(QSize(50, 50))

        self.verticalLayout_9.addWidget(self.cam_button_1)

        self.cam_button_2 = QPushButton(self.frame_9)
        self.cam_button_2.setObjectName(u"cam_button_2")
        self.cam_button_2.setMinimumSize(QSize(170, 0))
        self.cam_button_2.setFont(font21)
        self.cam_button_2.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3;\n"
"border-width:2;\n"
"border-color:rgb(0, 0, 0)")
        self.cam_button_2.setIcon(icon23)
        self.cam_button_2.setIconSize(QSize(50, 50))

        self.verticalLayout_9.addWidget(self.cam_button_2)

        self.cam_button_3 = QPushButton(self.frame_9)
        self.cam_button_3.setObjectName(u"cam_button_3")
        self.cam_button_3.setMinimumSize(QSize(170, 0))
        font22 = QFont()
        font22.setFamily(u"Arial Black")
        font22.setPointSize(10)
        font22.setBold(True)
        font22.setUnderline(False)
        font22.setWeight(75)
        self.cam_button_3.setFont(font22)
        self.cam_button_3.setAutoFillBackground(False)
        self.cam_button_3.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3;\n"
"border-width:2;\n"
"border-color:rgb(0, 0, 0)")
        self.cam_button_3.setIcon(icon23)
        self.cam_button_3.setIconSize(QSize(50, 50))

        self.verticalLayout_9.addWidget(self.cam_button_3)

        self.cam_button_4 = QPushButton(self.frame_9)
        self.cam_button_4.setObjectName(u"cam_button_4")
        self.cam_button_4.setMinimumSize(QSize(170, 0))
        self.cam_button_4.setFont(font21)
        self.cam_button_4.setStyleSheet(u"background-color:transparent;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3;\n"
"border-width:2;\n"
"border-color:rgb(0, 0, 0)")
        self.cam_button_4.setIcon(icon23)
        self.cam_button_4.setIconSize(QSize(50, 50))
        self.cam_button_4.setFlat(False)

        self.verticalLayout_9.addWidget(self.cam_button_4)


        self.horizontalLayout_10.addWidget(self.frame_9, 0, Qt.AlignLeft)

        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(700, 0))
        self.frame_10.setLayoutDirection(Qt.LeftToRight)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 500))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.output_screen = QLabel(self.frame_12)
        self.output_screen.setObjectName(u"output_screen")
        self.output_screen.setMinimumSize(QSize(0, 700))
        self.output_screen.setStyleSheet(u"border:4;\n"
"border-color: rgb(0,0,0);\n"
"background-color: rgb(225, 225, 225)")
        self.output_screen.setFrameShape(QFrame.Box)
        self.output_screen.setFrameShadow(QFrame.Raised)
        self.output_screen.setLineWidth(5)
        self.output_screen.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.output_screen)


        self.verticalLayout_10.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_10)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 60))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pushButton_6 = QPushButton(self.frame_13)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(16777215, 30))
        self.pushButton_6.setFont(font4)
        self.pushButton_6.setStyleSheet(u"background-color:rgb(85, 100, 109);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5;\n"
"\n"
"")

        self.horizontalLayout_13.addWidget(self.pushButton_6)

        self.pushButton_13 = QPushButton(self.frame_13)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMaximumSize(QSize(16777215, 30))
        self.pushButton_13.setFont(font4)
        self.pushButton_13.setStyleSheet(u"background-color:rgb(85, 100, 109);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5;\n"
"\n"
"")

        self.horizontalLayout_13.addWidget(self.pushButton_13)

        self.activity_show = QTextBrowser(self.frame_13)
        self.activity_show.setObjectName(u"activity_show")
        self.activity_show.setMaximumSize(QSize(800, 40))

        self.horizontalLayout_13.addWidget(self.activity_show)


        self.verticalLayout_10.addWidget(self.frame_13)


        self.horizontalLayout_10.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_5)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(150, 0))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_11)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_6 = QLabel(self.frame_11)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 0))
        self.label_6.setMaximumSize(QSize(190, 50))
        font23 = QFont()
        font23.setFamily(u"Arial")
        font23.setBold(False)
        font23.setItalic(False)
        font23.setWeight(50)
        self.label_6.setFont(font23)
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setStyleSheet(u"font: 8pt \"Arial\";\n"
"font: 20px \"Arial\";\n"
"background-color: rgb(83, 75, 93);\n"
"border-radius:3;\n"
"border-width:10;\n"
"border-color:rgb(255, 255, 255)\n"
"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_6)

        self.all_filters = QWidget(self.frame_11)
        self.all_filters.setObjectName(u"all_filters")
        self.all_filters.setStyleSheet(u"background-color: rgb(83, 75, 93);\n"
"border-radius:3;\n"
"\n"
"")
        self.verticalLayout_13 = QVBoxLayout(self.all_filters)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_32 = QLabel(self.all_filters)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(30, 30))
        self.label_32.setPixmap(QPixmap(u"icons/feather/cloud-svgrepo-com.svg"))
        self.label_32.setScaledContents(True)

        self.verticalLayout_13.addWidget(self.label_32, 0, Qt.AlignHCenter)

        self.dehazer_low_button = QPushButton(self.all_filters)
        self.dehazer_low_button.setObjectName(u"dehazer_low_button")
        self.dehazer_low_button.setMinimumSize(QSize(0, 30))
        self.dehazer_low_button.setFont(font4)
        self.dehazer_low_button.setStyleSheet(u"background-color:rgb(22, 22, 26);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5;\n"
"\n"
"")

        self.verticalLayout_13.addWidget(self.dehazer_low_button)

        self.label_33 = QLabel(self.all_filters)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(30, 30))
        self.label_33.setPixmap(QPixmap(u"icons/feather/foggy-svgrepo-com.svg"))
        self.label_33.setScaledContents(True)

        self.verticalLayout_13.addWidget(self.label_33, 0, Qt.AlignHCenter)

        self.dehazer_high_button = QPushButton(self.all_filters)
        self.dehazer_high_button.setObjectName(u"dehazer_high_button")
        self.dehazer_high_button.setMinimumSize(QSize(0, 30))
        self.dehazer_high_button.setFont(font4)
        self.dehazer_high_button.setStyleSheet(u"background-color:rgb(22, 22, 26);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5;\n"
"\n"
"")

        self.verticalLayout_13.addWidget(self.dehazer_high_button)

        self.label_34 = QLabel(self.all_filters)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(30, 30))
        self.label_34.setPixmap(QPixmap(u"icons/feather/moon-svgrepo-com.svg"))
        self.label_34.setScaledContents(True)

        self.verticalLayout_13.addWidget(self.label_34, 0, Qt.AlignHCenter)

        self.lle_low_button = QPushButton(self.all_filters)
        self.lle_low_button.setObjectName(u"lle_low_button")
        self.lle_low_button.setMinimumSize(QSize(0, 30))
        self.lle_low_button.setFont(font4)
        self.lle_low_button.setStyleSheet(u"background-color:rgb(22, 22, 26);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5;\n"
"")

        self.verticalLayout_13.addWidget(self.lle_low_button)

        self.label_35 = QLabel(self.all_filters)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(30, 30))
        self.label_35.setPixmap(QPixmap(u"icons/feather/moon-svgrepo-com (1).svg"))
        self.label_35.setScaledContents(True)

        self.verticalLayout_13.addWidget(self.label_35, 0, Qt.AlignHCenter)

        self.lle_high_button = QPushButton(self.all_filters)
        self.lle_high_button.setObjectName(u"lle_high_button")
        self.lle_high_button.setMinimumSize(QSize(0, 30))
        self.lle_high_button.setFont(font4)
        self.lle_high_button.setStyleSheet(u"background-color:rgb(22, 22, 26);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5;\n"
"\n"
"")

        self.verticalLayout_13.addWidget(self.lle_high_button)

        self.label_37 = QLabel(self.all_filters)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(30, 30))
        self.label_37.setPixmap(QPixmap(u"icons/feather/rain-svgrepo-com (1).svg"))
        self.label_37.setScaledContents(True)

        self.verticalLayout_13.addWidget(self.label_37, 0, Qt.AlignHCenter)

        self.derainer_low_button = QPushButton(self.all_filters)
        self.derainer_low_button.setObjectName(u"derainer_low_button")
        self.derainer_low_button.setMinimumSize(QSize(0, 30))
        self.derainer_low_button.setFont(font4)
        self.derainer_low_button.setStyleSheet(u"background-color:rgb(22, 22, 26);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5;\n"
"\n"
"")

        self.verticalLayout_13.addWidget(self.derainer_low_button)


        self.verticalLayout_14.addWidget(self.all_filters)


        self.horizontalLayout_10.addWidget(self.frame_11)


        self.gridLayout_8.addWidget(self.frame_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.cameras)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.nain_body_cont_frame = QFrame(self.main_body_frame)
        self.nain_body_cont_frame.setObjectName(u"nain_body_cont_frame")
        self.nain_body_cont_frame.setMinimumSize(QSize(0, 0))
        self.nain_body_cont_frame.setStyleSheet(u"")
        self.nain_body_cont_frame.setFrameShape(QFrame.NoFrame)
        self.nain_body_cont_frame.setFrameShadow(QFrame.Sunken)
        self.gridLayout_3 = QGridLayout(self.nain_body_cont_frame)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.nain_body_cont_frame, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.main_body_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setMinimumSize(QSize(0, 50))
        self.footer_frame.setMaximumSize(QSize(16777215, 50))
        self.footer_frame.setStyleSheet(u"background-color: rgb(35, 32, 53);\n"
"border:none;")
        self.footer_frame.setFrameShape(QFrame.NoFrame)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.size_grip_l = QFrame(self.footer_frame)
        self.size_grip_l.setObjectName(u"size_grip_l")
        self.size_grip_l.setFrameShape(QFrame.StyledPanel)
        self.size_grip_l.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.size_grip_l)

        self.label_2 = QLabel(self.footer_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255)")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.frame_8 = QFrame(self.footer_frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.time_browser_text = QTextBrowser(self.frame_8)
        self.time_browser_text.setObjectName(u"time_browser_text")
        self.time_browser_text.setMaximumSize(QSize(16777215, 30))
        self.time_browser_text.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.time_browser_text)


        self.horizontalLayout_5.addWidget(self.frame_8)

        self.help_btn = QPushButton(self.footer_frame)
        self.help_btn.setObjectName(u"help_btn")
        self.help_btn.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.help_btn.setFlat(True)

        self.horizontalLayout_5.addWidget(self.help_btn, 0, Qt.AlignRight)

        self.size_grip = QFrame(self.footer_frame)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 16777215))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.size_grip, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(8)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.open_close_side_bar_btn.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.app_logo.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"VISION AI", None))
        self.minimizeWindowButton.setText("")
        self.restoreWindowButton.setText("")
        self.closeWindowButton.setText("")
        self.page_login_button.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.page_profile_button.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Camera Filters", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Smart Intrusion Detection", None))
        self.page_home_button.setText("")
        self.page_database_button.setText("")
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.page_camera_button.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.page_settings_button.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"PC Statistics", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Video Database", None))
        self.page_intrusion_det_button.setText("")
        self.page_pc_stats_button.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Video", None))
        self.lbl_timer.setText(QCoreApplication.translate("MainWindow", u"timer (ms)", None))
        self.btn_open_video.setText("")
        self.btn_rewind.setText("")
        self.btn_back.setText("")
        self.btn_play_pause.setText("")
        self.btn_forward.setText("")
        self.lbl_frame.setText("")
        self.btn_take_picture.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"End-Time", None))
        self.system_sytem.setText(QCoreApplication.translate("MainWindow", u"CAMERA FEED", None))
        self.surviellance_op_1.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Activity Surviellance Detection", None))
        self.human_det_btn_1.setText(QCoreApplication.translate("MainWindow", u"Human Activity", None))
        self.mov_det_btn_1.setText(QCoreApplication.translate("MainWindow", u"Movement", None))
        self.start_detecting_btn_1.setText(QCoreApplication.translate("MainWindow", u"DETECT", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Start-Time", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Activity", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_18.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Activities", None))
        self.activity_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search process name", None))
        self.pushButton_5.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Process ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Process Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Process Status", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Started", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Suspend", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Resume", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Kill", None));
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Suspend", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Resume", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Terminate", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Kill", None))
        self.welcome.setText(QCoreApplication.translate("MainWindow", u"WELCOME, ", None))
        self.userlabel.setText(QCoreApplication.translate("MainWindow", u"Username :                                                                 No USERNAME", None))
        self.emaillabel.setText(QCoreApplication.translate("MainWindow", u"Email :                                                                          No email", None))
        self.phonelabel.setText(QCoreApplication.translate("MainWindow", u"Phone Number :                                                            no phone number", None))
        self.gohome.setText(QCoreApplication.translate("MainWindow", u"GO TO HOME", None))
        self.logout.setText(QCoreApplication.translate("MainWindow", u"LOGOUT", None))
        self.label_12.setText("")
        self.welcome_2.setText(QCoreApplication.translate("MainWindow", u"Give feedback and help us make this product better!!", None))
        self.clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.submit.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.feedback.setText("")
        self.all_cam_op3.setText("")
        self.all_cam_op1.setText("")
        self.all_cam_op4.setText("")
        self.all_cam_op2.setText("")
        self.all_cam_op_start_btn.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.all_cam_op1_stop_btn.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\ue785", None))
        self.tb1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.tb2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.b1.setText(QCoreApplication.translate("MainWindow", u"LOG IN", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"REGISTER", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\ue77b", None))
        self.username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.password.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.email.setText("")
        self.email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.phonenumber.setText("")
        self.phonenumber.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.b2.setText(QCoreApplication.translate("MainWindow", u"REGISTER", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Change Theme", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"  Dark", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"  Light", None))
        self.pushButton_7.setText("")
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"VISION AI", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Using state of the artificial intelligence techniques and machine learning models,VISION AI provides a clear output video regardless of the weather or poor lightning conditions.</p><p>It also uses advanced intrrusion detection techniques to have automated surviellance system in and out of the house.</p><p><br/></p></body></html>", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"VISIT WEBSITE", None))
        self.label_14.setText("")
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.label_18.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"CCTV 1", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Main Gate", None))
        self.label_24.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"CCTV 2", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Bedroom", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.label_28.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"CCTV 3", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Backyard", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.cam_button_1.setText(QCoreApplication.translate("MainWindow", u"Backyard", None))
        self.cam_button_2.setText(QCoreApplication.translate("MainWindow", u"Bedroom 2", None))
        self.cam_button_3.setText(QCoreApplication.translate("MainWindow", u"Bedroom 1", None))
        self.cam_button_4.setText(QCoreApplication.translate("MainWindow", u"Main Gate", None))
        self.output_screen.setText("")
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Normal Feed", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Apply Filter", None))
        self.label_32.setText("")
        self.dehazer_low_button.setText(QCoreApplication.translate("MainWindow", u"Dehazer Low", None))
        self.label_33.setText("")
        self.dehazer_high_button.setText(QCoreApplication.translate("MainWindow", u"Dehazer High", None))
        self.label_34.setText("")
        self.lle_low_button.setText(QCoreApplication.translate("MainWindow", u"LLE Low", None))
        self.label_35.setText("")
        self.lle_high_button.setText(QCoreApplication.translate("MainWindow", u"LLE High", None))
        self.label_37.setText("")
        self.derainer_low_button.setText(QCoreApplication.translate("MainWindow", u"Derainer Low", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Version 1.0 | VISION AI", None))
        self.help_btn.setText(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

