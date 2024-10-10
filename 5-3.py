import RPi.GPIO as gp
import time

def dec2bin(num):
    return [int(bit) for bit in bin(int(num))[2:].zfill(8)]


    
leds=[9,10,22,27,17,4,3,2]

dac = [8,11,7,1,0,5,12,6]
comp = 14
troyka = 13
gp.cleanup()
gp.setmode(gp.BCM)

gp.setup(comp, gp.IN)
gp.setup(troyka, gp.OUT, initial=gp.HIGH)

u_max = 3.3

gp.setup(leds, gp.OUT)
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
        time.sleep(0.01)
        if gp.input(comp):
            num[i] = 0
        
    return int(''.join(str(x) for x in num), 2)

try:
    gp.output(leds, [0]*8)
    while True:
        n = adc()
        print(n, n*3.3/255)

        perc = round(n/255*8)
        for i in range(perc):
            gp.output(leds[i],1)
        for i in range(perc, 8):
            gp.output(leds[i],0)
        time.sleep(0.1)

        
finally:
    gp.output(troyka, 0)
    for led in dac:
        gp.output(led, 0)



