from PySide2.QtWidgets import QApplication, QWidget,QPushButton, QLabel
app = QApplication()

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ilk Main Window")

        self.label = QLabel(self)
        self.label.setText('0')
        self.label.setGeometry(10,10, 200,40)

        self.button_azalt = QPushButton(self)
        self.button_azalt.setGeometry(10,70,100,50)
        self.button_azalt.setText('Azalt')

        self.button_artir = QPushButton(self)
        self.button_artir.setGeometry(120,70,100,50)
        self.button_artir.setText('Artir')

        self.button_azalt.clicked.connect(self.azalt)
        self.button_artir.clicked.connect(self.arttir)

        self.resize(250,250)
        font = self.font()
        font.setPointSize(30)
        self.setFont(font)
        self.show()
    def azalt(self):
        simdiki_deger = int(self.label.text())
        simdiki_deger -=1
        self.label.setText(str(simdiki_deger))
    def arttir(self):
        simdiki_deger = int(self.label.text())
        simdiki_deger +=1
        self.label.setText(str(simdiki_deger))

widget = Widget()


app.exec_()