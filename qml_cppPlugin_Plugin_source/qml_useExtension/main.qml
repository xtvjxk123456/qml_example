import QtQuick 2.11
import QtQuick.Window 2.11

import TimeExample 1.0

Window {
    visible: true
    width: 640
    height: 480
    title: qsTr("Hello World")

    Clock { // this class is defined in QML (imports/TimeExample/Clock.qml)

        Time { // this class is defined in C++ (plugin.cpp)
            id: time
        }

        hours: time.hour
        minutes: time.minute

    }
}
