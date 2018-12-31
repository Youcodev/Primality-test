# Primality test using two optimization methods in comparison with a naive solution that 
# iterates through all the positive integers less than the input number, to check if any divides it
# 1-Testing integers only up to the square root of the input number (trial division)
# 2-Testing integers only of the form 6k ± 1 after checking if the input number is even or divisible by 3 
# given that all prime numbers, except 2 and 3, are of this form

def primality(n):
    if(n == 2 or n == 3): # 2 and 3 are prime numbers
        return True 
    if(n % 2 == 0): # Input number is even
        primality.m = 2
        return False
    if(n % 3 == 0): # Input number is divisible by 3
        primality.m = 3
        return False
    m = 5 # Trying numbers of the form 6k ± 1 up to the square root of the input number
    while(m * m <= n): 
        if(n % m == 0):
            primality.m = m
            return False
        m = m + 2
        if(n % m == 0):
            primality.m = m
            return False
        m = m + 4
    return True

nbr = input("\nHello ! Enter a number to check if it's prime: ")
print("\nThe number you entered is prime") if primality(int(nbr)) else print("\nThe number you entered is not prime. It's divisible by " + str(primality.m)) 
