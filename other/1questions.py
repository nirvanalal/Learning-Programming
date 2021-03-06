# Question Pool: https://libraries.sta.uwi.edu/apps/index.php/PastPaperSearch/results
# Search: Programming

# Question:
# Write a program, Fence, to calculate and print the amount and cost of the wire needed to fence a rectangular field. 1 meter of wire costs $25. The program allows the user to enter the length and width of the field in meters.

def fence():
  l =  int(input("length: "))
  w = int(input("width: "))
  p = 2*(l+w)
  cost = p*25
  print ("$", cost)
#fence()



# Question:
# A local electronics store allows items to be purchased on hire purchase. The hire purchase option 
# requires a deposit of one fifth of the cash price. There is an interest charge of 10% on the 
# balance. 
# Consider the following example: A customer wishes to purchase a Dell Inspiron 15-inch laptop, 
# with an i5 processor and 8 GB RAM, for $3500. The item code is 12345 and the customer 
# chooses to pay via two years on hire purchase. 

# Write a program, HirePurchase, which prints the invoice for an item on hire purchase as detailed 
# above. The program prompts for the item code, cash price and number of years on hire purchase.

# hello:)

def hire_purchase():
  price = input('price: ')
  years = int(input('years: '))
  deposit = 0.2 * price
  remainder = price - deposit
  interest = 0.1 * remainder
  monthly = (remainder + interest)/(years*12)
  print(monthly)



# # Question:
# Data is available on items sold by a company. The data consists of a 4-digit item number, the
# unit price, the price-break quantity and the quantity sold.

# The price-break quantity is the smallest quantity that must be bought before a discount or
# reduction in price is given. For example, if the price-break quantity is 10, a discount can be
# applied if the quantity sold is greater than or equal to 10.
# The amount to be paid is normally calculated by multiplying the unit price by the quantity sold.
# However, the following applies:
# • If the quantity sold is greater than or equal to the price-break quantity, then a 10% discount is
# given for that item.
# • If a discount is given, and the new amount to be paid exceeds $1000.00, then a further 5%
# discount is given.
# • If a discount is not given, and the amount to be paid exceeds $1000.00, then a 5% discount is
# given.
# The following is an example of a line of input data: 1325 23.0 45 40
# This indicates that item 1325 costs $23.00 each with a price-break quantity of 45. The quantity
# sold was 40.

# Write a program, Items.cpp, to do the following:
# • Request from the user the number of items to be processed.
# • For each item, request from the user the item number, the unit price, the price-break quantity
# and the quantity sold.

# • Print a suitable heading and under it, for each item, list the item number, unit price, price-
# break quantity, quantity sold, amount normally paid, discount amount (0.00, if none) and net

# payment.
# • After all the items have been processed:
# o Print the number of valid items in the data
# o Print the number of invalid items in the data.
# o Print the total amount normally due, the total discount given and the total net payment.
# o Print the item number and the net payment of the item with the highest net payment.
# Ignore the possibility of a tie.

# Note:
# • Values entered by the user for the item number and the number of items must be validated.
# • To perform the validation for the number of items, your program must ensure that the item
# number has the following properties:
# o Each item number is a 4-digit number.
# o Item numbers begin at 1000.
# • To perform the validation for the number of items to be processed:
# o Consider the range of numbers that are valid item numbers and use this.
# o If the number of items to be processed is larger than this amount the user should be
# informed and asked to reenter the amount of numbers to be processed.
# • Only items with valid item numbers are processed.
# • If an item number is invalid, the item number and an appropriate message are displayed.









# Question:
# https://drive.google.com/drive/folders/10jMf0RjD--OonnMqes_AyKoneb9CYeN_
# A sports club is hosting its annual fund raising triathlon and needs a computer program to process the results
# and keep track of the funds raised. The triathlon consist of a 1 kilometre swim, a 4 kilometre bicycle ride,
# and a 5 kilometre run. The data for each competitor is stored in a file triath.txt. Each line of data consists
# of a competitor’s ID (integer), a single letter category (M for member, F for family of members, N for non
# members and A for administration) followed by times for the three events (integer numbers denoting time
# in minutes and seconds). A sample line of data is as follows:

