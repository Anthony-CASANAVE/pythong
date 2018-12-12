import time
import random
from sense_hat import SenseHat

sense = SenseHat()

x=random.randint(0, 7)
y=random.randint(0, 7)

if x > 6:
  movex=False
else:
  movex=True

if y > 6:
  movey=False
else:
  movey=True

while True:
  if movex is True and movey is True:
    x+=1
    y+=1
    sense.clear(0,0,0)
    sense.set_pixel(x,y,255,255,255)
    time.sleep(0.1)
    if x > 6:
      movex=False
    if y > 6:
      movey=False

  elif movex is True and movey is False:
    x+=1
    y-=1
    sense.clear(0,0,0)
    sense.set_pixel(x,y,255,255,255)
    time.sleep(0.1)
    if x > 6:
      movex=False
    if y < 1:
      movey=True

  elif movex is False and movey is False:
    x-=1
    y-=1
    sense.clear(0,0,0)
    sense.set_pixel(x,y,255,255,255)
    time.sleep(0.1)
    if x < 1:
      movex=True
    if y < 1:
      movey=True

  elif movex is False and movey is True:
    x-=1
    y+=1
    sense.clear(0,0,0)
    sense.set_pixel(x,y,255,255,255)
    time.sleep(0.1)
    if x < 1:
      movex=True
    if y > 6:
      movey=False

