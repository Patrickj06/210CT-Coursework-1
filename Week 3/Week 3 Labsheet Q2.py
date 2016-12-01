'''Program to return if integer inputed by user is prime'''
def Prime(n,i):
    if i == n or n == 1:    #Base case: end recursion if n = i or 1
        return(str(n) + " is Prime") #return value for n is prime
    elif n%i == 0:  #check if n can be divided by i
        return(str(n) + " is not Prime") #return value for n is not prime
    else:
        return(Prime(n,i+1)) #call itself, increment i
    
num = int(input("Please enter an integer: ")) # takes integer input from user
print(Prime(num,2))  # output result from Prime function 
