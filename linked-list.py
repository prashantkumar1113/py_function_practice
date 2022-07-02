class Node:
    def __init__(self, data, reference=None):
        self.data = data
        self.reference = reference

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def print_linked_list(self):
        if self.head is None:
            print("The linked list is empty")
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.data)
                current_node = current_node.reference

    def add_to_start(self, data):
        new_node = Node(data)
        new_node.reference = self.head
        self.head = new_node

    def add_item(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.reference is not None:
                print(current_node.reference)
                current_node = current_node.reference
            current_node.reference = new_node
            
    def add_item_after(self, data, node_data):
        new_node = Node(data)
        if self.head is None:
            print("ValueError")
        else:
            current_node = self.head
            while current_node is not None:
                if current_node.data == node_data:
                    new_node.reference = current_node.reference
                    current_node.reference = new_node
                    return
            print("ValueError")

    def remove_item(self, data):
        if self.head is None:
            print("ValueError")
        elif self.head.data == data:
            self.head = self.head.reference
            return
        else:
            current_node = self.head
            prev_node = None
            while current_node is not None:
                if current_node.data == data:
                    prev_node.reference = current_node.reference
                    return
                prev_node = current_node
                current_node = current_node.reference
            print("ValueError")

# node1 = Node(5)
# node2 = Node(11)
# node1.reference = node2
# print(node1.reference)
linked_list1 = LinkedList()
# linked_list1.print_linked_list()
linked_list1.add_item(82)
linked_list1.add_item(15)
linked_list1.add_item(21)
linked_list1.add_to_start(55)
linked_list1.add_item_after(23,55)
linked_list1.print_linked_list()
print("")
linked_list1.remove_item(15)
linked_list1.remove_item(55)
linked_list1.print_linked_list()
