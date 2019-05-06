from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox,QApplication
from PyQt5.QtGui import QPixmap, QPainter, QPen
from taskui import Ui_MainWindow
import sys
import PIL 
from PIL import Image, ImageEnhance
import numpy as np
from qimage2ndarray import gray2qimage, array2qimage
import pyqtgraph
from PIL import Image
import matplotlib.pyplot as plt
import math

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Browse.clicked.connect(self.browse)
        self.ui.FA.valueChanged.connect(self.FA)
        self.ui.TE.valueChanged.connect(self.TE)
        self.ui.TR.valueChanged.connect(self.TR)
        self.ui.SpanTime.valueChanged.connect(self.SpinTime)
        self.ui.PhantomSize.currentIndexChanged.connect(self.PhantomSize)
        self.ui.TissueProperty.currentIndexChanged.connect(self.TissueProperty)
        self.ui.kspace.clicked.connect(self.kspace)
        self.ui.Sliderb.valueChanged.connect(self.valuechangeb)
        self.ui.sliderc.valueChanged.connect(self.valuechangec)
        self.count=0

       
        
    def FA(self):
        global FA
        FA=self.ui.FA.value()
        
    def TE(self):
        global TE
        TE=self.ui.TE.value()
        
    def TR(self):
        global TR
        TR=self.ui.TR.value()
        
    def SpinTime(self):
        global ST
        ST=self.ui.SpanTime.value()
        
    def PhantomSize(self, text):
        global size
        size = text
    def getPos(self , event):
        global x ,y,T1,T2,n,result,imgarr,t1_value,t2_value,ST,mat
        x = math.floor((event.pos().x()*n)/self.ui.phantom.frameGeometry().width())
        y = math.floor((event.pos().y()*n)/self.ui.phantom.frameGeometry().height())
        print(x)
        print(y)
        t1_value =T1[x,y]
        t2_value=T2[x,y]
        if self.count<=4:
            self.draw()
            self.count=self.count+1
        else:
            QMessageBox.about(self, "Warning Message", "Already choose 5 pixels")
            self.draw=False
        
    def draw(self):
        arr1=[]
        arr2=[]
        arr3=[]
        arr4=[]
        arr5=[]
        arr6=[]
        arr7=[]
        arr8=[]
        arr9=[]
        arr10=[]
        plotWindow = self.ui.Decay
        plotWindow2 = self.ui.Recovery
        for t in range(ST):
            y = np.exp(-t/t2_value)
            arr1.append(y)
            y2= 1-np.exp(-t/t1_value)
            arr2.append(y2)
            y3 = np.exp(-t/t2_value)
            arr3.append(y3)
            y4= 1-np.exp(-t/t1_value)
            arr4.append(y4)
            y5 = np.exp(-t/t2_value)
            arr5.append(y5)
            y6= 1-np.exp(-t/t1_value)
            arr6.append(y6)
            y7 = np.exp(-t/t2_value)
            arr7.append(y7)
            y8= 1-np.exp(-t/t1_value)
            arr8.append(y8)
            y9 = np.exp(-t/t2_value)
            arr9.append(y9)
            y10= 1-np.exp(-t/t1_value)
            arr10.append(y10)
            QtGui.QApplication.processEvents()
            if (self.count==0):
                plotWindow.clear()
                plotWindow.plot(arr1,pen='b')
                plotWindow.plot([TR,TR],[1,0],  pen='g')
                plotWindow.plot([TE,TE],[1,0],   pen='r')
                plotWindow2.clear()
                plotWindow2.plot(arr2,pen='b')
                plotWindow2.plot([TR,TR],[1,0],  pen='g')
                plotWindow2.plot([TE,TE],[1,0],  pen='r')
            elif(self.count==1):
                plotWindow.plot(arr3,pen='w')
                plotWindow2.plot(arr4,pen='w')
            elif(self.count==2):
                plotWindow.plot(arr5,pen='y')
                plotWindow2.plot(arr6,pen='y')
            elif(self.count==3):
                plotWindow.plot(arr7,pen='c')
                plotWindow2.plot(arr8,pen='c')
            elif(self.count==4):
                plotWindow.plot(arr9,pen='m')
                plotWindow2.plot(arr10,pen='m')
            self.frame()
            

                
    def frame(self):
        global result,x,y
        QApplication.processEvents()
        self.painterInstance = QPainter(result)   #b3mel opject
        self.painterInstance.begin(self)  
        self.penRectangle =QPen(QtCore.Qt.red)  #yehdd el elon
        self.penRectangle.setWidth(1)
        self.penPoint =QPen(QtCore.Qt.blue)
        self.penPoint.setWidth(1)  #
        self.painterInstance.setPen(self.penPoint)  #apply el lon
        self.painterInstance.drawRect(x,y,1,1)
        self.painterInstance.setPen(self.penRectangle)
        self.painterInstance.drawRect(x-5,y-5,10,10)
        self.painterInstance.end()
        result=result.scaled(int(self.ui.phantom.height()), int(self.ui.phantom.width()),QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation) #scale 3la elabel
        result=QPixmap(result)
        self.ui.phantom.setPixmap(result)
        self.painterInstance.end()
        QApplication.processEvents()

    def browse(self):
        self.ui.phantom.clear()
        self.ui.phantom_2.clear()
        global imgarr,width,height,T1,T2,i,j,t1,t2,n,result,mat, img,size,n
        fileName, _filter = QFileDialog.getOpenFileName(self, "Choose a picture", "", "Filter -- (*.npy)")
        if fileName:
            if size ==1:
                mat = np.load(fileName)
                width=np.shape(mat)
                #if width==(128,128):
                imgarr = np.array(mat)
                result = gray2qimage(imgarr)
                result.save("result.png")
                self.ui.phantom.setPixmap(QPixmap.fromImage(result))
                #self.ui.phantom.setMaximumSize(512,512)
                self.ui.phantom_2.setPixmap(QPixmap.fromImage(result))
                self.ui.phantom.mousePressEvent = self.getPos
                T1=np.copy(imgarr)
                T2=np.copy(imgarr)
                n = 128
                for i in range(n):
                    for j in range(n):
                        if imgarr[i,j] == 0:
                            T1[i,j]= 0
                            T2[i,j]= 0
                        elif imgarr[i,j] > 0 and imgarr[i,j] < 25:
                            T1[i,j]= 10
                            T2[i,j]= 20
                        elif imgarr[i,j] > 25 and imgarr[i,j] < 50:
                            T1[i,j]= 20
                            T2[i,j]= 40
                        elif imgarr[i,j] > 50 and imgarr[i,j] < 75:
                            T1[i,j]= 30
                            T2[i,j]= 60
                        elif imgarr[i,j] > 75 and imgarr[i,j] < 100:
                            T1[i,j]= 40
                            T2[i,j]= 80
                        elif imgarr[i,j] > 100 and imgarr[i,j] < 110:
                            T1[i,j]= 50
                            T2[i,j]= 100
                        elif imgarr[i,j] > 110 and imgarr[i,j] < 120:
                            T1[i,j]= 60
                            T2[i,j]= 120
                        else:
                            T1[i,j]=70
                            T2[i,j]=140
