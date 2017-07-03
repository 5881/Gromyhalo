#!/bin/python
#Режим освещения  - цветное освещение

from time import sleep
import random
import math
from serial import *
global ki
#import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np
ser = Serial("/dev/ttyUSB0" , 115200)

#случайный выбор 1 элемента из списка клевых цветов

RGB = random.choice([[219, 240, 37],[254, 74, 0], [142, 47, 240], [178, 210, 0], [138, 139, 47], [219, 0, 240], [0, 144, 244], [254,0,0] ])

#отправка пакета на ШИМ LED       
ser.write(bytearray([int(RGB[0]),int(RGB[1]),RGB[2], int(RGB[0]),int(RGB[1]),RGB[2],0,0,0,0,0,0,0xff]))

#продолжительность свечения
#sleep(3600)

#выключение
#ser.write(bytearray([0,0,0,0,0,0,0,0,0,0,0,0,0xff]))


