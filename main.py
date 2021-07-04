"""
This Expert System can tell your cat's type based on some rules, the system takes user's requests
and then perform some magic/matching to find out.

engine.run() : runs the engine in real time.
engine.declare() : passes requests to the engine aka adds a fact to the engine.
engine.reset() : resets the engine.

more info : https://experta.readthedocs.io/en/latest/thebasics.html

"""
from experta import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

cat_out = None


class Cat(Fact):
    """Meow"""
    pass


cat_types = [
    "Maine coon" ,
    "Persia himalya" ,
    "Persia peaknose",
    "Exotic shorthair",
    "Russian blue",
    "Angora" ,
    "Siamese" ,
    "Scotishfold",
    "Sphynx" 
]

def get_output(num):    
    """assign the value of the output(engine run) to a global var called output"""

    # a sneaky why to do it, the stupid experta doesn't assign the output the a variable
    global cat_out
    cat_out = cat_types[num]
         
 
class CatEngine(KnowledgeEngine):

    @Rule(AND( Cat(body="big"), Cat(hair="long"),   Cat(eye="sharp"),   Cat(neck="medium"),  Cat(earlobe="wide"),  Cat(leg="medium"),  Cat(nose="pointed") ))  
    def maine_coon(self):
        get_output(0)

    @Rule(AND( Cat(body="big"), Cat(hair="long"),   Cat(eye="sharp"),   Cat(neck="medium"),  Cat(earlobe="wide"),  Cat(leg="medium"),  Cat(nose="flat") ))  
    def persia_himalya(self):
        get_output(1)

    @Rule(AND( Cat(body="big"), Cat(hair="long"),   Cat(eye="sharp"),   Cat(neck="short"),  Cat(earlobe="small"),  Cat(leg="short"),  Cat(nose="flat") ))  
    def persia_peaknose(self):
        get_output(2)
         
    @Rule(AND( Cat(body="big"), Cat(hair="long"),   Cat(eye="round"),   Cat(neck="short"),  Cat(earlobe="small"),  Cat(leg="short"),  Cat(nose="flat") ))  
    def exotic_shorthair(self):
        get_output(3)
         
    @Rule(AND( Cat(body="medium"), Cat(hair="short"),   Cat(eye="sharp"),   Cat(neck="medium"),  Cat(earlobe="medium"),  Cat(leg="medium"),  Cat(nose="pointed") ))  
    def russian_blue(self):
        get_output(4)

    @Rule(AND( Cat(body="medium"), Cat(hair="long"),   Cat(eye="sharp"),   Cat(neck="medium"),  Cat(earlobe="wide"),  Cat(leg="medium"),  Cat(nose="pointed") ))  
    def angora(self):
        get_output(5)

    @Rule(AND( Cat(body="medium"), Cat(hair="short"),   Cat(eye="sharp"),   Cat(neck="medium"),  Cat(earlobe="medium"),  Cat(leg="medium"),  Cat(nose="pointed") ))  
    def siamese(self):
        get_output(6)

    @Rule(AND( Cat(body="medium"), Cat(hair="short"),   Cat(eye="round"),   Cat(neck="short"),  Cat(earlobe="small"),  Cat(leg="medium"),  Cat(nose="flat") ))  
    def scotishfold(self):
        get_output(7)
         
    @Rule(AND( Cat(body="medium"), Cat(hair="unavailable"),   Cat(eye="sharp"),   Cat(neck="medium"),  Cat(earlobe="wide"),  Cat(leg="medium"),  Cat(nose="pointed") ))  
    def sphynx(self):
        get_output(8)

   

         
class Ui_MainWindow(object):

    def __init__(self):
        """idk"""

        self.engine = CatEngine()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(537, 663)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 181, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 181, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 80, 181, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 110, 181, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 140, 211, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 200, 221, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 170, 201, 16))
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 240, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(200, 290, 171, 41))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(60, 340, 421, 251))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(""))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(300, 20, 191, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(300, 50, 191, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(300, 80, 191, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(300, 110, 191, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(300, 140, 191, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(300, 170, 191, 22))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(300, 200, 191, 22))
        self.lineEdit_7.setObjectName("lineEdit_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 537, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # the push button 
        self.pushButton.clicked.connect(self.get_input) 

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Big or Medium body ?"))
        self.label_2.setText(_translate("MainWindow", "Long, Short or No hair ?"))
        self.label_3.setText(_translate("MainWindow", "Sharp or Round eyes ?"))
        self.label_4.setText(_translate("MainWindow", "Short or Medium neck ?"))
        self.label_5.setText(_translate("MainWindow", "Wide, Medium or Small earlobe ?"))
        self.label_6.setText(_translate("MainWindow", "Pointed or Flat nose ?"))
        self.label_7.setText(_translate("MainWindow", "Short or Medium legs ?"))
        self.pushButton.setText(_translate("MainWindow", "Send"))
        self.label_8.setText(_translate("MainWindow", ""))

    def get_input(self):
        """Get the user's input from the lineboxes"""

        body = self.lineEdit.text()
        hair = self.lineEdit_2.text()
        eye = self.lineEdit_3.text()
        neck = self.lineEdit_4.text()
        earlobe = self.lineEdit_5.text()
        legs = self.lineEdit_6.text()
        nose = self.lineEdit_7.text()



        self.engine.reset()

        self.engine.declare(Cat(body=body), Cat(hair=hair),   Cat(eye=eye),   Cat(neck=neck),  Cat(earlobe=earlobe),  Cat(leg=legs),  Cat(nose=nose)) 
        #self.engine.declare(Cat(body="big"), Cat(hair="long"),   Cat(eye="sharp"),   Cat(neck="medium"),  Cat(earlobe="wide"),  Cat(leg="medium"),  Cat(nose="pointed")) 

        self.engine.run()

        global cat_out

        if cat_out is None:
            # Cat not found 

            self.show_cat_name("Cat not found")

            # resetting the img
            self.label_9.setPixmap(QtGui.QPixmap(""))

        else :
            # Show the name of the cat + img
            self.show_cat_name(cat_out)

            self.show_cat_img(cat_out)

            # reset the output

            cat_out = None
            
    
    def show_cat_name(self, name):
        """Showing the cat's name after a successful searching"""

        # Changing the name
        self.label_8.setText(name)

    def show_cat_img(self, name):
        """Choosing a picture of the cat based on its name"""

        splitted_name = name.split(" ")
        f_name = splitted_name[0]

        try:
            l_name = splitted_name[1]
            display_name = f_name + "_" + l_name.lower()

        except :
            # it's only one name
            display_name = f_name

        self.label_9.setPixmap(QtGui.QPixmap(f"cats/{display_name}.jpg"))



if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())
