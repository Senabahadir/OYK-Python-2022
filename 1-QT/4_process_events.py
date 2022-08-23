import time
import random
from PySide2.QtWidgets import QApplication, QPushButton


# Uygulamayi olustur
app = QApplication()


def tiklama():
    global app
    rastgele_bir_sayi = random.randint(0, 100)
    for i in range(10):
        time.sleep(0.01)
        app.processEvents()
    print("Tikladin.", rastgele_bir_sayi)


# Formu Olustur.
button = QPushButton("Sakin Tiklama Pisman Olursun")
button.resize(500, 100)
button.show()  # Onemli formu goster.
button.clicked.connect(tiklama)

# Event dondugusunu baslat.
app.exec_()
