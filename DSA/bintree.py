class Node:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.mirrorCount = 0

    def insert(self, key):
        if (self.mirrorCount % 2 == 1 or self.mirrorCount == 1):
            self.root = self.__mirrorinserthelp(self.root,key)
        else:            
            self.root = self.__inserthelp(self.root, key)
    
    def __inserthelp(self, node, key):
        if node == None:
            node = Node(key)
        
        if (node.key > key):
            node.left = self.__inserthelp(node.left, key)
        elif (node.key < key):
            node.right = self.__inserthelp(node.right, key)
        return node
    
    def __mirrorinserthelp(self, node, key):
        if node == None:
            node = Node(key)
        
        if (node.key > key):
            node.right = self.__mirrorinserthelp(node.right, key)
        elif (node.key < key):
            node.left = self.__mirrorinserthelp(node.left, key)
        return node       
    
    def search (self, key):
        if (self.mirrorCount % 2 == 1 or self.mirrorCount == 1):
            return self.__mirrorsearchhelp(self.root, key)  
        else:
            return self.__searchhelp(self.root, key)
    
    def __searchhelp(self, node, key):
        if node == None:
            return False
        elif node.key > key:
            return self.__searchhelp(node.left, key)
        elif node.key < key:
            return self.__searchhelp(node.right, key)
        else:
            return True
    
    def __mirrorsearchhelp(self, node, key):
        if node == None:
            return False
        elif node.key > key:
            return self.__mirrorsearchhelp(node.right, key)
        elif node.key < key:
            return self.__mirrorsearchhelp(node.left, key)
        else:
            return True


    def preorder(self):
        return self.__preorderhelp(self.root)
    
    def __preorderhelp(self, node):
        if (node is not None):
            print(node.key, end='')
            self.__preorderhelp(node.left)
            self.__preorderhelp(node.right)

    def __getmax(self, node):
        if node.right == None:
            return node.key
        else:
            return self.__getmax(node.right)
        
    def __mirrorgetmax(self, node):
        if (node.left == None):
            return node.key
        else:
            return self.__mirrorgetmax(node.left)
    
    def __removemax(self,node):
        if node.right == None:
            return node.left
        node.right = self.__removemax(node.right)
        return node

    def __mirrorremovemax(self, node):
        if (node.left == None):
            return node.right
        node.left = self.__mirrorremovemax(node.left)
        return node
        
    def remove(self, key):
        if (self.mirrorCount % 2 == 1 or self.mirrorCount == 1):
            self.root = self.__mirrorremovehelp(self.root, key)  
        else:
            self.root = self.__removehelp(self.root, key)
    
    def __removehelp(self, node, key):
        if node == None:
            return None
        elif (node.key > key):
            node.left = self.__removehelp(node.left, key)
        elif (node.key < key):
            node.right = self.__removehelp(node.right, key)
        else:
            if (node.left) == None:
                return node.right
            elif (node.right) == None:
                return node.left
            else:
                node.key = self.__getmax(node.left)
                node.left = self.__removemax(node.left)

        return node
    
    def __mirrorremovehelp(self, node, key):
        if node == None:
            return None
        elif (node.key > key):
            node.right = self.__mirrorremovehelp(node.right, key)
        elif (node.key < key):
            node.left = self.__mirrorremovehelp(node.left, key)
        else:
            if (node.left) == None:
                return node.right
            elif (node.right) == None:
                return node.left
            else:
                node.key = self.__mirrorgetmax(node.right)
                node.right = self.__mirrorremovemax(node.right)

        return node
    


    def postorder(self):
        return self.__postorderhelp(self.root)
    
    def __postorderhelp(self, node):
        if (node is None):
            return
        self.__postorderhelp(node.left)
        self.__postorderhelp(node.right)
        print(node.key, end='')

    def inorder(self):
        return self.__inorderhelp(self.root) 
    
    def __inorderhelp(self, node):
        if (node is None):
            return
        self.__inorderhelp(node.left)
        print(node.key, end='')
        self.__inorderhelp(node.right)


    def breadthfirst(self, root=None):
        
        if (root is None):
            root=self.root
        else:
            root=root
        
        toVisit = [root]
        while toVisit:
            current = toVisit.pop(0)
            print(current.key, end='')
            if current.left:
                toVisit.append(current.left)
            if current.right:
                toVisit.append(current.right)


    def mirror(self):
        self.mirrorCount +=1
        return self.__mirrorhelp(self.root)
    
    def __mirrorhelp(self, node):
        if (node is None):
            return
        current = node

        self.__mirrorhelp(node.left)
        self.__mirrorhelp(node.right)
        current = node.left
        node.left = node.right
        node.right = current


if __name__ == "__main__":
    Tree = BST()
    keys = [5, 3, 8, 7, 9, 6, 4, 1, 2]

    for key in keys:
        Tree.insert(key)

    Tree.preorder()         # 5 1 3 2 4 9 7 6
    #Tree.mirror()
    #Tree.preorder()         # 5 9 7 6 1 3 4 2
    #Tree.insert(8)
    
    #Tree.remove(3)
    #print(Tree.search(2))   # True
    #Tree.preorder()         # 5 9 7 8 6 1 2 4
    #Tree.mirror()
    #Tree.preorder()         # 5 1 2 4 9 7 6 8