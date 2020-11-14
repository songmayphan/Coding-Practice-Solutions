# 7 Kyu Rank Up

## Find the Divisors

Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#)

### Deduction
What does it mean when a number has a divisor? It means that the modulus should be zero. 
The results have to be smaller than the integer, so we can loop through that

### My Solution

```
def isPrime(n):
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                # n is not prime
                return False
            else:
                continue
    return True
def divisors(integer):
    i = 2
    results = []
    if isPrime(integer):
        return "{num} is prime".format(num = integer)
    while i < integer:
        if integer % i == 0:
            results.append(i)
            i += 1
        else:
            i += 1
            continue            
    return results
    pass
```
Passed all test cases, although it can be optimized
