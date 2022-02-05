import random

#now srarts the game without any limitations 
p1 = 0
p2 = 0
draw = 0
for k in range (100):
    xartia = []
    figures = ["J", "Q", "K"]
    xarti = [i for i in range(1, 11)] + figures
    color = ["H", "S", "C", "D"]
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    random.shuffle(xartia)
    player1=[]
    sum1=0
    while sum1<16:
        sum1=0
        player1.append(xartia.pop())
        # print (player1)
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
        #print(sum1)
    if sum1>21:
        p1 = p1 +1 
    else:
        #print("P2 joins the game") #let me add one more player
        player2=[]
        sum2=0
        while sum2<16:
            sum2=0
            player2.append(xartia.pop())
            # print (player2)
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
            #print(sum2)
        if sum2>21:
            sum2=0
        if sum1>sum2:
            p1 = p1 + 1
        elif sum2>sum1:
            p2 = p2 +1
        else:
            draw = draw + 1
print ("WHEN PLAYER 1 AND PLAYER 2 STARTS WITHOUT ANY LIMITATION, THE RESULTS ARE :")
print ("Player 1 won the game" , p1 , "times") 
print ("Player 2 won the game" , p2 , "times")
print ("The game ended in a draw" , draw , "times")
print ("---------------------------------------------")


#now starts the game with the limitations

p1_2 = 0
p2_2 = 0
draw_2 = 0
for p in range (100):
    xartia = []
    figures = ["J", "Q", "K"]
    xarti = [i for i in range(1, 11)] + figures
    color = ["H", "S", "C", "D"]
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    random.shuffle(xartia)
    player1=[]
    sum1=0
    for i in range (52):
        k = xartia.pop()
        if k[0]==10 or k[0]=="J" or k[0]=="Q" or k[0]=="K" :
            player1.append(k)
            sum1 = sum1 + 10
            break
    #print(sum1)
    while sum1<16:
        j = xartia.pop()
        if j[0]=="J" or j[0]=="Q" or j[0]=="K" :
            sum1 = sum1 + 10
        else :
            sum1 = sum1 + j[0]
        #print(sum1)
    if sum1>21 :
        p2_2 = p2_2 + 1
    else :
        #add one more player
        #print("P2 joins the game")
        player2=[]
        sum2 = 0
        for i in range (len(xartia)) :
            k = xartia.pop()
            if k[0]==1 or k[0]==2 or k[0]==3 or k[0]==4 or k[0]==5 or k[0]==6 or k[0]==7 or k[0]==8 or k[0]==9 :
                player2.append(k)
                sum2 = sum2 + k[0]
                break
        #print(sum2)
        while sum2<16:
            j = xartia.pop()
            if j[0]=="J" or j[0]=="Q" or j[0]=="K" :
                sum2 = sum2 + 10
            else :
                sum2 = sum2 + j[0]
            #print(sum2)
        if sum2>21:
            sum2=0
        if sum1>sum2:
            p1_2 = p1_2 + 1
        elif sum2>sum1:
            p2_2 = p2_2 +1
        else:
            draw_2 = draw_2 + 1
print ("WHEN PLAYER 1 STARTS WITH '10' OR FIGURE AND PLAYER 2 STARTS WITH ANYTHING BUT '10' OR FIGURE, THE RESULTS ARE :")
print ("Player 1 won the game" , p1_2 , "times") 
print ("Player 2 won the game" , p2_2 , "times")
print ("The game ended in a draw" , draw_2 , "times")