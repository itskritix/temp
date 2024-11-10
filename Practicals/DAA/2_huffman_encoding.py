#Write a program to implement Huffman Encoding using a greedy strategy

import heapq
from collections import Counter

class Node:         # Node class to represent each character and its frequency
    def __init__(self, ch, freq):
        self.ch = ch
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):        # This allows the heap to compare nodes by frequency
        return self.freq < other.freq


def build_huffman_codes(root, code, code_table):
    if root is None:                            # Function to build the Huffman codes
        return

    # If it's a leaf node, add its code to the code table
    if root.left is None and root.right is None:
        code_table[root.ch] = code
        return

    # Traverse left with "0" and right with "1"
    build_huffman_codes(root.left, code + '0', code_table)
    build_huffman_codes(root.right, code + '1', code_table)

def huffman_encoding(text):
    freq = Counter(text)

    # Step 2: Create a priority queue of nodes
    heap = [Node(ch, freq) for ch, freq in freq.items()]
    heapq.heapify(heap)     #heapify is a function in Python's heapq module that converts a list into a binary heap

    # Step 3: Build the Huffman tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    # Step 4: Generate Huffman codes
    root = heapq.heappop(heap)
    huffman_code = {}
    build_huffman_codes(root, '', huffman_code)

    return huffman_code

text = input("Enter text to encode: ")
huffman_code = huffman_encoding(text)

print("\nHuffman Codes:")
for ch, code in huffman_code.items():
    print("'" + str(ch) + "': " + str(code))

