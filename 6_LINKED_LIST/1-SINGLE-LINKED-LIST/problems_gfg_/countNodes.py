# Definition of Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Definition of LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
    
    # Function to add a node at the end of the list (for testing)
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    # Function to count the number of nodes
    def getCount(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

# Test the solution
if __name__ == "__main__":
    # Create and populate the first linked list: 1->2->3->4->5
    llist1 = LinkedList()
    for data in [1, 2, 3, 4, 5]:
        llist1.append(data)
    print("Length of first linked list:", llist1.getCount())  # Output: 5
    
    # Create and populate the second linked list: 2->4->6->7->5->1->0
    llist2 = LinkedList()
    for data in [2, 4, 6, 7, 5, 1, 0]:
        llist2.append(data)
    print("Length of second linked list:", llist2.getCount())  # Output: 7