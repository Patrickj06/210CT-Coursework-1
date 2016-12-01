'''Program to extract largest sub-sequence of ascending order from a sequence of integers'''
def extract(aList):
    new_list = []
    max_list = []
    for ptr in range(len(aList)):      #goes through every element in sequence
        if (aList[ptr] < aList[ptr-1]):   #checks if current element is less than the previous
            if len(new_list)>len(max_list): #checks if the new list is larger than current maximum list
                max_list = new_list #makes the new list the max list and resets the new list
            new_list = []
        new_list.append(aList[ptr]) #adds current element to new list
    if len(new_list)>len(max_list):
        max_list = new_list
    return(max_list) #returns the max list

sequence = [int(i) for i in input("please enter a sequence of numbers: ").split(',')]
#takes a list of integers from user example input: 2, 3, 5, 7, 9, 13
print(extract(sequence)) #Output result from extract function using sequence as argument
        
