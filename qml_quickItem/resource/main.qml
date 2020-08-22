import QtQuick 2.11
import QtQuick.Window 2.0
import Demo 1.0

Window {
    visible: true
    width: 640
    height: 480
    title: qsTr("Hello Item")

    PaintItem {
        anchors.fill: parent
    }
}
