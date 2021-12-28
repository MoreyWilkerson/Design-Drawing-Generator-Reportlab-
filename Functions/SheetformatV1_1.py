# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 13:38:41 2021

@author: Morey
"""
#add needed libraries 
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

#create function for sheet format
def sheetformat(c,S):
    # Origin: bottom left 
 # define a font
     c.setFont("Times-Roman", 12)     
 # draw some lines
     # Horizontal
     c.line(.25*inch,2 *inch ,16.75 * inch ,2*inch)
     c.line(6.4375*inch,.855 *inch ,8.625 * inch ,.855 *inch)
         #THAT row
     c.line(10.625*inch,.4164*inch , 12.5*inch,.4164*inch)
     c.line(10.625*inch,.5467*inch , 12.5*inch,.5467*inch)
     c.line(10.625*inch,.6767*inch , 12.5*inch,.6767*inch)
     c.line(10.625*inch,.8067*inch , 12.5*inch,.8067*inch)
     c.line(10.625*inch,.9367*inch , 12.5*inch,.9367*inch)
     c.line(10.625*inch,1.0667*inch , 12.5*inch,1.0667*inch)
     c.line(10.625*inch,1.1967*inch , 12.5*inch,1.1967*inch)
     c.line(10.625*inch,1.3267*inch , 12.5*inch,1.3267*inch)
     c.line(10.625*inch,1.4567*inch , 12.5*inch,1.4567*inch)
     c.line(10.625*inch,1.5867*inch , 12.5*inch,1.5867*inch)
         #final row
     c.line(12.5*inch,.6138*inch , 16.75*inch,.6138*inch)  
     c.line(12.5*inch,.9638*inch , 16.75*inch,.9638*inch)  
     c.line(12.5*inch,1.3138*inch , 16.75*inch,1.3138*inch)  
     c.line(12.5*inch,1.6638*inch , 16.75*inch,1.6638*inch)  
     #Vertical 
     c.line(6.4375*inch,2 *inch , 6.4375*inch,.25*inch)
     c.line(8.625*inch,2 *inch , 8.625*inch,.25*inch)
     c.line(10.625*inch,2 *inch , 10.625*inch,.25*inch)
     c.line(12.5*inch,2 *inch , 12.5*inch,.25*inch)
     c.line(15.922*inch,.6138*inch , 15.922*inch,.25*inch)  
 # draw a rectangle
     c.setLineWidth(1.5)
     c.setStrokeColorRGB(0.75,0.75,0.75)
     c.rect(0.25*inch,0.25*inch,16.5*inch,10.5*inch, fill=0)

 # Section 1 
     c.drawString(12.55*inch, .3842*inch, "Project No: ")
     S = "S - " + S
     c.drawString(16*inch, .3842*inch, S)
     c.drawString(12.55*inch, .75*inch, "Title: ")
     c.drawString(12.55*inch, 1.1*inch, "Customer: ")
     c.drawString(12.55*inch, 1.45*inch, "Location: ")
     c.drawString(12.55*inch, 1.8*inch, "Project: ")
 # define a font but smaller 
     c.setFont("Times-Roman", 8)   
     c.drawString(10.675*inch, .2832*inch, "Last Saved: ")
     c.drawString(10.675*inch, .45*inch, "REVISION DATE: ")
     c.drawString(10.675*inch, .58*inch, "REVISION: A")
     c.drawString(10.675*inch, .71*inch, "APPROVAL DATE: ")
     c.drawString(10.675*inch, .84*inch, "PERMIT: ")
     c.drawString(10.675*inch, .97*inch, "Q.A: ")
     c.drawString(10.675*inch, 1.1*inch, "MFG APPR: ")
     c.drawString(10.675*inch, 1.23 * inch, "MFG DWG: ")
     c.drawString(10.675*inch, 1.36*inch, "CHECKED: ")
     c.drawString(10.675*inch, 1.49*inch, "DESIGN DWG: MEW ")
     c.drawString(10.675*inch, 1.90*inch, "Client Signature:  ")
# image
     #im = Image("wellbilt logo.jpg")
     c.drawInlineImage("python-logo.jpg",0.3*inch,0.3*inch,6*inch,1.65 * inch)

c = canvas.Canvas("hello.pdf",pagesize =(17*inch, 11*inch))
sheetformat(c,"1000")
c.showPage()
c.save()
