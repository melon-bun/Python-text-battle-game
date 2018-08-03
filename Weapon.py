# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 00:07:49 2018

@author: X
"""

import random
from Map_ import *
from Player import *
from Item import *
from Assistant import *

class weapon(item):
    __typeList = ['Handgun','Small Machine Gun','Rifle','Assult Rifle','Knife']
    randNum = len(__typeList)-1
    def setType(self):
        self.Name = self.__typeList[random.randint(0,self.randNum)]
        if self.Name == 'Handgun':
            self.type=handGun()
            self.shortName = 'hg'
        elif self.Name == 'Small Machine Gun':
            self.type=smallMachineGun()
            self.shortName = 'smg'
        elif self.Name == 'Rifle':
            self.type=rifle()
            self.shortName='rf'
        elif self.Name == 'Assult Rifle':
            self.type=assultRifle()
            self.shortName='ar'
        elif self.Name == 'Knife':
            self.type=knife()
            self.shortName='kn'
    pass

class weaponList(itemList):
    def generate(self):
        yCount = 0
        for y in self.map:
            xCount = 0
            for x in y:
                if x==1:
                    if (random.random()>self.prop):
                        Weapon = weapon()
                        Weapon.setType()
                        self.Dict[(yCount,xCount)]=Weapon
                xCount+=1
            yCount+=1
    pass

class gun(object):
    def __init__(self):
        self.magazine = 10
        self.demage = 10
        self.bullet = random.randint(1,self.magazine-5)
        self.accuracyRate = 100
        #self.distance = None
        self.isReloadable = True
        pass
    
    def shoot(self):
        if self.bullet>0:
            self.bullet-=1
            return self.demage
        else:
            print('out of ammo.')
            return -1
        pass
    
    def reload(self,bulletBag_,bulletNum):
        #amount = bulletNum
        moreBullet = bulletBag_.popBullet('Universal Bullet',bulletNum)
        if moreBullet>-1:
            self.bullet+=moreBullet
           
    def gunInfo(self):
        info = 'Demage:{value1}|Bullet:{value2}/{value3}'.format(value1 = self.demage,value2 = self.bullet,value3 = self.magazine)
        return info
    pass


class handGun(gun):
    def __init__(self):
        self.magazine = 15
        self.demage = random.randint(8,15)
        self.bullet = random.randint(1,self.magazine-5)
        self.accuracyRate = 100
        self.isReloadable = True
    pass

class smallMachineGun(gun):
    def __init__(self):
        self.magazine = 30
        self.demage = random.randint(5,10)
        self.bullet = random.randint(1,self.magazine-15)
        self.accuracyRate = 100
        self.isReloadable = True
    pass

class rifle(gun):
    def __init__(self):
        self.magazine = 6
        self.demage = random.randint(25,40)
        self.bullet = random.randint(1,self.magazine-3)
        self.accuracyRate = 100
        self.isReloadable = True
    pass

class assultRifle(gun):
    def __init__(self):
        self.magazine = 25
        self.demage = random.randint(15,30)
        self.bullet = random.randint(1,self.magazine-15)
        self.accuracyRate = 100
        self.isReloadable = True
    pass

class knife(gun):
    def __init__(self):
        self.magazine = 30
        self.demage = random.randint(8,15)
        self.bullet = self.magazine
        self.accuracyRate = 100
        self.isReloadable = False
        
    def gunInfo(self):
        info = 'Demage:{value1}|Durability:{value2}/{value3}'.format(value1 = self.demage,value2 = self.bullet,value3 = self.magazine)
        return info    
    pass
###################
