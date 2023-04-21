class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None

class LinkedList:
	
    def __init__(self, value):
        new_node  = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(f"{temp.value} -> ", end='')
            temp = temp.next
        print("None")

    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True


    def prepend(self, value):
        new_link = Node(value)
        if self.length == 0:
            self.head = new_link
            self.tail = new_link
        else:
            new_link.next = self.head
            self.head = new_link
        self.length += 1
        return True

    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        #return temp.value
        return temp

    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    
    def insert(self, index, value):
        
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        return new_node.value


if __name__ == "__main__":
    my_linked_list = LinkedList(2)
    my_linked_list.append(8)
    my_linked_list.append(9)
    my_linked_list.prepend(1)
    my_linked_list.set_value(3, 10)
    my_linked_list.insert(2, 7)
    my_linked_list.print_list()

