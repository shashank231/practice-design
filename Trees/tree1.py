class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def printLevelOrder(root):
    if not root:
        return []
    queue = []
    queue.append(root)
 
    while(len(queue) > 0):
        print(queue[0].data)
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

def printLevelOrderInLevels(root):
    if not root:
        return []
    queue = []
    queue.append(root)
 
    while(len(queue) > 0):
        temp_lst = []
        while(len(queue) > 0):
            node = queue.pop(0)
            print(node.data, end=" ")
            if node.left is not None:
                temp_lst.append(node.left)
            if node.right is not None:
                temp_lst.append(node.right)
        print()
        [queue.append(node) for node in temp_lst]

def printLeftView(root):
    if not root:
        return []
    queue = []
    queue.append(root)
 
    while(len(queue) > 0):
        temp_lst = []
        left_element_printed = False
        while(len(queue) > 0):
            node = queue.pop(0)
            if not left_element_printed:
                print(node.data, end=" ")
                left_element_printed = True
            if node.left is not None:
                temp_lst.append(node.left)
            if node.right is not None:
                temp_lst.append(node.right)
        print()
        [queue.append(node) for node in temp_lst]

def printRightView(root):
    if not root:
        return []
    queue = []
    queue.append(root)
 
    while(len(queue) > 0):
        temp_lst = []
        while(len(queue) > 0):
            node = queue.pop(0)
            if not len(queue):
                print(node.data, end=" ")
            if node.left is not None:
                temp_lst.append(node.left)
            if node.right is not None:
                temp_lst.append(node.right)
        print()
        [queue.append(node) for node in temp_lst]


def swap(root):
    if root is None:
        return
    temp = root.left
    root.left = root.right
    root.right = temp
 
def invertBinaryTree(root):
    if root is None:
        return     
    invertBinaryTree(root.left)
    invertBinaryTree(root.right)
    swap(root)


def minDepth(root):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 1
    return 1 + min(minDepth(root.left), minDepth(root.right))


def height(node):
	if node is None:
		return 0
	return 1 + max(
        height(node.left), 
        height(node.right))

def diameter(root):
	if root is None:
		return 0

	lheight = height(root.left)
	rheight = height(root.right)
	ldiameter = diameter(root.left)
	rdiameter = diameter(root.right)

	# Return max of the following tree:
	# 1) Diameter of left subtree
	# 2) Diameter of right subtree
	# 3) Height of left subtree + height of right subtree +1
	return max(
        1 + lheight + rheight,
        max(ldiameter, rdiameter))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.right.right.left = Node(9)



printLevelOrder(root)
print()
printLevelOrderInLevels(root)
print()
printLeftView(root)
print()
printRightView(root)
print()
a1 = minDepth(root)
print(a1)







