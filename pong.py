import time
from sense_hat import SenseHat

sense = SenseHat()

x=1
y=4

movex=True
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

