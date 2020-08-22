# -*- coding: utf-8 -*-

# Resource object code
#
# Created: 周一 八月 3 17:19:13 2020
#      by: The Resource Compiler for PySide (Qt v4.8.7)
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore

qt_resource_data = "\x00\x00\x09\xa0/****************************************************************************\x0d\x0a**\x0d\x0a** Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).\x0d\x0a** All rights reserved.\x0d\x0a** Contact: Nokia Corporation (qt-info@nokia.com)\x0d\x0a**\x0d\x0a** This file is part of the QtDeclarative module of the Qt Toolkit.\x0d\x0a**\x0d\x0a** You may use this file under the terms of the BSD license as follows:\x0d\x0a**\x0d\x0a** \x22Redistribution and use in source and binary forms, with or without\x0d\x0a** modification, are permitted provided that the following conditions are\x0d\x0a** met:\x0d\x0a**   * Redistributions of source code must retain the above copyright\x0d\x0a**     notice, this list of conditions and the following disclaimer.\x0d\x0a**   * Redistributions in binary form must reproduce the above copyright\x0d\x0a**     notice, this list of conditions and the following disclaimer in\x0d\x0a**     the documentation and/or other materials provided with the\x0d\x0a**     distribution.\x0d\x0a**   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor\x0d\x0a**     the names of its contributors may be used to endorse or promote\x0d\x0a**     products derived from this software without specific prior written\x0d\x0a**     permission.\x0d\x0a**\x0d\x0a** THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS\x0d\x0a** \x22AS IS\x22 AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT\x0d\x0a** LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR\x0d\x0a** A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT\x0d\x0a** OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,\x0d\x0a** SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT\x0d\x0a** LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,\x0d\x0a** DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY\x0d\x0a** THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT\x0d\x0a** (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE\x0d\x0a** OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.\x22\x0d\x0a**\x0d\x0a****************************************************************************/\x0d\x0a//![0]\x0d\x0aimport Charts 1.0\x0d\x0aimport Qt 4.7\x0d\x0a\x0d\x0aItem {\x0d\x0a    width: 300; height: 200\x0d\x0a\x0d\x0a    PieChart {\x0d\x0a        id: aPieChart\x0d\x0a        anchors.centerIn: parent\x0d\x0a        width: 100; height: 100\x0d\x0a        name: \x22A simple pie chart\x22\x0d\x0a        color: \x22red\x22\x0d\x0a    }\x0d\x0a\x0d\x0a    Text {\x0d\x0a        anchors { bottom: parent.bottom; horizontalCenter: parent.horizontalCenter; bottomMargin: 20 }\x0d\x0a        text: aPieChart.name\x0d\x0a    }\x0d\x0a}\x0d\x0a//![0]\x0d\x0a"
qt_resource_name = "\x00\x03\x00\x00x<\x00q\x00m\x00l\x00\x07\x08sX\xfc\x00a\x00p\x00p\x00.\x00q\x00m\x00l"
qt_resource_struct = "\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00"
def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
