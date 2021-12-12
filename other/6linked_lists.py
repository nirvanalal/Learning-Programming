class Node:
  def __init__(self, num):
    self.num = num
    self.next = None

# JamBoard - https://jamboard.google.com/d/1cnlQ8HecdyQ_ua1FVaNPO7DN6F_oa6r2t5IGbXmUaxo/viewer?f=10

head = Node(5)
head.next = Node(2)
head.next.next = Node(1)
# print(head.next.num)

class LinkedList:
  def __init__(self):
    self.head = None
  
  def prepend(self, num):
    pass
  
  def append(self)