# 123 M 17 24 25 04 30 09

# Here, the competitor’s ID is 123, the competitor is a member of the club, the time in the swim is 17 minutes
# 24 seconds, the time in the bicycle ride is 25 minutes 04 seconds, and her time in the run is 30 minutes 9
# seconds.
# A line containing 0 only terminates the data in the file.
# A competitor qualifies for the title “Elite” if the total time to complete all three events is at most 1 hour 15
# minutes.
# Write a program to read the data and send the following to a file, output.txt:
# 1.a) For each competitor, output the competitor’s ID, category and total time.
# 1.b) For each competitor also output whether or not the competitor is an Elite competitor.

# For part 2), you must write a function, isElite, which takes as parameters the competitor’s time in the
# swim in seconds, the time in the bicycle ride in seconds, and the time in the run in seconds and returns
# true if the competitor is an Elite competitor or false otherwise.


# 3) The number of competitors that are members, family of members, non-members and administration
# 4) The competitor ID of and total time taken by the overall champion
# 5) The competitor ID of the overall best swimmer and runner up
# 6) The competitor ID of the overall best biker and runner up
# 7) The competitor ID of the overall best runner and runner up
# 8) The total funds raised by the event.
# For part 1), you must write a function, printFees, which takes as a parameter the competitor’s category as
# a character and returns the fees the competitor must pay based on Table 1 below.

# Category Fee
# Member 100
# Family of member 75
# Non-member 200
# Administration Free
# Table 1: Triathlon Participation Fees


'''
1 M 
'''

def sports():

  import sys  # system.

  def is_elite(s, b, r):
    return s+b+r < (60*75)

  # Read lines from a file.
  with open ('data.txt', 'r') as f:
    lines = [line.rstrip() for line in f.readlines()]

  # Looping over all lines.
  id1, t1, = "dont't-care", sys.maxsize
  s1, s2, s1_id, s2_id = sys.maxsize, sys.maxsize, "don't-care", "don't-care"
  m, f, n, a = 0, 0, 0, 0

  for line in lines:
    id, cat, sm, ss, bm, bs, rm, rs = line.split()
    s = int(sm)*60 + int(ss)
    b = int(bm)*60 + int(bs)
    r = int(rm)*60 + int(rs)

    t = s + b + r
    print("Part 1")
    print(id, cat, t, is_elite(s, b, r))
    
    # open('output.txt', 'a')
    # output = open('output.txt', 'w')              
    # output.write(id, cat, total_time, is_elite)

    # M, F, N, A.
    if cat == 'M':
      m += 1
    elif cat == "F":
      f += 1
    elif cat == "N":
      n += 1
    else:
      a += 1

    # Finding the winner (shortest time taken).
    if t < t1:
      t1 = t
      id1 = id

    # Finding the best sr 
    # https://jamboard.google.com/d/1cnlQ8HecdyQ_ua1FVaNPO7DN6F_oa6r2t5IGbXmUaxo/viewer?f=1
    if s < s1:
      s2 = s1
      s1 = s
      s2_id = s1_id
      s1_id = id
    elif s < s2:
      s2 = s
      s2_id = id

    def funds():
      f = m*100 + f*75 + n*200

    print ('Part 3:')
    print("M: ", m, "F: ", f, "N: ", n, "A: ", a)
    print ("Part 4:")
    print("Champion:", id1)
    print("Best Swimmer ID:", s1_id, "Runner up Swimmer ID:", s2_id)
    print('$', f)
    
# sports()




# Question:
# A certain file, views.txt, contains the number of times a YouTube video was viewed for each
# day over a certain period. A view occurs whenever someone views the video on a browser or using
# the YouTube app on their mobile phone. The amount of days is unknown beforehand, but a
# negative view value means that there is no more data in the file.
# NB: The number of views in any given day is always less than 1000.
# Write a program VideoViews.cpp, which provides the following functionality in the order
# given:
# a) Open the file and read all the views contained in the file and store them in an array. Assume
# that the file contains view values for at most 366 days. Generate an exception report
# (exceptionReport.txt) for any view value that is greater than 999 (do not store these
# values in the array).
# b) Find and display:
# (i) The number of days processed,
# (ii) The highest number and the lowest number of views the video obtained in the given period,
# (iii)The average number of views,
# (iv)The amount of times that the views went above the average, and
# (v) The highest number of views in the first ten (10) days.
# c) In addition, find and display:
# (i) All the days when there were no views to the video.
# (ii) The two days when the video was viewed more than all the other days.

