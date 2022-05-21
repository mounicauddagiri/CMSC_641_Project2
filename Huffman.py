import heapq
from msilib.schema import Binary
from xml.sax.handler import feature_external_ges


class BinaryTree:
    def __init__(self,value,frequency):
        self.value = value
        self.frequency = frequency
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.frequency < other.frequency

    def __eq__(self, other) :
        return self.frequency == other.frequency

class HuffmanCode:
    code = {}
    reversecode = {}

    def get_frequency(text):
        frequ_dict = {}
        for char in text:
            if char not in frequ_dict:
                frequ_dict[char] = 0
            frequ_dict[char] +=1
        return frequ_dict 

    def build_heap(freq_dict):
        heap = []
        for key in freq_dict:
            frequency = freq_dict[key]
            btree_node = BinaryTree(key, frequency)
            heapq.heappush(heap,btree_node)
        return heap

    def build_Binarytree(heap):
        while len(heap) > 1:
            btree_node1 = heapq.heappop(heap)
            btree_node2 = heapq.heappop(heap)
            total_frequency = btree_node1.frequency + btree_node2.frequency
            tempnode = BinaryTree(None,total_frequency)
            tempnode.left = btree_node1
            tempnode.right = btree_node2
            heapq.heappush(heap,tempnode)
        return heap
    
    def get_code(self, root, current_bits):
        if root is None:
            return
        if root.value is not None:
            self.code[root.value] = current_bits
            self.reversecode[current_bits] = root.value
            return self.code, self.reversecode
        self.get_code(self, root.left, current_bits+'0')
        self.get_code(self, root.right, current_bits+'1')
        
        return self.code,self.reversecode

    def generate_tree_code(self,heap):
        root = heapq.heappop(heap)
        code, reverse = self.get_code(self, root, '')
        # print('CODE ', code)
        # print(' REVERSE', reverse)
        return code, reverse