class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove_beginning(self):
        if self.head is None:
            return None  
        removed_data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None  
        return removed_data


    def remove_at_end(self):
        if self.head is None:
            return None  
        if self.head == self.tail:
            removed_data = self.head.data
            self.head = self.tail = None
            return removed_data
    
        current = self.head
        while current.next != self.tail:
            current = current.next
        removed_data = self.tail.data
        current.next = None
        self.tail = current
        return removed_data

    def remove_at(self, data):
        if self.head is None:
            return None
        if self.head.data == data:
            return self.remove_beginning()
        current = self.head
        while current.next:
            if current.next.data == data:
                removed_data = current.next.data
                current.next = current.next.next
                if current.next is None:
                    self.tail = current  
                return removed_data
            current = current.next
        return None  
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
