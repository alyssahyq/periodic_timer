#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time 
import sys
import os   # For Mac users
#import winsound    # For Windows users


timer = input('Set a periodic timer as <hh:mm:ss>:')
Timer = timer.split(':')
ss = int(Timer[-1])
if len(Timer) > 1:
    mm = int(Timer[-2])
    if len(Timer) > 2:
        hh = int(Timer[-3])
    else:
        hh = 0
else:
    mm = 0
    hh = 0
    
sum_in_second = hh * 3600 + mm * 60 + ss

print('Counting down %d*60*60 + %d*60 + %d = %d seconds' % (hh, mm, ss, sum_in_second))
counter = 0
start_time =  time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print ('Start at', start_time)
while True:
    time.sleep(sum_in_second - 0.2)
    os.system('afplay /System/Library/Sounds/Submarine.aiff') # Hero.aiff
    # winsound.beep(800,0.2)
    counter = counter + 1
    print(counter,'*', timer, 'passed.')

