# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 16:50:09 2021

@author: morey
"""

import math

def Float2Feet(x):
  xft=math.floor(x/12) #how many feet?
  xin=x-(xft*12)
  xin = round(.0625* round(float(xin)/.0625),4) #changes to a normal decimal 
  xr=  math.floor(xin)
  base =16
  xfr=(xin-xr)*16
  for y in range(3):
      if xfr % 2 == 0:
          xfr = xfr/2
          base = base/2
      else : break
  if xfr == 0:
      x = str(int(xft))+"' " + str(int(xr))+'"'
      return x
  else :
      x = str(int(xft))+"' " + str(int(xr)) +" " +str(int(xfr))+"/"+str(int(base))+'"'
      return x
  
print(28.375)
print(Float2Feet(28.375))
