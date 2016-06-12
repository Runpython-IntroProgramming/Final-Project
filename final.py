"""
final.py
Author: Adam Glueck
Credit: Stack oveflow (for eval function), my own bottomless wisdom and creativity
Assignment:  Choice
I wrote a program to use several calculus estimation technqiues.  
I am most proud of its use of a class based parser,
allowing it to convert traditional math notation into python math notation the eval function can determine.
"""
going='False'
while going=='False':
    i=str(input("welcome to the calculus calculator.  Would you like to: a, find the area under a curve), b (estimate the center of mass of an area between two functions), c (do basic math), q (quit)"))
    for j in ["a","b","c","d","q"]:
        if i==j:
            going='True'
from math import sin, cos, log, pi, e
class parse():
    def __init__(self,j):
        self.j=j
        function=""
        f=list(self.j)
        for i in range (0,len(f)-1):
            if f[i]=='l' and f[i+1]=='n':
                f[i+1]='g'
                f.insert(i+1,'o')
        for i in range (0,len(f)):
            if f[i]=='^':
                f[i]='*'
                f.insert(i+1,'*')
        for i in range (0,len(f)-1):
            for k in ['1','2','3','4','5','6','7','8','9','0']:
                if f[i]==k and f[i+1]=='x':
                    f.insert(i+1,'*')  
        for i in range (0,len(f)-3):
            for k in ['1','2','3','4','5','6','7','8','9','0']:
                    if f[i]==k and f[i+1]=='l' and f[i+2]=='o' and f[i+3]=='g':
                        f.insert(i+1,'*')
        equation=""
        for i in range (0,len(f)):
            equation=equation+f[i]
        self.equation=equation
if i=='a':
    i=str(input("this function will approximate the area under a function, please enter your desired function"))
    c=parse(i)
    f=c.equation
    xmin=float(input("x min "))
    xmax=float(input("x max "))
    numbershapes=float(input("number of shapes "))
    step=(xmax-xmin)/numbershapes
    numbershapes=int(numbershapes)
    a=0
    for i in range (0,numbershapes):
        i=xmin+step*i
        x=i
        a=a+(eval(f))*step
    a=str(a)
    print("LRAM is "+a)
    b=0
    for i in range (1,numbershapes+1):
        i=xmin+step*i
        x=i
        b=b+(eval(f))*step
    b=str(b)
    print("RRAM is "+b)
    c=str((float(a)+float(b))/2)
    print("TRAPEZOID is "+c)
    d=0
    for i in range (0,numbershapes):
        i=(xmin+step/2)+step*i
        x=i
        d=d+(eval(f))*step
    d=str(d)
    print("MRAM is "+d)
    e=str(2*(float(d)+float(c))/3)
    print("SIMPSON'S is "+e)
    i='q'
if i=='b':
    yone=str(input("This program will find the center of mass of the shape between two functions, please input the upper function "))
    ytwo=str(input("please enter the second function "))
    xmin=float(input("please input the minimum x value "))
    xmax=float(input("please input the minimum y value "))
    one=parse(yone)
    two=parse(ytwo)
    equation=one.equation+'-('+two.equation+')'
    yavg='(('+one.equation+'+'+two.equation+')/2)'
    ytop=yavg+"*("+equation+")"
    equation2="x*("+equation+")"
    d=0
    step=(xmax-xmin)/500
    for i in range (0,500):
        i=(xmin+step/2)+step*i
        x=i
        d=d+(eval(equation2))*step
    e=0
    for i in range (0,500):
        i=(xmin+step/2)+step*i
        x=i
        e=e+(eval(equation))*step
    top=0
    for i in range (0,500):
        i=(xmin+step/2)+step*i
        x=i
        top=top+(eval(ytop))*step
    bottom=0
    for i in range (0,500):
        i=(xmin+step/2)+step*i
        x=i
        bottom=bottom+(eval(equation))*step   
    xcenter=str(d/e)
    ycenter=str(top/bottom)
    print('the center of mass is about ('+xcenter+', '+ycenter+')')
    i='q'
if i=='c':
    i=str(input("please enter a math problem, there is no need to use weird python notation." ))
    problem=parse(i)
    print(eval(problem.equation))
    i='q'
if i=='q':
    print("Goodbye")