#            else:
#                QMessageBox.about(self, "Error Message", "Phantom isn't 128x128")
#                self.ui.phantom.clear()
#                self.ui.phantom_2.clear()
#                self.ui.output.clear()
#                self.ui.contrast.clear()
                        
            elif size==2:
                mat = np.load(fileName)
                width=np.shape(mat)
                if width==(512,512):
                    imgarr = np.array(mat)
                    result = gray2qimage(imgarr)
                    result.save("result.png")
                    self.ui.phantom.setPixmap(QPixmap.fromImage(result))
                    self.ui.phantom_2.setPixmap(QPixmap.fromImage(result))
                    self.ui.phantom.mousePressEvent = self.getPos
                    T1=np.copy(imgarr)
                    T2=np.copy(imgarr)
                    n = 512
                    for i in range(n):
                        for j in range(n):
                            if imgarr[i,j] == 0:
                                T1[i,j]= 0
                                T2[i,j]= 0
                            elif imgarr[i,j] > 0 and imgarr[i,j] < 50:
                                T1[i,j]= 10
                                T2[i,j]= 20
                            elif imgarr[i,j] > 50 and imgarr[i,j] < 100:
                                T1[i,j]= 20
                                T2[i,j]= 40
                            elif imgarr[i,j] > 100 and imgarr[i,j] < 150:
                                T1[i,j]= 30
                                T2[i,j]= 60
                            elif imgarr[i,j] > 150 and imgarr[i,j] < 200:
                                T1[i,j]= 40
                                T2[i,j]= 80
                            elif imgarr[i,j] > 200 and imgarr[i,j] < 250:
                                T1[i,j]= 50
                                T2[i,j]= 100
                            elif imgarr[i,j] > 250 and imgarr[i,j] < 300:
                                T1[i,j]= 60
                                T2[i,j]= 120
                            elif imgarr[i,j] > 300 and imgarr[i,j] < 350:
                                T1[i,j]= 70
                                T2[i,j]= 140
                            elif imgarr[i,j] > 350 and imgarr[i,j] < 400:
                                T1[i,j]= 80
                                T2[i,j]= 160
                            elif imgarr[i,j] > 450 and imgarr[i,j] < 500:
                                T1[i,j]= 90
                                T2[i,j]= 180
                            elif imgarr[i,j] > 500 and imgarr[i,j] < n:
                                T1[i,j]= 100
                                T2[i,j]= 200
                            else:
                                T1[i,j]= 110
                                T2[i,j]= 220
                else:
                    QMessageBox.about(self, "Error Message", "Phantom isn't 512x512")
                    self.ui.phantom.clear()
                    self.ui.phantom_2.clear()
                    self.ui.output.clear()
                    self.ui.contrast.clear()
            elif size ==3:
                mat = np.load(fileName)
                width=np.shape(mat)
                #if width==(20,20):
                imgarr = np.array(mat)
                result = gray2qimage(imgarr)
                result.save("result.png")
                self.ui.phantom.setPixmap(QPixmap.fromImage(result))
                #self.ui.phantom.setMaximumSize(128,128)
                self.ui.phantom_2.setPixmap(QPixmap.fromImage(result))
                #self.ui.phantom_2.setMaximumSize(128,128)
                self.ui.phantom.mousePressEvent = self.getPos
                T1=np.copy(imgarr)
                T2=np.copy(imgarr)
                n = 20
                for i in range(n):
                    for j in range(n):
                        if imgarr[i,j] == 0:
                            T2[i,j]= 0
                            T1[i,j]= 0
                        elif imgarr[i,j] > 0 and imgarr[i,j] < 5:
                            T2[i,j]= 10
                            T1[i,j]= 20
                        elif imgarr[i,j] > 5 and imgarr[i,j] < 10:
                            T2[i,j]= 20
                            T1[i,j]= 40
                        elif imgarr[i,j] > 15 and imgarr[i,j] < 20:
                            T2[i,j]= 30
                            T1[i,j]= 60
                        else:
                            T2[i,j]=40
                            T1[i,j]=80
