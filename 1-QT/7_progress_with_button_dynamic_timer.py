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

def zar_at():
    timer.stop()
    window.btnStop.setEnabled(False)
    window.btnStart.setEnabled(True)
    mevcut_deger = window.progressBar.value()
    if mevcut_deger < 50:
        window.lblStatus.setText('Kazandin!!!!!!')
        soldaki_label_degeri = int(window.lblUser.text())
        soldaki_label_degeri = soldaki_label_degeri + 1
        if soldaki_label_degeri == 10:
            print('Oyuncu kazandi.')
            window.btnStart.setEnabled(False)
            window.btnStop.setEnabled(False)
        str_soldaki_label_degeri = str(soldaki_label_degeri)
        window.lblUser.setText(str_soldaki_label_degeri)
    else:
        window.lblStatus.setText('Kaybettin.')
        sagdaki_label_degeri = int(window.lblComputer.text())
        sagdaki_label_degeri = sagdaki_label_degeri + 1
        if sagdaki_label_degeri == 10:
            print('Bilgisayar kazandi.')
            window.btnStart.setEnabled(False)
            window.btnStop.setEnabled(False)
        str_sagdaki_label_degeri = str(sagdaki_label_degeri)
        window.lblComputer.setText(str_sagdaki_label_degeri)

# window.btnStart.setEnabled(False)   # ilgili nesneyi bloke eder.

def press_start():
    timer.start()
    window.btnStart.setEnabled(False)
    window.btnStop.setEnabled(True)

window.btnStart.clicked.connect(press_start)
window.btnStop.clicked.connect(zar_at)

window.show()  # Onemli formu goster.


# Event dondugusunu baslat.
app.exec_()
