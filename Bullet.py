# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 10:49:18 2018

@author: X
"""

import random
from Map_ import *
from Player import *
from Item import *

class bulletPack(item):
    __typeList = ['Universal Bullet']
    #randNum = len(__typeList)-1
    def __init__(self):
        self.numOfBullets = random.randint(5,22)
        self.type = None
        self.Name = self.__typeList[0]
        self.shortName = ''
        #self.location = location
        pass
    def setType(self):
        #self.Name = self.__typeList[random.randint(0,self.randNum)]
        self.Name = self.__typeList[0]
        #if self.Name == 'Disposable medical robot':
        self.type = bullet()
        self.shortName = 'ub'
        
        
class bulletPackList(itemList):
    def generate(self):
        yCount = 0
        for y in self.map:
            xCount = 0
            for x in y:
                if x==1:
                    if (random.random()>self.prop):
                        BP = bulletPack()
                        BP.setType()
                        self.Dict[(yCount,xCount)]=BP
                xCount+=1
            yCount+=1
            
class bullet(object):
    def __init__(self):
        self.type = 'Universal Bullet'
        self.demageIndex = 1
        #self.distance = None
        pass
    