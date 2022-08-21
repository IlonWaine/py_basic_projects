from os import P_WAIT
from random import choice

def computerChoice():
    list =('r','p','s')
    pcChoice = choice(list)
    return pcChoice

def getUserChoice():
    Uchoice = ''
    while(True):
        Uchoice = input('Write your choice by firs latter r/p/s (rock/paper/scissors)').lower()
        print(Uchoice)
        if Uchoice == 'r' or Uchoice == 'p' or Uchoice == 's':
            break
        else: print('Pleasw write r or p or s')
    return Uchoice

def Batle(U,C):
    if(U==C):
        print('Draw')
    elif(U=='r' and C=='s'):
        print('You won')
    elif(U=='r' and C=='p'):
        print('You lose')
    elif(U=='p' and C=='r'):
        print('You won')
    elif(U=='p' and C=='s'):
        print('You lose')
    elif(U=='s' and C=='p'):
        print('You won')
    elif(U=='s' and C=='r'):
        print('You lose')

Batle(getUserChoice(),computerChoice())