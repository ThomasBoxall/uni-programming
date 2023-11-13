class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None
    def _get_height(self, node): # get the height of a tree rooted at node
        if node is None:
            return 0
        return node.height
    def _update_height(self, node): # update the height of a tree rooted at node, 1 + max(height of left subtree, height of right subtree)
        if node is None:
            return 0
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
    def _get_balance_factor(self, node): # calculate the balance factor of a node
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
        
    def _rotate_right(self, y): # a single right rotation
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self._update_height(y) # update heights
        self._update_height(x)
        return x
    def _rotate_left(self, x): # a single left rotation
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self._update_height(x)
        self._update_height(y)
        return y
    def _balance(self, node):
        # update height of current node
        self._update_height(node)
        # calculate balance factor
        balance = self._get_balance_factor(node)
        if balance > 1: # left heavy
            if self._get_balance_factor(node.left) < 0:
                # Left-Right case: Perform left rotation on left childand then right rotation on current node
                node.left = self._rotate_left(node.left)
                # right rotation on current node
            return self._rotate_right(node)
        if balance < -1: # right heavy
            if self._get_balance_factor(node.right) > 0:
                # Right-Left case: Perform right rotation on right childand then left rotation on current node
                node.right = self._rotate_right(node.right)
                # left rotation on current node
            return self._rotate_left(node)
        return node
    
    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)
    def _insert_recursive(self, node, key):
        if node is None:
            return AVLNode(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        else:
            node.right = self._insert_recursive(node.right, key)
        return self._balance(node) # balance the tree and update height
    
    def search(self, key):
        return self._search_recursive(self.root, key)
    def _search_recursive(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)
        
    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)
    def _delete_recursive(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Case 1: Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Case 2: Node with two children, get the inorder successor (smallest in the right subtree)
            temp = self._find_min_value_node(node.right)
            node.key = temp.key
            # Delete the inorder successor
            node.right = self._delete_recursive(node.right, temp.key)
        return self._balance(node) # balance the tree and update height
    def _find_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def inorder(self):
        self._inorder(self.root)
        print() # for new line
    def _inorder(self, current_node):
        if current_node is not None:
            self._inorder(current_node.left)
            print(current_node.key, end=' ')
            self._inorder(current_node.right)
    def preorder(self):
        self._preorder(self.root)
        print() # for new line
    def _preorder(self, current_node):
        if current_node is not None:
            print(current_node.key, end=' ')
            self._preorder(current_node.left)
            self._preorder(current_node.right)
    def postorder(self):
        self._postorder(self.root)
        print() # for new line
    def _postorder(self, current_node):
        if current_node is not None:
            self._postorder(current_node.left)
            self._postorder(current_node.right)
            print(current_node.key, end=' ')
    def bft(self):
        result = []
        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            if current_node:
                result.append(current_node.key)
                queue.append(current_node.left)
                queue.append(current_node.right)
        print(result)

def ex1():
    avl_tree = AVLTree()
    keys = [10, 20, 30, 40, 50, 25]
    for key in keys:
        avl_tree.insert(key)
        print(f"After insertion of {key}, the bft is:")
        avl_tree.bft()
    print("Searching for 30:", avl_tree.search(30))
    print("Searching for 15:", avl_tree.search(15))
    avl_tree.delete(30)
    print("After deleting 30, the bft is:")
    avl_tree.bft()
    avl_tree.delete(10)
    print("After deleting 10, the bft is:")
    avl_tree.bft()
    print("Preorder traversal:")
    avl_tree.preorder()


def ex2():
    import random
    random_integers_python = [random.randint(0, 9999) for _ in range(1000)]

    import time
    startTime = time.time()

    tree = AVLTree()
    for current in random_integers_python:
        tree.insert(current)
    
    for i in range (0,100):
        tree.search(random_integers_python[random.randint(0, max(random_integers_python))])

    for i in range (0,100):
        tree.delete(random_integers_python[random.randint(0, max(random_integers_python))])
    


    endTime = time.time()
    runtime = endTime - startTime
    print("The runtime of the program is {runtime} seconds.")


ex2()