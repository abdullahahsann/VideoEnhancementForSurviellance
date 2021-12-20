import sys
import os
from multiprocessing import cpu_count
import datetime
import shutil 
from time import time, sleep
import datetime 
import webbrowser
import telegram_send

import winsound
#pyqt imports
from ui_vision_ai2 import *
import platform
import PySide2extn
from qt_material import *
from PySide2 import *
import psutil
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

#Image processing related imports
import imutils
from PIL import Image
import cv2 as cv
import numpy as np
import tensorflow as tf
import tensorflow.keras.backend as K
from tensorflow import keras
from tensorflow.keras.layers import *
from tensorflow.keras.models import Model
from tensorflow.keras import Input
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.optimizers import Adam
import mysql.connector as con
import re

tf.compat.v1.enable_eager_execution()

import json
from keras.models import model_from_json
########################################################################
## WORKER SIGNAL CLASS
########################################################################
class WorkerSignals(QObject):
	finished = Signal()
	error = Signal(tuple)
	result = Signal(object)
	progress = Signal(int)



########################################################################
## WORKER  CLASS
########################################################################
class Worker(QRunnable):
	def __init__(self, fn, *args, **kwargs):
		super(Worker, self).__init__()
		self.fn = fn
		self.args = args
		self.kwargs = kwargs
		self.signals = WorkerSignals()
		self.kwargs['progress_callback'] = self.signals.progress

	@Slot()
	def run(self):
		try:
			result = self.fn(*self.args, **self.kwargs)
		except:
			traceback.print_exc()
			exctype, value = sys.exc_info()[:2]
			self.signals.error.emit((exctype, value, traceback.format_exc()))
		else:
			self.signals.result.emit(result)  # Return the result of the processing
		finally:
			self.signals.finished.emit()  # Done


########################################################################
## 
########################################################################


