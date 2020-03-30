import machine
import utime
from machine import Pin
from machine import ADC

mosfet1 = Pin(13, Pin.OUT)
mosfet2 = Pin(12, Pin.OUT)
mosfet3 = Pin(27, Pin.OUT)

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
	d1 = int(input())
	d2 = int(input())
	d3 = int(input())

	triggerWaitH(bttn, 3500)
	mosfet1.on()
	print("m1 on")

	utime.sleep_ms(d1)
	mosfet1.off()
	print("m1 off")
	mosfet2.on()
	print("m2 on")

	utime.sleep_ms(d2)
	mosfet2.off()
	print("m2 off")
	mosfet3.on()
	print("m3 on")

	utime.sleep_ms(d3)
	mosfet3.off()
	print("m3 off")