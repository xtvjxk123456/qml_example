# -*- coding: utf-8 -*-

# Resource object code
#
# Created: 周日 八月 23 11:34:36 2020
#      by: The Resource Compiler for PySide2 (Qt v5.11.2)
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
\x00\x00\x01\xa0\
i\
mport QtQuick 2.\
11\x0d\x0aimport QtQui\
ck.Window 2.11\x0d\x0a\
\x0d\x0aimport TimeExa\
mple 1.0\x0d\x0a\x0d\x0aWind\
ow {\x0d\x0a    visibl\
e: true\x0d\x0a    wid\
th: 640\x0d\x0a    hei\
ght: 480\x0d\x0a    ti\
tle: qsTr(\x22Hello\
 World\x22)\x0d\x0a\x0d\x0a    \
Clock { // this \
class is defined\
 in QML (imports\
/TimeExample/Clo\
ck.qml)\x0d\x0a\x0d\x0a     \
   Time { // thi\
s class is defin\
ed in C++ (plugi\
n.cpp)\x0d\x0a        \
    id: time\x0d\x0a  \
      }\x0d\x0a\x0d\x0a     \
   hours: time.h\
our\x0d\x0a        min\
utes: time.minut\
e\x0d\x0a\x0d\x0a    }\x0d\x0a}\x0d\x0a\
"

qt_resource_name = b"\
\x00\x08\
\x08\x01Z\x5c\
\x00m\
\x00a\x00i\x00n\x00.\x00q\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
