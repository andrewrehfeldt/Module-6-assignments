from multiprocessing import Process
import os
from random import randrange
from datetime import datetime


def info(title):
    print(title)
    print('parent process', os.getppid())

def brushteeth():
    info('brush teeth')
    pause(10)
    print('Brushing teeth done')
    
def startcar():
    info('start car')
    pause(20)
    print("Starting our car")

def maketoast():
    info('making toast')
    pause(40)
    print('Toast finished')
    
def pause(time):
    targettime = datetime.now().second + time
while datetime.now().second < targettime:
    continue
    
info ('main line')
p = Process(target= brushteeth)

print(datetime.now())
