from PySide2.QtWidgets import QApplication, QWidget
from zar_oyunu import Ui_ZarOyunu
import random

class Widget(QWidget, Ui_ZarOyunu):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.btnAt.released.connect(self.zar_at)
        self.txtZar.textChanged.connect(self.kontrol_et)

        self.show()

    def kontrol_et(self, text):
        if text:
            self.btnAt.setEnabled(True)
            if int(text) < 1 or int(text) >6:
                self.txtZar.clear()
        else:
            self.btnAt.setEnabled(False)

    def zar_at(self):
        zar_deger = random.randint(1,6)
        if zar_deger == int(self.txtZar.text()):
            self.lblSonuc.setText('Kazandin.')
        else:
            self.lblSonuc.setText('Kaybettin! ' + str(zar_deger))
        self.txtZar.clear()

app = QApplication()
widget = Widget()
app.exec_()