#                else:
#                    QMessageBox.about(self, "Error Message", "Phantom isn't 20x20")
#                    self.ui.phantom.clear()
#                    self.ui.phantom_2.clear()
#                    self.ui.output.clear()
#                    self.ui.contrast.clear()
                        

    def TissueProperty(self, text):
        global tissue,T1 ,T2
        tissue = text
        if tissue==1:
            result1 = gray2qimage(T1)
            self.ui.phantom.setPixmap(QPixmap.fromImage(result1))
        elif tissue==2:
            result2 = gray2qimage(T2)
            self.ui.phantom.setPixmap(QPixmap.fromImage(result2))
        elif tissue ==3:
            self.ui.phantom.setPixmap(QPixmap.fromImage(result))
        else:
            self.ui.phantom.clear()
    
                
            
    def valuechangeb(self):
        global img, tissue
        if tissue==1:
            result1 = gray2qimage(T1)
            self.ui.phantom.setPixmap(QPixmap.fromImage(result1))
            result1.save("result1.png")
            img = PIL.Image.open("result1.png")
            factor = self.ui.Sliderb.value()
            brightness = ImageEnhance.Brightness(img).enhance(factor)
            brightness.save("out.png")
            self.ui.phantom.setPixmap(QPixmap("out.png"))
        elif tissue==2:
            result2 = gray2qimage(T2)
            self.ui.phantom.setPixmap(QPixmap.fromImage(result2))
            result2.save("result2.png")
            img = PIL.Image.open("result2.png")
            factor = self.ui.Sliderb.value()
            brightness = ImageEnhance.Brightness(img).enhance(factor)
            brightness.save("out.png")
            self.ui.phantom.setPixmap(QPixmap("out.png"))
        elif tissue ==3:
            img = PIL.Image.open("result.png")
            factor = self.ui.Sliderb.value()
            brightness = ImageEnhance.Brightness(img).enhance(factor)
            brightness.save("out.png")
            self.ui.phantom.setPixmap(QPixmap("out.png"))
