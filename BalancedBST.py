class BalancedBST:
    
    def __init__(self, value, c):
        self.left = None
        self.right = None
        self.value = value
        self.size = 1
        self.c = c

    def insert(self, value):
        # Left
        if value < self.value:
            if self.left is None:
                self.left = BalancedBST(value, self.c)
            else:
                self.left.insert(value)
        # Right
        else:
            if self.right is None:
                self.right = BalancedBST(value, self.c)
            else:
                self.right.insert(value)

        #Size = 1 + left.size + right.size
        self.size = 1 + (self.left.size if self.left else 0) + (self.right.size if self.right else 0)

        left_size = self.left.size if self.left else 0
        right_size = self.right.size if self.right else 0
        
        #Rebalance condition
        if left_size > self.c * self.size or right_size > self.c * self.size:
            self.rebalance()

    def rebalance(self):
        # Step 1: Extract all keys in sorted order
        keys = []
        self.in_order_traversal(self, keys)
    
        # Step 2: Build a balanced BST from the sorted keys
        new_root = self.build_balanced_tree(keys, self.c)
    
        # Step 3: Update the current node to match the new balanced subtree
        self.value = new_root.value
        self.left = new_root.left
        self.right = new_root.right
        self.size = new_root.size
    
    
    def in_order_traversal(self, node, keys):
        if node is None:
            return
        self.in_order_traversal(node.left, keys)
        keys.append(node.value)
        self.in_order_traversal(node.right, keys)
    
    
    def build_balanced_tree(self, keys, c):
        if not keys:
            return None
        mid = len(keys) // 2
        root = BalancedBST(keys[mid], c)
        root.left = self.build_balanced_tree(keys[:mid], c)
        root.right = self.build_balanced_tree(keys[mid + 1:], c)
        root.size = 1 + (root.left.size if root.left else 0) + (root.right.size if root.right else 0)
        return root


   


def main():
    tree = BalancedBST(10,0.7)
    tree.insert(5)
    tree.insert(4)
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(22)
    tree.insert(11)
    tree.insert(12)



if __name__ == "__main__":
    main()
