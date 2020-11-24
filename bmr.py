# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 17:36:05 2020

@author: Hitesh
"""
import os,sys
import bmr_sel
from tkinter import *

def foodpick(bmr):
    pass

def hclick():
    global height
    
    if htype.get()==1:
        height=int(e.get())/100
        ltext="height ="+str(height)+"m "
    elif htype.get()==2:
        height=int(e.get())*2.54/100
        ltext="height ="+str(height)+"m "
    if wtype.get()==1:
        weight=int(e2.get())
        l2text="weight ="+str(weight)+"KG \n"
    elif wtype.get()==2:
        weight=int(e2.get())/2.204
        l2text="weight ="+str(weight)+"KG \n"
    elif wtype.get()==2:
        weight=int(e2.get())/0.157473
        l2text="height ="+str(weight)+"KG \n"
    bmi=weight/height**2
    l3text="BMI="+str(bmi)   
    if bmi<15:
        l4text="Severly underweight"
        color="red"
    elif bmi>=15 and bmi<19.5:
        l4text="underweight"
        color="orange"
    elif bmi>=19.5 and bmi<24:
        l4text="adequate/healthy"
        color="green"
    elif bmi>=24 and bmi<30:
        l4text="overweight"
        color="orange"
    elif bmi>=30:
        l4text="obese"
        color="red"
    
    if stype.get()==1:
        bmr=88.362+13.397*weight+479.9*height-5.677*int(age.get())
    elif stype.get()==2:
        bmr=447.593+9.247*weight+309.8*height-4.33*int(age.get())
    if atype.get()==1:bmr=bmr*1.2
    if atype.get()==2:bmr=bmr*1.375
    if atype.get()==3:bmr=bmr*1.55
    if atype.get()==4:bmr=bmr*1.75
    l5text="bmr="+str(bmr)
    Label(root,text=l3text[:10]).place(x=200,y=300)
    Label(root,text=l4text,fg=color).place(x=200,y=320)
    Label(root,text=l5text).place(x=200,y=350)
    bmr_sel.datainit()
    menu=bmr_sel.calc(bmr)
    n,i,j=0,0,0
    for m in menu:
        i=n//5
        j=n%5
        temp=""
        M=m[0]
        #f=M.index["&"]
        #M=M[:f]
        temp+=str(M)
        Label(root,text=temp,font=("Helvetica",8)).place(x=225*(i+1),y=400+30*j)
        n+=1
        
    Label(root,text="Monday").place(x=225,y=370)
    Label(root,text="Tuesday").place(x=450,y=370)
    Label(root,text="Wednesday").place(x=675,y=370)
    Label(root,text="thursday").place(x=900,y=370)
    Label(root,text="Friday").place(x=1125,y=370)
    Label(root,text="Saturday").place(x=1350,y=370)
    Label(root,text="Sunday").place(x=1575,y=370)
    
    Label(root,text="Breakfast").place(x=0,y=400)
    Label(root,text="Brunch").place(x=0,y=430)
    Label(root,text="Lunch").place(x=0,y=460)
    Label(root,text="Tea").place(x=0,y=490)
    Label(root,text="Dinner").place(x=0,y=520)
    
def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)


root=Tk()
e=Entry(root)
label1=Label(root,text="enter your height").grid(column=0,row=0)
htype=IntVar()
R1=Radiobutton(root,text="cm",variable=htype,value=1).grid(column=0,row=1)
R2=Radiobutton(root,text="inches",variable=htype,value=2).grid(column=1,row=1)
#e.pack()
e.grid(column=1,row=0)
h=e.get()
print(h)

#b.pack()

label2=Label(root,text="enter your weight").grid(column=0,row=2)
e2=Entry(root)
e2.grid(column=1,row=2)
wtype=IntVar()
R3=Radiobutton(root,text="KG",variable=wtype,value=1).grid(column=0,row=3)
R4=Radiobutton(root,text="lbs",variable=wtype,value=2).grid(column=1,row=3)
R5=Radiobutton(root,text="stone",variable=wtype,value=3).grid(column=2,row=3)



label3=Label(root,text="enter your activity level").grid(column=0,row=5)
atype=IntVar()
Radiobutton(root,text="sedentary                        ",variable=atype,value=1).place(x=150,y=120)
Radiobutton(root,text="Light exercise :1-3 times/week   ",variable=atype,value=2).place(x=150,y=140)
Radiobutton(root,text="moderate exercise :3-5 times/week",variable=atype,value=3).place(x=150,y=160)
Radiobutton(root,text="heavy exercise :5+ times/week    ",variable=atype,value=4).place(x=150,y=180)

Label(root,text="enter sex").place(x=0,y=200)
stype=IntVar()
Radiobutton(root,text="Male",variable=stype,value=1).place(x=150,y=200)
Radiobutton(root,text="Female",variable=stype,value=2).place(x=150,y=220)

Label(root,text="enter Age").place(x=0,y=240)
age=Entry(root)
age.place(x=150,y=240)
ageval=age.get()




Button(root,text="enter data",command=hclick).place(x=150,y=260)
Button(root,text="RESET",command=restart_program).place(x=0,y=550)
# set window title
root.wm_title("BMR ")
root.geometry("2000x700")
root.mainloop()