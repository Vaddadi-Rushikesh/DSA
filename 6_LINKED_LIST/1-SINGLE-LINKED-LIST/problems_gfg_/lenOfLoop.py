# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None

# Solution class
class Solution:
    # Function to find the length of a loop in the linked list
    def countNodesinLoop(self, head):
        if not head or not head.next:  # if head is None or head.next is None:
            return 0
        
        # Step 1: Detect loop using Floyd's Cycle-Finding Algorithm
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next  # Moves one step
            fast = fast.next.next  # Moves two steps
            
            if slow == fast:  # Loop detected
                # Step 2: Count nodes in the loop
                count = 1
                temp = slow.next
                while temp != slow:
                    count += 1
                    temp = temp.next
                return count
        
        # No loop found
        return 0

# Helper function to create and test the linked list
def createLinkedList(arr, pos):
    if not arr:
        return None
    
    # Create nodes
    head = Node(arr[0])
    current = head
    loop_node = None
    
    for i in range(1, len(arr)):
        current.next = Node(arr[i])
        current = current.next
        if i == pos:
            loop_node = current
    
    # Create loop if pos is valid
    if loop_node:
        current.next = loop_node
    
    return head

# Test the solution
if __name__ == "__main__":
    # Test Case 1: 1->2->3->4->5, c=2 (loop starts at node 4)
    arr1 = [1, 2, 3, 4, 5]
    pos1 = 2  # Loop connects 5 back to 3
    head1 = createLinkedList(arr1, pos1)
    sol = Solution()
    print("Length of loop:", sol.countNodesinLoop(head1))  # Output: 4
    
    # Test Case 2: No loop
    arr2 = [1, 2, 3, 4, 5]
    pos2 = -1  # No loop
    head2 = createLinkedList(arr2, pos2)
    print("Length of loop:", sol.countNodesinLoop(head2))  # Output: 0