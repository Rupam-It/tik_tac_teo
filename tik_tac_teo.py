# this is tic tac tao project in python language

import os
def drawBord(res):
    print(str(res[1])+"  |  "+str(res[2])," |  "+str(res[3]))
    print("---|-----|----")
    print(str(res[4])+"  |  "+str(res[5])," |  "+str(res[6]))
    print("---|-----|----")
    print(str(res[7])+"  |  "+str(res[8])," |  "+str(res[9]))
    
def cheakWin(r):
    if (r[1]=='X' and r[2]=='X' and r[3]=='X') or (r[4]=='X' and r[5]=='X' and r[6]=='X') or (r[7]=='X' and r[8]=='X' and r[9]=='X') or (r[1]=='X' and r[4]=='X' and r[7]=='X') or (r[2]=='X' and r[5]=='X' and r[8]=='X') or(r[3]=='X' and r[6]=='X' and r[9]=='X') or (r[1]=='X' and r[5]=='X' and r[9]=='X') or (r[3]=='X' and r[5]=='X' and r[8]=='X'):
        print("Player 1 Win!")
        return 1
    elif (r[1]=='0' and r[2]=='0' and r[3]=='0') or (r[4]=='0' and r[5]=='0' and r[6]=='0') or (r[7]=='0' and r[8]=='0' and r[9]=='0') or (r[1]=='0' and r[4]=='0' and r[7]=='0') or (r[2]=='0' and r[5]=='0' and r[8]=='0') or(r[3]=='0' and r[6]=='0' and r[9]=='0') or (r[1]=='0' and r[5]=='0' and r[9]=='0') or (r[3]=='0' and r[5]=='0' and r[8]=='0') :
        print("player 2 Win")
        return 1
    else:
        return 0

def move(res:list):
    os.system('cls')
    print(str(res[1])+"  |  "+str(res[2])," |  "+str(res[3]))
    print("---|-----|----")
    print(str(res[4])+"  |  "+str(res[5])," |  "+str(res[6]))
    print("---|-----|----")
    print(str(res[7])+"  |  "+str(res[8])," |  "+str(res[9]))



res=['0',1,2,3,4,5,6,7,8,9]
player=1
turn=1
# drawBord(res)
# move(res)
i=0  # this is to cheak how many moves
drawBord(res)
while True:
    if player%2==0:
        player=2
    else:
        player=1

    make_move=int(input(f"Enter your move player:{player}==> "))
    if make_move<1 or make_move>9 or res[make_move]=='0' or res[make_move]=='X':
        print("Invalid move!")
        continue
    else:
        if player==1:
            res[make_move]="X"
        else:
            res[make_move]='0'
    move(res)
    player+=1
    i+=1
    if (i>4) and cheakWin(res):
        break
    elif i==9 and cheakWin(res)==0:
        print("Match is draw")
        break
    else:
        continue