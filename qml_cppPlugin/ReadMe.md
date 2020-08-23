# cpp qml plugin? qt 5.11.2
尝试使用c++做的plugin为python qml来显示
1 TimeExample 显示ok
2,ItemLib无法显示(已解决)
    原因:
        1,plugin生成正确
        2,qrc生成正确
        3,python(cpp端)(两端都是)测试时使用了 qmlEngine启动的，导致没有窗口(qml中root为item,而不是window)
# 注意
qt 5.11.2的类和最新qt的plugin类不一致，所以写法也一致，尽量参考qtcreator里的例子

