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


## Testing 1-2-3

Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.

Examples:
``
number([]) # => []
number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]
``

### Deduction
- the number index in the string is the number to be appended in front of the string

### My Solution

```
def number(lines):
    #your code here
    result = []
    if not lines: return []
    for i, c in enumerate(lines):
        ans = "{i}: {c}".format(i=i+1, c=c)
        result.append(ans)
    return result

```
Passed all test cases, space complexity is high though



## Binary Addition
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.

### My solution
This is pretty straigtforward for Python, it's different with Java though. 

```
def add_binary(a,b):
    #your code here
    return "{0:b}".format(a+b)
```
Passed all test cases


## Your order, please

Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

Examples
```
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"

```

### Deduction

- split the string with space as delimiter
- check if the char in the each str is a number. ASCII can come in handy. We know number can fall in the range of 46 and 57
- if yes, add the string to an array, at index of char - 1
- join the array with space

### My solution
````
def order(sentence):
    # base case
    if not sentence: return ""
    
    #split at space
    new_str = sentence.split()
    #new array
    result = [""] * len(new_str)
    
    for s in new_str:
        for i in s:
            #check if the char is a number
            if ord(i) > 48 and ord(i) <= 57:
                pos = int(i)
                result[pos-1] = s
    return " ".join(result)

````
Passed all the test case, however, after I submitted, I learnt that there is a function to check if a char is a digit built into python 3, isDigit()
So we can just remove the whole if statement if we want

This solution has time complexity of O(i * s), so with longer string it can take up more time, performance will take a hit
but it seems like that's the mininum time we can afford

