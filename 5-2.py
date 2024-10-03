import RPi.GPIO as gp
import time

def dec2bin(num):
    return [int(bit) for bit in bin(int(num))[2:].zfill(8)]
dac = [8,11,7,1,0,5,12,6]
comp = 14
troyka = 13
gp.cleanup()
gp.setmode(gp.BCM)
gp.setup(comp, gp.IN)
gp.setup(troyka, gp.OUT, initial=gp.HIGH)
u_max = 3.3
for led in dac:
    gp.setup(led, gp.OUT)
for led in dac:
    gp.output(led, 0)
def adc():
    num = [0]*8
    for i in range(8):
        # print('binary ', str(num))
        num[i] = 1
        for j in range(8):
            gp.output(dac[j], num[j])
        time.sleep(0.002)
        if gp.input(comp):
            num[i] = 0
        
    return int(''.join(str(x) for x in num), 2)
try:
    while True:
        n = adc()
        print(n, n*3.3/255)

        time.sleep(0.1)
finally:
    gp.output(troyka, 0)
    for led in dac:
        gp.output(led, 0)