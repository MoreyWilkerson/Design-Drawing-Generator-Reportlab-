# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 14:18:36 2021

@author: Morey
"""
import math
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

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
         
def note (c, xm,ym,xb,yb,note):
    c.line(xm,ym,xb,yb-.025*inch)
    if xb >= xm:
        c.line(xb,yb-.025*inch, xb + c.stringWidth(note),yb-.025*inch)
        c.drawString(xb,yb,note)
        lineends(c,xm,ym,xb,yb-.025*inch,1)
    elif  xb < xm:
        lineends(c,xm,ym,xb,yb,3)
        c.line(xb,yb-.025*inch, xb - c.stringWidth(note),yb-.025*inch)
        c.drawRightString(xb,yb-.025*inch,note)   
        
c = canvas.Canvas("Note.pdf",pagesize =(4*inch, 4*inch)) #page format

note(c,1.75*inch,1.75*inch,2.25*inch,2.25*inch,"This is a note")

c.showPage()
c.save()