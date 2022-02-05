#The project will take aproximatly 50 minutes since the site refreshes the numbers every 30 sec.


import requests
import math
from time import sleep 

zeros = []
ones = []

for p in range (100):
    round_1 = requests.get('https://drand.cloudflare.com/public/latest', headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    round_1 = round_1.json()
    round_1 = round_1["round"]
    r = requests.get('https://drand.cloudflare.com/public/'+str(round_1), headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = r.json()
    data = data["randomness"]

    # Initialising hex string
    ini_string = data
    print(ini_string)

    # Code to convert hex to binary
    res = "{0:08b}".format(int(ini_string, 16))
    
    # Print the resultant string
    print ("Resultant string", str(res))

    res = [int(x) for x in str(res)]
    #print (res)

    count = 0
    prev = 0
    indexend = 0
    for i in range(0,len(res)):
        if res[i] == 0:
            count += 1
        else:            
            if count > prev:
                prev = count
                indexend = i
            count = 0

    zeros.append(prev)
    print("The longest sequence of 0's is "+str(prev))
    print("index start at: "+ str(indexend-prev))
    print("index ends at: "+ str(indexend-1))

    count_2 = 0
    prev_2 = 0
    indexend_2 = 0
    for i in range(0,len(res)):
        if res[i] == 1:
            count_2 += 1
        else:            
            if count_2 > prev_2:
                prev_2 = count_2
                indexend_2 = i
            count_2 = 0

    ones.append(prev_2)
    print("The longest sequence of 1's is "+str(prev_2))
    print("index start at: "+ str(indexend_2-prev_2))
    print("index ends at: "+ str(indexend_2-1))
    sleep(30)

print("MAXIMUM LENGTH OF SEQUENCE OF 0'S :")
print (max(zeros))
print("MAXIMUM LENGTH OF SEQUENCE OF 1'S :")
print(max(ones))