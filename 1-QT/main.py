import sys

from PySide2.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = QWidget()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
