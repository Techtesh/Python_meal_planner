# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 19:12:02 2020

@author: Hitesh
"""
import csv
import random
import numpy as np



data=[]
Soups=[]
Mains=[]
Apps=[]
Breakfast=[]
Lunches=[]
types=[]
def datainit():
    try:
        with open("recepies.csv",newline="") as csvfile:
            read=csv.reader(csvfile)
            for row in read:
                #print(row)
                temp=[row[2],row[9],row[10],row[11],row[5]]
                r=row[5][1:-1]
                r=r.split(",")
                for R in r:
                    if R not in types:
                        types.append(R)
                data.append(temp)
                if "Soup" in row[5]:
                    Soups.append([row[2],eval(row[9]),eval(row[10]),eval(row[11])])
                if "Salad" in row[5]:
                    Soups.append([row[2],eval(row[9]),eval(row[10]),eval(row[11])])
                if "Side" in row[5]:
                    Soups.append([row[2],eval(row[9]),eval(row[10]),eval(row[11])])
                if "Sauce" in row[5]:
                    Soups.append([row[2],eval(row[9]),eval(row[10]),eval(row[11])])
                if "Main" in row[5]:
                    Mains.append([row[2],eval(row[9]),eval(row[10]),eval(row[11])])
                if "Appetizer" in row[5]:
                    Apps.append([row[2],eval(row[9]),eval(row[10]),eval(row[11])])
                if "Snack" in row[5]:
                    Apps.append([row[2],eval(row[9]),eval(row[10]),eval(row[11])])
                if "Breakfast" in row[5]:
                    Breakfast.append([row[2],eval(row[9]),eval(row[10]),eval(row[11])])
                if "Bake" in row[5]:
                    Apps.append([row[2],eval(row[9]),eval(row[10]),eval(row[11])])
                if "Dessert" in row[5]:
                    Apps.append([row[2],eval(row[9]),eval(row[10]),eval(row[11])])
                if "Lunch" in row[5]:
                    Lunches.append([row[2],eval(row[9]),eval(row[10]),eval(row[11])])
                if "Beverage" in row[5]:
                    Apps.append([row[2],eval(row[9]),eval(row[10]),eval(row[11])])
                if "Other" in row[5]:
                    Apps.append([row[2],eval(row[9]),eval(row[10]),eval(row[11])])
             
                
    except:
        pass



def Select(meal,lim):
    sublist=[b for b in meal if b[2]<=lim]
    n=random.randint(0, len(sublist)-1)
    return sublist[n]
    pass





def calc(bmr):
    BreakLim=0.35*bmr
    BrunchLim=0.1*bmr
    LunchLim=0.2*bmr
    TeaLim=0.05*bmr
    DinnerLim=0.4*bmr
    menu=[]
    
    for x in range (0,7):
        while True:
            a1=Select(Breakfast,BreakLim)
            if a1 not in menu:
                menu.append(a1)
                break
        while True:
            a1=Select(Soups,BrunchLim)
            if a1 not in menu:
                menu.append(a1)
                break
        while True:
            a1=Select(Lunches,LunchLim)
            if a1 not in menu:
                menu.append(a1)
                break
        while True:
            a1=Select(Apps,TeaLim)    
            if a1 not in menu:
                menu.append(a1)
                break
        while True:
            a1=Select(Mains,DinnerLim)
            if a1 not in menu:
                menu.append(a1)
                break
        pass
    print(menu)
    return(menu)
if __name__=="__main__":
    
    datainit()
    calc(2500)