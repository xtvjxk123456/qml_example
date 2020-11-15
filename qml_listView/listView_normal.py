from PySide2 import QtWidgets, QtCore, QtGui, QtQuick, QtQml
import sys
import os


# resource
from resource import res_main

if __name__ == "__main__":
    app = QtGui.QGuiApplication(sys.argv[1:])

    view = QtQuick.QQuickView()
    view.setResizeMode(QtQuick.QQuickView.SizeRootObjectToView)

    view.setSource("qrc:/qml/listView_normal.qml")

    view.show()
    sys.exit(app.exec_())