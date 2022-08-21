from cmath import pi
from random_word import RandomWords

def drawMan():
    aa =list('''   o__
  /|\ |
  / \ |''')
    bb =aa[:]
    indexes = tuple()
    for i in range(len(aa)):
        if(aa[i] ==' ' or aa[i] =='\n'):
            bb[i]=aa[i]
        else: 
            indexes = indexes +(i,)
            bb[i] = ' '
    #print(indexes)
    # print(aa)
    # print(bb)
    idOrdered = (7,8,4,3,5,0,9,6,2,1)
    indexes = [indexes[i] for i in idOrdered]
    #print(indexes)
    return aa,bb,indexes
def hangMan(i,a,b,indexes):
    a,b,indexes = ret[0],ret[1],ret[2]
    b[indexes[i]] = a[indexes[i]]
    print(''.join(b))

ret = drawMan()
a,b,indexes = ret[0],ret[1],ret[2]


def Play():
    wordstr = RandomWords().get_random_word().lower()
    word = list(wordstr)
    playWord =list('-'*len(word))

    print(' '.join(playWord))
    # print(' '.join(word))
    i = 0
    playerInput = ''
    check = False
    usedLetter = []
    while (playWord != list(wordstr)):
        # print('playword ',type(playWord))
        # print('wordstr ',type(wordstr))
        # print(playWord != list(wordstr),f'{playWord} = {list(wordstr)}')
        
        #take player input
        playerInput = input('Write word or letter: ').lower()
        # check if input was word or letter
        if len(playerInput) == 1:
            usedLetter.append(playerInput)
            checker = False
            #loop for finding same letters in word
            while playerInput in word:
                # print(playerInput,'   ',word.index(playerInput))
                playWord[word.index(playerInput)] = playerInput
                word[word.index(playerInput)] = '-'
                checker =True
            if(checker):
                print(' '.join(playWord))
                print('You already used: ',', '.join(usedLetter))
            else:
                hangMan(i,a,b,indexes)
                if(i==9):
                    check = True
                    break
                i+=1
                print('Try another letter.\nYou already used: ',', '.join(usedLetter))

        else: 
            if(playerInput == wordstr):
                break
            else: 
                hangMan(i,a,b,indexes)
                if(i==9):
                    check = True
                    break 
                i+=1
                print('Try another word.\nYou already used: ',', '.join(usedLetter))

    # print(check)            
    if(check):
        print('You LOSE. The word is ',wordstr)
    else:
        print('You won!!! The word is ',wordstr)
        print((
'''    FREE
    \o/  
     | 
    / \ '''))
Play()

# for i in range(10):
#         hangMan(i,a,b,indexes)
#print(''.join(aa))
