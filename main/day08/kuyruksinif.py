class BSTNode:
    def _init_(self, data=None):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insertNode(self, node_value):
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

    def preOrderTraversal(self, root_note):
        if not root_note:
            return
        print(root_note.data, end="-->")
        self.preOrderTraversal(root_note.leftChild)
        self.preOrderTraversal(root_note.rightChild)


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