def countVowels(string):
    num_vowels=0
    for char in string.lower():
        if char in "aeiouáéíóú":
           num_vowels = num_vowels+1
    return num_vowels

def countConsonants(string):
    num_Consonants=0
    for char in string.lower():
        if char in "bcdfghjklmnñopqrstwxyz,.#":
           num_Consonants = num_Consonants+1
    return num_Consonants

def ss(txt):
    if (len(txt) % 2) == 0:
        return 1.5
    else:
        return 1


def openAddressFile(fileName):
    addressFile = open(fileName, "r")
    arrOfAddress = []
    for textLine in addressFile:
        arrOfAddress.append([[textLine],[ss(textLine)]])
    print(arrOfAddress)

def openDriversFile(fileName):
    driversFile = open(fileName, "r")
    arrOfDrivers = []
    for textLine in driversFile:
        arrOfDrivers.append([[textLine],[countConsonants(textLine)],[countVowels(textLine)],[0]])
    print(arrOfDrivers)



#import numpy as np
#arrOfAddress = np.openAddressFile('C:/Users/Dell Inspiron/OneDrive/Escritorio/address.txt')
#arrOfDrivers = np.openDriversFile('C:/Users/Dell Inspiron/OneDrive/Escritorio/drivers.txt')
#arrOfSS = []
#for driver in arrOfDrivers:
#    for direction in arrOfAddress:
#            arrOfSS.append(direction[1],driver[0],direction[0]) <-- Matrix SS value, Driver's Name, Address Name
#arrOfSS.sort()
#delete all rows that have less SS of each driver
#print(arrOfSS)
    



