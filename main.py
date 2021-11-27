from pynput.keyboard import Controller
import random
import time



keyboard = Controller()
ad = ['a', 'd']

def autoforward():
    a_or_d = random.choice(ad)
    delay1 = random.randint(1,3)
    delay2 = random.randint(1,10)
    time.sleep(delay1)
    keyboard.press('w')
    keyboard.press(a_or_d)
    time.sleep(delay2)
    keyboard.release('w')
    keyboard.release(a_or_d)



while True:
    autoforward()
