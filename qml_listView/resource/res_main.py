# -*- coding: utf-8 -*-

# Resource object code
#
# Created: 周日 十一月 15 14:06:14 2020
#      by: The Resource Compiler for PySide2 (Qt v5.11.2)
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = "\
\x00\x00\x01\xbc\
i\
mport QtQuick 2.\
0\x0d\x0a\x0d\x0aItem {\x0d\x0a   \
 width: 300\x0d\x0a   \
 height: 300\x0d\x0a\x0d\x0a\
    Component {\x0d\
\x0a            id:\
 contactDelegate\
\x0d\x0a            Te\
xt{\x0d\x0a           \
     width: List\
View.view.width\x0d\
\x0a               \
 height: 30\x0d\x0a   \
             tex\
t: modelData\x0d\x0a\x0d\x0a\
\x0d\x0a            }\x0d\
\x0a        }\x0d\x0a\x0d\x0a  \
  ListView{\x0d\x0a   \
     anchors.fil\
l: parent\x0d\x0a     \
   anchors.margi\
ns: 2\x0d\x0a        m\
odel:[\x22fff\x22,\x22aa\x22\
,\x22ccc\x22]\x0d\x0a       \
 delegate: conta\
ctDelegate\x0d\x0a    \
    spacing: 10\x0d\
\x0a\x0d\x0a    }\x0d\x0a}\
"

qt_resource_name = "\
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

qt_resource_struct = "\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
