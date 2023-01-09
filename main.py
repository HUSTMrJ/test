import sys
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
import resource

class Mainwindow(QWidget):

    def __init__(self):
        self.ui = QUiLoader().load('main.ui')
        self.ui.listWidget.clicked.connect(self.table_click)
        self.ui.stackedWidget.setCurrentIndex(0)
        # 点击处理事件
    def table_click(self, item):
        # item 是你点击的那个单元格对象
        if item.row() == 0:
            self.ui.stackedWidget.setCurrentIndex(0)
        elif item.row() == 1:
            self.ui.stackedWidget.setCurrentIndex(1)
        elif item.row() == 2:
            self.ui.stackedWidget.setCurrentIndex(2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 为main_window类和login_window类创建对象
    main_window =Mainwindow()
     # 显示登录窗口
    main_window.ui.show()
    # 关闭程序，释放资源
    sys.exit(app.exec_())


