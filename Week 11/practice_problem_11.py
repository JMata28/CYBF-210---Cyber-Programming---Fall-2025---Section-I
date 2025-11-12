from collections import deque #needed to implement a queue

def levelOrder(root):
    if root is None:
        return
    
    result = []

    q = deque([root])

    while q:
        q_length = len(q)
        level = []
        #Notice we use the _ variable because we don't access the value of the _
        #This for loop builds each level list
        for _ in range(q_length): 
            node = q.popleft()
            print(node.data) #Just for us to see the order of traversal
            if node:
                level.append(node.data) #include the value of the node in the list of that level's nodes
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        result.append(level)
    
    return result


#Let's try it with the same tree we have:

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

print(levelOrder(root))