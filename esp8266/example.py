# With Logging (Regular Driver)

from machine import Pin, I2C
from ina219 import INA219
from logging import INFO

SHUNT_OHMS = 0.1

i2c = I2C(-1, Pin(5), Pin(4))
ina = INA219(SHUNT_OHMS, i2c, log_level=INFO)
ina.configure()

print("Bus Voltage: %.3f V" % ina.voltage())
print("Current: %.3f mA" % ina.current())
print("Power: %.3f mW" % ina.power())


# Without Logging (ESP8266)

from machine import Pin, I2C
from ina219_no_logging import INA219

SHUNT_OHMS = 0.1

i2c = I2C(-1, Pin(5), Pin(4))
ina = INA219(SHUNT_OHMS, i2c)
ina.configure()

print("Bus Voltage: %.3f V" % ina.voltage())
print("Current: %.3f mA" % ina.current())
print("Power: %.3f mW" % ina.power())
