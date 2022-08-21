
string1  = ''
word1 = 'man'

sentence = input('Write your story using - for missing word.\n')
splitted = sentence.split('-')
print(splitted[-1])
if (splitted[-1] == ' ' or splitted[-1] == '\t' or splitted[-1] == ''):
    splitted[-1] = '.'
elif(('.' in splitted[-1] or '?' in splitted[-1] or ';' in splitted[-1] or '!' in splitted[-1] or '...' in splitted[-1] )):
    pass
else: splitted[-1] = splitted[-1] + '.'
print(splitted)

# return sentence parts list
def addSentence():
    sentence = input('Write your story using - for missing word.\n')
    splitted = sentence.split('-')
    if (splitted[-1] == ' ' or splitted[-1] == '\t' or splitted[-1] == ''):
        splitted[-1] = '.'
    elif('.' or '?' or '!' or '...' or ';' not in splitted[-1]):
        splitted[-1] = splitted[-1] + '.'
    else: pass
    return splitted,sentence
    
# return dictionary [a: anser, b: answer]
def creteAnswers():
    variants = ("a","b","c")
    answers = {}
    for i in variants:
        answers[i] = input(f"{i}) write your answer ")
    return answers

# return dictionary [1:[a: anser, b: answer,c: answer], 2:[a: anser, b: answer,c: answer]]
def createSpacesAns(splitted):
    spaces = {}
    corect ={}
    for i in range(len(splitted)-1):
        print(i+1)
        spaces[i+1] = creteAnswers()
        corect[i+1] = input('write Correct answer (a/b/c)')
    return spaces,corect

class Sentence:
    def __init__(self,StringTuple) -> None:
        self.value = StringTuple[1]
        answ = createSpacesAns(StringTuple[0])
        self.answer = answ[0]
        self.realAnswers = answ[1]
        self.splitted = StringTuple[0]

sentenceObj = Sentence(addSentence())
#print(len(sentenceObj.answer))

def showFullSentence():
    keys = list(sentenceObj.answer.keys())
    keysCorrect = list(sentenceObj.realAnswers.keys())
    # print(sentenceObj.answer)
    # print('keys ',keys)
    # print('obj ', sentenceObj.splitted)
    for i in range(len(sentenceObj.splitted)):
        # print('i ',i)    
        print(sentenceObj.splitted[i], end='')
        if i == (len(sentenceObj.splitted)-1):
            #print('this',i)
            break
        else:
            # print('Kcor', keysCorrect[i])
            # print('Kcor', keysCorrect[i])
            #print('alsdjfalsd   ',sentenceObj.answer[1]['a'])
            print(sentenceObj.answer[keys[i]][sentenceObj.realAnswers[keysCorrect[i]]], end='')
    print()

def checkAnsw(playerAns,realAnsw,id):
    print(f'player:{playerAns} correct:{realAnsw} id: {id}')
    if playerAns == 'a' or playerAns =='b' or playerAns == 'c' :
        if playerAns == realAnsw[id]:
            print('True')
        else: print(f'False correct answer is {realAnsw[id]}')
    else: print('Incorrect input')

def solveTask():
    print(sentenceObj.value)
    for i in sentenceObj.answer.keys():
        playerAns = ''
        print(i,end=') ')
        print(sentenceObj.answer[i])
        playerAns = input('write your answer (a/b/c) ')
        checkAnsw(playerAns,sentenceObj.realAnswers,i)
    showFullSentence()

solveTask()




#if(splitted[0]==''):
#    splitted[0] = word1



#print(splitted[0],word1,sentence[1])
#print(sentence[0]+sentence[1])