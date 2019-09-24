from PySide import QtCore, QtGui
import FreeCAD, Part 

class Ui_Dialog(object):
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(380, 430)
        self.title = QtGui.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(10, 10, 390, 16))
        self.title.setObjectName("title")
        
        self.label_diceCubeSize = QtGui.QLabel(Dialog)
        self.label_diceCubeSize.setGeometry(QtCore.QRect(10, 50, 120, 16))
        self.label_diceCubeSize.setObjectName("label_diceCubeSize")
        
        
        self.label_diceSphereDeltaPercent = QtGui.QLabel(Dialog)
        self.label_diceSphereDeltaPercent.setGeometry(QtCore.QRect(10, 90, 120, 16))
        self.label_diceSphereDeltaPercent.setObjectName("label_diceSphereDeltaPercent")
        
        self.label_pointSphereRadius = QtGui.QLabel(Dialog)
        self.label_pointSphereRadius.setGeometry(QtCore.QRect(10, 130, 120, 16))
        self.label_pointSphereRadius.setObjectName("label_pointSphereRadius")
        
        self.label_pointSphereDistance = QtGui.QLabel(Dialog)
        self.label_pointSphereDistance.setGeometry(QtCore.QRect(10, 170, 120, 16))
        self.label_pointSphereDistance.setObjectName("label_pointSphereDistance")
        
        self.label_pointSphereSixH = QtGui.QLabel(Dialog)
        self.label_pointSphereSixH.setGeometry(QtCore.QRect(10, 210, 120, 16))
        self.label_pointSphereSixH.setObjectName("label_pointSphereSixH")
        
        self.label_pointSphereSixV = QtGui.QLabel(Dialog)
        self.label_pointSphereSixV.setGeometry(QtCore.QRect(10, 250, 120, 16))
        self.label_pointSphereSixV.setObjectName("label_pointSphereSixV")
        
        self.label_shellThikness = QtGui.QLabel(Dialog)
        self.label_shellThikness.setGeometry(QtCore.QRect(10, 290, 120, 16))
        self.label_shellThikness.setObjectName("label_shellThikness")
        
        self.label_positionShift = QtGui.QLabel(Dialog)
        self.label_positionShift.setGeometry(QtCore.QRect(10, 330, 120, 16))
        self.label_positionShift.setObjectName("label_positionShift")
        #############################

        self.value_diceCubeSize = QtGui.QLineEdit(Dialog)
        self.value_diceCubeSize.setGeometry(QtCore.QRect(160, 40, 180, 26))
        self.value_diceCubeSize.setObjectName("value_diceCubeSize")
        
        self.value_diceSphereDeltaPercent = QtGui.QLineEdit(Dialog)
        self.value_diceSphereDeltaPercent.setGeometry(QtCore.QRect(160, 80, 180, 26))
        self.value_diceSphereDeltaPercent.setObjectName("value_diceSphereDeltaPercent")
        
        self.value_pointSphereRadius = QtGui.QLineEdit(Dialog)
        self.value_pointSphereRadius.setGeometry(QtCore.QRect(160, 120, 180, 26))
        self.value_pointSphereRadius.setObjectName("value_pointSphereRadius")
        
        self.value_pointSphereDistance = QtGui.QLineEdit(Dialog)
        self.value_pointSphereDistance.setGeometry(QtCore.QRect(160, 160, 180, 26))
        self.value_pointSphereDistance.setObjectName("value_pointSphereDistance")
        
        self.value_pointSphereSixH = QtGui.QLineEdit(Dialog)
        self.value_pointSphereSixH.setGeometry(QtCore.QRect(160, 200, 180, 26))
        self.value_pointSphereSixH.setObjectName("value_pointSphereSixH")
        
        self.value_pointSphereSixV = QtGui.QLineEdit(Dialog)
        self.value_pointSphereSixV.setGeometry(QtCore.QRect(160, 240, 180, 26))
        self.value_pointSphereSixV.setObjectName("value_pointSphereSixV")
        
        self.value_shellThikness = QtGui.QLineEdit(Dialog)
        self.value_shellThikness.setGeometry(QtCore.QRect(160, 280, 180, 26))
        self.value_shellThikness.setObjectName("value_shellThikness")
        
        self.value_positionShift = QtGui.QLineEdit(Dialog)
        self.value_positionShift.setGeometry(QtCore.QRect(160, 320, 180, 26))
        self.value_positionShift.setObjectName("value_positionShift")

        #############################
        
        self.create = QtGui.QPushButton(Dialog)
        self.create.setGeometry(QtCore.QRect(50, 380, 83, 26))
        self.create.setObjectName("create")
        
        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.create,QtCore.SIGNAL("pressed()"),self.createDice)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Parameter Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.title.setText(QtGui.QApplication.translate("Dialog", "Dice Parameter ( by Rolf Weruminger weruminger@gmail.de )", None, QtGui.QApplication.UnicodeUTF8))
        self.label_diceCubeSize.setText(QtGui.QApplication.translate("Dialog", "Size (mm)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_diceSphereDeltaPercent.setText(QtGui.QApplication.translate("Dialog", "Sphere Cut Delta (+/-%)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_pointSphereRadius.setText(QtGui.QApplication.translate("Dialog", "Point Radius (mm)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_pointSphereDistance.setText(QtGui.QApplication.translate("Dialog", "Point Distance Multiplier", None, QtGui.QApplication.UnicodeUTF8))
        self.label_pointSphereSixH.setText(QtGui.QApplication.translate("Dialog", "SIX H Divider", None, QtGui.QApplication.UnicodeUTF8))
        self.label_pointSphereSixV.setText(QtGui.QApplication.translate("Dialog", "SIX V Multiplier", None, QtGui.QApplication.UnicodeUTF8))
        self.label_shellThikness.setText(QtGui.QApplication.translate("Dialog", "Shell Thikness", None, QtGui.QApplication.UnicodeUTF8))
        self.label_positionShift.setText(QtGui.QApplication.translate("Dialog", "Position shift", None, QtGui.QApplication.UnicodeUTF8))
        
        self.value_diceCubeSize.setText( '%s' % self.diceCubeSize )
        self.value_diceSphereDeltaPercent.setText( '%s' % self.diceSphereDeltaPercent )
        self.value_pointSphereRadius.setText( 'self.diceCubeSize * 0.10' )
        self.value_pointSphereDistance.setText( '%s' % self.pointSphereDistanceM )
        self.value_pointSphereSixH.setText( '%s' % self.pointSphereSixH )
        self.value_pointSphereSixV.setText( '%s' % self.pointSphereSixV )
        self.value_shellThikness.setText( 'self.pointSphereRadius * 2/3' )
        self.value_positionShift.setText( '%s' % self.positionShift )
        
        self.create.setText(QtGui.QApplication.translate("Dialog", "Create!", None, QtGui.QApplication.UnicodeUTF8))
 
    def refreshValuesFromGui(self):
        self.diceCubeSize = float(eval(self.value_diceCubeSize.text()))
        self.diceSphereDeltaPercent = float(eval(self.value_diceSphereDeltaPercent.text()))
        self.pointSphereRadius = float(eval(self.value_pointSphereRadius.text()))
        self.pointSphereDistanceM = float(eval(self.value_pointSphereDistance.text()))
        self.pointSphereSixH = float(eval(self.value_pointSphereSixH.text()))
        self.pointSphereSixV = float(eval(self.value_pointSphereSixV.text()))
        self.shellThikness = float(eval(self.value_shellThikness.text()))
        self.pointSphereDistance = self.pointSphereRadius * self.pointSphereDistanceM
        self.halfLength = self.diceCubeSize/2
        self.diceSphereRadius = math.sqrt(2) * self.halfLength
        self.diceSphereDelta = self.diceSphereDeltaPercent * self.diceSphereRadius/100
        self.positionShift = eval(self.value_positionShift.text())
        if ( not (isinstance(self.positionShift,list) and len(self.positionShift)>=3)):
            self.positionShift=[0.0,0.0,0.0]


    def __init__(self):
        self.diceSphereDeltaPercent = 0
        self.diceCubeSize = 30.0
        self.pointSphereRadius = 3.0
        self.pointSphereDistanceM = 2.2
        self.pointSphereSixH = 1.25
        self.pointSphereSixV = 1.2
        self.pointSphereDistance = self.pointSphereRadius * self.pointSphereDistanceM
        self.halfLength = self.diceCubeSize/2
        self.diceSphereRadius = math.sqrt(2) * self.halfLength
        self.diceSphereDelta = self.diceSphereDeltaPercent * self.diceSphereRadius/100
        self.shellThikness = self.pointSphereRadius * 2 / 3
        self.positionShift = [0.0,0.0,0.0]
    def createPoints(self):
        pointSphereArray = [[],[],[],[],[],[]]
        App.activeDocument().addObject("Part::MultiFuse","PointSphereFusion")
        locPointSphereFusion = App.ActiveDocument.ActiveObject
        pointSphereCollection = []
        for i in range(0, 6):
            for j in range(0, i+1):
                App.ActiveDocument.addObject("Part::Sphere","PointSphere")
                pointSphereArray[i].append(App.ActiveDocument.ActiveObject)
                pointSphereArray[i][j].Radius = self.pointSphereRadius
                pointSphereCollection.append(pointSphereArray[i][j])
                Gui.ActiveDocument.getObject(pointSphereArray[i][j].Name).Visibility = False
            if i == 5: # six
                helpDistanceH = self.pointSphereDistance / self.pointSphereSixH
                helpDistanceV = self.pointSphereDistance * self.pointSphereSixV
                pointSphereArray[i][0].Placement = App.Placement(App.Vector(helpDistanceH,0,+self.halfLength),App.Rotation(App.Vector(0,0,1),0))
                pointSphereArray[i][1].Placement = App.Placement(App.Vector(helpDistanceH,helpDistanceV,+self.halfLength),App.Rotation(App.Vector(0,0,1),0))
                pointSphereArray[i][2].Placement = App.Placement(App.Vector(helpDistanceH,-helpDistanceV,+self.halfLength),App.Rotation(App.Vector(0,0,1),0))
                pointSphereArray[i][3].Placement = App.Placement(App.Vector(-helpDistanceH,0,+self.halfLength),App.Rotation(App.Vector(0,0,1),0))
                pointSphereArray[i][4].Placement = App.Placement(App.Vector(-helpDistanceH,helpDistanceV,+self.halfLength),App.Rotation(App.Vector(0,0,1),0))
                pointSphereArray[i][5].Placement = App.Placement(App.Vector(-helpDistanceH,-helpDistanceV,+self.halfLength),App.Rotation(App.Vector(0,0,1),0))
            elif i == 0: # one
                pointSphereArray[i][0].Placement = App.Placement(App.Vector(0,0,-self.halfLength),App.Rotation(App.Vector(0,0,1),0))
            elif i == 4: # fife
                pointSphereArray[i][0].Placement = App.Placement(App.Vector(-self.halfLength,0,0),App.Rotation(App.Vector(0,0,1),0))
                pointSphereArray[i][1].Placement = App.Placement(App.Vector(-self.halfLength,self.pointSphereDistance,self.pointSphereDistance),App.Rotation(App.Vector(0,0,1),0))
                pointSphereArray[i][2].Placement = App.Placement(App.Vector(-self.halfLength,-self.pointSphereDistance,self.pointSphereDistance),App.Rotation(App.Vector(0,0,1),0))
                pointSphereArray[i][3].Placement = App.Placement(App.Vector(-self.halfLength,self.pointSphereDistance,-self.pointSphereDistance),App.Rotation(App.Vector(0,0,1),0))
                pointSphereArray[i][4].Placement = App.Placement(App.Vector(-self.halfLength,-self.pointSphereDistance,-self.pointSphereDistance),App.Rotation(App.Vector(0,0,1),0))
            elif i == 1: # two
                pointSphereArray[i][0].Placement = App.Placement(App.Vector(+self.halfLength,self.pointSphereDistance,self.pointSphereDistance),App.Rotation(App.Vector(0,0,1),0))
                pointSphereArray[i][1].Placement = App.Placement(App.Vector(+self.halfLength,-self.pointSphereDistance,-self.pointSphereDistance),App.Rotation(App.Vector(0,0,1),0))
            elif i == 3: # four
                pointSphereArray[i][0].Placement = App.Placement(App.Vector(self.pointSphereDistance,+self.halfLength,self.pointSphereDistance),App.Rotation(App.Vector(0,0,1),0))
                pointSphereArray[i][1].Placement = App.Placement(App.Vector(-self.pointSphereDistance,+self.halfLength,self.pointSphereDistance),App.Rotation(App.Vector(0,0,1),0))
                pointSphereArray[i][2].Placement = App.Placement(App.Vector(self.pointSphereDistance,+self.halfLength,-self.pointSphereDistance),App.Rotation(App.Vector(0,0,1),0))
                pointSphereArray[i][3].Placement = App.Placement(App.Vector(-self.pointSphereDistance,+self.halfLength,-self.pointSphereDistance),App.Rotation(App.Vector(0,0,1),0))
            elif i == 2: # three
                pointSphereArray[i][0].Placement = App.Placement(App.Vector(0,-self.halfLength,0),App.Rotation(App.Vector(0,0,1),0))
                pointSphereArray[i][1].Placement = App.Placement(App.Vector(self.pointSphereDistance,-self.halfLength,self.pointSphereDistance),App.Rotation(App.Vector(0,0,1),0))
                pointSphereArray[i][2].Placement = App.Placement(App.Vector(-self.pointSphereDistance,-self.halfLength,-self.pointSphereDistance),App.Rotation(App.Vector(0,0,1),0))
        locPointSphereFusion.Shapes=pointSphereCollection
        return locPointSphereFusion

    def createCommonDice(self, ccSize, ccLabel):
        App.ActiveDocument.addObject("Part::Box","SubDiceCube")
        locColorDiceCube = App.ActiveDocument.ActiveObject
        helpSize = ccSize - (self.pointSphereRadius *0.5)
        helpHalfLength = helpSize/2
        locColorDiceCube.Length = helpSize
        locColorDiceCube.Width = helpSize
        locColorDiceCube.Height = helpSize
        locColorDiceCube.Placement = App.Placement(App.Vector(-helpHalfLength,-helpHalfLength,-helpHalfLength),App.Rotation(App.Vector(0,0,1),0))

        helpDiceSphereRadius = math.sqrt(2) * helpHalfLength
        helpDiceSphereDelta = self.diceSphereDeltaPercent * helpDiceSphereRadius/100
        App.ActiveDocument.addObject("Part::Sphere","SubDiceSphere")
        locColorDiceSphere = App.ActiveDocument.ActiveObject
        locColorDiceSphere.Radius = helpDiceSphereRadius+helpDiceSphereDelta

        App.activeDocument().addObject("Part::MultiCommon",ccLabel)
        locColorDiceB = App.ActiveDocument.ActiveObject
        locColorDiceB.Shapes = [locColorDiceSphere,locColorDiceCube,]

        Gui.ActiveDocument.getObject(locColorDiceSphere.Name).Visibility = False
        Gui.ActiveDocument.getObject(locColorDiceCube.Name).Visibility = False
        return locColorDiceB

    def createDice(self):
        self.refreshValuesFromGui()
        pointSphereFusion = self.createPoints()
        diceCommon = self.createCommonDice(self.diceCubeSize, "DiceCommon")

        App.activeDocument().addObject("Part::Cut","Dice")
        DiceObj = App.ActiveDocument.ActiveObject
        DiceObj.Base = diceCommon
        DiceObj.Tool = pointSphereFusion
        Gui.ActiveDocument.getObject(diceCommon.Name).Visibility = False
        Gui.ActiveDocument.getObject(pointSphereFusion.Name).Visibility = False
        App.ActiveDocument.recompute()

        App.ActiveDocument.addObject('Part::Feature','SingleDice').Shape=DiceObj.Shape.removeSplitter()
        singleDiceObj = App.ActiveDocument.ActiveObject
        singleDiceObj.Placement = App.Placement(App.Vector(self.positionShift[0],self.positionShift[1],self.positionShift[2]),App.Rotation(App.Vector(0,0,1),0))
        
        Gui.ActiveDocument.getObject(DiceObj.Name).Visibility = False
        
        App.ActiveDocument.recompute()

        helpSize = self.diceCubeSize - self.shellThikness
        colorDiceBCommon = self.createCommonDice(helpSize, "ColorDiceBCommon")
        App.ActiveDocument.recompute()

        App.activeDocument().addObject("Part::Cut","ColorDiceACommon")
        colorDiceACommon = App.ActiveDocument.ActiveObject
        colorDiceACommon.Base = DiceObj
        colorDiceACommon.Tool = colorDiceBCommon
        Gui.ActiveDocument.getObject(DiceObj.Name).Visibility = False
        Gui.ActiveDocument.getObject(colorDiceBCommon.Name).Visibility = False
        App.ActiveDocument.recompute()

        App.ActiveDocument.addObject('Part::Feature','ColorDiceA').Shape=colorDiceACommon.Shape.removeSplitter()
        colorDiceA = App.ActiveDocument.ActiveObject
        App.ActiveDocument.recompute()
       
        Gui.ActiveDocument.getObject(colorDiceACommon.Name).Visibility = False
        colorDiceA.Placement = App.Placement(App.Vector((self.diceCubeSize * 1.5) + self.positionShift[0],self.positionShift[1],self.positionShift[2]),App.Rotation(App.Vector(0,0,1),0))
        App.ActiveDocument.recompute()

        App.ActiveDocument.addObject('Part::Feature','ColorDiceB').Shape=colorDiceBCommon.Shape.removeSplitter()
        colorDiceB = App.ActiveDocument.ActiveObject
        
        Gui.ActiveDocument.getObject(colorDiceACommon.Name).Visibility = False
        colorDiceB.Placement = App.Placement(App.Vector((self.diceCubeSize * 3) + self.positionShift[0],self.positionShift[1],self.positionShift[2]),App.Rotation(App.Vector(0,0,1),0))

        App.ActiveDocument.recompute()


class plane():
   def __init__(self):
       self.d = QtGui.QWidget()
       self.ui = Ui_Dialog()
       self.ui.setupUi(self.d)
       self.d.show()

GoForIt = plane()

