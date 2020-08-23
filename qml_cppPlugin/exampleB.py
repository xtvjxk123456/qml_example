# coding: utf-8
from PySide2 import QtWidgets, QtCore, QtGui, QtQuick, QtQml
import sys
import os
from resources import qmlB

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv[1:])

    engine = QtQml.QQmlApplicationEngine()
    engine.addImportPath(os.path.join(os.path.dirname(__file__), 'imports'))
    # import path 是qml中用来improt 的路径，类似python sys.path
    # plugin path 是能读到qmdir的路径

    engine.load("qrc:/main2.qml")

    sys.exit(app.exec_())
