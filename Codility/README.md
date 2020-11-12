# Count odd occurences in arrays

given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, since 7 does not have a pair

## Deduction
Return the value that has only 1 occurence in the array

## My submission
```
def solution(A):
    result = [[x,A.count(x)] for x in set(A)]
    for i in result:
        if i[1] == 1:
            return i[0]
    pass

```
## Score
55%

Errors detected: runtime errors, timeout errors

## Time complexity
`O(N**2)`


## A Better solution is to use Hash Map
````
def getOddOccurrence(arr,size): 
       
    # Defining HashMap in C++ 
    Hash=dict() 
   
    # Putting all elements into the HashMap  
    for i in range(size): 
        Hash[arr[i]]=Hash.get(arr[i],0) + 1; 
      
    # Iterate through HashMap to check an element 
    # occurring odd number of times and return it 
    for i in Hash: 
  
        if(Hash[i] == 1): 
            return i 
    return -1
 ````
Time complexity is O(N) but, space is needed
## The best solution is to use bitwise XOR

```
def solution(A):
	res = 0 

	for element in arr:
		res = res ^ element

	return res

```
Time complexity O(N)



# Binary Gap 

Return the largest binary gap in an interger

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. 

## Deduction:
  
1) Convert the number into binary
2) Loop through the number, count the number of 0s
3)if found a 1, save the current count, reset count to zero
4) repeat


## My submission

```
def solution (n):
	count = 0
	gaps =[]
	bin_str = "{0:b}".format(n)

	for c in bin_str:
		if c == 1:
			gaps.append(count)
			count = 0
			continue

		else:
			count+=1

	return max(gaps)

```

## Score: 
100%

## Time complexity

O(N) , N being the length of the binary string



# Frog Jump

 X = 10
  Y = 85
  D = 30
the function should return 3, because the frog will be positioned as follows:

after the first jump, at position 10 + 30 = 40
after the second jump, at position 10 + 30 + 30 = 70
after the third jump, at position 10 + 30 + 30 + 30 = 100

## Solution

```
import math

def solution(X,Y,D):
	distance = Y-X
	return math.ceil(distance/D)


```
## Time complexity

O(1)

# PermMisingElem

given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

## Deduction

1) sort
2) make a new array, with length bigger than the original one
3) find the difference of the arrays

## My solution
```
def solution(A):
    # write your code in Python 3.6
    sort_A = sorted (A)
    B = list(range(1, len(A) + 2))
    result = set(B) -set(A)
    num = list(result)
    return num[0]
    pass
````
## Time complexity
O(N)

## Score:
100%
# Splicing Tape

consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7

## Deduction
1) loop through P
2) totalling the value until P - 1
3) totalling the values until N - 1
4) find their difference
5) storing it in an array
6) return the max

## My solution

```

def solution(A):
    # write your code in Python 3.6
    res = [0]*(len(A)-1)
    sum_left = 0
    sum_right = 0
    sumA = sum(A)
    for P in range(1, len(A)):
        sum_left = sum_left+A[P-1]
        sum_right= sumA-sum_left #sum(A[P:])
        ans  = abs(sum_left - sum_right)
        res[P-1]=ans #res.append(ans)
    return min(res)
    pass


```
## Time complexity

O(N)

## Score 
100%


# Another Frog

A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.

For example, you are given integer X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.


## Deduction:
1) Find A[K]
2) if A[K] == X and A[0] -> A[K] != 0 , then return K

## My Solution

```
X_arr = list(range(X))
    for K in range(len(A)):
        if A[K] in X_arr:
            continue
        if A[K] == X:
            return K


```
