from machine import Pin, SPI
import time
from bme680 import BME680_SPI

spi = SPI(1, baudrate=1000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
cs = Pin(5, Pin.OUT)

sensor = BME680_SPI(spi, cs)

while True:
    try:
        print("Temp: {:.2f} °C".format(sensor.temperature))
        print("Hum : {:.2f} %".format(sensor.humidity))
        print("Pres: {:.2f} hPa".format(sensor.pressure))
        print("VOC : {:.2f} kΩ".format(sensor.gas / 1000))
        print("-" * 30)
    except Exception as e:
        print("Sensor read error:", e)
    time.sleep(2)
