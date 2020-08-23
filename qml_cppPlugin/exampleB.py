# coding: utf-8
from PySide2 import QtWidgets, QtCore, QtGui, QtQuick, QtQml
import sys
import os
from resources import qmlB

if __name__ == '__main__':
    # app = QtWidgets.QApplication(sys.argv[1:])
    app = QtGui.QGuiApplication(sys.argv[1:])

    # import path 是qml中用来improt 的路径，类似python sys.path
    # plugin path 是能读到qmdir的路径

    # root是item 只能用view来启动
    view = QtQuick.QQuickView()
    view.setResizeMode(QtQuick.QQuickView.SizeRootObjectToView)
    view.engine().addImportPath(os.path.join(os.path.dirname(__file__), 'imports'))
    view.setSource("qrc:/main2.qml")
    view.show()

    sys.exit(app.exec_())
