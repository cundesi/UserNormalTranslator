#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import pymel.core as pm
import maya.api.OpenMaya as om

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
        self.pBtnX.clicked.connect(self.set_normals)
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

    def update_normals(self, x_value, y_value, z_value, modle='add'):
        sel_list = om.MGlobal.getActiveSelectionList()
        for sel_index in range(sel_list.length()):
            (path, comp) = sel_list.getComponent(sel_index)
            mesh_fn = om.MFnMesh(path)

            if comp.apiType() in [om.MFn.kMeshVertComponent]:
                comp_fn = om.MFnSingleIndexedComponent(comp)
                indices = comp_fn.getElements()
                vtx_normals = []
                for vtx_index in indices:
                    vtx_normal = mesh_fn.getVertexNormal(vtx_index, True)
                    if modle == 'add':
                        new_vtx_normal = om.MVector(
                            vtx_normal.x + x_value, vtx_normal.y + y_value, vtx_normal.z + z_value
                        )
                    else:
                        new_vtx_normal = om.MVector(
                            vtx_normal.x * x_value, vtx_normal.y * y_value, vtx_normal.z * z_value
                        )
                    vtx_normals.append(new_vtx_normal)
                mesh_fn.setVertexNormals(vtx_normals, indices)

    def add_normals(self, x_value=0, y_value=0, z_value=0):
        self.update_normals(x_value, y_value, z_value)

    def mulltiply_normals(self, x_value=1, y_value=1, z_value=1):
        self.update_normals(x_value, y_value, z_value, modle='mulltiply')

    def set_normals(self):
        x_value = self.dbsBoxX.value()
        if self.rdBtnAdd.isChecked():
            self.add_normals(x_value=x_value)
        else:
            self.mulltiply_normals(x_value=x_value)

    def setXNormalValue1(self):
        self.resetNormalValue()
        self.dbsBoxX.setValue(-0.1)
        self.set_normals()

    def setXNormalValue2(self):
        self.resetNormalValue()
        self.dbsBoxX.setValue(-0.5)
        self.set_normals()

    def setXNormalValue3(self):
        self.resetNormalValue()
        self.dbsBoxX.setValue(0.5)
        self.set_normals()

    def setXNormalValue4(self):
        self.resetNormalValue()
        self.dbsBoxX.setValue(0.1)
        self.set_normals()

    def setYNormal(self):
        YValue = self.dbsBoxY.value()
        if self.rdBtnAdd.isChecked():
            self.add_normals(y_value=YValue)
        else:
            self.mulltiply_normals(y_value=YValue)

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
            self.add_normals(z_value=ZValue)
        else:
            self.mulltiply_normals(z_value=ZValue)

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

        sel_list = om.MGlobal.getActiveSelectionList()
        for sel_index in range(sel_list.length()):
            (path, comp) = sel_list.getComponent(sel_index)
            mesh_fn = om.MFnMesh(path)
            if self.center:
                bounding_box = self.center.boundingBox()
                pos = om.MVector(bounding_box.center())

            else:
                dag_node = om.MFnDagNode(path.transform())
                pos = dag_node.boundingBox.center
            if comp.apiType() in [om.MFn.kMeshVertComponent]:
                comp_fn = om.MFnSingleIndexedComponent(comp)
                indices = comp_fn.getElements()
                vtx_normals = []
                for vtx_index in indices:
                    vtx_normal = mesh_fn.getVertexNormal(vtx_index, True)
                    vtx_point = mesh_fn.getPoint(vtx_index, space=om.MSpace.kWorld)
                    new_vtx_normal = om.MVector(
                        (vtx_point - pos) * ratio + vtx_normal * (1 - ratio)
                    )
                    vtx_normals.append(new_vtx_normal)
                mesh_fn.setVertexNormals(vtx_normals, indices)

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
