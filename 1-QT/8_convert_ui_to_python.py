from PySide2.QtWidgets import QApplication, QWidget
from arayuz import Ui_Form

class Widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.show()

app = QApplication()
widget = Widget()
app.exec_()
