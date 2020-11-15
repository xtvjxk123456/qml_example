import QtQuick 2.0

Item {
    width: 300
    height: 300

    Component {
            id: contactDelegate
            Rectangle{
                width: ListView.view.width
                color: "lightgreen"

                Text{
                    text: modelData
                }

            }
        }

    ListView{
        anchors.fill: parent
        anchors.margins: 2
        model:["fff","aa","ccc"]
        delegate: contactDelegate
        spacing: 10

    }
}