#        else:
#            self.ui.output.clear()

    def valuechangec(self):
        global img, tissue
        if tissue==1:
            result1 = gray2qimage(T1)
            self.ui.phantom.setPixmap(QPixmap.fromImage(result1))
            result1.save("result1.png")
            img = PIL.Image.open("result1.png")
            factor = self.ui.sliderc.value()
            contrast = ImageEnhance.Contrast(img).enhance(factor)
            contrast.save("out.png")
            self.ui.phantom.setPixmap(QPixmap("out.png"))
        elif tissue==2:
            result2 = gray2qimage(T2)
            self.ui.phantom.setPixmap(QPixmap.fromImage(result2))
            result2.save("result2.png")
            img = PIL.Image.open("result2.png")
            factor = self.ui.sliderc.value()
            contrast = ImageEnhance.Contrast(img).enhance(factor)
            contrast.save("out.png")
            self.ui.phantom.setPixmap(QPixmap("out.png"))
        elif tissue ==3:
            img = PIL.Image.open("result.png")
            factor = self.ui.sliderc.value()
            contrast = ImageEnhance.Contrast(img).enhance(factor)
            contrast.save("out.png")
            self.ui.phantom.setPixmap(QPixmap("out.png"))
#        else:
#            self.ui.output.clear()

    def kspace(self):
        global T1,T2,ST,FA,PD,i,j,x,y,t1,t2,x,y,t1_value,t2_value, imgarr
        New_array = Rotation_decay(imgarr,T1,T2,FA,TE,TR) 
        final = KSPACE(New_array)
        final_image = np.around(np.abs(np.fft.ifft2(final)))
        final_image = final_image/np.amax(final_image) * 255
        final_image = gray2qimage(final_image)
        
        self.ui.output_2.setPixmap(QPixmap.fromImage(final_image))
        #self.ui.output_2.setMaximumSize(128,128)
       
def Rotation_decay(Phantom,T1,T2,FA,TE,TR): #1)rotate_decayrecovery_PrepareforKspace
    
    FA=FA*math.pi/180
    RX = np.array([[1,0,0],[0,math.cos(FA),math.sin(FA)],[0,-math.sin(FA),math.cos(FA)]])
    Height,Width = np.shape(Phantom)
    
    for i in range (Height):
        for j in range (Width):
            decayrecovery = np.array([[np.exp(-TE/T2[i,j]),0,0],[0,np.exp(-TE/T2[i,j]),0],[0,0,1-np.exp(-TR/T1[i,j])]])
            vector = decayrecovery.dot(RX.dot([0,0,1]))
            if vector[2] == 0 :
                vector = vector + decayrecovery[:,2]
            vector1 = Phantom[i,j] * decayrecovery.dot(RX.dot(vector))
            Phantom[i,j] = vector1[1]
            QtGui.QApplication.processEvents()
    

            
    return Phantom



def KSPACE(Phantom): #2)Create_K_space
    
    width,height = np.shape(Phantom)
    Gx,Gy = 2*np.pi/width,2*np.pi/height
    sum = 0
    
    K_Space = np.zeros([height,width],dtype='complex')
    
    for a in range(height):
        for b in range(width):
            
            for i in range (height):
                for j in range(width):
                    sum = sum + Phantom[i,j]*np.exp(-1j*(a*i*Gx+b*j*Gy))
                    
                    QtGui.QApplication.processEvents()
                    
            QtGui.QApplication.processEvents()
            K_Space[a,b] = sum
            sum=0
            print('running')
                
    return K_Space
         

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()