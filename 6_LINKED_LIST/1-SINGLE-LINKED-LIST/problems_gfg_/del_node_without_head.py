# Node class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None

# Solution class
class Solution:
    # Function to delete a node without head pointer
    def deleteNode(self, node):
        # Check if node or node.next is None (though guaranteed not last node)
        if not node or not node.next:
            return
        
        # Copy data from next node to current node
        node.data = node.next.data
        
        # Update the next pointer to skip the next node
        node.next = node.next.next

# Helper function to create a linked list
def createLinkedList(arr):
    if not arr:
        return None
    head = Node(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = Node(arr[i])
        curr = curr.next
    return head

# Helper function to print the list
def printList(head):
    curr = head
    while curr:
        print(curr.data, end=" -> " if curr.next else "\n")
        curr = curr.next

# Test the solution
if __name__ == "__main__":
    # Test Case: 1 -> 2, del_node = node with value 1
    head = createLinkedList([1, 2])
    curr = head
    while curr and curr.data != 1:
        curr = curr.next
    del_node = curr
    
    sol = Solution()
    sol.deleteNode(del_node)
    print("After deleting node with value 1:")
    printList(head)  # Expected: 2