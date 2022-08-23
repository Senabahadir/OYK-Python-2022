from PySide2.QtWidgets import QApplication, QWidget
from zar_oyunu import Ui_ZarOyunu

class Widget(QWidget, Ui_ZarOyunu):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.txtZar.textChanged.connect(self.kontrol_et)

        self.show()

    def kontrol_et(self, text):
        if text:
            if int(text) < 1 or int(text) >6:
                self.txtZar.clear()

app = QApplication()
widget = Widget()
app.exec_()
