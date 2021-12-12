class Node:
  def __init__(self, num):
    self.num = num
    self.next = None

# JamBoard - https://jamboard.google.com/d/1cnlQ8HecdyQ_ua1FVaNPO7DN6F_oa6r2t5IGbXmUaxo/viewer?f=10

# head = Node(5)
# head.next = Node(2)
# head.next.next = Node(1)
# # print(head.next.num)

class LinkedList:
  def __init__(self):
    self.head = None
  
  def print(self):
    curr = self.head
    print("head -> ", end='')
    while curr != None:
      print(curr.num, " -> ", end='')
      curr = curr.next
    print("None")
  
  def prepend(self, num):
    node = Node(num)
    node.next = self.head
    self.head = node
    
  def append(self, num):
    node = Node(num)

    if self.head is None:
      self.head = node

    curr = self.head
    while curr.next != None:
      curr = curr.next
    curr.next = node

  def length(self):
    pass    

  def insert_at(self, num, index):
    pass
  
  def delete(self, num):
    # https://www.geeksforgeeks.org/linked-list-set-3-deleting-node/
    pass
  
  def delete_at(self, index):
    # https://www.geeksforgeeks.org/delete-a-linked-list-node-at-a-given-position/
    pass

  def recursive_print():
    pass


  def recursive_length(self):
    pass
  
  def sort(self):
    pass

  def search(self, num):
    pass

linked_list = LinkedList()  # H -> None

# Initial: H -> 1 -> 2 -> 3 -> None
# Prepend: H -> 0 -> 1 -> 2 -> 3 -> None

linked_list.print()
linked_list.prepend(3)
linked_list.print()
linked_list.prepend(2)
linked_list.print()
linked_list.prepend(1)
linked_list.print()
linked_list.append(4)
linked_list.print()