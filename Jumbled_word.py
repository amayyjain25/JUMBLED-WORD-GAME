import random
from shlex import join


def choose():
    words =['rainbow','computer','science','mathematics','reverse','water','moniter','processor','economics','bangalore','jabalpur','nagpur','college','school','books','rain','three','crime','police']
    pick = random.choice(words)
    return pick
def jumble(word):
    jumbled =join(random.sample(word,len(word)))
    return jumbled
def play():
    p1=input("PLAYER 1 , ENTER YOUR NAME")
    p2 = input("PLAYER 2 , ENTER YOUR NAME")
    point1=0
    point2=0
    turn=0
    while(1):
        #computers task
        picked_word = choose()
        #creat the question
        qn = jumble(picked_word)
        print(qn)
        if turn %2 == 0:
            print("Player 1, ",p1,' this is your turn')
            ans = input('What is on my mind? - ')
            if ans == picked_word:
                point1  +=1
                print('Congragulation ')

            else:
                print('Ohh no the correct word was',picked_word)
            c = int(input("PRESS 1 TO CONTINUE AND 0 TO QUIT"))
            if c == 0:
                print('Thank you for playing \n', p1, '-', point1, '\n', p2, '-', point2)
                break
        else:
            print("Player 2, ",p2,' this is your turn')
            ans = input('What is on my mind? - ')
            if ans == picked_word:
                point2 +=1
                print('Congragulation ')
            else:
                print('Ohh no the correct word was',picked_word)
            c = int(input("PRESS 1 TO CONTINUE AND 0 TO QUIT"))
            if c == 0:
                    print('Thank you for playing \n',p1,'-',point1,'\n',p2,'-',point2)
                    break
        turn = turn + 1


play()