# (iii)All the occasions when there were three consecutive days where the number of views went
# above a certain number n, where n is input by the user at the keyboard. If no such three
# days exist, print “None exists.”.
# d) Display a table showing the number of days the views fell in each of the following categories:
# 0-99, 100-199, 200-299, 300-399, 400-499, 500-599, 600-699, 700-799, 800-899, and 900-
# 999.
# A sample format of the table is shown below (NB: The number of views in each range will
# depend on the actual data):

# Range of Video Views # Views
# ==================== =======
# 0 to 99 3
# 100 to 199 9
# 200 to 299 3
# 300 to 399 5
# 400 to 499 7
# 500 to 599 5
# 600 to 699 5
# 700 to 799 5
# 800 to 899 5
# 900 to 999 2

# Hint: Use another array of size ten (10) where each location represents a range. For example,
# location 0 represents range 0 to 99, location 1 represents range 100 to 199, and so on.
# e) Display all the views stored in the array, 10 view values per line.

# Note: All output is written to a file statistics.txt.






# Question.
# The sum of all the divisors of an integer a including 1 but not including a is denoted by sum (a).
# For example, sum (6) = 1 + 2 + 3, and sum (14) = 1 + 2 + 7.
# (a) Write a function sum, which given an integer a, returns the sum of all the divisors of a.
# (b) The integers a and b, are said to be amicable if sum (a) == b and sum (b) == a.
# Write a function isAmicable, which, given two integer parameters a and b, returns 1 (or true) if a
# and b are amicable and 0 (or false) otherwise. You must use the function sum written in 4(a)
# above.
# (c) Using the function sum written in 4(a) above, write a function classifyNumber, which, given a
# positive integer n, returns the value 1, 2 or 3 as follows:
# 1: If sum (n) == n.
# 2: If sum (n) < n.
# 3: If sum (n) > n.

