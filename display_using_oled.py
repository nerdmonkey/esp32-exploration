from machine import Pin, SoftI2C
import ssd1306


i2c = SoftI2C(scl=Pin(21), sda=Pin(22))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
oled.text('nerdmonkey', 0, 0)

oled.show()
