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
         
def weldnote(c,xm,ym,xb,yb,size,field,note): # field: if zero, field weld not shown 
    c.setFillColorRGB(0,0,0)
    for x in range(len(xm)):
        c.line(xm[x],ym[x],xb,yb)
        lineends(c,xm[x],ym[x],xb,yb,1)
        
    c.line(xb,yb,xb+inch,yb)#horz
    c.line(xb+.5*inch,yb,xb+.5*inch,yb-.1875*inch)
    c.line(xb+.5*inch,yb-.1875*inch,xb+.6875*inch,yb)
    c.line(xb+inch,yb,xb+1.168*inch,yb-.168*inch)
    c.line(xb+inch,yb,xb+1.168*inch,yb+.168*inch)
    c.drawString(xb+1.125*inch,yb-3/72*inch,note)
    c.drawRightString(xb+.4875*inch,yb-0.15*inch,size)
    if field ==1:
        c.line(xb,yb,xb,yb-.25*inch)
        p = c.beginPath()
        p.moveTo(xb,yb-.25*inch)
        p.lineTo(xb+.25*inch,yb-(.25+2.5/32)*inch)#right
        p.lineTo(xb,yb-(.25+5/32)*inch)#right
        p.lineTo(xb,yb-.25*inch)
        p.close()
        c.drawPath(p,fill=1)
c = canvas.Canvas("weldnote.pdf",pagesize =(4*inch, 4*inch)) #page format

weldnote(c,[1.5*inch,2*inch],[1.75*inch,1.75*inch],2.25*inch,2.25*inch,"1/4",1,"E7018")

c.showPage()
c.save()
