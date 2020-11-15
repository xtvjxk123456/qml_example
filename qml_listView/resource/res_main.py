# -*- coding: utf-8 -*-

# Resource object code
#
# Created: 周日 十一月 15 11:33:38 2020
#      by: The Resource Compiler for PySide2 (Qt v5.6.1)
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
\x00\x00\x00\xa2\
i\
mport QtQuick 2.\
5\x0d\x0a\x0d\x0aItem{\x0d\x0a    \
id: main\x0d\x0a    wi\
dth: 300\x0d\x0a    he\
ight:300\x0d\x0a\x0d\x0a    \
ListView{\x0d\x0a     \
   anchors.fill:\
 main\x0d\x0a        m\
odel: [\x22100\x22,\x2220\
0\x22]\x0d\x0a\x0d\x0a    }\x0d\x0a\x0d\x0a\
}\
"

qt_resource_name = b"\
\x00\x03\
\x00\x00x<\
\x00q\
\x00m\x00l\
\x00\x13\
\x06\xf9\x8d|\
\x00l\
\x00i\x00s\x00t\x00V\x00i\x00e\x00w\x00_\x00n\x00o\x00r\x00m\x00a\x00l\x00.\x00q\
\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