class MainWindow(QMainWindow):
	#dehazer model
	dehazer_model_path = './dehazer/trained_model/'
	global dehazer_model
	dehazer_model = tf.keras.models.load_model(dehazer_model_path, compile = False)

	#derainer model
	# derainer_model_path = './onh2/trained_model'
	global derainer_model
	global weight_decay
	weight_decay = 1e-4
	def aod_net_mod2_2():
		global weight_decay
		inputs = tf.keras.Input(shape = [480, 640, 3])     			
		#X = inputs
		conv1 = Conv2D(64,3,1,padding="SAME",activation="relu",use_bias=True,kernel_initializer=tf.initializers.random_normal(),
					kernel_regularizer=tf.keras.regularizers.l2(weight_decay))
		conv2 = Conv2D(64,3,1,padding="SAME",activation="relu",use_bias=True,kernel_initializer=tf.initializers.random_normal(),
					kernel_regularizer=tf.keras.regularizers.l2(weight_decay))
		conv3 = Conv2D(64,5,1,padding="SAME",activation="relu",use_bias=True,kernel_initializer=tf.initializers.random_normal(),
					kernel_regularizer=tf.keras.regularizers.l2(weight_decay))
		conv4 = Conv2D(64,7,1,padding="SAME",activation="relu",use_bias=True,kernel_initializer=tf.initializers.random_normal(),
					kernel_regularizer=tf.keras.regularizers.l2(weight_decay))
		conv5 = Conv2D(3,3,1,padding="SAME",activation="relu",use_bias=True,kernel_initializer=tf.initializers.random_normal(),
					kernel_regularizer=tf.keras.regularizers.l2(weight_decay))
		conv6 = Conv2D(128,3,1,padding="SAME",activation="relu",use_bias=True,kernel_initializer=tf.initializers.random_normal(),
					kernel_regularizer=tf.keras.regularizers.l2(weight_decay))
		mp_layer = MaxPooling2D((2,2))
		conv7 = Conv2D(256,3,1,padding="SAME",activation="relu",use_bias=True,kernel_initializer=tf.initializers.random_normal(),
					kernel_regularizer=tf.keras.regularizers.l2(weight_decay))
		relu = ReLU(max_value = 1.0)
		#concatenatio
		conv_1 = conv1(inputs)
		conv_2 = conv2(conv_1)
		conc_1 = tf.concat([conv_1 + conv_2], axis = -1)
		conv_3 = conv3(conc_1)
		conc_2 = tf.concat([conv_2 + conv_3], axis = -1)
		conv_6 = conv6(conc_2)
		mp6 = mp_layer(conv_6)
		conv_4 = conv4(mp6)
		mp1 = mp_layer(conv_1)
		mp2 = mp_layer(conv_2)
		mp3 = mp_layer(conv_3)
		conc_3 = tf.concat([mp1 + mp2 + mp3 + conv_4], axis = -1)
		mc = conv7(conc_3)
		k = conv5(mc)
		print(k)
		dc = Conv2DTranspose(filters = 64, kernel_size = 3, strides = 2, padding = 'same', kernel_initializer = tf.keras.initializers.glorot_normal(seed = 101),
								kernel_regularizer = tf.keras.regularizers.l2(weight_decay))(k)	
		dc_conv = Conv2D(32,3,1,padding="SAME",activation="relu",use_bias=True,kernel_initializer=tf.initializers.random_normal(),
					kernel_regularizer=tf.keras.regularizers.l2(weight_decay))(dc)
		dc_conv2 = Conv2D(3,3,1,padding="SAME",activation="relu",use_bias=True,kernel_initializer=tf.initializers.random_normal(),
					kernel_regularizer=tf.keras.regularizers.l2(weight_decay))(dc_conv)
		j = inputs - dc_conv2 + 1.0
		output = relu(j)
		#output = ReLU(max_value=1.0)(tf.math.multiply(K,X) - K + 1.0)
		#output = output / 255.0
		return Model(inputs = inputs, outputs = output)

	derainer_model = aod_net_mod2_2()
	derainer_model.load_weights("forgodssake.h5")

	# with open(model_architecture, 'r') as json_file:
	# 	architecture = json.load(json_file)
	# 	model = model_from_json(architecture)
	
	#lle model
	global lle_model
	input_img = Input(shape=(512, 512, 3))
	conv1 = Conv2D(32, (3, 3), strides=(1,1), activation='relu', padding='same')(input_img)
	conv2 = Conv2D(32, (3, 3), strides=(1,1), activation='relu', padding='same')(conv1)
	conv3 = Conv2D(32, (3, 3), strides=(1,1), activation='relu', padding='same')(conv2)
	conv4 = Conv2D(32, (3, 3), strides=(1,1), activation='relu', padding='same')(conv3)
	int_con1 = Concatenate(axis=-1)([conv4, conv3])
	conv5 = Conv2D(32, (3, 3), strides=(1,1), activation='relu', padding='same')(int_con1)
	int_con2 = Concatenate(axis=-1)([conv5, conv2])
	conv6 = Conv2D(32, (3, 3), strides=(1,1), activation='relu', padding='same')(int_con2)
	int_con3 = Concatenate(axis=-1)([conv6, conv1])
	x_r = Conv2D(24, (3,3), strides=(1,1), activation='tanh', padding='same')(int_con3)
	lle_model = Model(inputs=input_img, outputs = x_r)
	lle_model.load_weights("lle/ep_23_it_1000.h5")

	#Human Detection Model
	config_file='./activitymodel/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
	frozen_model='./activitymodel/frozen_inference_graph.pb'

	global human_model
	human_model = cv.dnn_DetectionModel(frozen_model, config_file)
	
	global labellist
	labellist= []
	file_name = 'label.txt'
	with open(file_name, 'rt') as fpt:
		labellist= fpt.read().rstrip('\n').split('\n')
	
	human_model.setInputSize(320,320)
	human_model.setInputScale(1.0/127.5)
	human_model.setInputMean((127.5,127.5,127.5))
	human_model.setInputSwapRB(True)

	# Global Valyes
	global camera_number
	camera_number = 0

	global filterValue 
	filterValue = 0

	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		apply_stylesheet(app, theme='dark_cyan.xml')
		self.ui.b1.clicked.connect(self.Login)
		self.ui.b2.clicked.connect(self.Registration)
		self.ui.submit.clicked.connect(self.Adminfeedback)
		self.ui.logout.clicked.connect(self.logoutend)
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

		self.shadow = QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(50)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.shadow.setColor(QColor(0,92,157,550))

		self.ui.centralwidget.setGraphicsEffect(self.shadow)

		self.setWindowIcon(QtGui.QIcon("\\icons\\feather\\app_logo.png"))
		self.setWindowTitle("VISION AI")

		#close_min_max buttons
		self.ui.minimizeWindowButton.clicked.connect(lambda: self.showMinimized())
		self.ui.closeWindowButton.clicked.connect(lambda: self.close())
		self.ui.restoreWindowButton.clicked.connect(lambda: self.restore_or_maximize_window())

		#Navigation Menu
		self.ui.page_home_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home))
		self.ui.page_camera_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.cameras))
		self.ui.page_intrusion_det_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.intrusion_detection))
		self.ui.page_database_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.video_database))
		#self.ui.page_analytics_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.analytics))
		self.ui.page_pc_stats_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pc_statistics))
		self.ui.page_profile_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.profile))
		self.ui.page_login_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.login))
		self.ui.page_settings_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.settings))



		# stop video feed
		self.ui.pushButton_6.clicked.connect(lambda: self.STOPClicked())

		#camera changing
		self.ui.cam_button_1.clicked.connect(lambda: self.camera_management(0))
		self.ui.cam_button_2.clicked.connect(lambda: self.camera_management(1))
		self.ui.cam_button_3.clicked.connect(lambda: self.camera_management(2))
		self.ui.cam_button_4.clicked.connect(lambda: self.camera_management(3))

		#filter buttons
		self.ui.pushButton_13.clicked.connect(lambda: self.back_to_normal())
		self.ui.dehazer_low_button.clicked.connect(lambda: self.dehaze_low_button())
		self.ui.dehazer_high_button.clicked.connect(lambda: self.dehaze_high_button())
		self.ui.lle_high_button.clicked.connect(lambda: self.lle_high_button())
		self.ui.lle_low_button.clicked.connect(lambda: self.lle_low_button())
		self.ui.derainer_low_button.clicked.connect(lambda: self.derain_low_button())

		#vdb buttons
		self.ui.btn_open_video.clicked.connect(lambda: self.btn_open_video_clicked())
		self.ui.btn_play_pause.clicked.connect(lambda: self.play_video_button())

		#human_movement_detection buttons
		self.ui.pushButton_14.clicked.connect(lambda: self.camera_management_detect(0))
		self.ui.pushButton_15.clicked.connect(lambda: self.camera_management_detect(3))
		self.ui.pushButton_16.clicked.connect(lambda: self.camera_management_detect(1))
		self.ui.pushButton_17.clicked.connect(lambda: self.camera_management_detect(2))

		self.ui.pushButton_18.clicked.connect(lambda: self.det_stop_button())
		self.ui.start_detecting_btn_1.clicked.connect(lambda: self.mov_human_management())
		self.ui.human_det_btn_1.clicked.connect(lambda: self.set_human())
		self.ui.mov_det_btn_1.clicked.connect(lambda: self.set_movement())

		#home page buttons
		self.ui.pushButton_9.clicked.connect(lambda: self.open_website())
		self.ui.pushButton_11.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.cameras))
		self.ui.pushButton_12.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.cameras))
		self.ui.pushButton_10.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.cameras))

		#change theme buttons
		self.ui.pushButton_19.clicked.connect(lambda: self.dark_thene())
		self.ui.pushButton_20.clicked.connect(lambda: self.light_thene())

		

		#move window
		def moveWindow(e):
			if self.isMaximized() == False:
				if e.buttons() == Qt.LeftButton:
					self.move(self.pos() + e.globalPos() - self.clickPosition)
					self.clickPosition = e.globalPos()
					e.accept()

		#Grip
		QSizeGrip(self.ui.size_grip)
		#Move Window
		self.ui.header_frame.mouseMoveEvent = moveWindow
		#Menu button movement
		self.ui.open_close_side_bar_btn.clicked.connect(lambda: self.slideLeftMenu())

		#start thread

		self.show()
		#self.show_time()
		#self.threadpool = QThreadPool()
		#self.psutil_thread()

	def psutil_thread(self):
		date_worker = Worker(self.show_time)
		date_worker.signals.result.connect(self.print_output)
		date_worker.signals.finished.connect(self.thread_complete)
		date_worker.signals.progress.connect(self.progress_fn)
		self.threadpool.start(date_worker)