def divisors():
  
  # part a
  def sum(a):
    s = 0
    for i in range (1, (a//2)+1):  # // rounds down
      if a%i == 0:
        s += i
    return s
  
  # print(sum(100))

  # part b
  def is_amicable(a, b):
    return sum(a) == b and sum(b) == a 

  # 220 and 284
  # print (is_amicable(220, 284))

  # part c
  def classify_number(a):
    s = sum(a)
    if s == a:
      return 1
    elif s < a:
      return 2
    return 3

# divisors()





# BAD QUESTION !!!
# Question:
# Write a function that accepts a string (aka an array of characters) and a char variable `ch` and replaces all instances of ch in the string with "$".

def replace(A, ch):
  B = ""
  for c in A:
    if c == ch:
      B += "$"
    else:
      B += c
  return B

# print(replace("abcdefg", "c"))




# Question:
# Write a function that accepts a character ch and a string s and returns true if ch is a letter in s.
def is_in(s, ch):
  for c in s:
    if c == ch:
      return True
  return False

def is_in_pythonic_way(s, ch):
  return ch in s

# print(is_in("chris", "q"))
# print(is_in_pythonic_way("chris", "c"))





# Question:
# Write a function that accept a year (int) and returns True if year is a leap year and false otherwise.
def is_leap_year(y):
  return y%400 == 0 or (y%4 == 0 and y%100 != 0)

# print(is_leap_year(2014))






# Question:
# https://libraries.sta.uwi.edu/apps/index.php/PastPaperSearch/viewPaper/comp1601_1_19.pdf
# Q3

def draw_stars(n):
  print("*"*n)
  
def print_bow_tie(h):
  for i in reversed(range(1, h+1)):  # or range(h+1, 1, -1)
    draw_stars(i)
  for i in range(1, h+1):
    draw_stars(i)

# OR Chris Version
def print_bow_tie_shorter(h):

  def print_steps(h, rev=False):
    r = range(1, h+1)
    if rev:  # if paramter rev is True
      r = reversed(r)
    for i in r:
      draw_stars(i)

  print_steps(h, True)
  print_steps(h)

# print_bow_tie(10)
# print_bow_tie_shorter(10)

#OR
def bow_tie(h):
    list = range(1, h+1)
    for i in list[:: -1]:
      draw_stars(i)
    for i in list:
      draw_stars(i)

# bow_tie(5)







# Q2a
def minute():
  v = int(input('V: '))
  d = int(input('D: '))
  i = 1
  while v > 10 and i <= 20:
    v_e = d/100 * v
    v -= v_e
    print('Minute: ', i, 'Vol escaped: ', v_e, 'Vol remaining: ', v)
    i += 1

# minute()


# Q2bi
def testHypot(n):
  a = n*3
  c = 0
  while a > 0:
    b = a%10
    a = a//10
    c += b
    # OR.
    # c += a%10
    # a //= 10
  return c%3 == 0

# Q2bii

def testHypot_b():
  is_proven = True
  for i in range(1, 10001):
    if not testHypot(i):
      is_proven = False
      print(i)
  if is_proven:
    print('Proven')

# testHypot_b()






# Question:
# https://libraries.sta.uwi.edu/apps/index.php/PastPaperSearch/viewPaper/comp1100_2_12.pdf
# Q2b
# Write a function that accepts an integer and returns the integer with the digits reversed.

#SHIT - works but not correct
#it takes any "input" as a string automatically, not what question asks for
def rev_inat():
  a = (input("Integer: "))
  print(a[::-1])
# rev_int()

#correct answer
# a = 123
# b = 3 , c = 12
# a = 12
# b = 2, c = 1
# a = 1
# b = 1, c = 0


# ex: 123 -> 321
def rev_int(a):
  res = 0
  
  while a > 0:
    b = a%10
    c = a//10
    res = res*10 + b
    a = c  
    
# OPTIMAL
def rev_int(a):
  res = 0
  while a > 0:
    res = res*10 + a%10
    a //= 10  #  a = a // 10
  return res
  
# print(rev_int(123))



# Question:
# https://libraries.sta.uwi.edu/apps/index.php/PastPaperSearch/viewPaper/comp1100_2_12.pdf
# Q2d
# Write a function to check if a number is "perfect"
# perfect number, a positive integer that is equal to the sum of its proper divisors. The smallest perfect number is 6, which is the sum of 1, 2, and 3 
def perf(n):
  sum=0
  for i in range(1, (n/2)+1):
    if (n%i == 0):
      sum += i
  return sum == n

# print(perf(28))


# Question:
# https://libraries.sta.uwi.edu/apps/index.php/PastPaperSearch/viewPaper/comp1100_2_12.pdf
# Q2e
# Write a function to print the number of vowels in a word.


############SHIT###################################################
def vow():
  s = str(input('phrase: '))
  num=0
  for i in s:
    if i == 'a' or 'e' or 'i' or 'o' or 'u':
      num += 1
  print(num)
# vow()


#works but not best
def vow():
  s = str(input('phrase: '))
  num=0
  for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
      num += 1
  print(num)
# vow()

#optimal - sets and dictionaries are more efficent 
def vow(word):
  count = 0
  vowels = {"a", "e", "i", "o", "u"}  # Set.
  for letter in word:
    if letter.lower() in vowels:
      count += 1
  print(count)
# vow('ABC?')

def lower(ch):
  if ch >= "A" and ch <= "Z":
    return chr(ord(ch) + ord(" "))  #ord(" ") = 32 ie space between a common & capital of same letter in ASCII table
  return ch

# print(lower("a"))
# print(lower("A"))








# Question:
# Write code to generate and print the numbers of this sequence: -4, 3, 10, 17, 24, 31, 38, 45.
# Also find and print the sum of the sequence.

def plus7():
  x = -4
  sum = 0
  while x <= 45 :
    print (x)
    sum += x
    x += 7
  print(sum)
# plus7()

  








# Question:
# Write a function that returns True if n is a prime number, else False.









# Question:
# Write a function to sum all the numbers in an array, who has a factor of 5.










# Question: 
# Write a function that prints the binary representation of an integer (n) to the screen.








# Question:
# https://libraries.sta.uwi.edu/apps/index.php/PastPaperSearch/viewPaper/comp1100_1_12.pdf
# Q2a
# Write a function which, given an integer n, returns the number of digits in the integer.
# For example, given 5017, the function returns 4.

def digits(n):
  if n == 0:
    return 1
  count = 0
  if n < 0:
    n = n*-1
  while n > 0:
    count += 1
    n = n//10
  return count

# print(digits(5017))


# Question.
# Write a function that prints all times tables from 1 to 12 as follows:
'''
1 x 1 = 1
1 x 2 = 2
...
1 x 12 = 12

2 x 1 = 2
2 x 2 = 4
...
2 x 12 = 24

...

12 x 1 = 12
...
12 x 12 = 144

'''

def tables():
  for i in range(1, 13):
    for j in range(1, 13):
      print( i, 'x', j, '=', i*j)
    print()
# tables()




# Question.
# There are n lockers numbered 1 to n arranged in a row.
# Initally they are all closed.
# Starting with locker 2, all even numbered lockers are open.
# Next, starting with locker 3, and visiting every third locker, it is closed if it is open, and vice versa.
# This procedure is repeated for every 4th locker, then every 5th locker, and so on, up to the nth locker.
# Write a function that accepts n and returns the number of lockers that are closed at the end of the procedure.

def lockers(n):
  # False = closed
  # True = open
  # for i in range(1, n+1):
  #   i = False
  # for i in range(2, n+1, 2):
  #   i = True
  count = 0
  lockers = [False]*(n+1)  # indices: 0 -> n, List you want: 1 -> n
  # print(lockers)
  for i in range(2, n+1):
      for j in range(i, n+1, i):
        lockers[j] = not lockers[j]
      print(lockers[1:])
  
  for i in range(1, n+1):
    if not lockers[i]:
      count += 1
  return count

# print(lockers(10))

    # if i = True:
    #   i = False
    # if i = False:
    #   i = True
    # i += 1
      



def multi_dim_arrays():
  A = []
  B = [1]
  C = [1, 2]
  D = [[1],
       [2]]
  E = [[1, 2], [3, 4]]
  F = [
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]]
  ]
  for row in F:
    for col in row:
      for val in col:
        print(val)

  for i, _ in enumerate(F):
    for j, _ in enumerate(F[i]):
      for k, _ in enumerate(F[i][j]):
        print(F[i][j][k])

