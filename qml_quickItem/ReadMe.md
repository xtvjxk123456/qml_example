1,使用QQuickPaintedItem来自定义Item
2,启动方式:
    1.使用QQmlApplicationEngine 支持window作为root Item
    2.使用QQuickView ,自带 engine,不支持window作为root,缩放模式需要自己设置
    
3,使用QQuickView 的updatePaintNode 来绘制Item(测试失败，例子中用到了qsg,但pyside2 qsg有点问题)
