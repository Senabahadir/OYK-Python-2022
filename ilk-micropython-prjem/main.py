#import time
#import machine

#pin = machine.Pin(2, machine.Pin.OUT)
#pin.on()
#pin.off()

#def toggle(p):
#   p.value(not p.value())

#while True:
#    toggle(pin)
#    time.sleep_ms(50)
##########################################

import urequests
import ujson
def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('conneting to network...')
        wlan.connect('OYK-Python', 'oykpython2022')
        while not wlan.isconnected():
            pass
        print('network.config:', wlan.ifconfig())

do_connect()

res = urequests.post('http://192.168.2.193:8000/collector/write/22815e19-e802-430e-a612-bc956e307f08/', data='{"data": "OYK Python 2022 Elveda"}')

res = urequests.get(url='http://192.168.2.193:8000/collector/read/22815e19-e802-430e-a612-bc956e307f08/')
data = ujson.loads(res.text)
print(data)

