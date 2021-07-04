from random import shuffle as sh

lineCount=0
spaceCount=0
vowelCount=0
wordCount=0

data=open('file', 'r')
new=open(data.name+'scrabble.txt','w')
allLines=data.readlines()

lineCount=len(allLines)

for line in allLines:
    statements=''
    l1=line.strip().split(' ')
    for word in l1:
        wordCount += 1
        if len(word)>3:
            if word[-1] in ('.',',','?'):
                w1=word[1:-2]
            else:
                w1=word[1:-1]
            w2=list(w1)
            sh(w2)
            if word[-1] in ('.',',','?'):
                statements=statements+(word[0]+''.join(w2)+word[-2]+word[-1]+" ")
            else:
                statements = statements + (word[0] + ''.join(w2) + word[-1] + " ")
        else:
            statements = statements + word+" "
    new.write(statements)
    new.write("\n")
    #print(statements)
    spaceCount+=line.count(' ')
    for v in 'aeiou':
        vowelCount+=line.lower().count(v)

print('\nData in file scribbled successfully...')
print('\nNo of Words : ',wordCount)
print('\nNo of Lines : ',lineCount)
print('\nNo of Space : ',spaceCount)
print('\nNo of Vowels : ',vowelCount)
