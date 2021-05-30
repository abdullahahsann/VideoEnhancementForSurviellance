import sys
import cv2
import datetime 
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
from PyQt5.QtGui import QImage , QPixmap
from PyQt5.QtWidgets import QDialog , QApplication
import ui_main
class tehseencode(QDialog):
    def __init__(self):
                super(tehseencode, self).__init__()
                loadUi('live_ui.ui', self)
                self.logic= 0

                self.START.clicked.connect(self.STARTClicked)

                self.TEXT.setText('Kindly press "start" to start recording')

                self.STOP.clicked.connect(self.STOPClicked)

    @pyqtSlot()
    def STARTClicked(self):
        self.logic=1
        cap = cv2.VideoCapture(1)
        date = datetime.datetime.now()
        out = cv2.VideoWriter('C:/Users/adil shamim/Desktop/python/video.mp4')
        print('here')
        while (cap.isOpened()):

            ret, frame = cap.read()
            if ret == True :

                self.displayImage(frame,1)
                cv2.waitkey()

                if (self.logic==1):
                    out.write(frame)
                

                    self.TEXT.setText('video recording start')
                if (self.logic==0):
                    self.TEXT.setText('video recording stop')

                    break
            else:
                print('return not found')
        cap.release()
        cv2.destroyAllWindows()

    def STOPClicked(self):
        self.logic=0
    
    def displayImage(self, img, window=1):
        qformat = QImage.Format_Indexed8

        if len(img.shape) ==3:

            if (img.shape[2])==4:
                qformat=QImage.Format_RGBA888
            else:
                qformat= QImage.format_RGB888
        img= QImage(img,img.shape[1], img.shape[0], qformat)
        img= img.rgbSwapped()


        self.imgLable.setPixmap(QPixmap.fromImage(img))

app = QApplication(sys.argv)
window=tehseencode()
window.show()
try:
    sys.exit(app.exec_())
except:
    print('exiting')








            
