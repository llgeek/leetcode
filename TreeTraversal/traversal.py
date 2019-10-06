class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def pre_order_recursive(root, res):
    def helper(node):
        if not node:
            return
        res.append(node.val)
        helper(node.left)
        helper(node.right)
    helper(root)


def pre_order_iterative(root, res):
    # from collections import deque
    if not root:
        return 
    stack = [root]
    while stack:
        curnode = stack.pop()
        res.append(curnode.val)
        if curnode.right:
            stack.append(curnode.right)
        if curnode.left:
            stack.append(curnode.left)


def in_order_recursive(root, res):
    def helper(node):
        if not node:
            return 
        helper(node.left)
        res.append(node.val)
        helper(node.right)
    helper(root)

def in_order_iterative(root, res):
    stack = []
    curnode = root
    while stack or curnode:
        if curnode:
            stack.append(curnode)
            curnode = curnode.left
        else:
            curnode = stack.pop()
            res.append(curnode.val)
            curnode = curnode.right


def post_order_recursive(root, res):
    def helper(node):
        if not node:
            return
        helper(node.left)
        helper(node.right)
        res.append(node.val)
    helper(root)

def post_order_iterative(root, res):
    stack = [root] 
    while stack:
        curnode = root.pop()
        res.append(root.val)
        if curnode.left:
            stack.append(curnode.left)
        if curnode.right:
            stack.append(curnode.right)
    res.reverse()





def create_tree():
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2.5)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(7)
    return root

if __name__ == "__main__":
    tree = create_tree()
    res11 = []
    pre_order_recursive(tree, res11)
    print(res11)

    res12 = []
    pre_order_iterative(tree, res12)
    print(res12)

    res21 = []
    in_order_recursive(tree, res21)
    print(res21)

    res22 = []
    in_order_iterative(tree, res22)
    print(res22)

    res31 = []
    post_order_recursive(tree, res31)
    print(res31)

    res32 = []
    post_order_recursive(tree, res32)
    print(res32)

