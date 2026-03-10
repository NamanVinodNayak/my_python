class Node:
    def __init__(self, val=None) -> None:
        self.val = val      # Stores the value
        self.next = None    # Pointer to the next node (initially None)
        
class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None  # Points to the first node (head of the list)
        
    def append(self, data):
        new_node = Node(data)  # Create a new node
        if not self.head:      # If list is empty, make new node the head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:  # Traverse to the end
                current = current.next
            current.next = new_node          # Link last node to new node
            
    def traverse(self):
        if not self.head:
            print("SLL is empty")
        else:
            current = self.head
            while current is not None:  # Move from node to node
                print(current.val, end=" ")  # Print current node value
                current = current.next
            print()  # For newline
            
            
    def delete(self, val):
        temp = self.head
        
        # If head contains the value
        if temp and temp.val == val:
            self.head = temp.next
            return
        
        prev = None
        found = False
        
        # Search for the node to delete
        while temp is not None:
            if temp.val == val:
                found = True
                break
            prev = temp
            temp = temp.next
        
        # If node is found, unlink it
        if found:
            prev.next = temp.next
        else:
            print("Node not found")
            
ssl = SinglyLinkedList()
ssl.append(10)
ssl.append(20)
ssl.append(30)
ssl.append(40)
ssl.append(50)
ssl.traverse()
ssl.delete(30)
ssl.traverse()