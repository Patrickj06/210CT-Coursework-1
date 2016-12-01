'''Program to count the number of trailing zeros at the end of a factorial'''
def TrailingZero(num):
    answer = 0
    count = 5
    done = False
    while not(done):
        #loop that computes until done is true
        five = num//count      
        answer += five
        if five == 0:
            done = True
        else:
            count *= 5
    return(answer) 

#output result of function using integer input from user as argument 
print(int(TrailingZero(int(input("Please enter an integer: ")))))
