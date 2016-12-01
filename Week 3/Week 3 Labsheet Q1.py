'''Program returns a the reverse of a sentence entered by user'''
sentence = input("Please enter a sentence: ") #recieves string as input from user
words = sentence.split() #creates a list of all words in string

def Reverse(text,answer):
    if len(text) == 1:  #Base case to end recursion when only 1 element left
            return(answer + " " + text[0]) #returns new reversed string
    else:
        answer = answer + " " + text[-1] #add last element in list onto reversed string
        return Reverse(text[:-1],answer) #calls itself passes everything apart from last element in list

print(Reverse(words,""))
