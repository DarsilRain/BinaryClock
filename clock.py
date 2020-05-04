from gpiozero import LED
from time import sleep
import datetime


ledR = [
    LED(2),
    LED(3),
    LED(4),
    LED(17)
]
ledG = [
    LED(10),
    LED(9),
    LED(11),
    LED(0),
    LED(5),
    LED(6)
]
ledB = [
    LED(23),
    LED(24),
    LED(25),
    LED(8),
    LED(7),
    LED(1)
]

def lit(num, leds):
    # Convert to binary, strip the '0b' and fill in 0s to == number of leds
    binnum = bin(int(num))[2:].zfill(len(leds))
    # print(binnum)
    for i in range(len(leds)):
        if int(binnum[i]):
            leds[i].on()
        else:
            leds[i].off()

while True:
    currentDT= datetime.datetime.now()
    # print (currentDT.strftime("%I:%M:%S %p"))

    hour=currentDT.strftime("%I")
    lit(hour, ledR)

    minute=currentDT.strftime("%M")
    lit(minute, ledG)

    second=currentDT.strftime("%S")
    lit(second, ledB)
    
    sleep(1)
