# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 21:06:46 2018

@author: X
"""
class Map(object):
    def __init__(self):
        self.map = [[1,0,1,1,1,1,1,1,1],
                    [1,1,1,0,0,1,1,0,1],
                    [1,0,1,0,0,0,1,1,1],
                    [1,1,1,1,1,1,0,1,0]]
        self.width = len(self.map[0])
        self.height = len(self.map)
        self.maxLength = 0
        pass

    def mapStructure(self):
        map__ = self.map
        for i in map__:
            for j in i:
                if j == 0 :
                    print(' ',end="")
                else:
                    print('X',end="")
            print('')                
    def drawMap(self,cell,playerLocation):
        structure = self.map
        playerX = playerLocation[1]
        playerY = playerLocation[0]
        y = 0
        
        for line in structure:
            row1 = ''
            row2 = ''
            row3 = ''
            row4 = ''
            x = 0
            for state in line:
#                if i==1:
                playerState = 0
                if (y==playerY)&(x==playerX)&(state==1):
                    playerState=1
                row1 = row1+cell.cellShape(state,playerState)[0]
                row2 = row2+cell.cellShape(state,playerState)[1]
                row3 = row3+cell.cellShape(state,playerState)[2]
                row4 = row4+cell.cellShape(state,playerState)[3]
                
                x+=1
            print(row1,"\n",row2,"\n",row3,"\n",row4,"\n",row1,sep="")
            y+=1
            self.maxLength=len(row1)
    def getMap(self,playerLocation):
        return self.map[playerLocation[0]][playerLocation[1]]

    def __str__(self):
        return str(self.map)
###┏━┓  ┃╋┃ ┗━┛
class Cell(object):
    def __init__(self):
        pass
    
    def cellShape(self,isCell,isPlayerHere=0):
        self.shape = [' '*2+('|'*isCell+' '*abs(isCell-1))+' '*2,\
                      ' '+('╔═╗')*isCell+(' '*abs(isCell-1))*3+' ',\
                       ('─'+'║')*isCell+(' '*abs(isCell-1))*2+' '+('║'+'─')*isCell+(' '*abs(isCell-1))*2,\
                       ' '+('╚═╝')*isCell+(' '*abs(isCell-1))*3+' ']
        if isPlayerHere == 1:
            self.shape[2] = ('─'+'║')*isCell+(' '*abs(isCell-1))*2+'X'+('║'+'─')*isCell+(' '*abs(isCell-1))*2
        return self.shape

class cellCheck(object):
    def __init__(self,itemList,weaponList,BPList,eList):
        self.itemList = itemList
        self.weaponList = weaponList
        self.bulletPackList = BPList
        self.enemyList = eList
        pass
    def assistantCheck(self,player):
        playerLoc = player.getLocation()
        itemDict_ = self.itemList.getList()
        if playerLoc in itemDict_.keys():
            itemName = itemDict_[playerLoc].Name
            itemShortName = itemDict_[playerLoc].shortName
            print('You find an item in this cell:{name}({shortname})'\
                  .format(name=itemName,shortname=itemShortName))
        else:
            print('There is no item in this cell')
        pass
    def weaponCheck(self,player):
        playerLoc = player.getLocation()
        weaponDict_ = self.weaponList.getList()
        if playerLoc in weaponDict_.keys():
            weaponName = weaponDict_[playerLoc].Name
            weaponShortName = weaponDict_[playerLoc].shortName
            print('You find an weapon in this cell:{name}({shortname})'\
                  .format(name=weaponName,shortname=weaponShortName))
        else:
            print('There is no weapon in this cell')
        pass
    def bulletCheck(self,player):
        playerLoc = player.getLocation()
        bulletPackDict_ = self.bulletPackList.getList()
        if playerLoc in bulletPackDict_.keys():
            bulletPackName = bulletPackDict_[playerLoc].Name
            bulletPackShortName = bulletPackDict_[playerLoc].shortName
            print('You find an bullet pack in this cell:{name}({shortname})'\
                  .format(name=bulletPackName,shortname=bulletPackShortName))
            print(bulletPackDict_[playerLoc].numOfBullets)
        else:
            print('There is no bullet pack in this cell')        
        pass    
    def enemyCheck(self,player):
        playerLoc = player.getLocation()
        enemyDict_ = self.enemyList.getList()
        if playerLoc in enemyDict_.keys():
            print('Enemy found')
            return True
        else:
            print('Nothing happened in this cell')          
            return False
        pass

if __name__ == '__main__':
    cell =Cell()
    map_ = Map()
    map_.mapStructure()
    map_.drawMap(cell,(0,2))
    print(map_)
    print(map_.getMap((1,1)))
