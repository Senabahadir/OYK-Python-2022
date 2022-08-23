from PySide2.QtWidgets import QApplication, QWidget

# Uygulamayi olustur
app = QApplication()

# Formu Olustur.
window = QWidget()
window.show()  # Onemli formu goster.

# Event dondugusunu baslat.
app.exec_()
