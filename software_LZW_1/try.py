import argparse
import os
import pickle
import cv2
import PIL as image
import numpy as np
import matplotlib.pyplot as plt

DICTIONARY_SIZE = 256
dictionary = {}
for i in range(0, DICTIONARY_SIZE):
        #question si on peut change i par str...
        dictionary[str(chr(i))] = i
img = np.array([[0, 1, 0, 1, 0, 1], 
                    [1, 0, 1, 0, 1, 0],
                    [0, 1, 0, 1, 0, 1],
                    [1, 0, 1, 0, 1, 0], 
                    [0, 1, 0, 1, 0, 1],
                  [1, 0, 1, 0, 1, 0]])*255
temp=" " 
img1=img.flatten() 
chaine =''                  
for f in img1 :
    chaine = chaine + str(f)
print(chaine)

    
 
                       
plt.imshow(img)
plt.show()
cv2.imwrite("img.jpeg",img)


def compress(inputr):
    global DICTIONARY_SIZE
    input = inputr.flatten()
    dictionary = {}
    result = []
    temp = ""

    for i in range(0, DICTIONARY_SIZE):
        #question si on peut change i par str...
        dictionary[str(chr(i))] = i

    for c in input:
        print(c)
        
        temp2 = temp+str(chr(c))
        print(temp2)
        if temp2 in dictionary.keys():
            temp = temp2
        else:
            result.append(dictionary[temp])
            dictionary[temp2] = DICTIONARY_SIZE
            DICTIONARY_SIZE+=1
            temp = ""+str(chr(c))

    if temp != "":
        result.append(dictionary[temp])  
        
    return result,dictionary

result,dictionary=compress(img)
print(result) 
print(dictionary)



def decompress(input):
    global DICTIONARY_SIZE
    dictionary = {}
    result = []

    for i in range(0, DICTIONARY_SIZE):
        dictionary[i] = str(chr(i))

    previous = chr(input[0])
    input = input[1:]
    result.append(previous)

    for bit in input:
        aux = ""
        if bit in dictionary.keys():
            aux = dictionary[bit]
          
            
        else:
            aux = previous+previous[0] 
            #Bit is not in the dictionary
                 # Get the last character printed + the first position of the last character printed
                 #because we must decode bits that are not present in the dictionary, so we have to guess what it represents, for example:
                 #let's say bit 37768 is not in the dictionary, so we get the last character printed, for example it was 'uh'
                 #and we take it 'uh' plus its first position 'u', resulting in 'uhu', which is the representation of bit 37768
                 #the only case where this can happen is if the substring starts and ends with the same character ("uhuhu").
      
        print(aux)
        result.append(aux)
        dictionary[DICTIONARY_SIZE] = previous + aux[0]
        DICTIONARY_SIZE+= 1
        previous = aux
    return result,dictionary


