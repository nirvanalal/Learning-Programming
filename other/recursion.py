# print('Nirvana'*5)

def name():
  for i in range(5):
    print("Nirvana")

# name()

'''
Recursion: calling a function within itself.

Main parts of a recrusive function:
BASE CASE
RECURSIVE CASE
'''

def recursive_print(n):
  # base case.
  if n == 0:
    return
  # recursive case.
  print("Nirvana")
  recursive_print(n-1)
# recursive_print(5)



# Q: print 10, 9, ....., 1 using reccursion

def print_reverse_num(n):
  # Base case, ie when n=0:
  if n == 0:
    return
  # Recursion case:
  print(n)
  print_reverse_num(n-1)

# print_reverse_num(10)

# Q: print 1, 2, ..... n
def print_num(n):
  # Base case, ie when n=0:
  if n == 0:
    return
  # Recursion case:
  print_num(n-1)
  print(n)
  
# print_num(10)

#Q: Print all even numbers from 1-10 using Recursion
def print_even(n):
  # Base case:
  if n == 0:
    return
  # Recursion case:
  if n%2 == 0:
    print(n)
  print_even(n-1)

# print_even(10)


# Q: RETURN the sum of the numbers from 1 to 10.
def sum(n):
  # Base case:
  if n == 0:
    return 0 
  # Recursion case:
  return n + sum(n-1)

# print(sum(3))



# Q: RETURN the product of the numbers from 1 to 10.


# Q: PRINTS the digits in an int "n" one on each line.


# Q: PRINTS the digits in an int "n" one digit on each line, in reversed order.


# Q: RETURNS an int n with the digits in reversed order.


# Q: Print the following sequence:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

