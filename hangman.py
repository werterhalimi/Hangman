import random

print ('We will play hangman game !')
input('Press Enter to start !\n')

# create clear screen function
def clearScreen():
    print ('\n'*100)

# init var
fault = 0 # max is 10
used = [] # array of char used
fund = [] # array of good char fund

# diagram drawing
#_____
#|   |
#|   O
#|  /|\
#|   /\
#|____
space = '\t'*4
diagram =[
 '',
 space + '____',
 (space + '|\n')*4 + space + '|____',
 space + '_____\n' + (space + '|\n')*4 + space + '|____',
 space + '_____\n' + space + '|   |\n' + (space + '|\n')*3 + space + '|____',
 space + '_____\n' + space + '|   |\n' + space + '|   O\n' + (space + '|\n')*2 + space + '|____',
 space + '_____\n' + space + '|   |\n' + space + '|   O\n' + space + '|   |\n' + space + '|\n' + space + '|____',
 space + '_____\n' + space + '|   |\n' + space + '|   O\n' + space + '|  /|\n' + space + '|\n' + space + '|____',
 space + '_____\n' + space + '|   |\n' + space + '|   O\n' + space + '|  /|\\\n' + space + '|\n' + space + '|____',
 space + '_____\n' + space + '|   |\n' + space + '|   O\n' + space + '|  /|\\\n' + space + '|   |\n' + space + '|____',
 space + '_____\n' + space + '|   |\n' + space + '|   O\n' + space + '|  /|\\\n' + space + '|  /|\n' + space + '|____',
 space + '_____\n' + space + '|   |\n' + space + '|   O\n' + space + '|  /|\\\n' + space + '|  /|\\\n' + space + '|____',]

# words init
word = random.choice(['cuivre','vache','canard','ecole','poire','idee','inspiration','pillule'])

# init fund to nothing
for c in word:
    fund.append('_')

# start game's loop
while fault != 11 and word != ''.join(fund):

    clearScreen()

    # print the hangman's draw
    print (diagram[fault])

    # print the word without unfund char
    print (' '.join(fund))

    # asking for char
    c = input('Give me a letter !\n')

    # refuse char if he was already used or if it's a string
    while len(c) != 1 or c in used:
        if c in used:
            c = input('You\'ve already used this char !\n')
        else:
            c = input('"' + c + '"' + ' is not a char. Give me one !\n')


    # add the used char to the used char list
    used.append(c)

    # check if the char is in the word
    if c not in word:
        fault += 1
    else:
        # replacing unknown char by known ones
        i=0
        for char in word:
            if char == c:
                fund[i] = c
            i += 1

# clear the screen for the score
clearScreen()

# draw the score
print (diagram[fault])
print (' '.join(fund))

# check if win
if fault == 11:
    input( 'You lost ! Press Enter to quit !')
else:
    input('You win ! Press Enter to quit !')
