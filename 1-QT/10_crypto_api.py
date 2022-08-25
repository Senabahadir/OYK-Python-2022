import requests
from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QApplication, QWidget

from design import Ui_Form


class Widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.show()

        self.key = "https://api.binance.com/api/v3/ticker/price?symbol="

        self.btn_add_coin.clicked.connect(self.add_coin)

        self.btn_get_price.clicked.connect(self.get_price)

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        self.timer.timeout.connect(self.get_price)

    def add_coin(self):
        coin_name = self.txt_coin_name.text().upper()
        self.coin_list_combo_box.addItem(coin_name)
        self.txt_coin_name.clear()

    def get_price(self):
        current_coin_name = self.coin_list_combo_box.currentText()
        url = self.key + current_coin_name + "USDT"
        data = requests.get(url).json()

        coin_price = round(float(data["price"]), 2)
        coin_name = data["symbol"]

        self.lbl_coin_price.setText(coin_name + " " + str(coin_price))


app = QApplication()
widget = Widget()
app.exec_()
