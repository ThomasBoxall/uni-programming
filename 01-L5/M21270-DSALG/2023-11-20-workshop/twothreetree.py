import random

class TwoThreeNode:
    def __init__(self, key):
        self.key1 = key
        self.key2 = None
        self.left = None
        self.middle = None
        self.right = None
    def isLeaf(self):
        return self.left is None and self.middle is None and self.right is None
    def isFull(self):
        return self.key2 is not None
    def hasKey(self, key):
        if (self.key1 == key) or (self.key2 is not None and self.key2 ==key):
            return True
        else:
            return False
    def getChild(self, key):
        if key < self.key1:
            return self.left
        elif self.key2 is None:
            return self.middle
        elif key < self.key2:
            return self.middle
        else:
            return self.right
        
class TwoThreeTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TwoThreeNode(key)
        else:
            pKey, pRef = self._insert(self.root, key)
            if pKey is not None: # new root created
                newnode = TwoThreeNode(pKey)
                newnode.left = self.root
                newnode.middle = pRef
                self.root = newnode
    
    def _insert(self, node, key):
        if node.hasKey(key): # duplicate key
            return None, None
        elif node.isLeaf(): # insert only to leaf node
            return self._addtoNode(node, key, None)
        else:
            child = node.getChild(key) # get reference to the child/subtreefor further operations
            pKey, pRef = self._insert(child, key)
            if pKey is None:
                return None, None
            else:
                return self._addtoNode(node, pKey, pRef)
            
    def _addtoNode(self, node, key, pRef):
        if node.isFull(): # insertion into a full node requires split
            return self._splitNode(node, key, pRef)
        else: # if not full, then insert into the node
            if key < node.key1:
                node.key2 = node.key1
                node.key1 = key
                if pRef is not None:
                    node.right = node.middle
                    node.middle = pRef
            else:
                node.key2 = key
                if pRef is not None:
                    node.right = pRef
            return None, None
        
    def _splitNode(self, node, key, pRef):
        newnode = TwoThreeNode(None)
        if key < node.key1: # key,key1,key2 -> key1 promoted to parent
            pKey = node.key1
            node.key1 = key
            newnode.key1 = node.key2
            if pRef is not None:
                newnode.left = node.middle
                newnode.middle = node.right
                node.middle = pRef
        elif key < node.key2: # key1,key,key2 -> key promoted to parent
            pKey = key
            newnode.key1 = node.key2
            if pRef is not None:
                newnode.left = pRef
                newnode.middle = node.right
        else: # key1,key2,key -> key2 promoted to parent
            pKey = node.key2
            newnode.key1 = key
            if pRef is not None:
                newnode.left = node.right
                newnode.middle = pRef
        node.key2 = None # only 1 key remains
        return pKey, newnode
    
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        elif key in [node.key1, node.key2]:
            return True
        elif key < node.key1:
            return self._search(node.left, key)
        elif not node.key2: # 2-node, larger than the only key
            return self._search(node.middle, key)
        elif key < node.key2: # 3-node
            return self._search(node.middle, key)
        else:
            return self._search(node.right, key)
    
    def bft(self):
        result = []
        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            if current_node:
                result.append([current_node.key1, current_node.key2] if
                current_node.key2 else [current_node.key1])
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.middle:
                    queue.append(current_node.middle)
                if current_node.right:
                    queue.append(current_node.right)
        print(result)
    
    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node.left is not None: # Visit left child
            self._inorder(node.left)
        print(node.key1, end=' , ') # Visit key1
        if node.middle is not None: # Visit middle child
            self._inorder(node.middle)
        # If there's a second key, visit it and then the right child
        if node.key2 is not None:
            print(node.key2, end=' , ')
            if node.right is not None:
                self._inorder(node.right)


x = 20
unique_rand_int = random.sample(range(1, x+1), x)
tree = TwoThreeTree()
for i in unique_rand_int:
    tree.insert(i)
    print(f"\nAfter insertion of {i}, the bft of the tree is:")
    tree.bft()
print("\nSearch for -1, Found? ", tree.search(-1))
print("Search for 10, Found? ", tree.search(10))
print("Search for 20, Found? ", tree.search(20))
print("Search for 21, Found? ", tree.search(21))
tree.inorder()
print("inorder traversal done.")