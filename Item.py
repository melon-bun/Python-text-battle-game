# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 18:29:53 2018

@author: X
"""
import random
from Map_ import *
from Player import *
from Assistant import *
from Weapon import *

import os

class item(object):
    __typeList = ['Disposable medical robot','Epinephrine','Medkit',
                  'Armer','Nano machine','Visual Strength Injection']
    randNum = len(__typeList)-1
    def __init__(self):
        self.Name = ''
        self.type = None
        #self.location = location
        self.shortName = ''
        pass 
    def setType(self):
        self.Name = self.__typeList[random.randint(0,self.randNum)]
        if self.Name == 'Disposable medical robot':
            self.type = dispMedRob()
            self.shortName = 'medbot'
        elif self.Name == 'Epinephrine':
            self.type = epine()
            self.shortName = 'epin'
        elif self.Name == 'Medkit':
            self.type = medkit()
            self.shortName='medkit'
        elif self.Name == 'Armer':
            self.type = armer()
            self.shortName='armer'
        elif self.Name == 'Nano machine':
            self.type = nanoMachine()
            self.shortName='nano'
        elif self.Name == 'Visual Strength Injection':
            self.type = vsi()
            self.shortName='vsi'
        
        #self.type = self.itemName
class itemList(object):
    def __init__(self,map_,prop):
        self.map = map_
        self.Dict = {}
        self.prop = prop
        pass
    def generate(self):
        yCount = 0
        for y in self.map:
            xCount = 0
            for x in y:
                if x==1:
                    if (random.random()>self.prop):
                        Item = item()
                        Item.setType()
                        self.Dict[(yCount,xCount)]=Item
                xCount+=1
            yCount+=1
    def getList(self):
        return self.Dict
    def removeItem(self,location):
        self.Dict.pop(location)
        
        pass
 
class dispMedRob:
    def __init__(self):
        self.Health=15
        self.Defense = 0
        self.Speed = 0
        self.Shooting_skill = 0
        self.Fighting_skill = 0 
        pass

class epine:
    def __init__(self):
        self.Health=0
        self.Defense = 0
        self.Speed = 10+random.randint(0,random.randint(0,10))
        self.Shooting_skill = 0
        self.Fighting_skill = 0 
        pass

class medkit:
    def __init__(self):
        self.Health=30
        self.Defense = 0
        self.Speed = 0
        self.Shooting_skill = 0
        self.Fighting_skill = 0 
        pass

class armer:
    def __init__(self):
        self.Health=0
        self.Defense = 10+random.randint(0,random.randint(0,10))
        self.Speed = 0
        self.Shooting_skill = 0
        self.Fighting_skill = 0 
        pass

class nanoMachine:
    def __init__(self):
        self.Health=10 + random.randint(0,random.randint(0,10))
        self.Defense = 0
        self.Speed = random.randint(0,random.randint(0,10))
        self.Shooting_skill = random.randint(0,random.randint(0,10))
        self.Fighting_skill = 0 
        pass

class vsi:
    def __init__(self):
        self.Health=0
        self.Defense = 0
        self.Speed = 0
        self.Shooting_skill = 5+random.randint(0,random.randint(0,10))
        self.Fighting_skill = 0     
        pass
##############
#item和weapon的additem方法完全一致，改写传入参数
#######################
#class weaponList(itemList):
#    def addItems(self):
#        yCount = 0
#        for y in self.map:
#            xCount = 0
#            for x in y:
#                if x==1:
#                    if (random.random()>0.5):
#                        Weapon = weapon((y,x))
#                        Weapon.setType()
#                        self.Dict[(yCount,xCount)]=Weapon
#                xCount+=1
#            yCount+=1
#    pass
           


