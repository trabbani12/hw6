#comment
def error():
    pass

def epsilon():
    pass

def alpha():
    pass

def future_weight():
    pass

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

    with open("hw6train.txt") as textFile:
        email_occurances_train = [line.split() for line in textFile]
    # with open("hw6test.txt") as textFile:
    #     email_occurances_test = [line.split() for line in textFile]
    with open("hw6dictionary.txt") as textFile:
        dicton = [line.split() for line in textFile]


    dictionary = dictionary_creater(dicton)
    print dictionary
