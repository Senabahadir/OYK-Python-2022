from PySide2.QtWidgets import QApplication, QLabel, QPushButton, QWidget

app = QApplication()


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ilk Main Window")

        self.label = QLabel(self)
        self.label.setText("0")
        self.label.setGeometry(10, 10, 200, 40)

        self.button_azalt = QPushButton(self)
        self.button_azalt.setGeometry(10, 70, 100, 50)
        self.button_azalt.setText("Azalt")

        self.button_artir = QPushButton(self)
        self.button_artir.setGeometry(120, 70, 100, 50)
        self.button_artir.setText("Artir")

        self.button_azalt.clicked.connect(lambda: self.degistir(-1))
        self.button_artir.clicked.connect(lambda: self.degistir(1))

        self.resize(250, 250)
        font = self.font()
        font.setPointSize(30)
        self.setFont(font)
        self.show()

    def degistir(self, deger):
        simdiki_deger = int(self.label.text())
        simdiki_deger += deger
        self.label.setText(str(simdiki_deger))


widget = Widget()


app.exec_()
