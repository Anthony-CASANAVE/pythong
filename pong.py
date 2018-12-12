import time
import random
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_RELEASED, ACTION_HELD
from signal import pause

sense = SenseHat()

x=random.randint(4, 6)
y=random.randint(1, 6)


movex=random.choice([True, False])
movey=random.choice([True, False])

s=0.8

running=True
controls=True

red=(255,0,0)
white=(254,254,254)

sense.show_message("3...2...1...GO!", text_colour=red, back_colour=white)

score=0

pong=random.randint(2, 5)

sense.set_pixel(0,pong,255,255,255)
sense.set_pixel(0,pong+1,255,255,255)
sense.set_pixel(0,pong-1,255,255,255)

def paint():
  global x
  global y
  global pong
  sense.clear(0,0,0)
  sense.set_pixel(x,y,255,255,255)
  sense.set_pixel(0,pong,0,0,255)
  sense.set_pixel(0,pong+1,0,0,255)
  sense.set_pixel(0,pong-1,0,0,255)

def clamp(value, min_value=1, max_value=6):
    return min(max_value, max(min_value, value))

def refresh():
    if controls is True:
      sense.clear()
      paint()

def pushed_up(event):
    global pong
    global controls
    if event.action != ACTION_PRESSED and controls is True:
      pong = clamp(pong - 1)

def pushed_down(event):
    global pong
    global controls
    if event.action != ACTION_PRESSED and controls is True:
      pong = clamp(pong + 1)
      


while running is True:
  
  sense.stick.direction_up = pushed_up
  sense.stick.direction_down = pushed_down
  sense.stick.direction_any = refresh
  refresh()
  
  if x == 1 and ((y == pong) or (y == (pong+1)) or (y == (pong-1))):
    movex = True
  
  if movex is True and movey is True:
    x+=1
    y+=1
    if s > 0.1:
      s-=0.01
    paint()
    time.sleep(s)
    if x > 6:
      movex=False
    if y > 6:
      movey=False

  elif movex is True and movey is False:
    x+=1
    y-=1
    if s > 0.1:
      s-=0.01
    paint()
    time.sleep(s)
    if x > 6:
      movex=False
    if y < 1:
      movey=True

  elif movex is False and movey is False:
    x-=1
    y-=1
    if s > 0.1:
      s-=0.01
    paint()
    time.sleep(s)
    if x < 1:
      movex=True
    if y < 1:
      movey=True

  elif movex is False and movey is True:
    x-=1
    y+=1
    if s > 0.1:
      s-=0.01
    paint()
    time.sleep(s)
    if x < 1:
      movex=True
    if y > 6:
      movey=False
      
  if x is 7:
    score+=1
      
  if x is 0:
    controls=False
    sense.show_message('SCORE = ' + str(score), text_colour=red, back_colour=white)
    running=False
    sense.clear()
    


    


    

