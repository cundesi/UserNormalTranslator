#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import pymel.core as pm

import inspect
if not hasattr(sys.modules[__name__], '__file__'):
    __file__ = inspect.getfile(inspect.currentframe())

homedir = os.path.dirname(__file__)
if not homedir in sys.path:
    sys.path.append(homedir)

from Qt import QtGui
from Qt import QtWidgets
from Qt import QtCore
from UserNormalTranslatorUI import Ui_userNormalTranslatorWindow


class userNormalTranslatorWindow(Ui_userNormalTranslatorWindow):
    def __init__(self, parent=None):
        super(userNormalTranslatorWindow, self).__init__(parent)
        self.setupUi(self)
        self.center = None
        self.pBtnX.clicked.connect(self.setXNormal)
        self.pBtnXValue1.clicked.connect(self.setXNormalValue1)
        self.pBtnXValue2.clicked.connect(self.setXNormalValue2)
        self.pBtnXValue3.clicked.connect(self.setXNormalValue3)
        self.pBtnXValue4.clicked.connect(self.setXNormalValue4)
        self.pBtnY.clicked.connect(self.setYNormal)
        self.pBtnYValue1.clicked.connect(self.setYNormalValue1)
        self.pBtnYValue2.clicked.connect(self.setYNormalValue2)
        self.pBtnYValue3.clicked.connect(self.setYNormalValue3)
        self.pBtnYValue4.clicked.connect(self.setYNormalValue4)
        self.pBtnZ.clicked.connect(self.setZNormal)
        self.pBtnZValue1.clicked.connect(self.setZNormalValue1)
        self.pBtnZValue2.clicked.connect(self.setZNormalValue2)
        self.pBtnZValue3.clicked.connect(self.setZNormalValue3)
        self.pBtnZValue4.clicked.connect(self.setZNormalValue4)
        self.pBtnResetValue.clicked.connect(self.resetNormalValue)
        self.rdBtnAdd.clicked.connect(self.resetNormalValue)
        self.rdBtnMultiply.clicked.connect(self.resetNormalValue)
        self.pBtnResetNormal.clicked.connect(self.resetNormal)
        self.pBtnRatioValue1.clicked.connect(self.setShperizeValue1)
        self.pBtnRatioValue2.clicked.connect(self.setShperizeValue2)
        self.pBtnRatioValue3.clicked.connect(self.setShperizeValue3)
        self.pBtnRatioValue4.clicked.connect(self.setShperizeValue4)
        self.pBtnSpherizeApply.clicked.connect(self.spherizerNormal)
        self.pBtnCreateCenter.clicked.connect(self.crerateCenterFn)

    def addNormal(self, xValue=0, yValue=0, zValue=0):
        for v in pm.filterExpand(ex=True, sm=31):
            temp_normal = pm.polyNormalPerVertex(v, q=True, xyz=True)[:3]
            pm.polyNormalPerVertex(
                v,
                xyz=((temp_normal[0] + xValue), (temp_normal[1] + yValue), (temp_normal[2] + zValue))
            )

    def mulNormal(self, xValue=1, yValue=1, zValue=1):
        for v in pm.filterExpand(ex=True, sm=31):
            temp_normal = pm.polyNormalPerVertex(v, q=True, xyz=True)[:3]
            pm.polyNormalPerVertex(
                v,
                xyz=((temp_normal[0] * xValue), (temp_normal[1] * yValue), (temp_normal[2] * zValue))
            )

    def setXNormal(self):
        XValue = self.dbsBoxX.value()
        if self.rdBtnAdd.isChecked():
            self.addNormal(xValue=XValue)
        else:
            self.mulNormal(xValue=XValue)

    def setXNormalValue1(self):
        self.resetNormalValue()
        self.dbsBoxX.setValue(-0.1)
        self.setXNormal()

    def setXNormalValue2(self):
        self.resetNormalValue()
        self.dbsBoxX.setValue(-0.5)
        self.setXNormal()

    def setXNormalValue3(self):
        self.resetNormalValue()
        self.dbsBoxX.setValue(0.5)
        self.setXNormal()

    def setXNormalValue4(self):
        self.resetNormalValue()
        self.dbsBoxX.setValue(0.1)
        self.setXNormal()

    def setYNormal(self):
        YValue = self.dbsBoxY.value()
        if self.rdBtnAdd.isChecked():
            self.addNormal(yValue=YValue)
        else:
            self.mulNormal(yValue=YValue)

    def setYNormalValue1(self):
        self.resetNormalValue()
        self.dbsBoxY.setValue(-0.1)
        self.setYNormal()

    def setYNormalValue2(self):
        self.resetNormalValue()
        self.dbsBoxY.setValue(-0.5)
        self.setYNormal()

    def setYNormalValue3(self):
        self.resetNormalValue()
        self.dbsBoxY.setValue(0.5)
        self.setYNormal()

    def setYNormalValue4(self):
        self.resetNormalValue()
        self.dbsBoxY.setValue(0.1)
        self.setYNormal()

    def setZNormal(self):
        ZValue = self.dbsBoxZ.value()
        if self.rdBtnAdd.isChecked():
            self.addNormal(zValue=ZValue)
        else:
            self.mulNormal(zValue=ZValue)

    def setZNormalValue1(self):
        self.resetNormalValue()
        self.dbsBoxZ.setValue(-0.1)
        self.setZNormal()

    def setZNormalValue2(self):
        self.resetNormalValue()
        self.dbsBoxZ.setValue(-0.5)
        self.setZNormal()

    def setZNormalValue3(self):
        self.resetNormalValue()
        self.dbsBoxZ.setValue(0.5)
        self.setZNormal()

    def setZNormalValue4(self):
        self.resetNormalValue()
        self.dbsBoxZ.setValue(0.1)
        self.setZNormal()

    def resetNormalValue(self):
        if self.rdBtnAdd.isChecked():
            self.dbsBoxX.setValue(0)
            self.dbsBoxY.setValue(0)
            self.dbsBoxZ.setValue(0)
        else:
            self.dbsBoxX.setValue(1)
            self.dbsBoxY.setValue(1)
            self.dbsBoxZ.setValue(1)

    def resetNormal(self):
        pm.polyNormalPerVertex(ufn=True)

    def crerateCenterFn(self):
        if self.center:
            pm.delete(self.center)
        self.center = pm.spaceLocator(name='center')

    def spherizerNormal(self):
        ratio = self.dbsBoxRatio.value()
        vetList = pm.filterExpand(ex=True, sm=31)
        print self.center
        if self.center:
            obj = self.center
        else:
            obj = pm.PyNode(vetList[0].split('.')[0])
        pos = pm.dt.Point((obj.getBoundingBoxMax() + obj.getBoundingBoxMin()) / 2)
        print pos
        for v in vetList:
            vPos = pm.PyNode(v).getPosition(space='world')
            temp_normal = pm.polyNormalPerVertex(v, q=True, xyz=True)[:3]
            new_normal = (vPos - pos) * ratio + pm.dt.Point(temp_normal) * (1 - ratio)
            pm.polyNormalPerVertex(v, xyz=new_normal)

    def setShperizeValue1(self):
        self.dbsBoxRatio.setValue(0.1)
        self.spherizerNormal()

    def setShperizeValue2(self):
        self.dbsBoxRatio.setValue(0.25)
        self.spherizerNormal()

    def setShperizeValue3(self):
        self.dbsBoxRatio.setValue(0.5)
        self.spherizerNormal()

    def setShperizeValue4(self):
        self.dbsBoxRatio.setValue(0.75)
        self.spherizerNormal()


def main():
    app = QtWidgets.QApplication.instance()
    if not app:
        app = QtWidgets.QApplication(sys.argv)

    for widget in app.allWidgets():
        if widget.objectName() == 'userNormalTranslatorWindow':
            widget.close()

    ex = userNormalTranslatorWindow()
    ex.setParent(app.activeWindow())
    ex.setWindowFlags(QtCore.Qt.Window)

    ex.show()

    if app.applicationName() in ['python', 'mayapy']:
        sys.exit(app.exec_())


if __name__ == '__main__':

    main()
