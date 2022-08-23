from PySide2.QtCore import QTimer
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication

# Uygulamayi olustur
app = QApplication()

loader = QUiLoader()
window = loader.load("progress_with_button.ui")


def progressbar_degistir():
    mevcut_deger = window.progressBar.value()
    yeni_deger = mevcut_deger + 1
    if yeni_deger > 100:
        window.progressBar.setValue(0)
    else:
        window.progressBar.setValue(yeni_deger)


timer = QTimer()
timer.setInterval(1)
timer.timeout.connect(progressbar_degistir)

window.btnStart.clicked.connect(timer.start)
window.btnStop.clicked.connect(timer.stop)

window.show()  # Onemli formu goster.


# Event dondugusunu baslat.
app.exec_()
