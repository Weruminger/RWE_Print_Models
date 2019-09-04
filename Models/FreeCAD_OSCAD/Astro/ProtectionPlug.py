#
# FreeCAD Makro ProtectionPlug
# Customizable creator for Protection / Dudt cover Plugs for telescopes and parts.
# 
#

from PySide import QtCore, QtGui
import FreeCAD, Part 

class Ui_Dialog(object):
   
   
   def __init__(self):
       self.plugDiameter = 32 
       self.plugHeight = 10 
       self.plugWall = 3 
       self.plugFilet = 0.8 
       self.cuffHight = 3 
       self.cuffCollar = 3  
       self.cuffFillet = 0.8
   
   def setupUi(self, Dialog):
       Dialog.setObjectName("Dialog")
       Dialog.resize(320, 400)
       self.title = QtGui.QLabel(Dialog)
       self.title.setGeometry(QtCore.QRect(10, 10, 271, 16))
       self.title.setObjectName("title")
       
       self.label_plugDiameter = QtGui.QLabel(Dialog)
       self.label_plugDiameter.setGeometry(QtCore.QRect(10, 50, 80, 16))
       self.label_plugDiameter.setObjectName("label_plugDiameter")
       
       self.label_plugHeight = QtGui.QLabel(Dialog)
       self.label_plugHeight.setGeometry(QtCore.QRect(10, 90, 80, 16))
       self.label_plugHeight.setObjectName("label_height")
       
       self.label_plugWall = QtGui.QLabel(Dialog)
       self.label_plugWall.setGeometry(QtCore.QRect(10, 130, 80, 16))
       self.label_plugWall.setObjectName("label_plugWall")
       
       self.label_plugFilet = QtGui.QLabel(Dialog)
       self.label_plugFilet.setGeometry(QtCore.QRect(10, 170, 80, 16))
       self.label_plugFilet.setObjectName("label_plugFilet")
       
       self.label_cuffHight = QtGui.QLabel(Dialog)
       self.label_cuffHight.setGeometry(QtCore.QRect(10, 210, 80, 16))
       self.label_cuffHight.setObjectName("label_cuffHight")
       
       self.label_cuffCollar = QtGui.QLabel(Dialog)
       self.label_cuffCollar.setGeometry(QtCore.QRect(10, 250, 80, 16))
       self.label_cuffCollar.setObjectName("label_cuffCollar")
       
       self.label_cuffFillet = QtGui.QLabel(Dialog)
       self.label_cuffFillet.setGeometry(QtCore.QRect(10, 290, 80, 16))
       self.label_cuffFillet.setObjectName("label_cuffFillet")
       
       self.value_plugDiameter = QtGui.QLineEdit(Dialog)
       self.value_plugDiameter.setGeometry(QtCore.QRect(100, 40, 111, 26))
       self.value_plugDiameter.setObjectName("value_plugDiameter")
       
       self.value_plugHeight = QtGui.QLineEdit(Dialog)
       self.value_plugHeight.setGeometry(QtCore.QRect(100, 80, 111, 26))
       self.value_plugHeight.setObjectName("value_plugHeight")
       
       ################################
       
       self.value_plugWall = QtGui.QLineEdit(Dialog)
       self.value_plugWall.setGeometry(QtCore.QRect(100, 120, 111, 26))
       self.value_plugWall.setObjectName("value_plugWall")
       
       self.value_plugFilet = QtGui.QLineEdit(Dialog)
       self.value_plugFilet.setGeometry(QtCore.QRect(100, 160, 111, 26))
       self.value_plugFilet.setObjectName("value_plugFilet")
       
       self.value_cuffHight = QtGui.QLineEdit(Dialog)
       self.value_cuffHight.setGeometry(QtCore.QRect(100, 200, 111, 26))
       self.value_cuffHight.setObjectName("value_cuffHight")
       
       self.value_cuffCollar = QtGui.QLineEdit(Dialog)
       self.value_cuffCollar.setGeometry(QtCore.QRect(100, 240, 111, 26))
       self.value_cuffCollar.setObjectName("value_cuffCollar")
       
       self.value_cuffFillet = QtGui.QLineEdit(Dialog)
       self.value_cuffFillet.setGeometry(QtCore.QRect(100, 280, 111, 26))
       self.value_cuffFillet.setObjectName("value_cuffFillet")
       
       
       
       #############################
       
       self.create = QtGui.QPushButton(Dialog)
       self.create.setGeometry(QtCore.QRect(50, 340, 83, 26))
       self.create.setObjectName("create")
       
       self.retranslateUi(Dialog)
       QtCore.QObject.connect(self.create,QtCore.SIGNAL("pressed()"),self.createProtectionCap)
       QtCore.QMetaObject.connectSlotsByName(Dialog)

   def retranslateUi(self, Dialog):
       Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Parameter Dialog", None, QtGui.QApplication.UnicodeUTF8))
       self.title.setText(QtGui.QApplication.translate("Dialog", "Plug/Cap Designer", None, QtGui.QApplication.UnicodeUTF8))
       self.label_plugDiameter.setText(QtGui.QApplication.translate("Dialog", "Pulg diameter", None, QtGui.QApplication.UnicodeUTF8))
       self.label_plugHeight.setText(QtGui.QApplication.translate("Dialog", "Plug height", None, QtGui.QApplication.UnicodeUTF8))
       self.label_plugWall.setText(QtGui.QApplication.translate("Dialog", "Plug wall", None, QtGui.QApplication.UnicodeUTF8))
       self.label_plugFilet.setText(QtGui.QApplication.translate("Dialog", "Plug fillet", None, QtGui.QApplication.UnicodeUTF8))
       self.label_cuffHight.setText(QtGui.QApplication.translate("Dialog", "Cuff height", None, QtGui.QApplication.UnicodeUTF8))
       self.label_cuffCollar.setText(QtGui.QApplication.translate("Dialog", "Cuff collar", None, QtGui.QApplication.UnicodeUTF8))
       self.label_cuffFillet.setText(QtGui.QApplication.translate("Dialog", "Cuff fillet", None, QtGui.QApplication.UnicodeUTF8))
       
       self.value_plugDiameter.setText( '%s' % self.plugDiameter )
       self.value_plugHeight.setText( '%s' % self.plugHeight )
       self.value_plugWall.setText( '%s' % self.plugWall )
       self.value_plugFilet.setText( '%s' % self.plugFilet )
       self.value_cuffHight.setText( '%s' % self.cuffHight )
       self.value_cuffCollar.setText( '%s' % self.cuffCollar )
       self.value_cuffFillet.setText( '%s' % self.cuffFillet )
       
       self.create.setText(QtGui.QApplication.translate("Dialog", "Create!", None, QtGui.QApplication.UnicodeUTF8))

   def refreshValuesFromGui(self):
        self.plugDiameter = float(self.value_plugDiameter.text())
        self.plugHeight = float(self.value_plugHeight.text())
        self.plugWall = float(self.value_plugWall.text())
        self.plugFilet = float(self.value_plugFilet.text())
        self.cuffHight = float(self.value_cuffHight.text())
        self.cuffCollar = float(self.value_cuffCollar.text())
        self.cuffFillet = float(self.value_cuffFillet.text())

   def createProtectionCap(self):
      self.refreshValuesFromGui()
      modelName = "ProtectionPlug_new"
      Plug = { 'd' : self.plugDiameter , 'h' : self.plugHeight , 'w' : self.plugWall, 'f' : self.plugFilet}
      Cuff = { 'h' : self.cuffHight , 'c' : self.cuffCollar, 'f' : self.cuffFillet}
      
      Plug['r'] = Plug['d']/2
      Cuff['r'] = Plug['r']+Cuff['c']
      PlugCut = {'r' : Plug['r']-Plug['w'], 'h' : Plug['h']}
      
      
      #App.newDocument(modelName)
      #App.setActiveDocument(modelName)
      #App.ActiveDocument=App.getDocument(modelName)
      #Gui.ActiveDocument=Gui.getDocument(modelName)
      Gui.activateWorkbench("PartWorkbench")
      App.ActiveDocument.addObject("Part::Cylinder","Plug")
      PlugObj = App.ActiveDocument.ActiveObject
      App.ActiveDocument.recompute()
      PlugObj.Radius = '%s mm' % Plug['r']
      PlugObj.Height = '%s mm' % Plug['h']
      PlugObj.Placement = App.Placement(App.Vector(0,0,Cuff['h']),App.Rotation(App.Vector(0,0,1),0))
      App.ActiveDocument.recompute()
      App.ActiveDocument.addObject("Part::Cylinder","PlugCut")
      PlugCutObj = App.ActiveDocument.ActiveObject
      App.ActiveDocument.recompute()
      PlugCutObj.Radius = '%s mm' % PlugCut['r']
      PlugCutObj.Height = '%s mm' % PlugCut['h']
      PlugCutObj.Placement = App.Placement(App.Vector(0,0,Cuff['h']),App.Rotation(App.Vector(0,0,1),0))
      App.ActiveDocument.addObject("Part::Cylinder","Cuff")
      CuffObj = App.ActiveDocument.ActiveObject
      App.ActiveDocument.recompute()
      CuffObj.Radius = Cuff['r']
      CuffObj.Height = Cuff['h']
      App.activeDocument().addObject("Part::MultiFuse","Fusion")
      FusionObj = App.ActiveDocument.ActiveObject
      FusionObj.Shapes = [PlugObj,CuffObj,]
      Gui.ActiveDocument.getObject(PlugObj.Name).Visibility = False
      Gui.ActiveDocument.getObject(CuffObj.Name).Visibility = False
      Gui.ActiveDocument.getObject(FusionObj.Name).ShapeColor = Gui.ActiveDocument.getObject(CuffObj.Name).ShapeColor
      Gui.ActiveDocument.getObject(FusionObj.Name).DisplayMode = Gui.ActiveDocument.getObject(CuffObj.Name).DisplayMode
      App.ActiveDocument.recompute()
      App.activeDocument().addObject("Part::Cut","Cut")
      CutObj = App.ActiveDocument.ActiveObject
      CutObj.Base = FusionObj
      CutObj.Tool = PlugCutObj
      Gui.ActiveDocument.getObject(FusionObj.Name).Visibility = False
      Gui.ActiveDocument.getObject(PlugCutObj.Name).Visibility = False
      Gui.ActiveDocument.getObject(CutObj.Name).ShapeColor = Gui.ActiveDocument.getObject(FusionObj.Name).ShapeColor
      Gui.ActiveDocument.getObject(CutObj.Name).DisplayMode = Gui.ActiveDocument.getObject(FusionObj.Name).DisplayMode
      App.ActiveDocument.recompute()
      FreeCAD.ActiveDocument.addObject("Part::Fillet","ProtectionCap")
      ProtectionCapObj = App.ActiveDocument.ActiveObject
      ProtectionCapObj.Base = CutObj
      __fillets__ = []
      __fillets__.append((1,Plug['f'],Plug['f']))
      __fillets__.append((2,Plug['f'],Plug['f']))
      __fillets__.append((7,Cuff['f'],Cuff['f']))
      __fillets__.append((9,Cuff['f'],Cuff['f']))
      ProtectionCapObj.Edges = __fillets__
      del __fillets__
      Gui.ActiveDocument.getObject(CutObj.Name).Visibility = False
      Gui.ActiveDocument.getObject(ProtectionCapObj.Name).LineColor = Gui.ActiveDocument.getObject(CutObj.Name).LineColor
      Gui.ActiveDocument.getObject(ProtectionCapObj.Name).PointColor = Gui.ActiveDocument.getObject(CutObj.Name).PointColor
      Gui.activeDocument().resetEdit()
      Gui.SendMsgToActiveView("ViewFit")
      App.ActiveDocument.recompute()
      Gui.SendMsgToActiveView("ViewFit")


class plane():
   def __init__(self):
       self.d = QtGui.QWidget()
       self.ui = Ui_Dialog()
       self.ui.setupUi(self.d)
       self.d.show()

GoForIt = plane()
