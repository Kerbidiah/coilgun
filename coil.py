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

bttn = ADC(Pin(33))
bttn.atten(ADC.ATTN_11DB)

def triggerWaitH(pin, number):
	while pin.read() < number:
		pass
def triggerWaitL(pin, number):
	while pin.read() > number:
		pass

cont = True

while cont:
	triggerWaitH(bttn, 3500)
	mosfet1.on()
	print("m1 on")
	triggerWaitH(snsr1, 500)
	mosfet1.off()
	print("m1 off")
	mosfet2.on()
	print("m2 on")
	triggerWaitH(snsr2, 400)
	mosfet2.off()
	print("m2 off")
	mosfet3.on()
	print("m3 on")
	triggerWaitH(snsr3, 100)
	mosfet3.off()
	print("m3 off")