########################################################################
## LOGIN LOGOUT FUNCTIONS
########################################################################
	def loginunlock(self):
			self.ui.page_home_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home))
			self.ui.page_camera_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.cameras))
			self.ui.page_intrusion_det_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.intrusion_detection))
			self.ui.page_database_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.video_database))
			#self.ui.page_analytics_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.analytics))
			self.ui.page_pc_stats_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pc_statistics))
			self.ui.page_profile_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.profile))
			self.ui.page_login_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.login))
			self.ui.page_settings_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.settings))
			#self.ui.page_all_feeds_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.all_cameras_page))


	def logoutend(self):
		QMessageBox.information(self,"Logout output","Logged out")
		self.ui.stackedWidget.setCurrentWidget(self.ui.login)
		self.ui.page_home_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.login))
		self.ui.page_camera_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.login))
		self.ui.page_intrusion_det_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.login))
		self.ui.page_database_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.login))
		#self.ui.page_analytics_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.login))
		self.ui.page_pc_stats_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.login))
		self.ui.page_profile_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.login))
		self.ui.page_login_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.login))
		self.ui.page_settings_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.login))
		#self.ui.page_all_feeds_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.login))

    
########################################################################
## VDB RELATED FUNCTIONS
########################################################################
	global fileName
	fileName = 'none'

	def change_image(self, frame):
		frame_r = frame
		qformat = QImage.Format_Indexed8
		if len(frame_r.shape) == 3:
			if (frame_r.shape[2]) == 4:
				qformat = QImage.Format_RGBA888
			else:
				qformat = QImage.Format_RGB888
		img = QImage(frame_r, frame_r.shape[1], frame_r.shape[0], qformat)
		img = img.rgbSwapped()
		return img

	def btn_open_video_clicked(self):
		global fileName
		self.logic = 1
		camera_number = 0
		fileName, _ = qtw.QFileDialog.getOpenFileName(caption="Open Video", directory="./Recorded/", filter="Image Files (*.avi *.mp4)")
		print(fileName)
		cap = cv.VideoCapture(fileName)
		#while(cap.isOpened()):
		ret, frame = cap.read()
		if ret == True:
			img = self.change_image(frame)
			self.ui.lbl_frame.setPixmap(QPixmap.fromImage(img))
				# cv.waitKey()
			# if (self.logic == 1):
			#   pass
			# if (self.logic == 0):
			#   break
		else:
			print("return not found")
		#cap.release()
		#cv.destroyAllWindows()

	def play_video_button(self):
		global fileName
		self.logic = 1
		cap = cv.VideoCapture(fileName)
		while(cap.isOpened()):
			ret, frame = cap.read()
			if ret == True:
				img = self.change_image(frame)
				self.ui.lbl_frame.setPixmap(QPixmap.fromImage(img))
				cv.waitKey()
				if (self.logic == 1):
					pass
				if (self.logic == 0):
					break
			else:
				print("return not found")
				cap.release()
				cv.destroyAllWindows()

	def displayNormalImage2(self, frame, window = 1):
		frame_r = frame
		qformat = QImage.Format_Indexed8
		if len(frame_r.shape) == 3:
			if (frame_r.shape[2]) == 4:
				qformat = QImage.Format_RGBA888
			else:
				qformat = QImage.Format_RGB888
		img = QImage(frame_r, frame_r.shape[1], frame_r.shape[0], qformat)
		img = img.rgbSwapped()
		self.ui.lbl_frame.setPixmap(QPixmap.fromImage(img))


########################################################################
## WINDOW RELATED FUNCTIONS
########################################################################
	def print_output(self, s):
		print(s)

	def thread_complete(self):
		print("THREAD COMPLETE!")
   
	def progress_fn(self, n):
		# n = progress value
		print("%d%% done" % n)

	def restore_or_maximize_window(self):
		if self.isMaximized():
			self.showNormal()
		else:
			self.showMaximized()
	

	def mousePressEvent(self, event):
		self.clickPosition = event.globalPos()
	
	def Login(self):
		un= self.ui.tb1.text()
		pw= self.ui.tb2.text()
		db= con.connect(host= "localhost",user="root",password="",db="userprofiling")
		cursor= db.cursor()
		cursor.execute("select * from userlist where username= '"+ un +"' and password= '"+ pw +"'")
		result= cursor.fetchone()
		self.ui.tb2.setText("")
		if result:
			QMessageBox.information(self,"Login Output", "Login Sucessful")
			self.loginunlock()
			self.ui.stackedWidget.setCurrentWidget(self.ui.profile)
			self.ui.pushButton_8.setText(un)
			self.ui.welcome.setText("Welcome, " + un.capitalize())
			cursor.execute("select username from userlist where username='"+un+"'")
			result=cursor.fetchone()
			pusername= str(result)
			self.ui.userlabel.setText("USERNAME: " + pusername[2:len(pusername)-3])
			cursor.execute("select email from userlist where username='"+un+"'")
			result=cursor.fetchone()
			pemail= str(result)
			self.ui.emaillabel.setText("EMAIL: " + pemail[2:len(pemail)-3])
			cursor.execute("select phonenumber from userlist where username='"+un+"'")
			result=cursor.fetchone()
			pphonenumber= str(result)
			self.ui.phonelabel.setText("PHONE NUMBER: " + pphonenumber[2:len(pphonenumber)-3])



			
			
		else:
			QMessageBox.information(self,"Login Output","Invalid Username or Password!")

	def Registration(self):
		un=self.ui.username.text()
		pw= self.ui.password.text()
		em= self.ui.email.text()
		ph= self.ui.phonenumber.text()

		db= con.connect(host= "localhost",user="root",password="",db="userprofiling")
		cursor= db.cursor()
		cursor.execute("select * from userlist where username='" + un +"'")
		result = cursor.fetchone()
		if result:
			QMessageBox.information(self, "Login Form","User Registered already")
		else:
			regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
			if(re.fullmatch(regex, em)):
				if(len(ph)==11):
					cursor.execute("insert into userlist values('"+ un +"','"+ pw +"','"+ em +"','"+ ph +"')")
					db.commit()
					QMessageBox.information(self,"Login form","User Registered sucessfully")
					self.ui.username.setText("")
					self.ui.password.setText("")
					self.ui.email.setText("")
					self.ui.phonenumber.setText("")
				else:
					QMessageBox.information(self,"Login form","Please Enter Valid Phone Number")	
			else:
				QMessageBox.information(self,"Login form","Enter Email Correctly")

	def Adminfeedback(self):
		fb= self.ui.feedback.text()
		unfb= self.ui.tb1.text()
		db= con.connect(host= "localhost",user="root",password="",db="userprofiling")
		cursor= db.cursor()
		cursor.execute("insert into admin values('"+ unfb +"','"+ fb +"')")
		db.commit()
		QMessageBox.information(self,"Feedback","Thank you for your feedback!")
		self.ui.feedback.setText("")





	def slideLeftMenu(self):
		width = self.ui.side_menu_frame.width()
		if width == 50:
			newWidth = 200
		else:
			newWidth = 50

		self.animation = QPropertyAnimation(self.ui.side_menu_frame, b"minimumWidth")
		self.animation.setDuration(250)
		self.animation.setStartValue(width)#Start value is the current menu width
		self.animation.setEndValue(newWidth)#end value is the new menu width
		self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
		self.animation.start()
	def show_time(self, progress_callback ):
		date = datetime.datetime.now()
		status = str(date.day) + "-" + str(date.month) + "-" + str(date.year) + " Time: " + str(date.hour) + " : " + str(date.minute) + " : " + str(date.second)
		self.ui.time_browser_text.setText(status)
		#sleep(1)

