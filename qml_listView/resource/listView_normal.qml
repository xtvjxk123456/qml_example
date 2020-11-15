import QtQuick 2.5

Item{
    id: main
    width: 300
    height:300

    ListView{
        anchors.fill: main
        model: ["100","200"]

    }

}