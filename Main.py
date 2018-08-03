# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 23:54:12 2018

@author: X
"""
import random
from Map_ import *
from Player import *
from Item import *
from Assistant import *
from Weapon import *
from Bullet import *
from Enemy import *
from Bag import *
import time
import os

if __name__ == '__main__':
    birthPoint = (0,0)
    player = Player(birthPoint)
    player.initalizeCharacterStatus()
    player.getCharacterStatus()
    cell =Cell()
    map_ = Map()
    #map_.mapStructure()
    #map_.drawMap(cell,birthPoint)
    itemList = itemList(map_.map,0.62)
    itemList.generate()
    weaponList = weaponList(map_.map,0.5)
    weaponList.generate()
    bulletPackList = bulletPackList(map_.map,0.52)
    bulletPackList.generate()
    enemyList = enemyList(map_.map,0.7)
    enemyList.generate(birthPoint)
    #print(itemList.getList())
    cellCheck = cellCheck(itemList,weaponList,bulletPackList,enemyList)
    bag = Bag()
    weaponSlot = weaponSlot()
    bulletBag =bulletBag()
    #print(itemList.itemsDict,len(itemList.itemsDict))
    while True:
        print('-'*50)
        map_.drawMap(cell,player.getLocation())
        command = input('Please input command...')
        
        os.system('CLS')
        if command in ['w','s','a','d']:
            direction = command
            player.move(direction,map_)
            #map_.drawMap(cell,player.getLocation())
            player.locationInfo()
            #print(direction)
            #print(player.getLocation())
        #elif command == 'search':
#            print('Searching...')
#            time.sleep(1)
            hasBattle = cellCheck.enemyCheck(player)
            while hasBattle==True:
                test = input('press "a" to end the battle')
                if test == 'a':
                    hasBattle=False
                    enemyList.removeEnemy(hasBattle,player)
            cellCheck.assistantCheck(player)
            cellCheck.weaponCheck(player)
            cellCheck.bulletCheck(player) 
             
            #isDirRight = True
            ########################
        elif command[:4] == 'take':
            if command[4:] in ['medbot','epin','medkit','armer','nano','vsi']:
                try:
                    anItem = itemList.getList()[player.getLocation()]
                    player.getItem(anItem,bag,itemList)
                except:
                    print('No item in this room')
            elif command[4:] in ['hg','smg','rf','ar','kn']:
                try:
                    anWeapon = weaponList.getList()[player.getLocation()]
                    player.getItem(weaponSlot.multiWeaponCheck(anWeapon),weaponSlot,weaponList)
                except:
                    print('No weapon in this room')

            elif command[4:] in ['ub']:
                try:
                    bP = bulletPackList.getList()[player.getLocation()]
                    player.getItem(bP,bulletBag,bulletPackList)
                except:
                    print('No bullet pack in this room')
            else:
                print('Type "take+short name of item" to take item')            
                
            #print(itemList.itemsDict,len(itemList.itemsDict))
        elif command == 'checkbag':
            bag.info()
            pass
        elif command == 'checkweapon':
            weaponSlot.info()
            pass
        elif command == 'checkbullet':
            bulletBag.info()
            pass
        elif command == 'self':
            player.getCharacterStatus()
            
        elif command == 'useitem':
            commandItem = input('what item do you want to use..')
            player.useItem(commandItem,bag)
        elif command == 'discarditem':
            bag.info()
            commandItem = input('what item do you want to discard..')
            if commandItem == 'q':
                continue
            else:
                player.discardItem(commandItem,bag)
        elif command[:6] == 'weapon':
            weaponSlot.info()
            commandWeapon = input('which weapon do you want to use..')
            player.useWeapon(commandWeapon,weaponSlot)
        elif command == 'fist':
            player.fist()
            
        elif command == 'discardweapon':
            weaponSlot.info()
            commandItem = input('what item do you want to discard..')
            if commandItem == 'q':
                continue
            else:
                player.discardItem(commandItem,weaponSlot)
                player.discardWeaponInHand(commandItem)
                
                
        elif command == 'attack':
            dV = player.attack()
            print(dV)
            
        elif command == 'reload':
            player.reloadWeapon(bulletBag)
            pass
        ############################
        elif command=='q':
            break
        else:
            #map_.drawMap(cell,player.getLocation())
            print('Invaild command')
