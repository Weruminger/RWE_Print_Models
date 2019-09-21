#
# FreeCAD Makro ProtectionPlug
# Customizable creator for Protection / Dudt cover Plugs for telescopes and parts.
# 
#
from math import *
from PySide import QtCore, QtGui
import FreeCAD, Part 

class Ui_Dialog(object):
   
   
   def __init__(self,dialog):
       self.dialog = dialog
       self.plugDiameter = 32.0 
       self.plugHeight = 10.0 
       self.plugWall = 3.0 
       self.plugFilet = 0.8 
       
       self.cuffHight = 3.0 
       self.cuffCollar = 3.0  
       self.cuffFillet = 0.8       
       
       self.capDiameter = 32.0 
       self.capHeight = 10.0 
       self.capWall = 1.6 
       self.capFilet = 0.79 
       
       self.capClipAngle = 20
       self.capClipCutGap = 1.5
       self.capClipCutAngle = lentoangle(self.capDiameter, self.capClipCutGap)
       self.capClipSnap = 0.6
       
       self.capBottom = 2.4
       self.capClipsCount = 3.0
       self.nozzleCorrection = 0.4
       
       self.outerPerimeterRelation = 0.75
       self.innerPerimeterRelation = 1.0
       
       self.switchCapPlug = False
   
   def setupUi(self):
       self.dialog.setObjectName("Dialog")
       self.dialog.resize(360, 520)
       self.title = QtGui.QLabel(self.dialog)
       self.title.setGeometry(QtCore.QRect(10, 10, 271, 16))
       self.title.setObjectName("title")      
       self.label_plugDiameter = QtGui.QLabel(self.dialog)
       self.label_plugDiameter.setGeometry(QtCore.QRect(10, 50, 80, 16))
       self.label_plugDiameter.setObjectName("label_plugDiameter")
       self.label_plugHeight = QtGui.QLabel(self.dialog)
       self.label_plugHeight.setGeometry(QtCore.QRect(10, 90, 80, 16))
       self.label_plugHeight.setObjectName("label_height")
       self.label_plugWall = QtGui.QLabel(self.dialog)
       self.label_plugWall.setGeometry(QtCore.QRect(10, 130, 80, 16))
       self.label_plugWall.setObjectName("label_plugWall")
       self.label_plugFilet = QtGui.QLabel(self.dialog)
       self.label_plugFilet.setGeometry(QtCore.QRect(10, 170, 80, 16))
       self.label_plugFilet.setObjectName("label_plugFilet")
       self.label_cuffHight = QtGui.QLabel(self.dialog)
       self.label_cuffHight.setGeometry(QtCore.QRect(10, 210, 80, 16))
       self.label_cuffHight.setObjectName("label_cuffHight")
       
       self.label_cuffCollar = QtGui.QLabel(self.dialog)
       self.label_cuffCollar.setGeometry(QtCore.QRect(10, 250, 80, 16))
       self.label_cuffCollar.setObjectName("label_cuffCollar")
       
       self.label_cuffFillet = QtGui.QLabel(self.dialog)
       self.label_cuffFillet.setGeometry(QtCore.QRect(10, 290, 80, 16))
       self.label_cuffFillet.setObjectName("label_cuffFillet")
       
       self.label_nozzleCorrection = QtGui.QLabel(self.dialog)
       self.label_nozzleCorrection.setGeometry(QtCore.QRect(10, 330, 80, 16))
       self.label_nozzleCorrection.setObjectName("label_nozzleCorrection")
       
       self.label_capClipsCount = QtGui.QLabel(self.dialog)
       self.label_capClipsCount.setGeometry(QtCore.QRect(10, 370, 80, 16))
       self.label_capClipsCount.setObjectName("label_capClipsCount")
       
       self.label_capBottom = QtGui.QLabel(self.dialog)
       self.label_capBottom.setGeometry(QtCore.QRect(10, 410, 80, 16))
       self.label_capBottom.setObjectName("label_capBottom")

       ################################
       
       self.switch_PlugCap = QtGui.QCheckBox("Plug/Cap", self.dialog)
       self.switch_PlugCap.stateChanged.connect(self.clickBox)
       self.switch_PlugCap.move(271,10)

       ################################
       
       self.value_plugDiameter = QtGui.QLineEdit(self.dialog)
       self.value_plugDiameter.setGeometry(QtCore.QRect(100, 40, 111, 26))
       self.value_plugDiameter.setObjectName("value_plugDiameter")
       
       self.value_plugHeight = QtGui.QLineEdit(self.dialog)
       self.value_plugHeight.setGeometry(QtCore.QRect(100, 80, 111, 26))
       self.value_plugHeight.setObjectName("value_plugHeight")
       
       self.value_plugWall = QtGui.QLineEdit(self.dialog)
       self.value_plugWall.setGeometry(QtCore.QRect(100, 120, 111, 26))
       self.value_plugWall.setObjectName("value_plugWall")
       
       self.value_plugFilet = QtGui.QLineEdit(self.dialog)
       self.value_plugFilet.setGeometry(QtCore.QRect(100, 160, 111, 26))
       self.value_plugFilet.setObjectName("value_plugFilet")
       
       self.value_cuffHight = QtGui.QLineEdit(self.dialog)
       self.value_cuffHight.setGeometry(QtCore.QRect(100, 200, 111, 26))
       self.value_cuffHight.setObjectName("value_cuffHight")
       
       self.value_cuffCollar = QtGui.QLineEdit(self.dialog)
       self.value_cuffCollar.setGeometry(QtCore.QRect(100, 240, 111, 26))
       self.value_cuffCollar.setObjectName("value_cuffCollar")
       
       self.value_cuffFillet = QtGui.QLineEdit(self.dialog)
       self.value_cuffFillet.setGeometry(QtCore.QRect(100, 280, 111, 26))
       self.value_cuffFillet.setObjectName("value_cuffFillet")
       
       self.value_nozzleCorrection = QtGui.QLineEdit(self.dialog)
       self.value_nozzleCorrection.setGeometry(QtCore.QRect(100, 320, 111, 26))
       self.value_nozzleCorrection.setObjectName("value_nozzleCorrection")
       
       self.value_capClipsCount = QtGui.QLineEdit(self.dialog)
       self.value_capClipsCount.setGeometry(QtCore.QRect(100, 360, 111, 26))
       self.value_capClipsCount.setObjectName("value_capClipsCount")
       
       self.value_capBottom = QtGui.QLineEdit(self.dialog)
       self.value_capBottom.setGeometry(QtCore.QRect(100, 400, 111, 26))
       self.value_capBottom.setObjectName("value_capBottom")
       
       
       
       #############################
       
       self.create = QtGui.QPushButton(self.dialog)
       self.create.setGeometry(QtCore.QRect(50, 460, 83, 26))
       self.create.setObjectName("create")
       
       self.retranslateUiPlug()
       QtCore.QObject.connect(self.create,QtCore.SIGNAL("pressed()"),self.startCreation)
       QtCore.QMetaObject.connectSlotsByName(self.dialog)


   def startCreation(self):
       if self.switchCapPlug:
           self.createProtectionCap()
       else:
           self.createProtectionPlug()
   
   
   def clickBox(self, state):
        if state == QtCore.Qt.Checked:
            self.switchCapPlug = False
            self.refreshValuesFromGui()
            self.switchCapPlug = True
            self.retranslateUiCup()
        else:
            self.switchCapPlug = True
            self.refreshValuesFromGui()
            self.switchCapPlug = False
            self.retranslateUiPlug()

   def retranslateUiCup(self):
       self.dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Parameter Dialog", None, QtGui.QApplication.UnicodeUTF8))
       self.title.setText(QtGui.QApplication.translate("Dialog", "Cap Designer", None, QtGui.QApplication.UnicodeUTF8))
       self.label_plugDiameter.setText(QtGui.QApplication.translate("Dialog", "Cap diameter", None, QtGui.QApplication.UnicodeUTF8))
       self.label_plugHeight.setText(QtGui.QApplication.translate("Dialog", "Cap height", None, QtGui.QApplication.UnicodeUTF8))
       self.label_plugWall.setText(QtGui.QApplication.translate("Dialog", "Cap wall", None, QtGui.QApplication.UnicodeUTF8))
       self.label_plugFilet.setText(QtGui.QApplication.translate("Dialog", "Cap fillet", None, QtGui.QApplication.UnicodeUTF8))
       self.label_cuffHight.setText(QtGui.QApplication.translate("Dialog", "Clip angle", None, QtGui.QApplication.UnicodeUTF8))
       self.label_cuffCollar.setText(QtGui.QApplication.translate("Dialog", "Clip gap mm", None, QtGui.QApplication.UnicodeUTF8))
       self.label_cuffFillet.setText(QtGui.QApplication.translate("Dialog", "Clip snap", None, QtGui.QApplication.UnicodeUTF8))
       self.label_nozzleCorrection.setText(QtGui.QApplication.translate("Dialog", "FDM Nozzle diameter", None, QtGui.QApplication.UnicodeUTF8))
       self.label_capClipsCount.setText(QtGui.QApplication.translate("Dialog", "Clip Count", None, QtGui.QApplication.UnicodeUTF8))
       self.label_capBottom.setText(QtGui.QApplication.translate("Dialog", "Cap Bottom", None, QtGui.QApplication.UnicodeUTF8))
       
       self.value_plugDiameter.setText( '%s' % self.capDiameter )
       self.value_plugHeight.setText( '%s' % self.capHeight )
       self.value_plugWall.setText( '%s' % self.capWall )
       self.value_plugFilet.setText( '%s' % self.capFilet )
       self.value_cuffHight.setText( '%s' % self.capClipAngle )
       self.value_cuffCollar.setText( '%s' % self.capClipCutGap )
       self.value_cuffFillet.setText( '%s' % self.capClipSnap )
       self.value_nozzleCorrection.setText( '%s' % self.nozzleCorrection )
       self.value_capClipsCount.setText( '%s' % self.capClipsCount )
       self.value_capBottom.setText( '%s' % self.capBottom )
       
       self.create.setText(QtGui.QApplication.translate("Dialog", "Create!", None, QtGui.QApplication.UnicodeUTF8))

   def retranslateUiPlug(self):
       self.dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Parameter Dialog", None, QtGui.QApplication.UnicodeUTF8))
       self.title.setText(QtGui.QApplication.translate("Dialog", "Plug Designer", None, QtGui.QApplication.UnicodeUTF8))
       self.label_plugDiameter.setText(QtGui.QApplication.translate("Dialog", "Pulg diameter", None, QtGui.QApplication.UnicodeUTF8))
       self.label_plugHeight.setText(QtGui.QApplication.translate("Dialog", "Plug height", None, QtGui.QApplication.UnicodeUTF8))
       self.label_plugWall.setText(QtGui.QApplication.translate("Dialog", "Plug wall", None, QtGui.QApplication.UnicodeUTF8))
       self.label_plugFilet.setText(QtGui.QApplication.translate("Dialog", "Plug fillet", None, QtGui.QApplication.UnicodeUTF8))
       self.label_cuffHight.setText(QtGui.QApplication.translate("Dialog", "Cuff height", None, QtGui.QApplication.UnicodeUTF8))
       self.label_cuffCollar.setText(QtGui.QApplication.translate("Dialog", "Cuff collar", None, QtGui.QApplication.UnicodeUTF8))
       self.label_cuffFillet.setText(QtGui.QApplication.translate("Dialog", "Cuff fillet", None, QtGui.QApplication.UnicodeUTF8))
       self.label_nozzleCorrection.setText(QtGui.QApplication.translate("Dialog", "FDM Nozzle diameter", None, QtGui.QApplication.UnicodeUTF8))
       self.label_capClipsCount.setText(QtGui.QApplication.translate("Dialog", "!! UNUSED FOR PLUGS !!", None, QtGui.QApplication.UnicodeUTF8))
       self.label_capBottom.setText(QtGui.QApplication.translate("Dialog", "!! UNUSED FOR PLUGS !!", None, QtGui.QApplication.UnicodeUTF8))
       
       self.value_plugDiameter.setText( '%s' % self.plugDiameter )
       self.value_plugHeight.setText( '%s' % self.plugHeight )
       self.value_plugWall.setText( '%s' % self.plugWall )
       self.value_plugFilet.setText( '%s' % self.plugFilet )
       self.value_cuffHight.setText( '%s' % self.cuffHight )
       self.value_cuffCollar.setText( '%s' % self.cuffCollar )
       self.value_cuffFillet.setText( '%s' % self.cuffFillet )
       self.value_nozzleCorrection.setText( '%s' % self.nozzleCorrection )
       self.value_capClipsCount.setText( '%s' % self.capClipsCount )
       self.value_capBottom.setText( '%s' % self.capBottom )
       
       self.create.setText(QtGui.QApplication.translate("Dialog", "Create!", None, QtGui.QApplication.UnicodeUTF8))

   def refreshValuesFromGui(self):
        if self.switchCapPlug:
            self.capDiameter = float(eval(self.value_plugDiameter.text()))
            self.capHeight = float(eval(self.value_plugHeight.text()))
            self.capWall = float(eval(self.value_plugWall.text()))
            self.capFilet = float(eval(self.value_plugFilet.text()))
            self.capClipAngle = float(eval(self.value_cuffHight.text()))
            self.capClipCutGap = float(eval(self.value_cuffCollar.text()))
            self.capClipCutAngle = lentoangle(self.capDiameter, self.capClipCutGap)
            self.capClipSnap = float(eval(self.value_cuffFillet.text()))
            self.nozzleCorrection = float(eval(self.value_nozzleCorrection.text()))
            self.capClipsCount = float(eval(self.value_capClipsCount.text()))
            self.capBottom = float(eval(self.value_capBottom.text()))
        else:
            self.plugDiameter = float(eval(self.value_plugDiameter.text()))
            self.plugHeight = float(eval(self.value_plugHeight.text()))
            self.plugWall = float(eval(self.value_plugWall.text()))
            self.plugFilet = float(eval(self.value_plugFilet.text()))
            self.cuffHight = float(eval(self.value_cuffHight.text()))
            self.cuffCollar = float(eval(self.value_cuffCollar.text()))
            self.cuffFillet = float(eval(self.value_cuffFillet.text()))
            self.nozzleCorrection = float(eval(self.value_nozzleCorrection.text()))
            self.capClipsCount = float(eval(self.value_capClipsCount.text()))
            self.capBottom = float(eval(self.value_capBottom.text()))

   def createProtectionPlug(self):
      self.refreshValuesFromGui()
      modelName = "ProtectionPlug_new"
      Plug = { 'd' : self.plugDiameter - (self.nozzleCorrection*self.outerPerimeterRelation), 'h' : self.plugHeight , 'w' : self.plugWall, 'f' : self.plugFilet}
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
      FreeCAD.ActiveDocument.addObject("Part::Fillet","ProtectionPlug")
      ProtectionPlugObj = App.ActiveDocument.ActiveObject
      ProtectionPlugObj.Base = CutObj
      __fillets__ = []
      __fillets__.append((1,Plug['f'],Plug['f']))
      __fillets__.append((2,Plug['f'],Plug['f']))
      __fillets__.append((7,Cuff['f'],Cuff['f']))
      __fillets__.append((9,Cuff['f'],Cuff['f']))
      ProtectionPlugObj.Edges = __fillets__
      del __fillets__
      Gui.ActiveDocument.getObject(CutObj.Name).Visibility = False
      Gui.ActiveDocument.getObject(ProtectionPlugObj.Name).LineColor = Gui.ActiveDocument.getObject(CutObj.Name).LineColor
      Gui.ActiveDocument.getObject(ProtectionPlugObj.Name).PointColor = Gui.ActiveDocument.getObject(CutObj.Name).PointColor
      Gui.activeDocument().resetEdit()

      App.ActiveDocument.recompute()
      App.ActiveDocument.addObject('Part::Feature','ProtectionPlugFinal').Shape=ProtectionPlugObj.Shape.removeSplitter()
      Gui.ActiveDocument.getObject(ProtectionPlugObj.Name).Visibility = False
      App.ActiveDocument.recompute()

      Gui.SendMsgToActiveView("ViewFit")

      App.ActiveDocument.recompute()
      Gui.SendMsgToActiveView("ViewFit")

   def createProtectionCap(self):
      d = self.capDiameter + ( self.nozzleCorrection * self.innerPerimeterRelation )
      self.refreshValuesFromGui()
      modelName = "ProtectionCap_new"
      Gui.activateWorkbench("PartWorkbench")
      App.ActiveDocument.addObject("Part::Cylinder","Cap")
      CapObbj = App.ActiveDocument.ActiveObject
      CapObbj.Radius = d/2 + self.capWall
      CapObbj.Height = self.capHeight + self.capBottom

      FreeCAD.ActiveDocument.addObject("Part::Fillet","ProtectionCap")
      ProtectionCapObj = App.ActiveDocument.ActiveObject
      ProtectionCapObj.Base = CapObbj
      __fillets__ = []
      __fillets__.append((1,self.cuffFillet,self.cuffFillet))
      __fillets__.append((3,self.cuffFillet,self.cuffFillet))
      ProtectionCapObj.Edges = __fillets__
      del __fillets__
      Gui.ActiveDocument.getObject(CapObbj.Name).Visibility = False

      App.ActiveDocument.addObject("Part::Cylinder","CupFullCut")
      CupFullCutObj = App.ActiveDocument.ActiveObject
      CupFullCutObj.Radius = d/2 - self.capClipSnap
      CupFullCutObj.Height = self.capHeight

      App.ActiveDocument.addObject("Part::Cylinder","CupFullCutB")
      CupFullCutBObj = App.ActiveDocument.ActiveObject
      CupFullCutBObj.Radius = d/2 
      CupFullCutBObj.Height = self.capHeight - self.capClipSnap

      cut1Obj = self.createClampSegemet()
      cut2Obj = self.createClampCut()
      deltaHight = self.capHeight - 8
      if (self.capHeight < 5):
          deltaHight = 0
      elif (self.capHeight <= 9 ) :
          deltaHight = 1
      cut2Obj.Placement = App.Placement(App.Vector(0,0,deltaHight),App.Rotation(App.Vector(0,0,1),0))
      App.activeDocument().addObject("Part::MultiFuse","CapCutFusion")
      CapCutFusionObj = App.ActiveDocument.ActiveObject
      CapCutFusionObj.Shapes = [cut1Obj,cut2Obj,CupFullCutObj,CupFullCutBObj,]
      Gui.ActiveDocument.getObject(cut1Obj.Name).Visibility = False
      Gui.ActiveDocument.getObject(cut2Obj.Name).Visibility = False
      Gui.ActiveDocument.getObject(CupFullCutObj.Name).Visibility = False
      Gui.ActiveDocument.getObject(CupFullCutBObj.Name).Visibility = False
      CapCutFusionObj.Placement = App.Placement(App.Vector(0,0,self.capBottom),App.Rotation(App.Vector(0,0,1),0))
      App.activeDocument().addObject("Part::Cut","ProtectionCapCommon")
      ProtectionCapFinalObj = App.ActiveDocument.ActiveObject
      ProtectionCapFinalObj.Base = ProtectionCapObj
      ProtectionCapFinalObj.Tool = CapCutFusionObj
      Gui.ActiveDocument.getObject(ProtectionCapObj.Name).Visibility = False
      Gui.ActiveDocument.getObject(CapCutFusionObj.Name).Visibility = False
      App.ActiveDocument.recompute()
      App.ActiveDocument.addObject('Part::Feature','ProtectionCapFinal').Shape=ProtectionCapFinalObj.Shape.removeSplitter()
      Gui.ActiveDocument.getObject(ProtectionCapFinalObj.Name).Visibility = False
      App.ActiveDocument.recompute()

      Gui.SendMsgToActiveView("ViewFit")

   def createClampSegemet(self):
      d = self.capDiameter + ( self.nozzleCorrection * self.innerPerimeterRelation )
      r=d/2
      w=self.capWall
      h=self.capHeight
      a=120 - self.capClipAngle
      b=self.capClipCutAngle
      deltaA = self.capClipAngle # + b
      Gui.activateWorkbench("PartWorkbench")
      App.ActiveDocument.addObject("Part::Cylinder","ClampSegmentA")
      ClampSegmentAObj = App.ActiveDocument.ActiveObject
      ClampSegmentAObj.Angle = a if (self.capClipsCount > 1) else 120
      ClampSegmentAObj.Radius = r
      ClampSegmentAObj.Height = h
      ClampSegmentAObj.Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0+deltaA))
      App.ActiveDocument.addObject("Part::Cylinder","ClampSegmentB")
      ClampSegmentBObj = App.ActiveDocument.ActiveObject
      ClampSegmentBObj.Angle = a if (self.capClipsCount > 2) else 120
      ClampSegmentBObj.Radius = r
      ClampSegmentBObj.Height = h
      ClampSegmentBObj.Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),120+deltaA))
      App.ActiveDocument.addObject("Part::Cylinder","ClampSegmentC")
      ClampSegmentCObj = App.ActiveDocument.ActiveObject
      ClampSegmentCObj.Angle = a
      ClampSegmentCObj.Radius = r
      ClampSegmentCObj.Height = h
      ClampSegmentCObj.Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),240+deltaA))
      
      App.activeDocument().addObject("Part::MultiFuse","Fusion")
      FusionObj = App.ActiveDocument.ActiveObject
      FusionObj.Shapes = [ClampSegmentAObj,ClampSegmentBObj,ClampSegmentCObj,]
      Gui.ActiveDocument.getObject(ClampSegmentAObj.Name).Visibility = False
      Gui.ActiveDocument.getObject(ClampSegmentBObj.Name).Visibility = False
      Gui.ActiveDocument.getObject(ClampSegmentCObj.Name).Visibility = False
      return FusionObj

   def createClampCut(self):
      d = self.capDiameter + ( self.nozzleCorrection * self.innerPerimeterRelation )
      r=d/2 + self.capWall
      w=self.capWall
      h=self.capHeight
      a=self.capClipAngle
      b=self.capClipCutAngle
      Gui.activateWorkbench("PartWorkbench")
      s=0
      App.ActiveDocument.addObject("Part::Cylinder","ClampCutAa")
      ClampCutAaObj = App.ActiveDocument.ActiveObject
      ClampCutAaObj.Angle = b
      ClampCutAaObj.Radius = r
      ClampCutAaObj.Height = h
      ClampCutAaObj.Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),s))
      App.ActiveDocument.addObject("Part::Cylinder","ClampCutAb")
      ClampCutAbObj = App.ActiveDocument.ActiveObject
      ClampCutAbObj.Angle = b
      ClampCutAbObj.Radius = r
      ClampCutAbObj.Height = h
      ClampCutAbObj.Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),s+a-b))
      s=120
      App.ActiveDocument.addObject("Part::Cylinder","ClampCutBa")
      ClampCutBaObj = App.ActiveDocument.ActiveObject
      ClampCutBaObj.Angle = b
      ClampCutBaObj.Radius = r if (self.capClipsCount > 1) else 1
      ClampCutBaObj.Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),s))
      App.ActiveDocument.addObject("Part::Cylinder","ClampCutBb")
      ClampCutBbObj = App.ActiveDocument.ActiveObject
      ClampCutBbObj.Angle = b
      ClampCutBbObj.Radius = r if (self.capClipsCount > 1) else 1
      ClampCutBbObj.Height = h
      ClampCutBbObj.Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),s+a-b))
      s=240
      App.ActiveDocument.addObject("Part::Cylinder","ClampCutCa")
      ClampCutCaObj = App.ActiveDocument.ActiveObject
      ClampCutCaObj.Angle = b
      ClampCutCaObj.Radius = r if (self.capClipsCount > 2) else 1
      ClampCutCaObj.Height = h
      ClampCutCaObj.Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),s))
      App.ActiveDocument.addObject("Part::Cylinder","ClampCutCb")
      ClampCutCbObj = App.ActiveDocument.ActiveObject
      ClampCutCbObj.Angle = b
      ClampCutCbObj.Radius = r if (self.capClipsCount > 2) else 1
      ClampCutCbObj.Height = h
      ClampCutCbObj.Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),s+a-b))
      App.activeDocument().addObject("Part::MultiFuse","ClampCutFusion")
      ClampCutFusion = App.ActiveDocument.ActiveObject
      ClampCutFusion.Shapes = [ClampCutAaObj,ClampCutAbObj,ClampCutBaObj,ClampCutBbObj,ClampCutCaObj,ClampCutCbObj,]
      Gui.ActiveDocument.getObject(ClampCutAaObj.Name).Visibility = False
      Gui.ActiveDocument.getObject(ClampCutAbObj.Name).Visibility = False
      Gui.ActiveDocument.getObject(ClampCutBaObj.Name).Visibility = False
      Gui.ActiveDocument.getObject(ClampCutBbObj.Name).Visibility = False
      Gui.ActiveDocument.getObject(ClampCutCaObj.Name).Visibility = False
      Gui.ActiveDocument.getObject(ClampCutCbObj.Name).Visibility = False
      return ClampCutFusion

class plane():
   def __init__(self):
       self.d = QtGui.QWidget()
       self.ui = Ui_Dialog(self.d)
       self.ui.setupUi()
       self.d.show()

def pytagoras(h,a):
    return sqrt(pow(float(h),2)+pow(float(a),2))

def lentoangle(h,a):
    return degrees(sin(float(a)/float(h)))

GoForIt = plane()