########################################################################
##  Camera Related - Filters Page
########################################################################

	def camera_management(self, cm_number):
		date = datetime.datetime.now()
		self.logic = 1
		cap = cv.VideoCapture(0)
		cap2 = cv.VideoCapture(1)
		cap3 = cv.VideoCapture(2)
		cap4 = cv.VideoCapture(3)

		frame_width1 = int(cap.get(3))
		frame_height1 = int(cap.get(4))

		frame_width2 = int(cap2.get(3))
		frame_height2 = int(cap2.get(4))

		frame_width3 = int(cap3.get(3))
		frame_height3 = int(cap3.get(4))

		frame_width4 = int(cap4.get(3))
		frame_height4 = int(cap4.get(4))

		# out1 = cv.VideoWriter('.\\Recorded\\Camera1\\cctv_%s_%s_%s_%s_%s_%s.mp4'%(date.year, date.month, date.day, date.hour, date.minute, date.second),cv.VideoWriter_fourcc ('M', 'J', 'P', 'G'), 20.0 , (frame_width1, frame_height1) )
		# out2 = cv.VideoWriter('.\\Recorded\\Camera2\\cctv_%s_%s_%s_%s_%s_%s.mp4'%(date.year, date.month, date.day, date.hour, date.minute, date.second),cv.VideoWriter_fourcc ('M', 'J', 'P', 'G'), 20.0 , (frame_width2, frame_height2) )
		# out3 = cv.VideoWriter('.\\Recorded\\Camera3\\cctv_%s_%s_%s_%s_%s_%s.mp4'%(date.year, date.month, date.day, date.hour, date.minute, date.second),cv.VideoWriter_fourcc ('M', 'J', 'P', 'G'), 20.0 , (frame_width3, frame_height3) )
		# out4 = cv.VideoWriter('.\\Recorded\\Camera4\\cctv_%s_%s_%s_%s_%s_%s.mp4'%(date.year, date.month, date.day, date.hour, date.minute, date.second),cv.VideoWriter_fourcc ('M', 'J', 'P', 'G'), 20.0 , (frame_width4, frame_height4) )
		
		if cm_number == 0:
			out1 = cv.VideoWriter('.\\Recorded\\Camera1\\cctv_%s_%s_%s_%s_%s_%s.mp4'%(date.year, date.month, date.day, date.hour, date.minute, date.second),cv.VideoWriter_fourcc ('M', 'J', 'P', 'G'), 20.0 , (frame_width1, frame_height1) )
			while(cap.isOpened()):
				ret, frame = cap.read()
				if ret == True:
					print(filterValue)
					if filterValue == 1:
						self.display_dehaze_low(out1, frame, 1)
					elif filterValue == 2:
						self.diplay_dehaze_high(out1, frame, 1)
					elif filterValue == 3:
						self.display_lle_low(out1, frame, 1)
					elif filterValue == 4:
						self.display_lle_high(out1, frame, 1)
					elif filterValue == 5:
						self.display_derain_low(out1, frame, 1)
					else:
						self.displayNormalImage(out1, frame, 1)
					cv.waitKey()
					if (self.logic == 1):
						pass
					if (self.logic == 0):
						break
				else:
					print("return not found")
			cap.release()
			cv.destroyAllWindows()
		elif cm_number == 1:
			out2 = cv.VideoWriter('.\\Recorded\\Camera2\\cctv_%s_%s_%s_%s_%s_%s.mp4'%(date.year, date.month, date.day, date.hour, date.minute, date.second),cv.VideoWriter_fourcc ('M', 'J', 'P', 'G'), 20.0 , (frame_width2, frame_height2) )
			while(cap2.isOpened()):
				ret, frame = cap2.read()
				if ret == True:
					print(filterValue)
					if filterValue == 1:
						self.display_dehaze_low(out2,frame, 1)
					elif filterValue == 2:
						self.diplay_dehaze_high(out2,frame, 1)
					elif filterValue == 3:
						self.display_lle_low(out2,frame, 1)
					elif filterValue == 4:
						self.display_lle_high(out2,frame, 1)
					elif filterValue == 5:
						self.display_derain_low(out2, frame, 1)
					else:
						self.displayNormalImage(out2,frame, 1)
					cv.waitKey()
					if (self.logic == 1):
						pass
					if (self.logic == 0):
						break
				else:
					print("return not found")
			cap.release()
			cv.destroyAllWindows()
		elif cm_number == 2:
			out3 = cv.VideoWriter('.\\Recorded\\Camera3\\cctv_%s_%s_%s_%s_%s_%s.mp4'%(date.year, date.month, date.day, date.hour, date.minute, date.second),cv.VideoWriter_fourcc ('M', 'J', 'P', 'G'), 20.0 , (frame_width3, frame_height3) )
			while(cap3.isOpened()):
				ret, frame = cap3.read()
				if ret == True:
					print(filterValue)
					if filterValue == 1:
						self.display_dehaze_low(out3,frame, 1)
					elif filterValue == 2:
						self.diplay_dehaze_high(out3,frame, 1)
					elif filterValue == 3:
						self.display_lle_low(out3,frame, 1)
					elif filterValue == 4:
						self.display_lle_high(out3,frame, 1)
					elif filterValue == 5:
						self.display_derain_low(out3, frame, 1)
					else:
						self.displayNormalImage(out3,frame, 1)
					cv.waitKey()
					if (self.logic == 1):
						pass
					if (self.logic == 0):
						break
				else:
					print("return not found")
			cap.release()
			cv.destroyAllWindows()
		elif cm_number == 3:
			out4 = cv.VideoWriter('.\\Recorded\\Camera4\\cctv_%s_%s_%s_%s_%s_%s.mp4'%(date.year, date.month, date.day, date.hour, date.minute, date.second),cv.VideoWriter_fourcc ('M', 'J', 'P', 'G'), 20.0 , (frame_width4, frame_height4) )
			while(cap4.isOpened()):
				ret, frame = cap4.read()
				if ret == True:
					print(filterValue)
					if filterValue == 1:
						self.display_dehaze_low(out4,frame, 1)
					elif filterValue == 2:
						self.diplay_dehaze_high(out4,frame, 1)
					elif filterValue == 3:
						self.display_lle_low(out4,frame, 1)
					elif filterValue == 4:
						self.display_lle_high(out4,frame, 1)
					elif filterValue == 5:
						self.display_derain_low(out4, frame, 1)
					else:
						self.displayNormalImage(out4,frame, 1)
					cv.waitKey()
					if (self.logic == 1):
						pass
					if (self.logic == 0):
						break
				else:
					print("return not found")
			cap.release()
			cv.destroyAllWindows()


	def STARTClicked(self):
		self.logic = 1
		op_scrn_w = self.ui.output_screen.width()
		op_scrn_h = self.ui.output_screen.height()
		print(op_scrn_w, op_scrn_h)
		cap = cv.VideoCapture(1)
		frame_width = int(cap.get(3))
		frame_height = int(cap.get(4))
		print(frame_width, frame_height)

		while(cap.isOpened()):
			ret, frame = cap.read()
			if ret == True:
				self.displayNormalImage(frame, 1)
				cv.waitKey()
				if (self.logic == 1):
					pass
				if (self.logic == 0):
					break
			else:
				print("return not found")
		cap.release()
		cv.destroyAllWindows()

	def STOPClicked(self):
		self.logic = 0

