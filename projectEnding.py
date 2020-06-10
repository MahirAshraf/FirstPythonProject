import csv
import re
fh = open('Arrests.csv')
count = 0
sum = 0
male = 0
max = 0
lst = list()
lst2 = list()
for la in fh:  #la is a string.
    count = count+1
    lx = la.rstrip()
    ly = lx.replace('"', "")  #removed all the " from the string
    lz = ly.replace(',', " ")  #removed all the , fromm the new string
    arfa=lz.split() #made a list with proper indexing

    #calculating number of male and female
    mahir = arfa[5]
    if mahir == "Male":
        male = male +1 #adding total male number

    #calculating average age
    promitee = arfa[4]
    sami = promitee.replace('sex', '0')
    sum = sum + int(sami)

    lst.append(int(sami))

    #calculating maximum age
    if int(sami) > int(max):
        max = sami

#calculating minimum age
lst.remove(0)
min = 50
for i in range(len(lst)):
    if lst[i] < min:
        min = lst[i]


female = (count - 1) - male
avg = sum/(count-1)
print('Number of Male stoners :',male)
print('Number of Female stoners :',female)
print('Stoners average age is: ',avg)
print('Most senior stoner is',max,'years old')
print('Most junior stoner is',min,'years old')