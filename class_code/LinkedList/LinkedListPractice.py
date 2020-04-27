class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        if self.head is None:
            self.head = Node(value)
            return

        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
        pass
    
    def append(self, value):
        """ Append a value to the end of the list. """
        if self.head is None:
            self.head = Node(value)
            return
        
        node = self.head
        while node.next:
            node = node.next
        
        new_node = Node(value)
        node.next = new_node
        
        pass
    
    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        
        if self.head is None:
            return
        
        node = self.head
        while node.next:
            if node.value is value:
                return node
            node = node.next
        
        pass
    
    def remove(self, value):
        """ Remove first occurrence of value. """
        
        if self.head is None:
            return
        
        if self.head.value is value:
            self.head = self.head.next
            return
        
        node = self.head
        while node.next:
            if node.next.value is value:
                prev = node
                curr = node.next
                prev.next = curr.next
                curr.next = None
                return
            node = node.next
        
        pass
    
    def pop(self):
        """ Return the first node's value and remove it from the list. """
        
        if self.head is None:
            return

        node_out = self.head
        self.head = self.head.next
        return node_out.value
        pass
    
    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """
        node = self.head
        if node is None:
            self.head = Node(value)
            return

        if pos is 0:
            new_node = Node(value)
            new_node.next = node
            self.head = new_node
            return
        
        count = 0
        while node.next:
            if count == pos-1:
                break
            node = node.next
            count += 1

        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node

        pass
    
    def size(self):
        """ Return the size or length of the linked list. """
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count
        pass
    
    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


## Test your implementation here

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"
    
# Test append
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

# Test insert 
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

# Test size
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"