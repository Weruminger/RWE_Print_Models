#
# FreeCAD Makro ProtectionPlug
# Customizable creator for Protection / Dudt cover Plugs for telescopes and parts.
# 
#
from math import *
from PySide import QtCore, QtGui
import FreeCAD, Part 

class finderMount(object):
   baseWidth = 32
   roofWidth = 23
   roofHight = 10
   mountHight = 20
   extrutionDeepth = 25
   
   def __init__(self,dialog):
       self.dialog = dialog

   def setupUi(self):
       self.dialog.setObjectName("FMDialog")
       self.dialog.resize(360, 400)
       self.title = QtGui.QLabel(self.dialog)
       self.title.setGeometry(QtCore.QRect(10, 10, 271, 16))
       self.title.setObjectName("title")      
       self.label_baseWidth = QtGui.QLabel(self.dialog)
       self.label_baseWidth.setGeometry(QtCore.QRect(10, 50, 80, 16))
       self.label_baseWidth.setObjectName("label_baseWidth")
       self.label_roofWidth = QtGui.QLabel(self.dialog)
       self.label_roofWidth.setGeometry(QtCore.QRect(10, 90, 80, 16))
       self.label_roofWidth.setObjectName("label_roofWidth")
       self.label_roofHight = QtGui.QLabel(self.dialog)
       self.label_roofHight.setGeometry(QtCore.QRect(10, 130, 80, 16))
       self.label_roofHight.setObjectName("label_roofHight")
       self.label_mountHight = QtGui.QLabel(self.dialog)
       self.label_mountHight.setGeometry(QtCore.QRect(10, 170, 80, 16))
       self.label_mountHight.setObjectName("label_mountHight")
       self.label_extrutionDeeptht = QtGui.QLabel(self.dialog)
       self.label_extrutionDeeptht.setGeometry(QtCore.QRect(10, 210, 80, 16))
       self.label_extrutionDeeptht.setObjectName("label_extrutionDeeptht")
       self.value_baseWidth = QtGui.QLineEdit(self.dialog)
       self.value_baseWidth.setGeometry(QtCore.QRect(100, 40, 111, 26))
       self.value_baseWidth.setObjectName("value_baseWidth")
       
       self.value_roofWidth = QtGui.QLineEdit(self.dialog)
       self.value_roofWidth.setGeometry(QtCore.QRect(100, 80, 111, 26))
       self.value_roofWidth.setObjectName("value_roofWidth")
       
       self.value_roofHight = QtGui.QLineEdit(self.dialog)
       self.value_roofHight.setGeometry(QtCore.QRect(100, 120, 111, 26))
       self.value_roofHight.setObjectName("value_roofHight")
       
       self.value_mountHight = QtGui.QLineEdit(self.dialog)
       self.value_mountHight.setGeometry(QtCore.QRect(100, 160, 111, 26))
       self.value_mountHight.setObjectName("value_mountHight")
       
       self.value_extrutionDeepth = QtGui.QLineEdit(self.dialog)
       self.value_extrutionDeepth.setGeometry(QtCore.QRect(100, 200, 111, 26))
       self.value_extrutionDeepth.setObjectName("value_extrutionDeepth")
       
       self.create = QtGui.QPushButton(self.dialog)
       self.create.setGeometry(QtCore.QRect(50, 340, 83, 26))
       self.create.setObjectName("create")
       
       self.retranslateUi()
       QtCore.QObject.connect(self.create,QtCore.SIGNAL("pressed()"),self.createFinderMount)
       QtCore.QMetaObject.connectSlotsByName(self.dialog)

   def retranslateUi(self):
       self.dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Finder Mount Dialog", None, QtGui.QApplication.UnicodeUTF8))
       self.title.setText(QtGui.QApplication.translate("Dialog", "Finder Mount Designer", None, QtGui.QApplication.UnicodeUTF8))
       self.label_baseWidth.setText(QtGui.QApplication.translate("Dialog", "Base Width", None, QtGui.QApplication.UnicodeUTF8))
       self.label_roofWidth.setText(QtGui.QApplication.translate("Dialog", "Roof Width", None, QtGui.QApplication.UnicodeUTF8))
       self.label_roofHight.setText(QtGui.QApplication.translate("Dialog", "Roo Hight", None, QtGui.QApplication.UnicodeUTF8))
       self.label_mountHight.setText(QtGui.QApplication.translate("Dialog", "Mount Hight", None, QtGui.QApplication.UnicodeUTF8))
       self.label_extrutionDeeptht.setText(QtGui.QApplication.translate("Dialog", "Clip angle", None, QtGui.QApplication.UnicodeUTF8))
       
       self.value_baseWidth.setText( '%s' % self.baseWidth )
       self.value_roofWidth.setText( '%s' % self.roofWidth )
       self.value_roofHight.setText( '%s' % self.roofHight )
       self.value_mountHight.setText( '%s' % self.mountHight )
       self.value_extrutionDeepth.setText( '%s' % self.extrutionDeepth )
       
       self.create.setText(QtGui.QApplication.translate("Dialog", "Create!", None, QtGui.QApplication.UnicodeUTF8))

   def refreshValuesFromGui(self):
       self.baseWidth = float(eval(self.value_baseWidth.text()))
       self.roofWidth = float(eval(self.value_roofWidth.text()))
       self.roofHight = float(eval(self.value_roofHight.text()))
       self.mountHight = float(eval(self.value_mountHight.text()))
       self.extrutionDeepth = float(eval(self.value_extrutionDeepth.text()))


   def createFinderMount(self):
       self.refreshValuesFromGui()
       deltBaseRoof = (self.baseWidth - self.roofWidth) / 2
       points = [FreeCAD.Vector(0,0,0),
           FreeCAD.Vector(self.baseWidth,0,0),
           FreeCAD.Vector(self.baseWidth-deltBaseRoof,self.roofHight,0),
           FreeCAD.Vector(self.baseWidth-deltBaseRoof,self.roofHight+self.mountHight,0),
           FreeCAD.Vector(deltBaseRoof,self.roofHight+self.mountHight,0),
           FreeCAD.Vector(deltBaseRoof,self.roofHight,0),
           FreeCAD.Vector(0,0,0)]
       MyPoly = Part.makePolygon(points)
       MyFace = Part.Face(MyPoly)
       MyExtrude = MyFace.extrude(FreeCAD.Vector(0,0,self.extrutionDeepth))
       myObj2 = FreeCAD.ActiveDocument.addObject("Part::Feature","FinderMount_Common")
       myObj2.Shape = MyExtrude
       Myfilllet = FreeCAD.ActiveDocument.addObject("Part::Fillet","FinderMount_A")
       Myfilllet.Base = myObj2
       __fillets__ = []
       __fillets__.append((1,1.00,1.00))
       __fillets__.append((2,1.00,1.00))
       __fillets__.append((3,1.00,1.00))
       __fillets__.append((4,1.00,1.00))
       __fillets__.append((6,1.00,1.00))
       __fillets__.append((7,1.00,1.00))
       __fillets__.append((8,1.00,1.00))
       __fillets__.append((9,1.00,1.00))
       __fillets__.append((10,1.00,1.00))
       __fillets__.append((11,1.00,1.00))
       __fillets__.append((12,1.00,1.00))
       __fillets__.append((13,1.00,1.00))
       __fillets__.append((15,1.00,1.00))
       __fillets__.append((16,1.00,1.00))
       __fillets__.append((17,1.00,1.00))
       __fillets__.append((18,1.00,1.00))
       Myfilllet.Edges = __fillets__
       del __fillets__
       Gui.ActiveDocument.getObject(myObj2.Name).Visibility = False
       App.ActiveDocument.recompute()
       
       MyFinderMount = App.ActiveDocument.addObject('Part::Feature','FinderMount').Shape=App.ActiveDocument.getObject(Myfilllet.Name).Shape.removeSplitter()
       App.ActiveDocument.ActiveObject.Label=App.ActiveDocument.FinderMount.Label
       Gui.ActiveDocument.getObject(Myfilllet.Name).hide()
       
       App.ActiveDocument.removeObject(myObj2.Name)
       App.ActiveDocument.recompute()
       App.ActiveDocument.removeObject(Myfilllet.Name)
       App.ActiveDocument.recompute()
       App.ActiveDocument.recompute()


class planeFinderMount():
   def __init__(self):
       self.d = QtGui.QWidget()
       self.ui = finderMount(self.d)
       self.ui.setupUi()
       self.d.show()

def pytagoras(h,a):
    return sqrt(pow(float(h),2)+pow(float(a),2))

def lentoangle(h,a):
    return degrees(sin(float(a)/float(h)))

fm = planeFinderMount()
