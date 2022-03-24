class Heap(object):
    """
      Arr[(i-1)/2] Returns the parent node
      Arr[(2*i)+1] Returns the left child node
      Arr[(2*i)+2] Returns the right child node
    """
    
    def __init__(self):
        self.nodes = []

    def insert(self, elem):
        self.nodes.append(elem)
        self.__swap_up(len(self.nodes)-1)

    def __swap_up(self, index):
        
        parent_node_index = (index-1)//2

        if parent_node_index < 0:
          return

        if self.nodes[parent_node_index] < self.nodes[index]:
          self.nodes[parent_node_index], self.nodes[index] = self.nodes[index], self.nodes[parent_node_index]
          return self.__swap_up(parent_node_index)

    def __swap_down(self, index):
        
        n = len(self.nodes)
        largest = index       # Initialize largest as root
        l = 2 * index + 1     # left =  2*i + 1
        r = 2 * index + 2     # right = 2*i + 2
    
        # See if left child of root exists and is
        # greater than root
        if l < n and self.nodes[largest] < self.nodes[l]:
            largest = l
    
        # See if right child of root exists and is
        # greater than root
        if r < n and self.nodes[largest] < self.nodes[r]:
            largest = r
    
        # Change root, if needed
        if largest != index:
            self.nodes[index], self.nodes[largest] = self.nodes[largest], self.nodes[index]  # swap
            self.__swap_down(largest)

    def get(self):
        if not self.nodes:
          return None

        last_index = len(self.nodes) - 1
        root = self.nodes[0]

        self.nodes[0] , self.nodes[last_index] = self.nodes[last_index], self.nodes[0]
        self.nodes.pop(last_index)
        self.__swap_down(0)

        return root


heap = Heap()

l = [2,4,5,3,2,1,5,5,7,7,8]
for x in l:
    heap.insert(x)

sorted = []
elem = heap.get()
while elem:
    sorted.append(elem)
    elem = heap.get()

print(sorted)
