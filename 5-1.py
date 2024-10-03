import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp=14
troyka=13
maxvoltage=3.3
bits=8
levels=2**8
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def dec2binary(a):
    return[int(element) for element in bin(a)[2:].zfill(8)]

def num2dac(value):
    signal=dec2binary(value)
    GPIO.output(dac,signal)
    return signal

try:
    while True:
        for value in range(256):
            time.sleep(0.002)
            signal=num2dac(value)
            voltage=value/levels*maxvoltage
            comparatorValue=GPIO.input(comp)
            if comparatorValue == 1:
                print("ADC value = {:^3} -> {}, input voltage = {:.2f}".format(value,signal,voltage))
                break
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print("Готово")