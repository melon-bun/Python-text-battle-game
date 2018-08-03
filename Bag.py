# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 07:44:14 2018

@author: X
"""

class Bag(object):
    def __init__(self):
        self.bagCapacity = 5
        self.bag_ = []
        self.bagName = 'bag'
        pass
    def addItem(self,item_):
        if len(self.bag_)<self.bagCapacity:
            self.bag_.append(item_)
            return False
        else:
            return True
        pass
    def popItem(self,itemName_):
        itemTemp = None
        for i in self.bag_:
            if (i.Name == itemName_)or(i.shortName == itemName_):
                itemTemp = i
                #assiIndex = self.bag_.index(itemTemp)
                break
        if itemTemp is not None:
            self.bag_.remove(itemTemp)
            return itemTemp
        else:
            #print('No such thing in your bag.')
            return None
        pass
    def info(self):
        if len(self.bag_)>0:
            for i in self.bag_:
                print('{num}\{itemname}({shortname})'.format(num=self.bag_.index(i)+1,itemname=i.Name,shortname=i.shortName))
                #print(self.bag_.index(i)+1,'\\',i.Name)
        else:
            print('Empty')
        #print(self.bag_)
        #print(len(self.bag_))
        pass
#    def discard(self,itemName_):
#        _=popItem(itemName_)
#        pass

class weaponSlot(Bag):
    def __init__(self):
        self.bagCapacity = 3
        self.bag_ = []
        self.bagName = 'weapon slot'
    def multiWeaponCheck(self,weapon_):
        weaponCount = 1
        for i in self.bag_:
            if weapon_.Name == i.Name:
                weaponCount+=1
        weapon_.shortName=weapon_.shortName+str(weaponCount)
        return weapon_
    def info(self):
        if len(self.bag_)>0:
            for i in self.bag_:
                print('{num}|{itemname}({shortname})|{gunInfo}'.format(num=self.bag_.index(i)+1,\
                      itemname=i.Name,shortname=i.shortName,gunInfo = i.type.gunInfo()))
        else:
            print('Empty')
    pass

class bulletBag(object):
    def __init__(self):
        self.bulletPackCapacity = 80
        self.bagCapacity = 3
        self.bag_=[]
        self.bagName = 'bullet bag'
        self.bulletNumDict = {}
    def addItem(self,bP):
        if len(self.bag_)<self.bagCapacity:
            if bP.Name in self.bulletNumDict.keys():
                self.bulletNumDict[bP.Name]+=bP.numOfBullets
            else:
                self.bulletNumDict[bP.Name]=bP.numOfBullets
            #self.bag_.append(item_)  
            return False
        else:  
            return True
        
    def popBullet(self,bullteName,requiredBulletNum):
        if bullteName in self.bulletNumDict.keys():
            bulletNum = self.bulletNumDict[bullteName]
            if bulletNum>0 and bulletNum>=requiredBulletNum:
                self.bulletNumDict[bullteName] -= requiredBulletNum
                
                return requiredBulletNum
            else:
                self.bulletNumDict[bullteName] = 0 
                return bulletNum
        else:
            print("This type of bullet doesn't existed. ")
            return 0
        pass
    
    def info(self):
        for key,value in self.bulletNumDict.items():
            print('{name}:{num}'.format(name=key,num=value))
        pass