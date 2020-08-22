# coding: utf-8
from PySide2 import QtWidgets, QtCore, QtGui, QtQuick, QtQml,shiboken2
import sys
import os


# use qt QSG
class CurveItem(QtQuick.QQuickItem):
    p1Changed = QtCore.Signal(object)
    p2Changed = QtCore.Signal(object)
    p3Changed = QtCore.Signal(object)
    p4Changed = QtCore.Signal(object)
    segmentCountChanged = QtCore.Signal(int)

    def __init__(self, *argv, **kwargs):
        super(CurveItem, self).__init__(*argv, **kwargs)
        self.setFlag(QtQuick.QQuickItem.ItemHasContents)
        # DATA
        self._p1 = QtCore.QPointF(0, 0)
        self._p2 = QtCore.QPointF(1, 0)
        self._p3 = QtCore.QPointF(0, 1)
        self._p4 = QtCore.QPointF(1, 1)
        self._count = 32

    def p1(self):
        return self._p1

    def p2(self):
        return self._p2

    def p3(self):
        return self._p3

    def p4(self):
        return self._p4

    def setP1(self, p):
        if p == self._p1:
            return
        self._p1 = p
        self.p1Changed.emit(p)
        self.update()

    def setP2(self, p):
        if p == self._p2:
            return
        self._p2 = p
        self.p2Changed.emit(p)
        self.update()

    def setP3(self, p):
        if p == self._p3:
            return
        self._p3 = p
        self.p3Changed.emit(p)
        self.update()

    def setP4(self, p):
        if p == self._p4:
            return
        self._p4 = p
        self.p4Changed.emit(p)
        self.update()

    def segmentCount(self):
        return self._count

    def setSegmentCount(self, count):
        if count == self._count:
            return
        self._count = count
        self.segmentCountChanged.emit(count)
        self.update()

    def updatePaintNode(self, oldNode, updatePaintData):
        node = None
        geo = None
        if not oldNode:
            node = QtQuick.QSGGeometryNode()
            geo = QtQuick.QSGGeometry(QtQuick.QSGGeometry.defaultAttributes_Point2D(), self._count)
            geo.setLineWidth(2)
            geo.setDrawingMode(QtQuick.QSGGeometry.DrawLineStrip)
            node.setGeometry(geo)
            node.setFlag(QtQuick.QSGNode.OwnsGeometry)

        else:
            node = oldNode
            geo = node.geometry()
            geo.allocate(self._count)

        itemSize = self.size()
        verts = geo.vertexData()
        # 出现了bug,这里pyside返回不正常
        for x in xrange(self._count):
            t = x / (self._count - 1)
            invt = 1 - t

            pos = invt * invt * invt * self._p1 + 3 * invt * invt * t * self._p2 + 3 * invt * t * t * self._p3 + t * t * t * self._p4
            x = pos.x() * itemSize.width()
            y = pos.y() * itemSize.height()
            verts[x].set(x, y)
        node.markDirty(QtQuick.QSGNode.DirtyGeometry)
        return node

    # Property
    p1 = QtCore.Property(QtCore.QPointF, p1, setP1, notify=p1Changed)
    p2 = QtCore.Property(QtCore.QPointF, p2, setP1, notify=p2Changed)
    p3 = QtCore.Property(QtCore.QPointF, p3, setP1, notify=p3Changed)
    p4 = QtCore.Property(QtCore.QPointF, p4, setP1, notify=p4Changed)
    segmentCount = QtCore.Property(int, segmentCount, setSegmentCount, notify=segmentCountChanged)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv[1:])

    QtQml.qmlRegisterType(CurveItem, "CustomGeometry", 1, 0, 'BezierCurve')

    view = QtQuick.QQuickView()
    surface = view.format()
    surface.setSamples(16)
    view.setFormat(surface)

    view.engine().addImportPath(os.path.dirname(__file__))
    view.setSource('resource\\main2.qml')
    view.show()

    sys.exit(app.exec_())
