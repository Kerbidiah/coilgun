import machine
import utime
from machine import Pin
from machine import ADC

mosfet1 = Pin(13, Pin.OUT)
mosfet2 = Pin(12, Pin.OUT)
mosfet3 = Pin(27, Pin.OUT)

snsr1 = ADC(Pin(34, Pin.IN, Pin.PULL_UP))
snsr2 = ADC(Pin(39, Pin.IN, Pin.PULL_UP))
snsr3 = ADC(Pin(36, Pin.IN, Pin.PULL_UP))
snsr1.atten(ADC.ATTN_11DB)
snsr2.atten(ADC.ATTN_11DB)
snsr3.atten(ADC.ATTN_11DB)

button = ADC(Pin(33))
button.atten(ADC.ATTN_11DB)

cont = True
i = 0
while cont:
	print(button.read())
	print(snsr1.read())
	print(snsr2.read())
	print(snsr3.read())
	print("------------" + str(i))
	i += 1
	utime.sleep_ms(250)

print("done")