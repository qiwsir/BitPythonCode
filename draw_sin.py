#!/usr/bin/env python
#coding:utf-8

import math
import turtle

#draw a line from (x1,y1) to (x2,y2)
def drawLine(ttl,x1,y1,x2,y2):
    ttl.penup()
    ttl.goto(x1,y1)
    ttl.pendown()
    ttl.goto(x2,y2)
    ttl.penup()

#write label at location x,y
def labelPoint(ttl,x,y,label):
    ttl.penup()
    ttl.goto(x,y)
    ttl.pendown()
    ttl.write(label)
    ttl.penup()

def drawGridMark(ttl,x,y,isVertical):
    if isVertical:
        drawLine(ttl,x,y+5,x,y-5)
    else:
        drawLine(ttl,x-5,y,x+5,y)

def labelGridPoint(ttl,x,y,isVertical,text):
    if isVertical:
        labelPoint(ttl,x-20,y-20,text)
    else:
        labelPoint(ttl,x+20,y,text)

def drawGridScaled(ttl):
    #draw the axes
    drawLine(ttl,-400,0,400,0)
    drawLine(ttl,0,400,0,-400)

    #label the x axis
    for x in [-300,-200,-100,100,200,300]:
        drawGridMark(ttl,x,0,True)
        labelGridPoint(ttl,x,0,True,(x/100,0))

    #label the y axis
    for y in [-300,-200,-100,100,200,300]:
        drawGridMark(ttl,0,y,False)
        labelGridPoint(ttl,0,y,False,(0,y/100))

def drawFnScaled(ttl,fn,lower,upper,step):
    ttl.penup()
    x = lower
    y = fn(x)
    scaledX = x*100
    scaledY = y*100
    ttl.goto(scaledX,scaledY)
    ttl.pendown()
    while x<upper:
        y=x+step
        y=fn(x)
        scaledX,scaledY = x*100,y*100
        ttl.goto(scaledX,scaledY)
    ttl.penup()

def myFunc(x):
    return (x**2-4)

def main():
    #put label on top of page
    turtle.title("Graphs of Functions")

    #setup screen size
    turtle.setup(800,800,0,0)

#create a turtle object
    ttl=turtle.Turtle()

#draw the grid
    drawGridScaled(ttl)

#draw sin finction
    ttl.pencolor("red")
    drawFnScaled(ttl,math.sin,-math.pi,math.pi,0.01)

#persist drawing
    turtle.done()

if __name__=="__main__":
    main()
