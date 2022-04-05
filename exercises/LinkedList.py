class LinkedList:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def append(self, new_node): 
        node = self
        while node.next:
            node = node.next
        node.next = new_node

    def get_on_index(self, n):
        count = 0
        node = self
        while node.next:
            if count == n:
                return node.value
            count +=1
            node = node.next

    def remove_node(self, n):
        temp = self.node 
        count = 0 
        while(temp is not None):
            if temp.value == n:
                break
            prev = temp
            temp = temp.next

    



ama = LinkedList("Ama")
ama.append(LinkedList("javi"))
ama.append(LinkedList("julieta"))
ama.append(LinkedList("anto"))
ama.append(LinkedList("mariela"))

print(ama.get_on_index(0))

def print_linked_list(node):
    while node.next:
        print(node.value)
        node = node.next
    print(node.value)



# print_linked_list(ama)

