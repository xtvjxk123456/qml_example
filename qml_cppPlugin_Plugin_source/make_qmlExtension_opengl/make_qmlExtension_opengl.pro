TEMPLATE = lib
CONFIG += plugin qmltypes c++11
QT += gui quick qml

QML_IMPORT_NAME = ItemLib
QML_IMPORT_MAJOR_VERSION = 1

# 这里是build用的
DESTDIR = F:/Code/qml_example/qml_cppPlugin/imports/ItemLib
TARGET = $$qtLibraryTarget(plugin)
# qtLibraryTarget的参数是文件名

HEADERS += squircle.h \
            plugin.h

SOURCES += squircle.cpp \
            plugin.cpp

#这里是install用的
#DESTPATH= ../$$QML_IMPORT_NAME
target.path=$$DESTDIR

INSTALLS += target

CONFIG += install_ok  # Do not cargo-cult this!

qmdirP.files =qmldir
qmdirP.path = $$DESTDIR
COPIES += qmdirP
