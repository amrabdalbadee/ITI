class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    def connect_node(self,left,right):
        self.left = left
        self.right = right
    def __repr__(self):
        print(f"Data of node is {self.data}, its left is {self.left}, and its right is {self.right}")
def preorder(root):
    if root ==None:
        return
    print(root.data)
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if root ==None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data)

def inorder(root):
    if root ==None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)


def main():
  root = Node(1)
  node_2 = Node(2)
  node_3 = Node(3)
  root.connect_node(node_2,node_3)
  node_4 = Node(4)
  node_5 = Node(5)
  node_2.connect_node(node_4,node_5)
  node_7 = Node(7)
  node_8 = Node(8)
  node_4.connect_node(node_7,None)
  node_5.connect_node(node_8,None)
  node_6 = Node(6)
  node_9 = Node(9)
  node_10 = Node(10)
  node_11 = Node(11)
  node_12 = Node(12)
  node_3.connect_node(None,node_6)
  node_6.connect_node(node_9,node_10)
  node_9.connect_node(node_11,None)
  node_10.connect_node(node_12,None)
  #inorder(root)
  #postorder(root)
  preorder(root)
if __name__  =="__main__" :
    main()
