# coding: utf-8

from PySide2 import QtWidgets, QtCore, QtGui, QtQuick, QtQml
import sys
import os

# resource
from resource import res_main


def debug(statue, view):
    if statue == QtQuick.QQuickView.Error:
        print view.errors()


if __name__ == "__main__":
    app = QtGui.QGuiApplication(sys.argv[1:])

    # 使用qml QApplication engine
    view = QtQuick.QQuickView()
    view.setResizeMode(QtQuick.QQuickView.SizeRootObjectToView)

    view.statusChanged.connect(lambda x: debug(x, view))

    view.setSource("qrc:/qml/listView_normal.qml")

    view.show()
    sys.exit(app.exec_())
