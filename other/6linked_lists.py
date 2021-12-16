class Node:
  def __init__(self, num):
    # Data in this Node.
    self.num = num # Defining & initialising 'num'
    # Reference to the next node.
    self.next = None # Defining 'next'

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
    '''
    head -> Node(1) -> Node(2) -> None

    Step 1:
    new_node -> Node(0) -> None

    ===

    Step 2:

                head -> Node(1) -> Node(2) -> None
                          ^
                          |
    new_node -> Node(0) - |


    ===

    Step 3:

                head   Node(1) -> Node(2) -> None
                   |      ^
                   V      |
    new_node -> Node(0)-- |

    '''
    new_node = Node(num)
    new_node.next = self.head
    self.head = new_node
    
  def append(self, num):
    new_node = Node(num)

    if self.head is None:
      self.head = new_node
      return

    curr = self.head
    while curr.next != None:
      curr = curr.next
    curr.next = new_node

  def length(self):
    len = 0
    if self.head is None:
      len = 0
      return len
    
    curr = self.head
    while curr.next != None:
      curr = curr.next
      len += 1
    len += 1
    return len

  def length2(self):
    len = 0
    curr = self.head
    while curr != None:
      curr = curr.next
      len += 1
    return len

  def insert_at(self, num, index):
    '''
    Cases:
    0. Insert at head
    1. Empty List
    2. If index >= len(list)
    3. Insert somewhere in the middle
    '''
    i = 0
    new_node = Node(num)
    prev = None
    curr = self.head
    while curr != None and i < index:
      prev = curr
      curr = curr.next
      i += 1

    new_node.next = curr
    if curr == self.head:
      self.head = new_node
    else:
      prev.next = new_node    

  
  def delete(self, num): 
    # https://www.geeksforgeeks.org/linked-list-set-3-deleting-node/
    curr = self.head
    prev = None
    while curr != None and curr.num != num:
      prev = curr
      curr = curr.next
    if curr == None:
      return
    if curr == self.head:
      self.head = curr.next
    else:
      prev.next = curr.next
    del curr


  def delete_at(self, index):
    # https://www.geeksforgeeks.org/delete-a-linked-list-node-at-a-given-position/
    
    pass

  def recursive_print(self, curr):
    # Base case - empty list:
    if curr == None:
      return
    # Recursive case:
    print(curr.num)
    self.recursive_print(curr.next)

  def recursive_length(self, curr):
    if curr == None:
      return 0
    return 1 + self.recursive_length(curr.next)
  
  def sort(self):
    pass

  def search(self, num):
    pass

linked_list = LinkedList()  # H -> None

# Initial: H -> 1 -> 2 -> 3 -> None
# Prepend: H -> 0 -> 1 -> 2 -> 3 -> None
if __name__ == "__main__":
  linked_list.print()
  linked_list.prepend(3)
  linked_list.print()
  linked_list.prepend(2)
  linked_list.print()
  linked_list.prepend(1)
  linked_list.print()
  linked_list.append(4)
  linked_list.print()
  print(linked_list.length())
  linked_list.insert_at(0, 0)
  linked_list.print()
  linked_list.insert_at(1.5, 2)
  linked_list.print()
  linked_list.insert_at(5, 10)
  linked_list.print()

  #New list
  ll2 = LinkedList()
  # ll2.insert_at(1, 0)
  ll2.print()
  ll2.delete(1.5)
  ll2.print()
  ll2.append(1)
  ll2.print()
  ll2.delete(1)
  ll2.print()


  linked_list.delete(0)
  linked_list.print()
  linked_list.delete(1.5)
  linked_list.print()
  linked_list.delete(5)
  linked_list.print()
  linked_list.delete(6)
  linked_list.print()

  linked_list.recursive_print(linked_list.head)

