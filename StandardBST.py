class StandardBST:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def ainsert(self, value):
        # Left
        if value < self.value:
            if self.left is None:
                self.left = StandardBST(value)
            else:
                self.left.insert(value)
        # Right
        else:
            if self.right is None:
                self.right = StandardBST(value)
            else:
                self.right.insert(value)

    def insert(self, value):
        current = self
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = StandardBST(value)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = StandardBST(value)
                    break
                else:
                    current = current.right
