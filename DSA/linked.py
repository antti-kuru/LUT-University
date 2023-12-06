class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        #self.head is the first node in the linked list
        self.head = None
        self.len = 0

    
    def append (self, data):
        # let's create a new node
        newNode = Node(data)
        # We have to check whether the linked list is empty (head is null) or if it is not
        # then we add the current.next to point the newNode
        if (self.head is None):
            self.head = newNode
        else:
             # mark current Node with the following
            currentNode = self.head
            # then we have a loop where we go through each node 
            while (currentNode.next is not None):
                currentNode = currentNode.next
            # when the last node is found so that the currentNode.next points to Null, we break the loop and then initialize the currentNode.next to point out to newNode
            # which is now the tail node in this linked list
            currentNode.next = newNode
        self.len +=1
    

    def insert (self, data, i):
        newNode = Node(data)
        currentNode = self.head
        pos = 0
        # first we check if the wanted inserting index is 0
        if (pos == i):
            # if it is, then we have to check is the linked list empty or not
            if (self.head is None):
                self.head = newNode
            else:
            # if it nos empty, we need to put the inserted newNode.next to point towards current first item in linked list
                newNode.next = self.head
                # then we have to put that the first item in linked list is the newNode
                self.head = newNode
        else:
            # then we start going through the linked list whithin the lenght of the list
            while (currentNode is not None):
                # when the index is one more than the current position, we know we are on the right place to add the newNode
                if (pos + 1 == i):
                    # then we put the newNode.next to being the same as currentNode.next
                    newNode.next = currentNode.next
                    # then we put the currentNode.next to being the newNode
                    currentNode.next = newNode
                    break
                else:
                    # here we initialize the loop that we will start from the index 0 and increase it by 1 each round
                    pos = pos + 1
                    currentNode = currentNode.next
        self.len += 1



    def delete (self, i):
        pos = 0
        # firs we check if the index is out of range
        if (i < 0 or i >= self.len):
            return None
        
        deletedData = None
        
        # then we check if the wanted deleting index is 0
        if (pos == i):
            # if it is, then we check if the linked list is empty and then we do nothing
            if (self.head is None):
                return
            # if the list wasn't empty, then we delete the first item by making the head node being the next one
            deletedData = self.head.data
            self.head = self.head.next
        else:
            # let's mark the previous node as the self.head because we have to find the previous node before the one we delete
            previousNode = self.head
            # then we go through the linked list when position + 1 is less than index
            while (pos + 1 < i):
                previousNode = previousNode.next
                pos += 1
            # here we check that the next node after previous (the one we want to delete) isn't null
            if (previousNode.next is not None):
                # if the deleted node isn't null, then we take the data of the node to deletedData
                deletedData = previousNode.next.data
                # and then we put the pointer to the next node after the deleted node
                previousNode.next = previousNode.next.next
        
        self.len -= 1

        return deletedData
            


    def print(self):
        currentNode=self.head
        firstItem = True

        while (currentNode is not None):
            if not firstItem:
                print(" -> ", end="")
            print(str(currentNode.data), end="")
            firstItem = False
            currentNode = currentNode.next
        
        print("")



    def index (self, data):
        currentNode = self.head
        index = 0
        while (currentNode is not None):
            if (currentNode.data == data):
                break
            
            index += 1
            currentNode = currentNode.next
        else:
            return -1
        
        return index
        

    def swap (self, i, j):
        # checking invalid indexes
        if (i < 0 or i >= self.len or j < 0 or j >= self.len or i == j):
            return None
        pos = 0
        dataForIndexI = None
        dataForIndexJ = None
        currentNode = self.head
        # First we want to know the data values for index i and j
        while (currentNode is not None):
            if (pos == i):
                dataForIndexI = currentNode.data
            
            if (pos == j):
                dataForIndexJ = currentNode.data
            
            pos += 1
            currentNode = currentNode.next

        # then we go through the linked list again and this time swap the data values
        currentNode = self.head
        pos = 0
        while (currentNode is not None):
            if (pos == i):
                currentNode.data = dataForIndexJ
            
            if (pos == j):
                currentNode.data = dataForIndexI
            
            pos += 1
            currentNode = currentNode.next
                
    def isort(self):
        currentNode = self.head
        # we need two inside loops
        while (currentNode is not None): 
            minNode = currentNode
            followingNode = currentNode.next
            # here we compare the following node to the previous which is minNode
            # if the following is smaller than the previous, then we make the previous as the
            # found smaller one which is followingNode
            while (followingNode is not None):
                if (followingNode.data < minNode.data):
                    minNode = followingNode
                followingNode = followingNode.next
            # on outer loop we change the smallest node to current node
            currentNode.data, minNode.data = minNode.data, currentNode.data
            currentNode = currentNode.next  

if __name__ == "__main__":
    L = LinkedList()
    for num in (3, 5, 2, 7, 8, 10, 6):
        L.append(num)
    L.print()   # 3 -> 5 -> 2 -> 7 -> 8 -> 10 -> 6
    L.isort()
    L.print()   # 2 -> 3 -> 5 -> 6 -> 7 -> 8 -> 10