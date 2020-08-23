#ifndef PLUGIN_H
#define PLUGIN_H

#include <QtQml/qqmlextensionplugin.h>


class itemPlugin : public QQmlExtensionPlugin
{
    Q_OBJECT
    Q_PLUGIN_METADATA(IID QQmlExtensionInterface_iid)

public:
    void registerTypes(const char *uri);
};
//![0]


#endif // PLUGIN_H
