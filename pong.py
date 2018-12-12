import time
import random
from sense_hat import SenseHat

sense = SenseHat()

x=random.randint(4, 6)
y=random.randint(1, 6)


movex=random.choice([True, False])
movey=random.choice([True, False])

s=0.3

running=True
red=(255,0,0)

score=0

while running is True:
  if movex is True and movey is True:
    x+=1
    y+=1
    s-=0.05
    sense.clear(0,0,0)
    sense.set_pixel(x,y,255,255,255)
    time.sleep(s)
    if x > 6:
      movex=False
    if y > 6:
      movey=False

  elif movex is True and movey is False:
    x+=1
    y-=1
    sense.clear(0,0,0)
    sense.set_pixel(x,y,255,255,255)
    time.sleep(s)
    if x > 6:
      movex=False
    if y < 1:
      movey=True

  elif movex is False and movey is False:
    x-=1
    y-=1
    sense.clear(0,0,0)
    sense.set_pixel(x,y,255,255,255)
    time.sleep(s)
    if x < 1:
      movex=True
    if y < 1:
      movey=True

  elif movex is False and movey is True:
    x-=1
    y+=1
    sense.clear(0,0,0)
    sense.set_pixel(x,y,255,255,255)
    time.sleep(s)
    if x < 1:
      movex=True
    if y > 6:
      movey=False
      
  if x is 7:
    score+=1
      
  if x is 0:
    sense.show_message('SCORE = ' + str(score), text_colour=red)
    running=False

