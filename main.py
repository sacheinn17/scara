from PySide6 import QtWidgets
from PySide6 import QtCore
from qt_material import apply_stylesheet
import threading
import serial
import time
import serial.tools.list_ports
ports = serial.tools.list_ports.comports()
from PySide6.QtUiTools import QUiLoader

t = []
c = []

file = "setting.txt"
f = open(file,'w')
f.close()


for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))
        t.append(port)
print(ports)

app = QtWidgets.QApplication()

# print(t)

ser = serial.Serial(t[0],9600)

class uiHandeller(QtCore.QObject):
    def __init__(self,slider,addBtn,subBtn,txt,set,store,no):

        self.baseSlider = slider
        self.addBtn = addBtn
        self.subBtn = subBtn 
        self.txt = txt
        self.t = "000"
        self.no = no
        self.val = 0
        self.txt.setText(str(self.val))
        self.c = []

        self.set = set
        self.store = store

        self.baseSlider.valueChanged.connect(self.baseSliderFunc)
        self.addBtn.clicked.connect(self.baseButtonAdd)
        self.set.clicked.connect(self.setBtn)
        self.subBtn.clicked.connect(self.baseButtonSub)
        self.txt.textChanged.connect(self.baseTextChanged)
    
    def baseSliderFunc(self):
        self.val = self.baseSlider.value()
        self.txt.setText(str(self.val))
    def baseButtonAdd(self):
        self.val +=1
        self.txt.setText(str(self.val))
    def baseButtonSub(self):
        self.val -=1
        self.txt.setText(str(self.val))
    def baseTextChanged(self):
        self.baseSlider.setSliderPosition(self.val)
        self.t = str(self.val)
    def setBtn(self):
        c.append(str(self.no)+" "+str(self.val)+"\n")
        print(self.no,self.val)
        print(c)
    
    
def storeBtn():
    f = open(file,'r')
    a = f.readlines()
    f.close()
    f = open(file,"w")
    f.writelines(a)
    f.writelines(c)
    f.close()

class mainWidget(QtCore.QObject):
    def __init__(self):
        # super().__init__(self, parent=None)
        self.baseVal = 0
        self.ui = QUiLoader().load("scaraui.ui",None)

        self.base = uiHandeller(self.ui.baseSlider,self.ui.base_add,self.ui.base_sub,self.ui.baseVal,self.ui.set,self.ui.store,0)
        self.axis1 = uiHandeller(self.ui.arm1Slider,self.ui.axis_add,self.ui.axis_sub,self.ui.axisVal,self.ui.set,self.ui.store,1)
        self.end = uiHandeller(self.ui.endSlider,self.ui.end_add,self.ui.end_sub,self.ui.endVal,self.ui.set,self.ui.store,2)

        self.x1= 'v'
        self.x2 = 'v'
        self.x3 = 'v'

        self.ui.store.clicked.connect(storeBtn)


        self.ui.send.clicked.connect(self.send)
        self.ui.sendAll.clicked.connect(self.sendAll)
        self.ui.save.clicked.connect(self.save)
        self.ui.load.clicked.connect(self.load)



    def send(self):
            print("hi")
            print(self.base.t)
            if self.compare(self.x1,self.base.t):
                ser.write(("0 "+self.base.t+"\n").encode())
                print(self.x1 ,self.base.t)
                time.sleep(0.5)
                try:
                    print(ser.read_all().decode())
                except:
                    pass

            self.x1 = self.base.t
            if self.compare(self.x2,self.axis1.t):
                ser.write(("1 "+self.axis1.t+"\n").encode())
                print(self.x2,self.axis1.t)
                time.sleep(0.5)

            self.x2 = self.axis1.t
            if self.compare(self.x3,self.end.t):
                ser.write(("2 "+self.end.t+"\n").encode())
                print(self.x3,self.end.t)
                time.sleep(0.5)
            self.x3 = self.end.t



    
    def sendAll(self):
        f = open(file,'r') 
        t = f.readlines()
        for i in t:
            ser.write(i.encode())
            print(i)
            time.sleep(0.8)


    def update(self):
        while True:

            if self.compare(self.x1,self.temp):
                ser.write(("0 "+self.temp+"\n").encode())
                # print(self.x1 ,self.temp)
                time.sleep(0.5)
                try:
                    print(ser.read_all().decode())
                except:
                    pass

            self.x1 = self.temp
            if self.compare(self.x2,self.temp3):
                ser.write(("1 "+self.temp2+"\n").encode())
                print(self.x2,self.temp2)
                time.sleep(0.5)
            self.x2 = self.temp2
            if self.compare(self.x3,self.temp3):
                ser.write(("2 "+self.temp3+"\n").encode())
                print(self.x3,self.temp3)
                time.sleep(0.5)
            self.x3 = self.temp3


    def compare(self,x,y):
        if x!=y:
            return True
        else:
            return False
    def show(self):
        self.ui.show()

    def save(self):
        name = QtWidgets.QFileDialog.getSaveFileName(None,"Save commands as","",".ccia")
        print(name)
        # f = QtCore.QFile(nam))
        # f.open(QtCore.QIODevice.WriteOnly)
        f = open(name[0]+name[1],'w')
        temp = open(file)
        t = temp.read()

        f.write(t)
        temp.close()
        f.close()
    
    def load(self):
        name = QtWidgets.QFileDialog.getOpenFileName(None,"Open commands file","")
        print(name)
        disp = name[0].split('/')
        self.ui.file.setText(disp[-1])
        f = open(name[0],'r')
        t = f.read()

        temp = open(file,'w')
        temp.write(t)

        temp.close()
        f.close()





window = mainWidget()
window.show()

apply_stylesheet(app, theme='dark_medical.xml')
app.exec()