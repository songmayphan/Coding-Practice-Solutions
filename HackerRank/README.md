# Strings

## Making Anagrams


### My solution
``
 def makeAnagram(a, b):
     common = Counter(a) & Counter(b)
     print(common)
     remain = sum(common.values())
     print(remain)
     ans_a = len(a) - remain
     ans_b = len(b) - remain
     print(ans_a)
     print(ans_b)
     ans = ans_a + ans_b
     return ans
``     
### Time complexity
O(1), passed all test cases


## Alternating Characters
 return an integer representing the minimum number of deletions to make the alternating string.
Sample input
``
5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB
``
Sample output
```
3
4
0
0
4
```
### My Solution
````

def alternatingCharacters(s):
    se = list(s)
    count = 0
    for i in range(len(se) - 1):
        if se[i+1] != se[i]:
            continue
        else:
            count+=1
            print(count)
            continue
    
    return count
````

### Time Complexity
O(N), N is the length of the string
passed all test cases


## Sherlock and the Valid String
[Sherlock and the Valid String](https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings&h_r=next-challenge&h_v=zen)

### My Solution

```
def isValid(s):
    count = 0
    count_char = Counter(s)
    freq = Counter(count_char.values())
    print(freq)
    if len(freq) == 1:
        return "YES"
    if len(freq) == 2:
        dom_key = max(freq.keys())
        sub_key = min(freq.keys())
        print(dom_key, sub_key)
        if dom_key - sub_key == 1 and freq[dom_key] == 1:
            return "YES"
        elif sub_key == 1 and freq[sub_key] == 1: 
            return "YES"
    return "NO"

```
