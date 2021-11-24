'''
https://www.algoexpert.io/questions/Palindrome%20Check

A string is a character array.

c h r i s
0 1 2 3 4

s = "chris"
s[3]  ## i.


l e v e l
0 1 2 3 4
    i
    j

l e v e l s
    i j
    j i


'''

'''
# this is shit
def is_palindrome(string):
  l = len(string)
  for i in string:
    return [0, l] == [0, l, -1]
'''

def is_palindrome_0(s):
  return s == reversed(s)

def is_palindrome_1(s):
  return s == s[::-1]

# i - left Index
# j - right index

def is_palindrome(s):
  i, j = 0, len(s)-1
  while i < j:
    if s[i] != s[j]:
      return False
    i += 1
    j -=1
  return True






  
