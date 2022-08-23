from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QLabel, QPushButton,QHBoxLayout, QVBoxLayout, QWidget


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        ylayout = QHBoxLayout()

        self.label = QLabel("0")
        self.label.setAlignment(Qt.AlignCenter)
        button1 = QPushButton("Artir")
        button2 = QPushButton("Azalt")

        
        layout.addWidget(self.label)
        layout.addLayout(ylayout)
        
        ylayout.addWidget(button1)
        ylayout.addWidget(button2)

        self.setLayout(layout)

        button1.clicked.connect(lambda: self.degistir(1))
        button2.clicked.connect(lambda: self.degistir(-1))

        self.resize(250, 250)
        font = self.font()
        font.setPointSize(30)
        self.setFont(font)
        self.show()

    def degistir(self, deger):
        simdiki_deger = int(self.label.text())
        simdiki_deger += deger
        self.label.setText(str(simdiki_deger))


app = QApplication()
widget = Widget()
app.exec_()
