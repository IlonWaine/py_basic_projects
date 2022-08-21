from random import randint

def Boundaries(): 
    while(True):
        try:
            min = int(input('write minimum number: '))
            max = int(input('write maximum number: '))
            break
        except:
            print('You should type only integer numbers')
    pcNumber = randint(min,max)
    return pcNumber,min,max
boundaries = Boundaries()


def playerInputcheck():
    min = boundaries[1]
    max = boundaries[2]
    while(True):
        try:
            PlayerGuess = int(input('Guess number : '))
            if(PlayerGuess < min):
                print('Your guess less than minimum')
            elif(PlayerGuess > max):
                print('Your guess greater than grater')
            else: 
                break
        except:
            print('You should type a number')
    return PlayerGuess


def check():
    pc = boundaries[0]
    pl = 0
    while(pl != pc):
        pl = playerInputcheck()
        if pc > pl:
            print('More')
        elif pc<pl:
            print('Less')
    print(f"pc number is {pc}. Correct You WIN!!!")


check()