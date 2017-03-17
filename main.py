import numpy as np
import math


def error(D,h_x, y_x):
    h = int(h_x)
    y = int(y_x)

    if(h == 1):
        if(y == 1):
            return [0,1]
        elif(y == -1):
            return [D,0]
    if(h == 0):
        if(y == -1):
            return [0,1]
        elif(y == 1):
            return [D,0]

def alpha_calc(epsilon):
    if(epsilon == 0):
        return 0
    return .5*np.log((1-epsilon)/epsilon)

def future_weight(D,correct,incorrect,alpha,epsilon,h,y):
    Z = (correct*(math.exp(-alpha))*D) + (incorrect*(math.exp(alpha))*D)
    if(Z == 0):
        return 0
    else:
        return (D*(math.exp(-alpha*y*h)))/Z

def dictionary_creater(dictionary):
    temp_dictionary = dict()
    for i in range(len(dictionary)):
        temp_dictionary[str(dictionary[i])] = 0

    return temp_dictionary

if __name__=="__main__":
    email_occurances_train = []
    email_occurances_test = []
    dicton = []
    dictionary = dict()
    D = 1/450 #450 = number of emails = "n"

    with open("hw6train.txt") as textFile:
        email_occurances_train = [line.split() for line in textFile]
    # with open("hw6test.txt") as textFile:
    #     email_occurances_test = [line.split() for line in textFile]
    with open("hw6dictionary.txt") as textFile:
        dicton = [line.split() for line in textFile]

    #print email_occurances_train[4][4003]
    #print len(email_occurances_train[0]) #4004 - 1 base index
    #print len(email_occurances_train) #450 - 1 base index
    #print email_occurances_train[0][4003]

    dictionary = dictionary_creater(dicton) #dictionary created -- works

    err = 0
    alpha = 0
    epsilon = 0
    incorrect = 0
    correct = 0
    #print len(email_occurances_train[0])
    #print email_occurances_train[0][10]
    for x in range(3): #t=3
        for y in range(4003): #row
            for z in range(449): #col
                h_x = email_occurances_train[z][y]
                y_x = email_occurances_train[z][4003]
                temp = error(D,h_x,y_x)
                if (temp[1] == 0):
                    incorrect+=1
                    err += temp[0]
                if (temp[1] == 1):
                    correct+=1
                    err += temp[0]
                epsilon = err
                alpha += alpha_calc(epsilon)
                D = future_weight(D,correct,incorrect,alpha,epsilon,int(h_x),int(y_x))
