import QtQuick 2.2
import QtQuick.Controls 1.1
import QtWebView 1.0

Item{
    id: root
    WebView {
          id: webView
          anchors.fill: parent
          url: 'www.baidu.com'
      }

}