########################################################################
## Surviellance related functions
########################################################################

	
	def det_stop_button(self):
			self.logic_det = 0
			self.ui.mov_det_btn_1.setStyleSheet(u"background-color:rgb(85, 100, 109);\n"
												"color: rgb(255,255,255);\n"
												"border-radius: 5;\n"
												"\n"
												"")
			self.ui.human_det_btn_1.setStyleSheet(u"background-color:rgb(85, 100, 109);\n"
												"color: rgb(255,255,255);\n"
												"border-radius: 5;\n"
												"\n"
												"")

			self.ui.start_detecting_btn_1.setStyleSheet(u"background-color:rgb(122, 21, 0);\n"
												"color: rgb(255,255,255);\n"
												"border-radius: 5;\n"
												"\n"
												"")

			self.ui.intrusion_detection.setStyleSheet(u"color: rgb(255,255,255)")

			global send_once
			send_once = 0
			global alert_once 
			alert_once = 0

	def displayNormalImage_detect(self, frame, window = 1):
		frame_r = frame
		qformat = QImage.Format_Indexed8
		if len(frame_r.shape) == 3:
			if (frame_r.shape[2]) == 4:
				qformat = QImage.Format_RGBA888
			else:
				qformat = QImage.Format_RGB888
		img = QImage(frame_r, frame_r.shape[1], frame_r.shape[0], qformat)
		img = img.rgbSwapped()
		self.ui.surviellance_op_1.setPixmap(QPixmap.fromImage(img))

	global detecttrue 
	detecttrue = 0

	global toggledetect
	toggledetect = 0

	global movement
	movement = 0

	global human
	human = 0

	def set_human(self):
		global human 
		global movement
		human = 1
		movement = 0
		self.ui.human_det_btn_1.setStyleSheet(u"background-color:rgb(0, 255, 0);\n"
												"color: rgb(255,255,255);\n"
												"border-radius: 5;\n"
												"\n"
												"")

		self.ui.mov_det_btn_1.setStyleSheet(u"background-color:rgb(85, 100, 109);\n"
												"color: rgb(255,255,255);\n"
												"border-radius: 5;\n"
												"\n"
												"")

		self.ui.start_detecting_btn_1.setStyleSheet(u"background-color:rgb(122, 21, 0);\n"
												"color: rgb(255,255,255);\n"
												"border-radius: 5;\n"
												"\n"
												"")

	def set_movement(self):
		global human
		global movement
		human = 0
		movement = 1

		self.ui.mov_det_btn_1.setStyleSheet(u"background-color:rgb(0, 255, 0);\n"
												"color: rgb(255,255,255);\n"
												"border-radius: 5;\n"
												"\n"
												"")

		self.ui.human_det_btn_1.setStyleSheet(u"background-color:rgb(85, 100, 109);\n"
												"color: rgb(255,255,255);\n"
												"border-radius: 5;\n"
												"\n"
												"")

		self.ui.start_detecting_btn_1.setStyleSheet(u"background-color:rgb(122, 21, 0);\n"
												"color: rgb(255,255,255);\n"
												"border-radius: 5;\n"
												"\n"
												"")

	def mov_human_management(self):
		global human
		global movement
		global detecttrue

		self.ui.start_detecting_btn_1.setStyleSheet(u"background-color:rgb(0, 0, 255);\n"
												"color: rgb(255,255,255);\n"
												"border-radius: 5;\n"
												"\n"
												"")
		if human == 1:
			detecttrue = 1
		elif movement == 1:
			detecttrue = 2
		else:
			detecttrue = 0

		val = self.ui.start_time_1.dateTime()
		dt_string = val.toString(self.ui.start_time_1.displayFormat())
		print(dt_string.split(" ")[0])

		date = datetime.datetime.now()
		print(date)
		#print(val)

	# def setdetectvalue(self):
	# 	global detecttrue 
	# 	global toggledetect
	# 	if (toggledetect == 0):
	# 		detecttrue = 1
	# 		toggledetect = 1
	# 	else:
	# 		detecttrue = 0
	# 		toggledetect = 0

	global send_once
	send_once = 0

	global alert_once
	alert_once = 0

	def start_detecting(self, cm_number,  frame):
		global send_once
		date = datetime.datetime.now()
		checkt = 0
		ClassIndex,confidece, bbox = human_model.detect(frame, confThreshold= 0.5)
		if(len(ClassIndex)!=0):
			for ClassInd, conf, boxes in zip(ClassIndex.flatten(),confidece.flatten(),bbox):
				if(ClassInd<= 80):
					if (labellist[ClassInd-1] == 'person'):
						self.ui.intrusion_detection.setStyleSheet(u"color: rgb(255,255,255);\n"
																"background-color: rgb(150, 0, 0);\n")
						f = open("IntrusionDetection.txt", "a")
						if cm_number == 0:
							status = "Intrusion Detected at Cam 1: " + "(" + str(date.day) + "-" + str(date.month) + "-" + str(date.year) + ") Time: " + str(date.hour) + " : " + str(date.minute) + " : " + str(date.second)
						elif cm_number == 1: 
							status = "Intrusion Detected at Cam 2: " + "(" + str(date.day) + "-" + str(date.month) + "-" + str(date.year) + ") Time: " + str(date.hour) + " : " + str(date.minute) + " : " + str(date.second)
						elif cm_number == 2: 
							status = "Intrusion Detected at Cam 3: " + "(" + str(date.day) + "-" + str(date.month) + "-" + str(date.year) + ") Time: " + str(date.hour) + " : " + str(date.minute) + " : " + str(date.second)
						elif cm_number == 3: 
							status = "Intrusion Detected at Cam 4: " + "(" + str(date.day) + "-" + str(date.month) + "-" + str(date.year) + ") Time: " + str(date.hour) + " : " + str(date.minute) + " : " + str(date.second)

						# if send_once == 0:
						# 	telegram_send.send(messages=[status])
						# 	send_once = 1
						st = status + "\n"
						if checkt != date.second:
							f.write(st)
							f.close()
							checkt = date.second
						self.ui.textBrowser_2.setText(status)
					else:
						self.ui.intrusion_detection.setStyleSheet(u"color: rgb(255,255,255)")


	global firstFrame
	firstFrame = None
	def start_movement_detection(self, frame):
		global alert_once
		global firstFrame
		text = "Unoccupied"

		gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
		gray = cv.GaussianBlur(gray, (21, 21), 0)

		if firstFrame is None:
			firstFrame = gray
			#continue
		
		frameDelta = cv.absdiff(firstFrame, gray)
		thresh = cv.threshold(frameDelta, 25, 255, cv.THRESH_BINARY)[1]
		thresh = cv.dilate(thresh, None, iterations=2)
		cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)

		for c in cnts:
			if cv.contourArea(c) < 2000:
				self.ui.intrusion_detection.setStyleSheet(u"color: rgb(255,255,255)")
			else:
				self.ui.intrusion_detection.setStyleSheet(u"color: rgb(255,255,255);\n"
																"background-color: rgb(150, 0, 0);\n")
				if alert_once == 0:
					winsound.PlaySound('alert.wav', winsound.SND_FILENAME) 
					alert_once = 1
			(x, y, w, h) = cv.boundingRect(c)
			cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
			text = "INTRUSION"


		cv.putText(frame, "Room Status: {}".format(text), (10, 20),cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
		cv.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),(10, frame.shape[0] - 10), cv.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
		frame_r = frame
		qformat = QImage.Format_Indexed8
		if len(frame_r.shape) == 3:
			if (frame_r.shape[2]) == 4:
				qformat = QImage.Format_RGBA888
			else:
				qformat = QImage.Format_RGB888
		img = QImage(frame_r, frame_r.shape[1], frame_r.shape[0], qformat)
		img = img.rgbSwapped()
		self.ui.surviellance_op_1.setPixmap(QPixmap.fromImage(img))

		
	def camera_management_detect(self, cm_number):
		self.logic_det = 1
		cap = cv.VideoCapture(0)
		cap2 = cv.VideoCapture(1)
		cap3 = cv.VideoCapture(2)
		cap4 = cv.VideoCapture(3)

		if cm_number == 0:
			while(cap.isOpened()):
				ret, frame = cap.read()
				if ret == True:
					if detecttrue == 0:
						self.displayNormalImage_detect(frame, 1)
					elif (detecttrue == 1):
						self.displayNormalImage_detect(frame, 1)
						self.start_detecting(cm_number, frame)
					elif (detecttrue == 2):
						self.start_movement_detection(frame)
					cv.waitKey()
					if (self.logic_det == 1):
						pass
					if (self.logic_det == 0):
						break
				else:
					print("return not found")
			cap.release()
			cv.destroyAllWindows()

		elif cm_number == 1:
			while(cap2.isOpened()):
				ret, frame = cap2.read()
				if ret == True:
					if detecttrue == 0:
						self.displayNormalImage_detect(frame, 1)
					elif (detecttrue == 1):
						self.displayNormalImage_detect(frame, 1)
						self.start_detecting(cm_number, frame)
					elif (detecttrue == 2):
						self.start_movement_detection(frame)
					cv.waitKey()
					if (self.logic_det == 1):
						pass
					if (self.logic_det == 0):
						break
				else:
					print("return not found")
			cap.release()
			cv.destroyAllWindows()
		elif cm_number == 2:
			while(cap3.isOpened()):
				ret, frame = cap3.read()
				if ret == True:
					if detecttrue == 0:
						self.displayNormalImage_detect(frame, 1)
					elif (detecttrue == 1):
						self.displayNormalImage_detect(frame, 1)
						self.start_detecting(cm_number, frame)
					elif (detecttrue == 2):
						self.start_movement_detection(frame)
					cv.waitKey()
					if (self.logic_det == 1):
						pass
					if (self.logic_det == 0):
						break
				else:
					print("return not found")
			cap.release()
			cv.destroyAllWindows()
		elif cm_number == 3:
			while(cap4.isOpened()):
				ret, frame = cap4.read()
				if ret == True:
					if detecttrue == 0:
						self.displayNormalImage_detect(frame, 1)
					elif (detecttrue == 1):
						self.displayNormalImage_detect(frame, 1)
						self.start_detecting(cm_number, frame)
					elif (detecttrue == 2):
						self.start_movement_detection(frame)
					cv.waitKey()
					if (self.logic_det == 1):
						pass
					if (self.logic_det == 0):
						break
				else:
					print("return not found")
			cap.release()
			cv.destroyAllWindows()






