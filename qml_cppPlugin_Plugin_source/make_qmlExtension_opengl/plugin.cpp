#include <plugin.h>
#include <squircle.h>

void itemPlugin::registerTypes(const char *uri)
{
    qmlRegisterType<Squircle>(uri, 1, 0, "Squircle");

}
