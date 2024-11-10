import heapq
from collections import Counter
from typing import Dict, Optional

class HuffmanNode:
    """Node class for Huffman tree"""
    def __init__(self, char: Optional[str], freq: int):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other: 'HuffmanNode') -> bool:
        return self.freq < other.freq

class HuffmanCoding:
    """Class to handle Huffman encoding and decoding operations"""
    
    def __init__(self):
        self.heap = []
        self.codes = {}
        self.reverse_codes = {}
        
    def _build_heap(self, text: str) -> None:
        """Build priority queue from character frequencies"""
        frequency = Counter(text)
        for char, freq in frequency.items():
            node = HuffmanNode(char, freq)
            heapq.heappush(self.heap, node)
            
    def _build_tree(self) -> Optional[HuffmanNode]:
        """Build Huffman tree from priority queue"""
        while len(self.heap) > 1:
            left = heapq.heappop(self.heap)
            right = heapq.heappop(self.heap)
            
            # Create internal node with combined frequency
            internal = HuffmanNode(None, left.freq + right.freq)
            internal.left = left
            internal.right = right
            
            heapq.heappush(self.heap, internal)
            
        return heapq.heappop(self.heap) if self.heap else None
            
    def _build_codes_helper(self, root: Optional[HuffmanNode], code: str) -> None:
        """Recursively build Huffman codes"""
        if not root:
            return
            
        if root.char is not None:
            self.codes[root.char] = code
            self.reverse_codes[code] = root.char
            return
            
        self._build_codes_helper(root.left, code + "0")
        self._build_codes_helper(root.right, code + "1")
        
    def _build_codes(self, root: HuffmanNode) -> None:
        """Initialize building of Huffman codes"""
        self.codes = {}
        self.reverse_codes = {}
        self._build_codes_helper(root, "")
        
    def compress(self, text: str) -> tuple[str, Dict[str, str]]:
        """
        Compress the input text using Huffman coding
        
        Args:
            text: Input text to compress
            
        Returns:
            tuple: (compressed_text, codes_dictionary)
        """
        if not text:
            return "", {}
            
        # Build Huffman tree
        self._build_heap(text)
        root = self._build_tree()
        self._build_codes(root)
        
        # Generate compressed text
        compressed = "".join(self.codes[char] for char in text)
        
        return compressed, self.codes
        
    def decompress(self, compressed_text: str, codes: Dict[str, str]) -> str:
        """
        Decompress the compressed text using Huffman codes
        
        Args:
            compressed_text: Binary string of compressed text
            codes: Dictionary of Huffman codes
            
        Returns:
            str: Decompressed original text
        """
        if not compressed_text:
            return ""
            
        # Build reverse lookup for codes
        self.reverse_codes = {code: char for char, code in codes.items()}
        
        # Decompress text
        current_code = ""
        decompressed = ""
        
        for bit in compressed_text:
            current_code += bit
            if current_code in self.reverse_codes:
                decompressed += self.reverse_codes[current_code]
                current_code = ""
                
        return decompressed

def main():
    """Main function to demonstrate Huffman coding"""
    try:
        # Get input text
        text = input("Enter text to encode: ")
        if not text:
            print("Error: Empty input")
            return
            
        # Create Huffman coding instance
        huffman = HuffmanCoding()
        
        # Compress text
        compressed, codes = huffman.compress(text)
        
        # Calculate compression ratio
        original_size = len(text) * 8  # Assuming 8 bits per character
        compressed_size = len(compressed)
        compression_ratio = (original_size - compressed_size) / original_size * 100
        
        # Print results
        print("\nHuffman Codes:")
        for char, code in sorted(codes.items()):
            print(f"'{char}': {code}")
            
        print("\nCompressed binary string:")
        print(compressed)
        
        print(f"\nCompression ratio: {compression_ratio:.2f}%")
        
        # Verify compression by decompressing
        decompressed = huffman.decompress(compressed, codes)
        print("\nVerification - Decompressed text:")
        print(decompressed)
        print(f"Original text matches decompressed text: {text == decompressed}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()