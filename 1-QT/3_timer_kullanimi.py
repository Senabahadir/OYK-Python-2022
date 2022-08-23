from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QApplication, QPushButton


def tiklama():
    print("Tikladin.")


# Uygulamayi olustur
app = QApplication()

# Formu Olustur.
button = QPushButton("Sakin Tiklama Pisman Olursun")
button.resize(500, 100)
button.show()  # Onemli formu goster.
button.clicked.connect(tiklama)

timer = QTimer()
timer.setInterval(1000)
timer.start()
timer.timeout.connect(lambda: print("saat calisiyor."))

# Event dondugusunu baslat.
app.exec_()
