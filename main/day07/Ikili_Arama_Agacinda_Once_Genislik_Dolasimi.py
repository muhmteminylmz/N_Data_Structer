import main.day06.Ikili_Arama_Agaci as queue

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

    def leverOrderTraversal(self,root_node):
        if not root_node:
            return
        else:
            customQueue = queue.Queue()
            customQueue.enqueue(root_node)
            while not(customQueue.isEmpty()):
                root = customQueue.dequeue()
                print(root.value.data,end='->')
                if root.value.leftChild is not None:
                    customQueue.enqueue(root.value.leftChild)
                    if root.value.rightChild is not None:
                        customQueue.enqueue(root.value.rightChild)

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

#Düzel dolasim
print("\n\n")
newTree.leverOrderTraversal(newTree)