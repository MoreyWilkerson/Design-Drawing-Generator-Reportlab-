# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 14:18:36 2021

@author: Morey
"""
import math
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch



def fracking(x):
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
    
def lineends(c,x1,y1,x2,y2,n):#triangles, Bro 
     ffs = 1
     if n == 3: 
         ffs = -1
     h=ffs * .0625*inch #how far back to go
     b=.0625*inch/4 #sides of arrow 
     #OHHH MASTER, WHAT IF ITS VERTICAL? :(( SLOPE IS UNDEFINDED
     
     if (x1-x2)== 0:
         slope = 90 #this should work dirty girl
     else :
         slope =(y1-y2)/(x1-x2)
    
     hyp = math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
     theta=math.atan(slope)   
     if hyp <= h*2:
         h = -h
     #make new axis     
     p2x=-h*math.cos(theta)+b*math.sin(theta)
     p2y=-h*math.sin(theta)-b*math.cos(theta)
     p3x=-h*math.cos(theta)-b*math.sin(theta)
     p3y=-h*math.sin(theta)+b*math.cos(theta) 
     if slope == 90:
         p2x = b
         p3x = -b
         p2y = -h
         p3y = -h
     p = c.beginPath()
     p.moveTo(x1,y1)
     p.lineTo(x1-p2x,y1-p2y)
     p.lineTo(x1-p3x,y1-p3y)
     p.lineTo(x1,y1)
     p.close()
     c.drawPath(p,fill=1)
     if n==2 : 
         p = c.beginPath()
         p.moveTo(x2,y2)
         p.lineTo(x2+p2x,y2+p2y)
         p.lineTo(x2+p3x,y2+p3y)
         p.lineTo(x2,y2)
         p.close()
         c.drawPath(p,fill=1) 
        
def typDim(c,x1,y1,x2,y2,xstr,dim):    
    c.line(x1,y1,x2,y2)
    lineends(c,x1,y1,x2,y2,2)
    
    f=1 # is it to the left? 
    if xstr > x2: 
            c.line(x2,y2,xstr-.0625*inch,y2)    
    elif xstr < x1: 
            c.line(xstr+.0625*inch,y1,x1,y2)
            f= -1
    c.setStrokeColorRGB(1,1,1) #TIME FOR DIMS 
    c.setFillColorRGB(1,1,1)
    c.rect((xstr),(y1+(y2-y1)/2-6/72*inch),(f)*c.stringWidth(dim),12/72*inch,fill=1)
    c.setStrokeColorRGB(0,0,0)
    c.setFillColorRGB(0,0,0)
    c.drawString((xstr-((1-f)/2*c.stringWidth(dim))),y1+(y2-y1)/2-.04*inch,dim)#mf Clear width

        
c = canvas.Canvas("Dimspace.pdf",pagesize =(17*inch, 11*inch)) #page format

c.line(0.25*inch,1.75*inch,.25*inch,2.25*inch)
c.line(4*inch,1.75*inch,4*inch,2.25*inch)


typDim(c,0.25*inch,2*inch,4*inch,2*inch,2*inch,fracking(500))

c.showPage()
c.save()
