from gpiozero import LED
from time import sleep
import datetime


ledR = [
    LED(2),
    LED(3),
    LED(4),
    LED(17)
]

x=0

while x<5:
    ledR[0].on()
    ledR[1].on()
    ledR[2].on()
    ledR[3].on()

    # Wait for 5 seconds
    sleep(5)

    ledR[0].off()
    ledR[1].off()
    ledR[2].off()
    ledR[3].off()
    
    sleep(5)
    
    x+=1