''' Program to shuffle an array of integers '''

import random        #imports the random module

def RandomShuffle(array):
    for i in range(100):    #loop to perform 100 swaps of two numbers in the list
        #gets 2 random numbers in the range of the list
        pos1 = random.randint(0,len(array)-1)    
        pos2 = random.randint(0,len(array)-1)
        #swap the numbers at the two random locations in the list
        temp = array[pos1]
        array[pos1] = array[pos2]
        array[pos2] = temp
        
    print(array)    #display the new shuffled array of numbers

#call the function using a input of integers from the user, example input: 1 2 3 4 5 6
RandomShuffle([int(x) for x in input("Please Enter the integers to shuffle: ").split()])
