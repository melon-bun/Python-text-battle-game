# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 23:30:21 2018

@author: X
"""

class commandsBook():
    
    
    
    def __init__(self,command):
        print('hhhh')
        self.command = command
        self.commandList = {'quit':"press 'q'",
                            'move':"press 'w' to move upward,press 's' to move downward,press 'd' to move right,\
                            press 'a' to move left",
                            }
    pass
    def comm(self):
        if self.command in self.commandList.keys():
            print(self.commandList[self.command])
        elif self.command == 'all':
            for key,value in self.commandList.items():
                print('{key}:{value}'.format(key=key,value=value))
        else:
            print('invaild command')
            
ww= input('input')
cb=commandsBook(ww)
cb.comm()