# multi_dim_arrays()



# Question:
# Write a function that accepts a two dimensional array and prints all the values in the array.
# Return the sum of all the positive values in the array.

def print_2d_list(A):
  for row in A:
    for col in row:
      print(col)

# print_2d_list([[1, 2], [3, 4]])
'''
1
2
3
4
'''
  

def multi_returns():
  return 1, 2, "not chris"  # returns a tuple
# print(multi_returns())
# val1, val2, val3 = multi_returns()  # unpacking
# print(val1)
# val1, *val2 = multi_returns()  # unknown amount
# print(val1, val2)



# Question.
# Write a function that accepts two matrices and returns the result of their matrix addition.
def add(A, B):
  pass





# Question.
# Write a function that accepts two matrices and returns the matrix product.






# Question.
# https://libraries.sta.uwi.edu/apps/index.php/PastPaperSearch/viewPaper/comp1602_1_18.pdf
# Basically the whole paper.






# Question.
# https://libraries.sta.uwi.edu/apps/index.php/PastPaperSearch/viewPaper/comp1602_1_19.pdf
# Q3







# Question: Pixels (structs)
# https://libraries.sta.uwi.edu/apps/index.php/PastPaperSearch/viewPaper/comp1602_2_17.pdf
# Q2








# Question
# Write a recursive function that accepts an integer n and prints the digits in the reverse order.




# Question
# Write a recursive function that accepts an integer n and returns a new integer with the digits reversed.





