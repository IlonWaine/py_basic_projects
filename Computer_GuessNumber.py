from random import randint

def playerInputcheck():
    while(True):
        try:
            PlayerInput = int(input('Write your number : '))
            if(PlayerInput < 0):
                print('Type number > 0')
            else: break
        except:
            print('You should type a number')
    return PlayerInput

def Boundaries(pl): 
    min = randint(0,pl)
    max = randint(pl, pl+1000)
    print(f'Number between {min} and {max}')
    return min,max,pl

def pcGues(bound):
    pc = randint(bound[0],bound[1])
    pl = bound[2]
    max =  bound[1]
    min = bound[0]
    count = 1
    while(pc!=pl):
        print('pc gues is ',pc)
        if(pc<pl):
            min = pc
            pc = int(round((pc+max)/2))
        elif(pc>pl):
            max = pc
            pc = int(round((pc+min)/2))
        count+=1
    print("Computer guess your number it is ",pc,f' by {count} turns')

pcGues(Boundaries(playerInputcheck()))