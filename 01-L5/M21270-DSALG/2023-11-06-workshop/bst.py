class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BST:
    def __init__(self):
        self.root = None
    def insert(self, key):
        if self.root is None: # Special case: if the BST is empty
            self.root = Node(key)
        else:
            self._insert(self.root, key)
    def _insert(self, current_node, key):
        if key < current_node.value:
            if current_node.left is None: # Stopping case - if thesubtree is empty, insert a new node to the empty space.
                current_node.left = Node(key)
            else:
                self._insert(current_node.left, key)
        elif key > current_node.value:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert(current_node.right, key)
        else:
            print("Key value already in the BST!")

    def search(self, key):
        return self._search(self.root, key)
    def _search(self, current_node, key):
        if current_node is None:
            return False
        if key == current_node.value:
            return True
        elif key < current_node.value:
            return self._search(current_node.left, key)
        else:
            return self._search(current_node.right, key)
        
    def delete(self, key):
        self.root = self._delete(self.root, key)
    def _delete(self, current_node, key):
        if current_node is None:
            return current_node
        if key < current_node.value:
            current_node.left = self._delete(current_node.left, key)
        elif key > current_node.value:
            current_node.right = self._delete(current_node.right, key)
        else:
            # Node with only one child or no child
            if current_node.left is None:
                temp = current_node.right
                current_node = None
                return temp
            elif current_node.right is None:
                temp = current_node.left
                current_node = None
                return temp
        # Node with two children: Get the inorder successor (smallest/leftmost node in the right subtree) to replace the value of thedeleted node
        temp = self._min_value_node(current_node.right)
        # Copy the inorder successor's content to this node
        current_node.value = temp.value
        # Delete the inorder successor
        current_node.right = self._delete(current_node.right, temp.value)
        return current_node
    def _min_value_node(self, node):
        # Locate the smallest/leftmost node in the right subtree
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
            print(current_node.value, end=' ')
            self._inorder(current_node.right)
    def preorder(self):
        self._preorder(self.root)
        print() # for new line
    def _preorder(self, current_node):
        if current_node is not None:
            print(current_node.value, end=' ')
            self._preorder(current_node.left)
            self._preorder(current_node.right)
    def postorder(self):
        self._postorder(self.root)
        print() # for new line
    def _postorder(self, current_node):
        if current_node is not None:
            self._postorder(current_node.left)
            self._postorder(current_node.right)
            print(current_node.value, end=' ')

    def bft(self):
        result = []
        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            if current_node:
                result.append(current_node.value)
                queue.append(current_node.left)
                queue.append(current_node.right)
                print(result)

    def iterative_preorder(self):
        if not self.root:
            return []
        stack, output = [self.root], []
        while stack:
            node = stack.pop()
            if node:
                output.append(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        print(output)

    def iterative_inorder(self):
        stack, output = [], []
        current = self.root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            output.append(current.value)
            current = current.right
        print(output)

    def iterative_postorder(self):
        if not self.root:
            return []
        stack1, stack2 = [self.root], []
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        output = []
        while stack2:
            node = stack2.pop()
            output.append(node.value)
        print(output)

    def countNodes(self):
        stack = []
        count = 0
        current = self.root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            count+=1
            current = current.right
        print(count)


bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)
print("Inorder traversal:")
bst.inorder()
print("Preorder traversal:")
bst.preorder()
print("Postorder traversal:")
bst.postorder()
print("Breadth-first traversal:")
bst.bft()
print("Is 40 in the tree?", bst.search(40))
print("Is 100 in the tree?", bst.search(100))
# print("Deleting 20")
# bst.delete(20)
# print("Inorder traversal after deleting 20:")
# bst.inorder()
print("============================")
print("Iterative inorder traversal:")
bst.iterative_inorder()
print("Iterative preorder traversal:")
bst.iterative_preorder()
print("Iterative postorder traversal:")
bst.iterative_postorder()
print("Count:")
bst.countNodes()