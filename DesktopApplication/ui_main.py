# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import cv2
import datetime 
import os
import numpy as np
import matplotlib.pyplot as plt
import glob
import random
from PIL import Image
import time
import cv2
import tensorflow as tf
from tensorflow.keras.layers import *
from tensorflow.keras.models import Model
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.optimizers import Adam
from PyQt5.QtCore import pyqtSlot

from PyQt5.uic import loadUi

from PyQt5.QtGui import QImage , QPixmap

from PyQt5.QtWidgets import QDialog , QApplication

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

	model_path = './dehazer/trained_model'
	global test_net
	test_net = tf.keras.models.load_model(model_path, compile = False)

	config_file='./activitymodel/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
	frozen_model='./activitymodel/frozen_inference_graph.pb'

	global human_model
	human_model = cv2.dnn_DetectionModel(frozen_model, config_file)
	
	global labellist
	labellist= []
	file_name = 'label.txt'
	with open(file_name, 'rt') as fpt:
		labellist= fpt.read().rstrip('\n').split('\n')
	
	human_model.setInputSize(320,320)
	human_model.setInputScale(1.0/127.5)
	human_model.setInputMean((127.5,127.5,127.5))
	human_model.setInputSwapRB(True)

	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(901, 600)
		MainWindow.setMinimumSize(QtCore.QSize(900, 600))
		MainWindow.setStyleSheet("background-color:\'#8bbdd9\';")
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setMinimumSize(QtCore.QSize(700, 0))
		self.centralwidget.setObjectName("centralwidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setSpacing(0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.Top_Bar = QtWidgets.QFrame(self.centralwidget)
		self.Top_Bar.setMaximumSize(QtCore.QSize(16777215, 40))
		self.Top_Bar.setStyleSheet("background-color: rgb(35, 35, 35);")
		self.Top_Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
		self.Top_Bar.setObjectName("Top_Bar")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_Bar)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setSpacing(0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.frame_toggle = QtWidgets.QFrame(self.Top_Bar)
		self.frame_toggle.setMaximumSize(QtCore.QSize(70, 40))
		self.frame_toggle.setStyleSheet("background-color: rgb(85, 170, 255);")
		self.frame_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_toggle.setObjectName("frame_toggle")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_toggle)
		self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_2.setSpacing(0)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.Btn_Toggle = QtWidgets.QPushButton(self.frame_toggle)
		self.Btn_Toggle.setEnabled(True)
		sizePolicy = QtWidgets.QSizePolicy(
			QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(
			self.Btn_Toggle.sizePolicy().hasHeightForWidth())
		self.Btn_Toggle.setSizePolicy(sizePolicy)
		self.Btn_Toggle.setMinimumSize(QtCore.QSize(100, 40))
		self.Btn_Toggle.setStyleSheet("QPushButton {\n"
									  "    color: rgb(255, 255, 255);\n"
									  "    background-color: \'#0079bf\';\n"
									  "    border: 0px solid;\n"
									  "}\n"
									  "QPushButton:hover {\n"
									  "    background-color: rgb(85, 170, 255);\n"
									  "}")
		self.Btn_Toggle.setObjectName("Btn_Toggle")
		self.verticalLayout_2.addWidget(self.Btn_Toggle)
		self.horizontalLayout.addWidget(self.frame_toggle)
		self.frame_top = QtWidgets.QFrame(self.Top_Bar)
		self.frame_top.setMinimumSize(QtCore.QSize(0, 0))
		self.frame_top.setStyleSheet("background-color: \'#0079bf\';")
		self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_top.setObjectName("frame_top")
		self.horizontalLayout.addWidget(self.frame_top)
		self.verticalLayout.addWidget(self.Top_Bar)
		self.Content = QtWidgets.QFrame(self.centralwidget)
		self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
		self.Content.setObjectName("Content")
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
		self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_2.setSpacing(0)
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.frame_left_menu = QtWidgets.QFrame(self.Content)
		self.frame_left_menu.setMinimumSize(QtCore.QSize(100, 0))
		self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
		self.frame_left_menu.setStyleSheet("background-color:\'#0079bf\';")
		self.frame_left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_left_menu.setObjectName("frame_left_menu")
		self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
		self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_3.setObjectName("verticalLayout_3")
		self.btn_page_1 = QtWidgets.QPushButton(self.frame_left_menu)
		sizePolicy = QtWidgets.QSizePolicy(
			QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(
			self.btn_page_1.sizePolicy().hasHeightForWidth())
		self.btn_page_1.setSizePolicy(sizePolicy)
		self.btn_page_1.setMinimumSize(QtCore.QSize(0, 40))
		self.btn_page_1.setStyleSheet("QPushButton {\n"
									  "    font-size: 15px;\n"
									  "    color: rgb(255, 255, 255);\n"
									  "    background-color: \'#0079bf\';\n"
									  "    border: 0px solid;\n"
									  "}\n"
									  "QPushButton:hover {\n"
									  "    background-color: rgb(85, 170, 255);\n"
									  "}")
		self.btn_page_1.setObjectName("btn_page_1")
		self.verticalLayout_3.addWidget(self.btn_page_1)
		self.btn_page_2 = QtWidgets.QPushButton(self.frame_left_menu)
		self.btn_page_2.setMinimumSize(QtCore.QSize(0, 40))
		self.btn_page_2.setStyleSheet("QPushButton {\n"
									  "    font-size: 15px;\n"
									  "    color: rgb(255, 255, 255);\n"
									  "    background-color: \'#0079bf\';\n"
									  "    border: 0px solid;\n"
									  "}\n"
									  "QPushButton:hover {\n"
									  "    background-color: rgb(85, 170, 255);\n"
									  "}")
		self.btn_page_2.setObjectName("btn_page_2")
		self.verticalLayout_3.addWidget(self.btn_page_2)
		self.btn_page_3 = QtWidgets.QPushButton(self.frame_left_menu)
		self.btn_page_3.setMinimumSize(QtCore.QSize(0, 40))
		self.btn_page_3.setStyleSheet("QPushButton {\n"
									  "    font-size: 15px;\n"
									  "    color: rgb(255, 255, 255);\n"
									  "    background-color: \'#0079bf\';\n"
									  "    border: 0px solid;\n"
									  "}\n"
									  "QPushButton:hover {\n"
									  "    background-color: rgb(85, 170, 255);\n"
									  "}")
		self.btn_page_3.setObjectName("btn_page_3")
		self.verticalLayout_3.addWidget(self.btn_page_3)
		self.pushButton = QtWidgets.QPushButton(self.frame_left_menu)
		self.pushButton.setStyleSheet("QPushButton {\n"
									  "    font-size: 15px;\n"
									  "    color: rgb(255, 255, 255);\n"
									  "    background-color: \'#0079bf\';\n"
									  "    border: 0px solid;\n"
									  "    height: 40px;\n"
									  "}\n"
									  "QPushButton:hover {\n"
									  "    background-color: rgb(85, 170, 255);\n"
									  "}")
		self.pushButton.setObjectName("pushButton")
		self.verticalLayout_3.addWidget(self.pushButton)
		self.pushButton_2 = QtWidgets.QPushButton(self.frame_left_menu)
		self.pushButton_2.setStyleSheet("QPushButton {\n"
										"    font-size: 15px;\n"
										"    color: rgb(255, 255, 255);\n"
										"    background-color: \'#0079bf\';\n"
										"    border: 0px solid;\n"
										"    height: 40px;\n"
										"}\n"
										"QPushButton:hover {\n"
										"    background-color: rgb(85, 170, 255);\n"
										"}")
		self.pushButton_2.setObjectName("pushButton_2")
		self.verticalLayout_3.addWidget(self.pushButton_2)
		self.pushButton_5 = QtWidgets.QPushButton(self.frame_left_menu)
		self.pushButton_5.setStyleSheet("QPushButton {\n"
										"    font-size: 15px;\n"
										"    color: rgb(255, 255, 255);\n"
										"    background-color: \'#0079bf\';\n"
										"    border: 0px solid;\n"
										"    height: 40px;\n"
										"}\n"
										"QPushButton:hover {\n"
										"    background-color: rgb(85, 170, 255);\n"
										"}")
		self.pushButton_5.setObjectName("pushButton_5")
		self.verticalLayout_3.addWidget(self.pushButton_5)
		self.pushButton_4 = QtWidgets.QPushButton(self.frame_left_menu)
		self.pushButton_4.setStyleSheet("QPushButton {\n"
										"    font-size: 15px;\n"
										"    color: rgb(255, 255, 255);\n"
										"    background-color: \'#0079bf\';\n"
										"    border: 0px solid;\n"
										"    height: 40px;\n"
										"}\n"
										"QPushButton:hover {\n"
										"    background-color: rgb(85, 170, 255);\n"
										"}")
		self.pushButton_4.setObjectName("pushButton_4")
		self.verticalLayout_3.addWidget(self.pushButton_4)
		self.frame_top_menus = QtWidgets.QFrame(self.frame_left_menu)
		self.frame_top_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.frame_top_menus.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_top_menus.setObjectName("frame_top_menus")
		self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_top_menus)
		self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_4.setSpacing(0)
		self.verticalLayout_4.setObjectName("verticalLayout_4")
		self.verticalLayout_3.addWidget(
			self.frame_top_menus, 0, QtCore.Qt.AlignTop)
		self.label_10 = QtWidgets.QLabel(self.frame_left_menu)
		self.label_10.setMaximumSize(QtCore.QSize(100, 100))
		self.label_10.setText("")
		self.label_10.setPixmap(QtGui.QPixmap("logoo.png"))
		self.label_10.setScaledContents(True)
		self.label_10.setObjectName("label_10")
		self.verticalLayout_3.addWidget(self.label_10)
		self.horizontalLayout_2.addWidget(self.frame_left_menu)
		self.frame_pages = QtWidgets.QFrame(self.Content)
		self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_pages.setObjectName("frame_pages")
		self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_pages)
		self.verticalLayout_5.setObjectName("verticalLayout_5")
		self.stackedWidget = QtWidgets.QStackedWidget(self.frame_pages)
		self.stackedWidget.setObjectName("stackedWidget")
		self.page_0 = QtWidgets.QWidget()
		self.page_0.setObjectName("page_0")
		self.verticalWidget = QtWidgets.QWidget(self.page_0)
		self.verticalWidget.setGeometry(QtCore.QRect(590, 80, 191, 181))
		self.verticalWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
										  "")
		self.verticalWidget.setObjectName("verticalWidget")
		self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalWidget)
		self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_9.setObjectName("verticalLayout_9")



		#-----------------------RADIO BUTTONS -----------------
		'''
		self.radioButton_2 = QtWidgets.QRadioButton(self.verticalWidget)
		self.radioButton_2.setObjectName("radioButton_2")
		self.verticalLayout_9.addWidget(self.radioButton_2)
		self.radioButton_2.toggled.connect(self.onRadioBtn)
		#self.radioButton_2.setChecked(True)
'''

		self.dehazeButton = QtWidgets.QPushButton(self.verticalWidget)
		self.dehazeButton.setGeometry(QtCore.QRect(0, 0, 200, 40))
		#self.dehazeButton.setMinimumSize(QtCore.QSize(200, 20))
		#self.dehazeButton.setMaximumSize(QtCore.QSize(100, 20))
		self.dehazeButton.setStyleSheet("QPushButton{\n"
								 "        border-radius : 10;\n"
								 "        border: 6px solid \n"
								 "        border-style: double;\n"
								 "        font-size: 20px;\n"
								 "}")
		self.dehazeButton.setObjectName("dehazeButton")
		self.dehazeButton.clicked.connect(self.dehaze)



		self.derainButton = QtWidgets.QPushButton(self.verticalWidget)
		self.derainButton.setGeometry(QtCore.QRect(0, 45, 200, 40))
		#self.derainButton.setMinimumSize(QtCore.QSize(200, 20))
		#self.derainButton.setMaximumSize(QtCore.QSize(100, 20))
		self.derainButton.setStyleSheet("QPushButton{\n"
								 "        border-radius : 10;\n"
								 "        border: 6px solid \n"
								 "        border-style: double;\n"
								 "        font-size: 20px;\n"
								 "}")
		self.derainButton.setObjectName("derainButton")

		self.lle = QtWidgets.QPushButton(self.verticalWidget)
		self.lle.setGeometry(QtCore.QRect(0, 90, 200, 40))
		#self.lle.setMinimumSize(QtCore.QSize(200, 20))
		#self.lle.setMaximumSize(QtCore.QSize(100, 20))
		self.lle.setStyleSheet("QPushButton{\n"
								 "        border-radius : 10;\n"
								 "        border: 6px solid \n"
								 "        border-style: double;\n"
								 "        font-size: 20px;\n"
								 "}")
		self.lle.setObjectName("lle")

		self.stopfilter = QtWidgets.QPushButton(self.verticalWidget)
		self.stopfilter.setGeometry(QtCore.QRect(0, 135, 200, 40))
		#self.lle.setMinimumSize(QtCore.QSize(200, 20))
		#self.lle.setMaximumSize(QtCore.QSize(100, 20))
		self.stopfilter.setStyleSheet("QPushButton{\n"
								 "        border-radius : 10;\n"
								 "        border: 6px solid \n"
								 "        border-style: double;\n"
								 "        font-size: 20px;\n"
								 "}")
		self.stopfilter.setObjectName("stopfilter")
		self.stopfilter.clicked.connect(self.backtoNormal)
		
		#--------------------------------------------------------

		self.label_3 = QtWidgets.QLabel(self.page_0)
		self.label_3.setGeometry(QtCore.QRect(590, 30, 190, 50))
		self.label_3.setMinimumSize(QtCore.QSize(0, 0))
		self.label_3.setMaximumSize(QtCore.QSize(190, 50))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(-1)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(50)
		self.label_3.setFont(font)
		self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.label_3.setStyleSheet("background-color: \'#5ba4cf\';\n"
								   "font: 8pt \"Arial\";\n"
								   "font: 20px \"Arial\";\n"
								   "")
		self.label_3.setAlignment(QtCore.Qt.AlignCenter)
		self.label_3.setObjectName("label_3")
		self.calendarWidget = QtWidgets.QCalendarWidget(self.page_0)
		self.calendarWidget.setEnabled(True)
		self.calendarWidget.setGeometry(QtCore.QRect(491, 318, 281, 211))
		sizePolicy = QtWidgets.QSizePolicy(
			QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(
			self.calendarWidget.sizePolicy().hasHeightForWidth())
		self.calendarWidget.setSizePolicy(sizePolicy)
		self.calendarWidget.setFocusPolicy(QtCore.Qt.TabFocus)
		self.calendarWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
		self.calendarWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.calendarWidget.setVerticalHeaderFormat(
			QtWidgets.QCalendarWidget.NoVerticalHeader)
		self.calendarWidget.setNavigationBarVisible(False)
		self.calendarWidget.setDateEditEnabled(True)
		self.calendarWidget.setDateEditAcceptDelay(1500)
		self.calendarWidget.setObjectName("calendarWidget")
		self.label_4 = QtWidgets.QLabel(self.page_0)
		self.label_4.setGeometry(QtCore.QRect(0, 50, 81, 81))
		self.label_4.setText("")
		self.label_4.setPixmap(QtGui.QPixmap("cctv.png"))
		self.label_4.setObjectName("label_4")
		self.label_6 = QtWidgets.QLabel(self.page_0)
		self.label_6.setGeometry(QtCore.QRect(0, 140, 81, 81))
		self.label_6.setText("")
		self.label_6.setPixmap(QtGui.QPixmap(
			"../../.designer/backup/python/cctv.png"))
		self.label_6.setObjectName("label_6")
		self.label_7 = QtWidgets.QLabel(self.page_0)
		self.label_7.setGeometry(QtCore.QRect(0, 230, 81, 81))
		self.label_7.setText("")
		self.label_7.setPixmap(QtGui.QPixmap(
			"../../.designer/backup/python/cctv.png"))
		self.label_7.setObjectName("label_7")
		self.label_5 = QtWidgets.QLabel(self.page_0)
		self.label_5.setGeometry(QtCore.QRect(20, 130, 47, 13))
		self.label_5.setObjectName("label_5")
		self.label_8 = QtWidgets.QLabel(self.page_0)
		self.label_8.setGeometry(QtCore.QRect(20, 230, 47, 13))
		self.label_8.setObjectName("label_8")
		self.label_9 = QtWidgets.QLabel(self.page_0)
		self.label_9.setGeometry(QtCore.QRect(20, 330, 47, 13))
		self.label_9.setObjectName("label_9")
		self.label_14 = QtWidgets.QLabel(self.page_0)
		self.label_14.setGeometry(QtCore.QRect(0, 150, 81, 81))
		self.label_14.setText("")
		self.label_14.setPixmap(QtGui.QPixmap("cctv.png"))
		self.label_14.setObjectName("label_14")
		self.label_15 = QtWidgets.QLabel(self.page_0)
		self.label_15.setGeometry(QtCore.QRect(0, 250, 81, 81))
		self.label_15.setText("")
		self.label_15.setPixmap(QtGui.QPixmap("cctv.png"))
		self.label_15.setObjectName("label_15")
		self.imgLabel = QtWidgets.QLabel(self.page_0)
		self.imgLabel.setGeometry(QtCore.QRect(90, 0, 491, 311))
		self.imgLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.imgLabel.setText("")
		self.imgLabel.setObjectName("imgLabel")
		self.START = QtWidgets.QPushButton(self.page_0)
		self.START.setGeometry(QtCore.QRect(90, 380, 200, 60))
		self.START.setMinimumSize(QtCore.QSize(200, 60))
		self.START.setMaximumSize(QtCore.QSize(200, 60))
		self.START.setStyleSheet("QPushButton{\n"
								 "        border-radius : 30;\n"
								 "        border: 6px solid \'#0079bf\';\n"
								 "        border-style: double;\n"
								 "        font-size: 20px;\n"
								 "        color: \'white\';\n"
								 "}")
		self.START.setObjectName("START")
		self.START.clicked.connect(self.STARTClicked)
		self.STOP = QtWidgets.QPushButton(self.page_0)
		self.STOP.setGeometry(QtCore.QRect(290, 380, 200, 60))
		self.STOP.setMinimumSize(QtCore.QSize(200, 60))
		self.STOP.setMaximumSize(QtCore.QSize(200, 60))
		self.STOP.setStyleSheet("QPushButton{\n"
								"        border-radius : 30;\n"
								"        border: 6px solid \'#0079bf\';\n"
								"        border-style: double;\n"
								"        font-size: 20px;\n"
								"        color: \'white\';\n"
								"}")
		self.STOP.setObjectName("STOP")
		self.STOP.clicked.connect(self.STOPClicked)

		#self.TEXT = QtWidgets.QTextBrowser(self.page_0)
		#self.TEXT.setGeometry(QtCore.QRect(90, 320, 391, 51))
		#self.TEXT.setStyleSheet("background-color: rgb(255, 255, 255);")
		#self.TEXT.setObjectName("TEXT")

		self.ODButton = QtWidgets.QPushButton(self.page_0)
		self.ODButton.setGeometry(QtCore.QRect(90, 320, 391, 51))
		#self.dehazeButton.setMinimumSize(QtCore.QSize(200, 20))
		#self.dehazeButton.setMaximumSize(QtCore.QSize(100, 20))
		self.ODButton.setStyleSheet("QPushButton{\n"
								 "        border-radius : 10;\n"
								 "        border: 6px solid \n"
								 "        border-style: double;\n"
								 "        font-size: 100px;\n"
								 "}")
		self.ODButton.setObjectName("ODButton")

		self.dehazeButton.clicked.connect(self.dehaze)
		self.ODButton.clicked.connect(self.setdetectvalue)
		self.stackedWidget.addWidget(self.page_0)
		self.page1 = QtWidgets.QWidget()
		self.page1.setObjectName("page1")
		self.frame2 = QtWidgets.QFrame(self.page1)
		self.frame2.setGeometry(QtCore.QRect(-1, 269, 781, 281))
		self.frame2.setStyleSheet("background-color: \'#5ba4cf\';")
		self.frame2.setObjectName("frame2")
		self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame2)
		self.horizontalLayout_4.setObjectName("horizontalLayout_4")
		self.frame = QtWidgets.QFrame(self.frame2)
		self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame.setObjectName("frame")
		self.verticalWidget1 = QtWidgets.QWidget(self.frame)
		self.verticalWidget1.setGeometry(QtCore.QRect(-1, -1, 231, 251))
		self.verticalWidget1.setObjectName("verticalWidget1")
		self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalWidget1)
		self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_10.setObjectName("verticalLayout_10")
		self.label_19 = QtWidgets.QLabel(self.verticalWidget1)
		self.label_19.setMaximumSize(QtCore.QSize(200, 150))
		self.label_19.setText("")
		self.label_19.setPixmap(QtGui.QPixmap("cctv2.png"))
		self.label_19.setScaledContents(True)
		self.label_19.setObjectName("label_19")
		self.verticalLayout_10.addWidget(
			self.label_19, 0, QtCore.Qt.AlignHCenter)
		self.label_16 = QtWidgets.QLabel(self.verticalWidget1)
		self.label_16.setObjectName("label_16")
		self.verticalLayout_10.addWidget(
			self.label_16, 0, QtCore.Qt.AlignHCenter)
		self.label_22 = QtWidgets.QLabel(self.verticalWidget1)
		self.label_22.setObjectName("label_22")
		self.verticalLayout_10.addWidget(
			self.label_22, 0, QtCore.Qt.AlignHCenter)
		self.pushButton_6 = QtWidgets.QPushButton(self.verticalWidget1)
		self.pushButton_6.setMinimumSize(QtCore.QSize(200, 60))
		self.pushButton_6.setMaximumSize(QtCore.QSize(200, 60))
		self.pushButton_6.setStyleSheet("QPushButton{\n"
										"        border-radius : 30;\n"
										"        border: 6px solid \'#0079bf\';\n"
										"        border-style: double;\n"
										"        font-size: 20px;\n"
										"        color: \'white\';\n"
										"}")
		self.pushButton_6.setObjectName("pushButton_6")
		self.verticalLayout_10.addWidget(
			self.pushButton_6, 0, QtCore.Qt.AlignHCenter)
		self.verticalWidget_2 = QtWidgets.QWidget(self.frame)
		self.verticalWidget_2.setGeometry(QtCore.QRect(229, -1, 281, 251))
		self.verticalWidget_2.setObjectName("verticalWidget_2")
		self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
		self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_11.setObjectName("verticalLayout_11")
		self.label_17 = QtWidgets.QLabel(self.verticalWidget_2)
		self.label_17.setMaximumSize(QtCore.QSize(200, 150))
		self.label_17.setText("")
		self.label_17.setPixmap(QtGui.QPixmap("cctv2.png"))
		self.label_17.setScaledContents(True)
		self.label_17.setObjectName("label_17")
		self.verticalLayout_11.addWidget(
			self.label_17, 0, QtCore.Qt.AlignHCenter)
		self.label_20 = QtWidgets.QLabel(self.verticalWidget_2)
		self.label_20.setObjectName("label_20")
		self.verticalLayout_11.addWidget(
			self.label_20, 0, QtCore.Qt.AlignHCenter)
		self.label_23 = QtWidgets.QLabel(self.verticalWidget_2)
		self.label_23.setObjectName("label_23")
		self.verticalLayout_11.addWidget(
			self.label_23, 0, QtCore.Qt.AlignHCenter)
		self.pushButton_7 = QtWidgets.QPushButton(self.verticalWidget_2)
		self.pushButton_7.setMinimumSize(QtCore.QSize(200, 60))
		self.pushButton_7.setMaximumSize(QtCore.QSize(200, 60))
		self.pushButton_7.setStyleSheet("QPushButton{\n"
										"        border-radius : 30;\n"
										"        border: 6px solid \'#0079bf\';\n"
										"        border-style: double;\n"
										"        font-size: 20px;\n"
										"        color: \'white\';\n"
										"}")
		self.pushButton_7.setObjectName("pushButton_7")
		self.verticalLayout_11.addWidget(
			self.pushButton_7, 0, QtCore.Qt.AlignHCenter)
		self.verticalWidget_3 = QtWidgets.QWidget(self.frame)
		self.verticalWidget_3.setGeometry(QtCore.QRect(509, -1, 251, 251))
		self.verticalWidget_3.setObjectName("verticalWidget_3")
		self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.verticalWidget_3)
		self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_12.setObjectName("verticalLayout_12")
		self.label_18 = QtWidgets.QLabel(self.verticalWidget_3)
		self.label_18.setMaximumSize(QtCore.QSize(200, 150))
		self.label_18.setText("")
		self.label_18.setPixmap(QtGui.QPixmap("cctv2.png"))
		self.label_18.setScaledContents(True)
		self.label_18.setObjectName("label_18")
		self.verticalLayout_12.addWidget(
			self.label_18, 0, QtCore.Qt.AlignHCenter)
		self.label_21 = QtWidgets.QLabel(self.verticalWidget_3)
		self.label_21.setMaximumSize(QtCore.QSize(200, 200))
		self.label_21.setObjectName("label_21")
		self.verticalLayout_12.addWidget(
			self.label_21, 0, QtCore.Qt.AlignHCenter)
		self.label_24 = QtWidgets.QLabel(self.verticalWidget_3)
		self.label_24.setObjectName("label_24")
		self.verticalLayout_12.addWidget(
			self.label_24, 0, QtCore.Qt.AlignHCenter)
		self.pushButton_8 = QtWidgets.QPushButton(self.verticalWidget_3)
		self.pushButton_8.setMinimumSize(QtCore.QSize(200, 60))
		self.pushButton_8.setMaximumSize(QtCore.QSize(200, 60))
		self.pushButton_8.setStyleSheet("QPushButton{\n"
										"        border-radius : 30;\n"
										"        border: 6px solid \'#0079bf\';\n"
										"        border-style: double;\n"
										"        font-size: 20px;\n"
										"        color: \'white\';\n"
										"}")
		self.pushButton_8.setObjectName("pushButton_8")
		self.verticalLayout_12.addWidget(
			self.pushButton_8, 0, QtCore.Qt.AlignHCenter)
		self.horizontalLayout_4.addWidget(self.frame)
		self.widget1 = QtWidgets.QWidget(self.page1)
		self.widget1.setGeometry(QtCore.QRect(-1, -1, 791, 271))
		self.widget1.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.widget1.setObjectName("widget1")
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
		self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		self.verticalLayout_7 = QtWidgets.QVBoxLayout()
		self.verticalLayout_7.setObjectName("verticalLayout_7")
		self.label_12 = QtWidgets.QLabel(self.widget1)
		self.label_12.setStyleSheet("color: \'#5ba4cf\';\n"
									"font: 25px \"Arial\";\n"
									"text-decoration: underline;\n"
									"")
		self.label_12.setAlignment(
			QtCore.Qt.AlignBottom | QtCore.Qt.AlignJustify)
		self.label_12.setObjectName("label_12")
		self.verticalLayout_7.addWidget(self.label_12)
		self.textEdit_2 = QtWidgets.QTextEdit(self.widget1)
		self.textEdit_2.setMaximumSize(QtCore.QSize(400, 60))
		self.textEdit_2.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.textEdit_2.setObjectName("textEdit_2")
		self.verticalLayout_7.addWidget(self.textEdit_2)
		self.pushButton_3 = QtWidgets.QPushButton(self.widget1)
		self.pushButton_3.setMinimumSize(QtCore.QSize(200, 60))
		self.pushButton_3.setMaximumSize(QtCore.QSize(200, 150))
		self.pushButton_3.setStyleSheet("QPushButton{\n"
										"        border-radius : 30;\n"
										"        border: 6px solid \'#0079bf\';\n"
										"        border-style: double;\n"
										"        font-size: 20px;\n"
										"        color: \'#5ba4cf\';\n"
										"}")
		self.pushButton_3.setObjectName("pushButton_3")
		self.verticalLayout_7.addWidget(self.pushButton_3)
		self.label_11 = QtWidgets.QLabel(self.widget1)
		self.label_11.setStyleSheet("font: 12pt \"Arial\";\n"
									"text-decoration: underline;")
		self.label_11.setObjectName("label_11")
		self.verticalLayout_7.addWidget(self.label_11, 0, QtCore.Qt.AlignTop)
		self.horizontalLayout_3.addLayout(self.verticalLayout_7)
		self.label_13 = QtWidgets.QLabel(self.widget1)
		self.label_13.setMaximumSize(QtCore.QSize(400, 16777215))
		self.label_13.setText("")
		self.label_13.setPixmap(QtGui.QPixmap("picture.jpg"))
		self.label_13.setScaledContents(True)
		self.label_13.setObjectName("label_13")
		self.horizontalLayout_3.addWidget(
			self.label_13, 0, QtCore.Qt.AlignRight)
		self.stackedWidget.addWidget(self.page1)
		self.page_2 = QtWidgets.QWidget()
		self.page_2.setObjectName("page_2")
		self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_2)
		self.verticalLayout_6.setObjectName("verticalLayout_6")
		self.label_2 = QtWidgets.QLabel(self.page_2)
		font = QtGui.QFont()
		font.setPointSize(40)
		self.label_2.setFont(font)
		self.label_2.setStyleSheet("color: #FFF;")
		self.label_2.setAlignment(QtCore.Qt.AlignCenter)
		self.label_2.setObjectName("label_2")
		self.verticalLayout_6.addWidget(self.label_2)
		self.stackedWidget.addWidget(self.page_2)
		self.page_4 = QtWidgets.QWidget()
		self.page_4.setObjectName("page_4")
		self.stackedWidget.addWidget(self.page_4)
		self.page_3 = QtWidgets.QWidget()
		self.page_3.setObjectName("page_3")
		self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_3)
		self.verticalLayout_8.setObjectName("verticalLayout_8")
		self.label = QtWidgets.QLabel(self.page_3)
		font = QtGui.QFont()
		font.setPointSize(40)
		self.label.setFont(font)
		self.label.setStyleSheet("color: #FFF;")
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setObjectName("label")
		self.verticalLayout_8.addWidget(self.label)
		self.stackedWidget.addWidget(self.page_3)
		self.verticalLayout_5.addWidget(self.stackedWidget)
		self.horizontalLayout_2.addWidget(self.frame_pages)
		self.verticalLayout.addWidget(self.Content)
		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		self.stackedWidget.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.Btn_Toggle.setText(_translate("MainWindow", "Menu"))
		self.btn_page_1.setText(_translate("MainWindow", "Dashboard"))
		self.btn_page_2.setText(_translate("MainWindow", "Live Cam"))
		self.btn_page_3.setText(_translate("MainWindow", "History"))
		self.pushButton.setText(_translate("MainWindow", "Recordings"))
		self.pushButton_2.setText(_translate("MainWindow", "Feedback"))
		self.pushButton_5.setText(_translate("MainWindow", "Video Cabinet"))
		self.pushButton_4.setText(_translate("MainWindow", "Account"))
		#self.radioButton_2.setText(_translate("MainWindow", "Dehazing"))
		#self.radioButton_3.setText(_translate("MainWindow", "Deraining"))
		#self.radioButton.setText(_translate("MainWindow", "Low Light Enhanchement"))
		self.label_3.setText(_translate("MainWindow", "Apply Filter"))
		self.label_5.setText(_translate("MainWindow", "camera 1"))
		self.label_8.setText(_translate("MainWindow", "camera 2"))
		self.label_9.setText(_translate("MainWindow", "camera 3"))
		self.START.setText(_translate("MainWindow", "Start"))
		self.dehazeButton.setText(_translate("MainWindow", "DEHAZE"))
		self.derainButton.setText(_translate("MainWindow", "DERAIN"))
		self.lle.setText(_translate("MainWindow", "Low Light Enhancement"))
		self.ODButton.setText(_translate("MainWindow", "Detect Human Activity"))
		self.stopfilter.setText(_translate("MainWindow", "NORMAL"))
		self.STOP.setText(_translate("MainWindow", "Stop"))
		
		self.label_16.setText(_translate("MainWindow", "CCTV 1"))
		self.label_22.setText(_translate("MainWindow", "Main Gate"))
		self.pushButton_6.setText(_translate("MainWindow", "View"))
		self.label_20.setText(_translate("MainWindow", "CCTV 2"))
		self.label_23.setText(_translate("MainWindow", "Backyard"))
		self.pushButton_7.setText(_translate("MainWindow", "View"))
		self.label_21.setText(_translate("MainWindow", "CCTV 3"))
		self.label_24.setText(_translate("MainWindow", "Rooftop"))
		self.pushButton_8.setText(_translate("MainWindow", "View"))
		self.label_12.setText(_translate("MainWindow", "Home Keeper"))
		self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
										   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
										   "p, li { white-space: pre-wrap; }\n"
										   "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
										   "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#5ba4cf; vertical-align:super;\">AI vision not only helps clear out blurred videos. It also helps detect suspicious human movement in and out of the house.</span></p></body></html>"))
		self.pushButton_3.setText(_translate("MainWindow", "Get Started"))
		self.label_11.setText(_translate("MainWindow", "upgrade now"))
		self.label_2.setText(_translate("MainWindow", "PAGE 2"))
		self.label.setText(_translate("MainWindow", "PAGE 3"))

	
	global filtervalue
	filtervalue = 0
	global detecttrue 
	detecttrue = 0

	global toggledetect
	toggledetect = 0

	def setdetectvalue(self):
		global detecttrue 
		global toggledetect
		if (toggledetect == 0):
			detecttrue = 1
			toggledetect = 1
		else:
			detecttrue = 0
			toggledetect = 0


	def start_detecting(self, frame):
		ClassIndex,confidece, bbox = human_model.detect(frame, confThreshold= 0.65)
		if(len(ClassIndex)!=0):
			for ClassInd, conf, boxes in zip(ClassIndex.flatten(),confidece.flatten(),bbox):
				if(ClassInd<= 80):
					if (labellist[ClassInd-1] == 'person'):
						print("Intrusion Activity Detected")

	def STARTClicked(self):
		self.logic=1
		cap = cv2.VideoCapture(1)
		date = datetime.datetime.now()
		frame_width = int(cap.get(3))
		frame_height = int(cap.get(4))
		out = cv2.VideoWriter('./Recorded/cctv_%s_%s_%s_%s_%s_%s.mp4'%(date.year, date.month, date.day, date.hour, date.minute, date.second),cv2.VideoWriter_fourcc ('M', 'J', 'P', 'G'), 30.0 , (frame_width, frame_height) )
		print('here')
		while (cap.isOpened()):
				#%s%s%sT%s%s%s.mp4'%(date.year, date,month, date.daym date.hour, date.minute, date.second)
			ret, frame = cap.read()
			if ret == True :
				if filtervalue == 1:
					self.displayImage(out ,frame,1)
				else:
					self.displayNormalImage(out, frame, 1)
				if (detecttrue == 1):
					self.start_detecting(frame)
					#print("Detecting")
				cv2.waitKey()
				if (self.logic==1):
					pass 
				if (self.logic==0):
					break
			else:
				print('return not found')
		cap.release()
		cv2.destroyAllWindows()

	def STOPClicked(self):
		self.logic=0

	def backtoNormal(self):
		global filtervalue
		filtervalue = 0


	def dehaze(self):
		global filtervalue
		filtervalue = 1

	def displayNormalImage(self, out, img, window=1):
		frame_r = img
		out.write(frame_r)
		qformat = QImage.Format_Indexed8
		#print(type(frame_r))
		if len(frame_r.shape) ==3:

			if (frame_r.shape[2])==4:
				qformat=QImage.Format_RGBA888
			else:
				qformat= QImage.Format_RGB888

		img= QImage(frame_r,frame_r.shape[1], frame_r.shape[0], qformat)
		img= img.rgbSwapped()

		
		self.imgLabel.setPixmap(QPixmap.fromImage(img))

	
	def displayImage(self, out, img, window=1):
		#frame_r = img
		frame_p = img
		
		#-----------FOR NET PASSING---------
		frame_tensor = tf.convert_to_tensor(frame_p)
		temp_zero = frame_tensor.shape[0]
		temp_one = frame_tensor.shape[1]
		frame_tensor = tf.image.resize(frame_tensor, size = (480, 640), antialias = True)

		frame_tensor = frame_tensor / 255.0
		frame_tensor = tf.expand_dims(frame_tensor, axis = 0) 
		dehaze = test_net(frame_tensor, training = False)
		dehaze = tf.image.resize(dehaze, size = (temp_zero, temp_one), antialias = True)
		
		d_op = dehaze[0].numpy()
		# make sure that values are between 0 and 255, i.e. within 8bit range
		d_op *= 255/d_op.max() 
		# cast to 8bit
		d_op = np.array(d_op, np.uint8)
		#print('dop:',type(d_op))
		#-----------------------------------
		out.write(d_op)
		frame_r = d_op

		qformat = QImage.Format_Indexed8
		#print(type(frame_r))
		if len(frame_r.shape) ==3:

			if (frame_r.shape[2])==4:
				qformat=QImage.Format_RGBA888
			else:
				qformat= QImage.Format_RGB888

		img= QImage(frame_r,frame_r.shape[1], frame_r.shape[0], qformat)
		img= img.rgbSwapped()


		self.imgLabel.setPixmap(QPixmap.fromImage(img))

	def onRadioBtn(self):
		radioBtn = self.sender()
		if radioBtn.isChecked():
			self.TEXT.setText("yipeees")

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
