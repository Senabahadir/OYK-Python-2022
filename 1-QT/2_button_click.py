import time

from PySide2.QtWidgets import QApplication, QPushButton


def tiklama():
    time.sleep(10)
    print("Tikladin.")


# Uygulamayi olustur
app = QApplication()

# Formu Olustur.
button = QPushButton("Sakin Tiklama Pisman Olursun")
button.resize(500, 100)
button.show()  # Onemli formu goster.
button.clicked.connect(tiklama)

# Event dondugusunu baslat.
app.exec_()
