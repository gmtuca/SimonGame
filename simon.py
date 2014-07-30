#SimonGame
#=========
#Simple Raspberry Pi Simon Memory Game, which requires\n
#-Raspberry Pi Model B
#-3 buttons (and 3x 1000Ω resistors - depending on current and voltage)
#-3 LEDs (and 3x 165Ω resistors - depending on current and voltage)
#-a few jumper wires -optional: a breadboard

import RPi.GPIO as gpio
import time
from random import randint

lights = [11, 12, 13]
n_lights = len(lights)

random = []

buttons = [15, 16, 18]

gpio.setmode(gpio.BOARD)

def getbuttonI(value):
  for x in range(n_lights):
    if(buttons[x] == value):
      return x
  return -1

def getlightsI(value):
  for x in range(n_lights):
    if(lights[x] == value):
      return x
  return -1

def setup():
  for x in range(n_lights):
    gpio.setup(lights[x], gpio.OUT)
    gpio.setup(buttons[x], gpio.IN, pull_up_down=gpio.PUD_DOWN)

def clean():
  for x in range(n_lights):
    gpio.output(lights[x], 0)

def clicked():
  while True:
    time.sleep(0.01)
    for x in range(n_lights):
      if(gpio.input(buttons[x]) == 1):
        return x
  return -1

def gameover():
  for x in range(n_lights):
    gpio.output(lights[x], 1)
  random[:] = []
  time.sleep(3)

  clicked()
  start()

def start():
  setup()

  time.sleep(2)
  while True:
    random.append(randint(0,2))

    for i in range(len(random)):
      clean()
      time.sleep(0.2)
      gpio.output(lights[random[i]], 1)
      time.sleep(0.5)

    clean()
    time.sleep(1)

    for i in range(len(random)):
      i_clicked = clicked()
      gpio.output(lights[i_clicked], 1)
      time.sleep(0.2)
      clean()

      if(i_clicked != random[i]):
        gameover()

    time.sleep(1)


try:
  start()
except KeyboardInterrupt:
   gpio.cleanup()
