# Primality test using two optimization methods in comparison with a naive solution that 
# iterates through all the positive integers less than the input number, to check if any divides it
# 1-Testing integers only up to the square root of the input number (trial division)
# 2-Testing integers only of the form 6k ± 1 after checking if the input number is even or divisible by 3 
# given that all prime numbers, except 2 and 3, are of this form

def primality(n):
    if(n == 2 or n == 3):
        return True
    if(n % 2 == 0 or n % 3 == 0):
        return False
    m = 5
    while(m * m <= n):
        if(n % m == 0):
            return False
        m = m + 2
        if(n % m == 0):
            return False
        m = m + 4
    return True

nbr = input("\nHello ! Enter a number to check if it's prime: ")
print("\nThe number you entered is prime") if primality(int(nbr)) else print("\nThe number you entered is not prime")