########################################################################
## FEED OUTPUTS ---- APPLYING MODELS
########################################################################

	################## Normal Image ########################
	def displayNormalImage(self,out, frame, window = 1):
		frame_r = frame
		out.write(frame_r)
		qformat = QImage.Format_Indexed8
		if len(frame_r.shape) == 3:
			if (frame_r.shape[2]) == 4:
				qformat = QImage.Format_RGBA888
			else:
				qformat = QImage.Format_RGB888
		img = QImage(frame_r, frame_r.shape[1], frame_r.shape[0], qformat)
		img = img.rgbSwapped()
		self.ui.output_screen.setPixmap(QPixmap.fromImage(img))

	################ DEHAZING #############################3

	def display_derain_low(self,out, img, window = 1 ):
		frame_p = img
		#-----------FOR NET PASSING---------
		frame_tensor = tf.convert_to_tensor(frame_p)
		temp_zero = frame_tensor.shape[0]
		temp_one = frame_tensor.shape[1]
		frame_tensor = tf.image.resize(frame_tensor, size = (480, 640), antialias = True)

		frame_tensor = frame_tensor / 255.0
		frame_tensor = tf.expand_dims(frame_tensor, axis = 0) 
		dehaze = derainer_model(frame_tensor, training = False)
		dehaze = tf.image.resize(dehaze, size = (temp_zero, temp_one), antialias = True)
		
		d_op = dehaze[0].numpy()
		d_op *= 255/d_op.max() 
		d_op = np.array(d_op, np.uint8)
		#--------------------------------------------
		out.write(d_op)
		frame_r = d_op
		qformat = QImage.Format_Indexed8

		if len(frame_r.shape) ==3:
			if (frame_r.shape[2])==4:
				qformat=QImage.Format_RGBA888
			else:
				qformat= QImage.Format_RGB888

		img2 = QImage(frame_r,frame_r.shape[1], frame_r.shape[0], qformat)
		img2 = img2.rgbSwapped()
		self.ui.output_screen.setPixmap(QPixmap.fromImage(img2))


	def display_dehaze_low(self,out, img, window = 1 ):
		frame_p = img
		#-----------FOR NET PASSING---------
		frame_tensor = tf.convert_to_tensor(frame_p)
		temp_zero = frame_tensor.shape[0]
		temp_one = frame_tensor.shape[1]
		frame_tensor = tf.image.resize(frame_tensor, size = (480, 640), antialias = True)

		frame_tensor = frame_tensor / 255.0
		frame_tensor = tf.expand_dims(frame_tensor, axis = 0) 
		dehaze = dehazer_model(frame_tensor, training = False)
		dehaze = tf.image.resize(dehaze, size = (temp_zero, temp_one), antialias = True)
		
		d_op = dehaze[0].numpy()
		d_op *= 255/d_op.max() 
		d_op = np.array(d_op, np.uint8)
		#--------------------------------------------
		out.write(d_op)
		frame_r = d_op
		qformat = QImage.Format_Indexed8

		if len(frame_r.shape) ==3:
			if (frame_r.shape[2])==4:
				qformat=QImage.Format_RGBA888
			else:
				qformat= QImage.Format_RGB888

		img2 = QImage(frame_r,frame_r.shape[1], frame_r.shape[0], qformat)
		img2 = img2.rgbSwapped()
		self.ui.output_screen.setPixmap(QPixmap.fromImage(img2))

	def diplay_dehaze_high(self,out, frame, window = 1):
		frame_p = frame

		#-----------FOR NET PASSING---------
		frame_tensor = tf.convert_to_tensor(frame_p)
		temp_zero = frame_tensor.shape[0]
		temp_one = frame_tensor.shape[1]
		frame_tensor = tf.image.resize(frame_tensor, size = (480, 640), antialias = True)

		frame_tensor = frame_tensor / 255.0
		frame_tensor = tf.expand_dims(frame_tensor, axis = 0) 
		dehaze = dehazer_model(frame_tensor, training = False)
		dehaze = tf.image.resize(dehaze, size = (temp_zero, temp_one), antialias = True)
		
		d_op = dehaze[0].numpy()
		d_op *= 255/d_op.max() 
		d_op = np.array(d_op, np.uint8)
		#--------------------------------------------
		#-----------Second net passing---------------
		frame_p = d_op
		frame_tensor = tf.convert_to_tensor(frame_p)
		temp_zero = frame_tensor.shape[0]
		temp_one = frame_tensor.shape[1]
		frame_tensor = tf.image.resize(frame_tensor, size = (480, 640), antialias = True)

		frame_tensor = frame_tensor / 255.0
		frame_tensor = tf.expand_dims(frame_tensor, axis = 0) 
		dehaze = dehazer_model(frame_tensor, training = False)
		dehaze = tf.image.resize(dehaze, size = (temp_zero, temp_one), antialias = True)
		
		d_op = dehaze[0].numpy()
		d_op *= 255/d_op.max() 
		d_op = np.array(d_op, np.uint8)
		#--------------------------------------------
		out.write(d_op)

		frame_r = d_op
		qformat = QImage.Format_Indexed8

		if len(frame_r.shape) ==3:
			if (frame_r.shape[2])==4:
				qformat=QImage.Format_RGBA888
			else:
				qformat= QImage.Format_RGB888

		img= QImage(frame_r,frame_r.shape[1], frame_r.shape[0], qformat)
		img= img.rgbSwapped()
		self.ui.output_screen.setPixmap(QPixmap.fromImage(img))

	################## low light enhancement ##############################
	def display_lle_high(self,out, img, window=1):
		o_i = Image.fromarray((img))
		original_size = (np.array(o_i).shape[1], np.array(o_i).shape[0])
		original_img = o_i.resize((512,512), Image.ANTIALIAS) 
		original_img = (np.asarray(original_img)/255.0)

		img_lowlight = o_i.resize((512,512), Image.ANTIALIAS)
		img_lowlight = (np.asarray(img_lowlight)/255.0) 
		img_lowlight = np.expand_dims(img_lowlight, 0)
	 
		A = lle_model.predict(img_lowlight)
		r1, r2, r3, r4, r5, r6, r7, r8 = A[:,:,:,:3], A[:,:,:,3:6], A[:,:,:,6:9], A[:,:,:,9:12], A[:,:,:,12:15], A[:,:,:,15:18], A[:,:,:,18:21], A[:,:,:,21:24]
		x = original_img + r1 * (K.pow(original_img,2)-original_img)
		x = x + r2 * (K.pow(x,2)-x)
		x = x + r3 * (K.pow(x,2)-x)
		enhanced_image_1 = x + r4*(K.pow(x,2)-x)
		x = enhanced_image_1 + r5*(K.pow(enhanced_image_1,2)-enhanced_image_1)      
		x = x + r6*(K.pow(x,2)-x)   
		x = x + r7*(K.pow(x,2)-x)
		enhance_image = x + r8*(K.pow(x,2)-x)

		enhance_image = tf.cast((enhance_image[0,:,:,:] * 255), dtype=np.uint8)
		enhance_image = Image.fromarray(enhance_image.numpy())
		enhance_image = enhance_image.resize(original_size, Image.ANTIALIAS)
		enhance_image = np.array(enhance_image)

		#process image again#
		again_image = enhance_image

		original_img2 = Image.fromarray((again_image))
		original_size2 = (np.array(original_img2).shape[1], np.array(original_img2).shape[0])
		original_img2 = original_img2.resize((512,512), Image.ANTIALIAS) 
		original_img2 = (np.asarray(original_img2)/255.0)

		img_lowlight2 = Image.fromarray(again_image)   
		img_lowlight2 = img_lowlight2.resize((512,512), Image.ANTIALIAS)
		img_lowlight2 = (np.asarray(img_lowlight2)/255.0) 
		img_lowlight2 = np.expand_dims(img_lowlight2, 0)


		A2 = lle_model.predict(img_lowlight2)
		r1, r2, r3, r4, r5, r6, r7, r8 = A2[:,:,:,:3], A2[:,:,:,3:6], A2[:,:,:,6:9], A2[:,:,:,9:12], A2[:,:,:,12:15], A2[:,:,:,15:18], A2[:,:,:,18:21], A2[:,:,:,21:24]
		x = original_img2 + r1 * (K.pow(original_img2,2)-original_img2)
		x = x + r2 * (K.pow(x,2)-x)
		x = x + r3 * (K.pow(x,2)-x)
		enhanced_image_2 = x + r4*(K.pow(x,2)-x)
		x = enhanced_image_2 + r5*(K.pow(enhanced_image_2,2)-enhanced_image_2)      
		x = x + r6*(K.pow(x,2)-x)   
		x = x + r7*(K.pow(x,2)-x)
		enhance_image2 = x + r8*(K.pow(x,2)-x)
		enhance_image2 = tf.cast((enhance_image2[0,:,:,:] * 255), dtype=np.uint8)
		enhance_image2 = Image.fromarray(enhance_image2.numpy())
		enhance_image2 = enhance_image2.resize(original_size2, Image.ANTIALIAS)
		enhance_image2 = np.array(enhance_image2)
		frame_r = enhance_image2
		out.write(enhance_image2)

		qformat = QImage.Format_Indexed8
		#print(type(frame_r))
		if len(frame_r.shape) ==3:
			if (frame_r.shape[2])==4:
				qformat=QImage.Format_RGBA888
			else:
				qformat= QImage.Format_RGB888

		img= QImage(frame_r,frame_r.shape[1], frame_r.shape[0], qformat)
		img= img.rgbSwapped()

		self.ui.output_screen.setPixmap(QPixmap.fromImage(img))


	def display_lle_low(self,out, img, window=1):
		o_i = Image.fromarray((img))
		original_size = (np.array(o_i).shape[1], np.array(o_i).shape[0])
		original_img = o_i.resize((512,512), Image.ANTIALIAS) 
		original_img = (np.asarray(original_img)/255.0)

		img_lowlight = o_i.resize((512,512), Image.ANTIALIAS)
		img_lowlight = (np.asarray(img_lowlight)/255.0) 
		img_lowlight = np.expand_dims(img_lowlight, 0)
	 
		A = lle_model.predict(img_lowlight)
		r1, r2, r3, r4, r5, r6, r7, r8 = A[:,:,:,:3], A[:,:,:,3:6], A[:,:,:,6:9], A[:,:,:,9:12], A[:,:,:,12:15], A[:,:,:,15:18], A[:,:,:,18:21], A[:,:,:,21:24]
		x = original_img + r1 * (K.pow(original_img,2)-original_img)
		x = x + r2 * (K.pow(x,2)-x)
		x = x + r3 * (K.pow(x,2)-x)
		enhanced_image_1 = x + r4*(K.pow(x,2)-x)
		x = enhanced_image_1 + r5*(K.pow(enhanced_image_1,2)-enhanced_image_1)      
		x = x + r6*(K.pow(x,2)-x)   
		x = x + r7*(K.pow(x,2)-x)
		enhance_image = x + r8*(K.pow(x,2)-x)

		enhance_image = tf.cast((enhance_image[0,:,:,:] * 255), dtype=np.uint8)
		enhance_image = Image.fromarray(enhance_image.numpy())
		enhance_image = enhance_image.resize(original_size, Image.ANTIALIAS)
		enhance_image = np.array(enhance_image)
		frame_r = enhance_image
		out.write(enhance_image)

		qformat = QImage.Format_Indexed8
		#print(type(frame_r))
		if len(frame_r.shape) ==3:
			if (frame_r.shape[2])==4:
				qformat=QImage.Format_RGBA888
			else:
				qformat= QImage.Format_RGB888

		img= QImage(frame_r,frame_r.shape[1], frame_r.shape[0], qformat)
		img= img.rgbSwapped()

		self.ui.output_screen.setPixmap(QPixmap.fromImage(img))

	####################### Deraining ################################

	
