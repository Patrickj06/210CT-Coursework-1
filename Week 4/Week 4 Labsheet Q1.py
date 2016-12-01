'''Program to use binary search in order to check if a value within a given interval was found'''
#take in a list of integers from user example: 2 3 5 7 9 13
aList = [int(x) for x in input("Please Enter a ordered list of numbers: ").split()]
range_min = int(input("Please enter a range minimum: ")) #gets an integer from user for range minimum
range_max = int(input("Please enter a range maximum: ")) #gets an integer from user for range maximum
def binary_search(hi,lo):
    mid = (hi+lo)//2  #finds the midpoint between hi and lo
    if mid == lo:     # base case to end recursion if every element has been checked
        return(False)
    elif aList[mid]<range_max and aList[mid]>range_min: #check if midpoint is within the range max and min
        return(True)
    elif aList[mid]>range_max:
    #if midpoint is larger than range max function calls itself but sets hi to midpoint to look in lower half of list
        return(binary_search(mid,lo))
    elif aList[mid]<range_min:
    #if midpoint is less than range min function calls itself but sets lo to midpoint to look in upper half of list
        return(binary_search(hi,mid))
print(binary_search(len(aList),0)) #Output result from the binary search function using inputs from user as arguments
