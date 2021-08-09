import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QVBoxLayout
from example.openpyxl.example.main import work

# 简单的输入+按钮 窗口
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 窗口大小
        self.resize(400, 100)
        self.setWindowTitle('简易Excel整合工具')
        # 实例化QLineEdit对象 <input>
        self.input = QLineEdit(self)

        # self.input.resize(300,20)
        self.input.setGeometry(90, 10, 300, 20)
        # 实例化QLabel对象 <label>
        self.label = QLabel(self)
        self.label_input = QLabel(self)
        self.label_input.setText("文件路径：")
        # 设置标签的位置和大小(x,y,宽，高)
        self.label.setGeometry(90, 30, 300, 20)
        self.label_input.setGeometry(10, 10, 200, 20)
        # 连接信号和槽(将input输入的内容实时显示)
        # self.input.textChanged.connect(self.label.setText)
        # 按钮 <button>
        self.btn_1 = QPushButton(self)
        self.btn_1.setText("开始运行")
        self.btn_1.setGeometry(90, 50, 80, 30)
        self.btn_1.clicked.connect(self.btnState)

        # self.btn_1.clicked.connect(self.btnState)
        # self.btn_1.clicked.connect(lambda: self.wichBtn(self.btn_1))
        # layout = QVBoxLayout()
        # layout.addWidget(self.btn_1)
        self.show()

    def btnState(self):
        if self.btn_1.isChecked():
            # fixme 为什么这里单击显示反的？
            print("被单击")
        else:
            print("未被单击")
            str = self.input.text()
            print(str)
            if (str != ''):
                result = work(str)
                self.label.setText("导出成功，文件名：" + result)
            else:
                self.label.setText("请输入路径")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
