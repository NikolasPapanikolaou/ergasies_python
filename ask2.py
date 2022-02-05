import random
import numpy as np

number = []
for j in range (100):
    number_of_places = [i for i in range(1, 10)]
    places = []
    cups = []
    sizes = ["s","m","l"]
    board = ["","","","","","","","",""]

    for i in range (9):
        for j in range (3):
            cups.append(sizes[j])
    random.shuffle(cups)


    for i in range (3):
        for j in range (9):
            places.append(number_of_places[j])
    random.shuffle(places)
    


    for i in range (27):
        k = places[i]
        moves = i+1
        if (board[k-1]=="l" and cups[i]=="s") or (board[k-1]=="l" and cups[i]=="m") :
            continue
        elif board[k-1]=="m" and cups[i]=="s" :
            continue 
        else :
            board[k-1] = cups[i]
            



        if (board[0]==board[3]==board[6]=="l") or (board[0]==board[3]==board[6]=="m") or (board[0]==board[3]==board[6]=="s") :
            #print("win1")
            break
        elif (board[1]==board[4]==board[7]=="l") or (board[1]==board[4]==board[7]=="m") or (board[1]==board[4]==board[7]=="s") :
            #print("win2")
            break
        elif (board[2]==board[5]==board[8]=="l") or (board[2]==board[5]==board[8]=="m") or (board[2]==board[5]==board[8]=="s") :
            #print("win3")
            break
        elif (board[0]==board[1]==board[2]=="l") or (board[0]==board[1]==board[2]=="m") or (board[0]==board[1]==board[2]=="s") :
            #print("win4")
            break
        elif (board[3]==board[4]==board[5]=="l") or (board[3]==board[4]==board[5]=="m") or (board[3]==board[4]==board[5]=="s") :
            #print("win5")
            break
        elif (board[6]==board[7]==board[8]=="l") or (board[6]==board[7]==board[8]=="m") or (board[6]==board[7]==board[8]=="s") :
            #print("win6")
            break
        elif (board[0]==board[4]==board[8]=="l") or (board[0]==board[4]==board[8]=="m") or (board[0]==board[4]==board[8]=="s") :
            #print("win7")
            break
        elif (board[2]==board[4]==board[6]=="l") or (board[2]==board[4]==board[6]=="m") or (board[2]==board[4]==board[6]=="s") :
            #print("win8")
            break
        elif (board[0]=="s" and board[3]=="m" and board[6]=="l") or (board[0]=="l" and board[3]=="m" and board[6]=="s") :
            #print("win9")
            break
        elif (board[1]=="s" and board[4]=="m" and board[7]=="l") or (board[1]=="l" and board[4]=="m" and board[7]=="s") :
            #print("win10")
            break
        elif (board[2]=="s" and board[5]=="m" and board[8]=="l") or (board[2]=="l" and board[5]=="m" and board[8]=="s") :
            #print("win11")
            break
        elif (board[0]=="s" and board[1]=="m" and board[2]=="l") or (board[0]=="l" and board[1]=="m" and board[2]=="s") :
            #print("win12")
            break
        elif (board[3]=="s" and board[4]=="m" and board[5]=="l") or (board[3]=="l" and board[4]=="m" and board[5]=="s") :
            #print("win13")
            break
        elif (board[6]=="s" and board[7]=="m" and board[8]=="l") or (board[6]=="l" and board[7]=="m" and board[8]=="s") :
            #print("win14")
            break
        elif (board[0]=="s" and board[4]=="m" and board[8]=="l") or (board[0]=="l" and board[4]=="m" and board[8]=="s") :
            #print("win15")
            break
        elif (board[2]=="s" and board[4]=="m" and board[6]=="l") or (board[2]=="l" and board[4]=="m" and board[6]=="s") :
            #print("win16")
            break
    print (board)
    print(moves)
    number.append(moves)

average = sum(number) / len(number)
print("THE AVERAGE NUMBER OF MOVES FOR 100 GAMES IS :")
print (average)