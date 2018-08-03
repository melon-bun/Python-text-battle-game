# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 00:29:13 2018

@author: X
"""
import random
from Map_ import *
from Weapon import *
from Bag import *

class Player(object):
    def __init__(self,initalLoaction): #(y,x) y is the vertical axis, x is the horizen axis
        self.__currentLocation = initalLoaction
        self.locInfo = ''
        self.__Y = self.__currentLocation[0]
        self.__X = self.__currentLocation[1]
        self.__Health=100
        self.__Defense = 0
        self.__Speed = 0
        self.__Shooting_skill = 0
        self.__Fighting_skill = 0
        self.__hand = None
        self.bag_ = None
        self.weaponSlot = None
        self.bulletSlot = None
        pass
    
    def initalizeCharacterStatus(self):
        self.__Defense = random.randint(50,90)
        self.__Speed = random.randint(50,90)
        self.__Shooting_skill = random.randint(50,90)
        self.__Fighting_skill = random.randint(50,90) 
        pass
    def setCharacterStatus(self,property_):       
        pass
    
    def getCharacterStatus(self):
        print("Health: ",self.__Health)
        print("Defense: ",self.__Defense)
        print("Speed: ",self.__Speed)
        print("Shooting_skill: ",self.__Shooting_skill)
        print("Fighting_skill: ",self.__Fighting_skill)
        if self.__hand is not None:    
            print("Weapon:{name}({shortname})|{gunInfo}".format(name = self.__hand.Name,\
                  shortname = self.__hand.shortName,gunInfo = self.__hand.type.gunInfo()))
        else:
            print("Weapon:Fist")
        pass
    
    def move(self,direction,map_):
        if direction == 'w':
            walk =  (-1,0)
        elif direction == 's':
            walk =  (1,0)
        elif direction == 'a':
            walk = (0,-1)
        else:
            walk = (0,1)
            
        __locationTemp = (self.__currentLocation[0]+walk[0],self.__currentLocation[1]+walk[1])
            
        if (__locationTemp[0]<0) or (__locationTemp[1]<0):
            self.locInfo = "You can't move to there."
            self.__currentLocation = self.__currentLocation
        elif (__locationTemp[0]>map_.height-1) or (__locationTemp[1]>map_.width-1):
            self.locInfo = "You can't move to there."
            self.__currentLocation = self.__currentLocation
        elif (map_.getMap(__locationTemp)==0):
            self.locInfo = "There is no room."
            self.__currentLocation = self.__currentLocation
        else:
            self.__currentLocation = __locationTemp
            self.locInfo = "Move to cell"+str(self.__currentLocation)
        pass
    
    def locationInfo(self):
        print(self.locInfo)
        pass
    
    def attack(self):
        if self.__hand is None:
            demageValue = int(self.__Fighting_skill/10)+6
        else:
            weaponInHand = self.__hand.type
            demageValue = weaponInHand.shoot()
        return demageValue 
        pass

    def getItem(self,item_,bag,itemList):
        isFull = bag.addItem(item_)
        if isFull != True:           
            itemList.removeItem(self.__currentLocation)
            print('Get',item_.Name)
        else:
            print('The {bag} is full.'.format(bag=bag.bagName))
        pass
    
    def useItem(self,item_,bag):
        itemInHand = bag.popItem(item_)
        if itemInHand is None:
            print('No such thing in your bag.')    
        else:    
            print('use',itemInHand.type)
            self.updataCharacterStatus(itemInHand)
        pass
    
    def useWeapon(self,weapon,weaponSlot):
        isWeaponExist=False
        for weapon_ in weaponSlot.bag_:
            if weapon==weapon_.shortName:
                self.__hand=weapon_
                print('{weapon} is equiped'.format(weapon=weapon_.Name))
                isWeaponExist=True
                break
        if isWeaponExist==False:
            print('No such thing in your bag.')
        pass
    
    def reloadWeapon(self,bulletBag__):
        if (self.__hand is None) or (self.__hand.type.isReloadable==False):
            print('Unreloadable')
        else:
            weaponInHand = self.__hand.type
            neededBullet = weaponInHand.magazine-weaponInHand.bullet
            weaponInHand.reload(bulletBag__,neededBullet)
        pass
    
    def fist(self):
        self.__hand = None
    
    def discardItem(self,item_,bag):
        disItem = bag.popItem(item_)
        if disItem is None:
            print('No such thing in your bag.')
        else:
            print('{item} has been discarded.'.format(item=disItem.Name))
        disItem = None
        pass
    
    def discardWeaponInHand(self,discardWeapon):
        if self.__hand is not None and self.__hand.shortName == discardWeapon:
            self.__hand=None
        pass
    
    def updataCharacterStatus(self,item_):
        self.__Health += item_.type.Health
        if self.__Health>100:
            self.__Health=100
        self.__Defense += item_.type.Defense
        self.__Speed += item_.type.Speed
        self.__Shooting_skill += item_.type.Shooting_skill
        self.__Fighting_skill += item_.type.Fighting_skill
        
    def getLocation(self):
        currentLocation = self.__currentLocation
        return currentLocation
        pass     
    pass

