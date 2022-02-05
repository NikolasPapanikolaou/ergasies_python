import requests

sum1 = 0
numbers = []
one_time_numbers = []
r = requests.get('https://drand.cloudflare.com/public/latest', headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = r.json()
data = data["randomness"]
#print(data)

for i in range (32):
    numbers.append((int(data[:2], 16))%80)
    data = data[2:] 
print("The numbers are:",numbers)

d = requests.get('https://api.opap.gr/draws/v3.0/1100/last-result-and-active')
data_2 = d.json()
data_2 = data_2["last"]["winningNumbers"]["list"]
print("KINO numbers:",data_2)

for j in range (32) :
    if numbers[j] in one_time_numbers :
        continue
    else :
        one_time_numbers.append(numbers[j])
#print(one_time_numbers)

for k in range (len(one_time_numbers)) :
    for l in range (20) :
        if one_time_numbers[k]==data_2[l] :
            sum1 = sum1 + 1
print("The amount of these numbers that would be drawn in the last KINO draw is :", sum1)