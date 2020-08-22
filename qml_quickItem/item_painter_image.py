# coding:utf-8
from PySide2 import QtWidgets, QtCore, QtGui, QtQuick, QtQml
import sys
import os


# 纯painter
# 还有fbo模式，不过现在不会
class QuickItem(QtQuick.QQuickPaintedItem):
    def __init__(self, *args, **kwargs):
        super(QuickItem, self).__init__(*args, **kwargs)

        # SIGNAL

    def paint(self, painter):
        rect = self.boundingRect()
        painter.save()
        test_rect = QtCore.QRectF()
        test_rect.setTopLeft(rect.topLeft() + QtCore.QPointF(rect.width() / 6, rect.height() / 6).toPoint())
        test_rect.setBottomRight(rect.bottomRight() - QtCore.QPointF(rect.width() / 6, rect.height() / 6).toPoint())
        pen = QtGui.QPen(QtGui.QBrush(QtCore.Qt.red), 2)
        painter.setPen(pen)
        painter.drawRoundRect(test_rect, 10)
        painter.drawRoundRect(rect, 10)
        painter.restore()


if __name__ == "__main__":
    app = QtGui.QGuiApplication(sys.argv[1:])
    QtQml.qmlRegisterType(QuickItem, "Demo", 1, 0, "PaintItem")
    # 类型不能小写开头，要和qml中的类似，大写开头
    # -------------------------------------------主体是window
    # engine = QtQml.QQmlApplicationEngine()
    # engine.addImportPath(os.path.dirname(__file__))
    # engine.load('resource\\main.qml')
    # --------------------------------------------------------
    view = QtQuick.QQuickView()
    # view 不支持window 作为root
    view.setResizeMode(QtQuick.QQuickView.SizeRootObjectToView)
    view.engine().addImportPath(os.path.dirname(__file__))
    view.setSource('resource\\main.qml')
    view.show()
    # ----------------------------------------------------------

    sys.exit(app.exec_())
