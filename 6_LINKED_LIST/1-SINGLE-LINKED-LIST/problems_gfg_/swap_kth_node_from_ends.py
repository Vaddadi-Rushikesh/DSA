# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Solution class
class Solution:
    def swapkthnode(self, head, num, k):
        if not head or k <= 0 or k > num:
            return head
        
        # If k is equal to num, swap head and last node
        if k == num:
            # Find the second-to-last node
            prev = None
            curr = head
            while curr.next:
                prev = curr
                curr = curr.next
            # Swap head and last node
            prev.next = head
            head.next, curr.next = curr.next, head
            return curr
        
        # Step 1: Find length of the list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        # If k > length/2, adjust k to find from end
        if k > length // 2:
            k = length - k + 1
        
        # Step 2: Find the kth node from the beginning
        curr = head
        prev_kth_start = None
        for i in range(k - 1):
            prev_kth_start = curr
            curr = curr.next
        kth_start = curr
        
        # Step 3: Find the kth node from the end (which is (length - k + 1)th from start)
        curr = head
        prev_kth_end = None
        for i in range(length - k):
            prev_kth_end = curr
            curr = curr.next
        kth_end = curr
        
        # Step 4: Swap the nodes
        if prev_kth_start:
            prev_kth_start.next = kth_end
        else:
            head = kth_end
        
        if prev_kth_end:
            prev_kth_end.next = kth_start
        else:
            head = kth_start
        
        # Swap the next pointers of kth_start and kth_end
        kth_start.next, kth_end.next = kth_end.next, kth_start.next
        
        # Adjust prev pointers if needed (for doubly linked list, but here it's singly)
        return head

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
    # Test Case 1: 1->2->3->4, k = 1
    arr1 = [1, 2, 3, 4]
    head1 = createLinkedList(arr1)
    sol = Solution()
    head1 = sol.swapkthnode(head1, len(arr1), 1)
    print("After swapping k=1:")
    printList(head1)  # Expected: 4->2->3->1 (true)

    # Test Case 2: 1->2->3->4->5, k = 7
    arr2 = [1, 2, 3, 4, 5]
    head2 = createLinkedList(arr2)
    head2 = sol.swapkthnode(head2, len(arr2), 7)
    print("After swapping k=7:")
    printList(head2)  # Expected: 1->2->3->4->5 (no change, true)