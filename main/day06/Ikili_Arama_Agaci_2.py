class BSTNode:
    def __init__(self,data=None):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insertNode(self,root_node,node_value):
        if root_node.data == None:
            root_node.data = node_value
        elif node_value <= root_node.data:
            if root_node.leftChild is None:
                root_node.leftChild = BSTNode(node_value)
            else:
                self.insertNode(root_node.leftChild,node_value)
        else:
            if root_node.rightChild is None:
                root_node.rightChild = BSTNode(node_value)
            else:
                self.insertNode(root_node.rightChild,node_value)
        return "eklendi"

    def preOrderTraversal(self, root_node):
        if not root_node:
            return
        print(root_node.data, end="-->")
        self.preOrderTraversal(root_node.leftChild)
        self.preOrderTraversal(root_node.rightChild)

    def inOrderTraversal(self, root_node):
        if not root_node:
            return
        self.inOrderTraversal(root_node.leftChild)
        self.inOrderTraversal(root_node.rightChild)
        print(root_node.data, end="-->")

    def postOrderTraversal(self, root_node):
        if not root_node:
            return
        self.postOrderTraversal(root_node.leftChild)
        self.postOrderTraversal(root_node.rightChild)
        print(root_node.data, end="-->")

#Ikili Arama agaci olusturulmasi

newTree = BSTNode()
newTree.insertNode(newTree,70)
newTree.insertNode(newTree,50)
newTree.insertNode(newTree,90)
newTree.insertNode(newTree,30)
newTree.insertNode(newTree,80)
newTree.insertNode(newTree,100)
newTree.insertNode(newTree,20)
newTree.insertNode(newTree,40)

print(newTree.insertNode(newTree,60))

#preOrder dolasim
print("once kok dolasimi")
newTree.preOrderTraversal(newTree)
print("\n\n")

#inOrder dolasim
print("ortada kok dolasimi")
newTree.inOrderTraversal(newTree)
print("\n\n")

#postOrder dolasim
print("sonra kok dolasimi")
newTree.postOrderTraversal(newTree)

"""
class BSTNode:
    def __init__(self, data=None):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insertNode(self,node_value):
        if self.data is None:
            self.data = node_value
        elif node_value < self.data:
            if self.leftChild is None:
                self.leftChild = BSTNode(node_value)
            else:
                self.leftChild.insertNode(node_value)
        elif node_value > self.data:
            if self.rightChild is None:
                self.rightChild = BSTNode(node_value)
            else:
                self.rightChild.insertNode(node_value)
        else:
            return "Duplicate value"
        return "eklendi"

    def preOrderTraversal(self,root_node):
        if not root_node:
            return
        print(root_node.data,end="-->")
        self.preOrderTraversal(root_node.leftChild)
        self.preOrderTraversal(root_node.rightChild)

    def inOrderTraversal(self,root_node):
        if not root_node:
            return
        self.inOrderTraversal(root_node.leftChild)
        self.inOrderTraversal(root_node.rightChild)
        print(root_node.data,end="-->")

    def postOrderTraversal(self,root_node):
        if not root_node:
            return
        self.postOrderTraversal(root_node.leftChild)
        self.postOrderTraversal(root_node.rightChild)
        print(root_node.data, end="-->")

# Binary Search Tree creation
newTree = BSTNode()
newTree.insertNode(70)
newTree.insertNode(50)
newTree.insertNode(90)
newTree.insertNode(30)
newTree.insertNode(80)
newTree.insertNode(100)
newTree.insertNode(20)
newTree.insertNode(40)

print(newTree.insertNode(60))

#preOrder dolasim
print("once kok dolasimi")
newTree.preOrderTraversal(newTree)
print("\n\n")

#inOrder dolasim
print("ortada kok dolasimi")
newTree.inOrderTraversal(newTree)
print("\n\n")

#postOrder dolasim
print("snora kok dolasimi")
newTree.postOrderTraversal(newTree)
"""
