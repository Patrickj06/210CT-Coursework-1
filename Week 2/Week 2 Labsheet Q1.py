'''Function to find perfect square of a positive integer iteratively '''

'''def perfect_square(num):
    i=1
    not_found = True
    while not_found == True:  #loops through N times until perfect square found
        if i**2 < num:
            i += 1     # increments i if i^2 is less than num
        elif i**2 > num:
            not_found = False   # stops the loop if i^2 is higher than num
            highest_square = (i-1)**2   # makes highest_square equal to (i-1)^2
        elif i**2 == num:
            not_found = False   # stops the loop if i^2 = num
            highest_square = i**2       # makes highest_square equal to (i)^2
    return(highest_square)

print(perfect_square(int(input("Please enter a positive integer: "))))'''


'''Function to find perfect square of a positive integer recursively using
binary search'''

def perfect_square(num,hi,lo):
    pos = int((hi+lo)/2) # find midpoint between hi and lo
    if (num == pos**2)or(hi == lo):     # base case: end recursion if perfect square found or no numbers left to check
        if (hi == lo) and (pos**2 > num): #check if no numbers left and current number^2 is more than given value
            return((pos-1)**2)  # return previous number^2 as answer
        return(pos**2) # return answer squared
    elif pos**2 > num:
        #if its above value check lower half of numbers
        return(perfect_square(num,pos-1,lo)) 
    elif pos**2 < num:
        #if its below value check upper half of numbers
        return(perfect_square(num,hi,pos+1))
    
value = int(input("Please enter a positive integer: ")) # take a integer as input from the user
print(perfect_square(value,value,1)) # output result from function

