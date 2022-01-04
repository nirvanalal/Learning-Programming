class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


class BinaryTree:
  def __init__(self):
    self.root = None

  def print_preorder(self, node):
    # Base case:
    if node is None:
      return
    print(node.data, " ", end="")
    self.print_preorder(node.left)
    self.print_preorder(node.right)
    
  def print_inorder(self, node):
    # Base case:
    if node is None:
      return
    self.print_inorder(node.left)
    print(node.data, " ", end="")
    self.print_inorder(node.right)
  
  def print_postorder(self, node):
    # Base case:
    if node is None:
      return
    self.print_inorder(node.left)
    self.print_inorder(node.right)
    print(node.data, " ", end="")
    
    # 15 10 20 6 1 10 5 

  # Q: Return num of nodes in binary tree
  def num_nodes(self, node):
    if node is None:
      return 0
    return 1 + self.num_nodes(node.left) + self.num_nodes(node.right)

  def print_levels(self):
    pass
  

node5 = Node(5)
node6 = Node(6)
node10 = Node(10)
node15 = Node(15)
node20 = Node(20)
node1 = Node(1)
node10_2 = Node(10)

bt = BinaryTree()
bt.root = node5
node5.left = node6
node5.right = node10
node6.left = node15
node6.right = node20
node10.right = node1
node20.left = node10_2

bt.print_preorder(bt.root)
print()

print(bt.num_nodes(bt.root))