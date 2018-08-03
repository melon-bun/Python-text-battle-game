# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 04:24:26 2018

@author: X
"""
from Item import *
import random
class enemy:
    def __init__(self):
        self.Name = 'enemy'
        self.type = ''
        #self.location=location
    def setType(self):
        self.type='Mark I'
    
class enemyList(itemList):
    def generate(self,birthLoc):
        yCount = 0
        for y in self.map:
            xCount = 0
            for x in y:
                if (x==1) and (yCount,xCount)!=birthLoc:
                    if (random.random()>self.prop):
                        Enemy = enemy()
                        Enemy.setType()
                        self.Dict[(yCount,xCount)]=Enemy
                xCount+=1
            yCount+=1
    def removeEnemy(self,hasBattle,player):
        if hasBattle==False:
            self.Dict.pop((player.getLocation()))
            
    
    
    