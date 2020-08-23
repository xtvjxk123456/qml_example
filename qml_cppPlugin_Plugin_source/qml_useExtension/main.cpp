#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQuickView>

int main(int argc, char *argv[])
{
    QCoreApplication::setAttribute(Qt::AA_EnableHighDpiScaling);

    QGuiApplication app(argc, argv);

//    QQmlApplicationEngine engine;
////    engine.addImportPath(QStringLiteral("F:/Code/qml_example/qml_cppPlugin/imports"));

//    const QUrl url(QStringLiteral("qrc:/main2.qml"));
//    QObject::connect(&engine, &QQmlApplicationEngine::objectCreated,
//                     &app, [url](QObject *obj, const QUrl &objUrl) {
//        if (!obj && url == objUrl)
//            QCoreApplication::exit(-1);
//    }, Qt::QueuedConnection);
//    engine.load(url);

    QQuickView view;
    view.setResizeMode(QQuickView::SizeRootObjectToView);
    view.setSource(QUrl("qrc:/main2.qml"));
    view.show();

    return app.exec();
}
