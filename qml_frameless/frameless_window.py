from PySide2 import QtWidgets, QtCore, QtGui, QtQuick, QtQml
import sys
import os
import pprint


def printError(status, view):
    if status == QtQuick.QQuickView.Error:
        pprint.pprint(view.errors())


if __name__ == "__main__":
    app = QtGui.QGuiApplication(sys.argv[1:])
    # view = QtQuick.QQuickView()
    # view.statusChanged.connect(lambda x: printError(x, view))
    # view.setResizeMode(QtQuick.QQuickView.SizeRootObjectToView)
    # view.setSource("resource/frameless.qml")
    # view.show()
    engine = QtQml.QQmlApplicationEngine()
    engine.load("resource/frameless.qml")
    sys.exit(app.exec_())
