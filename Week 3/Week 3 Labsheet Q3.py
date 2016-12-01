'''Program that uses recursion to remove all vowels from a string inputed by user'''

vowels = ['a','e','i','o','u'] # creates a list of all the vowels

def remove_vowel(text):
    if text == "":    #base case to end recursion when text is empty
        return(text)  
    elif text[0] in vowels:   #checks if the first letter in text is a vowel 
        return remove_vowel(text[1:]) #calls itself passing all of text except the first letter
    else:
        return text[0] + remove_vowel(text[1:]) #returns the first letter of text and calls itself passing the rest of text

word = input("Please enter a String: ").lower() # takes an string as input from user and converts it to lowercase
print(remove_vowel(word)) #outputs result from function remove_vowel
