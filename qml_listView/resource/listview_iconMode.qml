import QtQuick 2.0

Item {
    width: 200
    height: 200

    ListModel{
        id:myModel
        ListElement{
            name:"cc"
            aa:30
            }
        ListElement{
            name:"ccd"
            aa:20
            }
        ListElement{
            name:"AA"
            aa:10
            }
        ListElement{
            name:"AA"
            aa:10
            }
        ListElement{
            name:"AA"
            aa:10
            }
        ListElement{
            name:"AA"
            aa:10
            }
    }
    Component{
        id:myDelegate
        Text{
            id:wrapper
            text: name
            width: GridView.view.cellWidth
            height: GridView.view.cellHeight
            MouseArea{
                anchors.fill: parent
                onClicked: {
                    wrapper.GridView.view.currentIndex = index
                }
            }
        }
    }
    Component{
        id:myHightLight
        Rectangle{
            width: GridView.view.cellWidth
            height: GridView.view.cellHeight
            color: "lightblue"

        }

    }

    GridView{
        anchors.fill: parent
        model: myModel
        delegate: myDelegate
        highlight: myHightLight
        focus: true




    }
}