########################################################################
## Filter Buttons
########################################################################
	def dehaze_low_button(self):
		global filterValue
		filterValue = 1

	def dehaze_high_button(self):
		global filterValue
		filterValue = 2

	def lle_low_button(self):
		global filterValue
		filterValue = 3

	def lle_high_button(self):
		global filterValue
		filterValue = 4

	def derain_low_button(self):
		global filterValue
		filterValue = 5

	def back_to_normal(self):
		global filterValue
		filterValue = 0

########################################################################
## Home page
########################################################################

	def open_website(self):
		webbrowser.open('https://abdullahahsan68248.wixsite.com/vision-ai', new=2)

	def dark_thene(self):
		self.ui.centralwidget.setStyleSheet(u"\n"
				"background-color: rgb(39, 43, 54);\n"
				"")
		self.ui.header_frame.setStyleSheet(u"border:none;\n"
				"\n"
				"background-color: rgb(35, 32, 53)")
		self.ui.footer_frame.setStyleSheet(u"background-color: rgb(35, 32, 53);\n"
				"border:none;")
		self.ui.side_menu_frame.setStyleSheet(u"border:none;\n"
		"background-color: rgb(35, 32, 53)")

	def light_thene(self):
		self.ui.centralwidget.setStyleSheet(u"\n"
				"background-color: rgb(39, 200, 54);\n"
				"")
		self.ui.header_frame.setStyleSheet(u"border:none;\n"
				"\n"
				"background-color: rgb(35, 200, 53)")
		self.ui.footer_frame.setStyleSheet(u"background-color: rgb(200, 32, 53);\n"
				"border:none;")
		self.ui.side_menu_frame.setStyleSheet(u"border:none;\n"
		"background-color: rgb(35, 150, 53)")


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	sys.exit(app.exec_())