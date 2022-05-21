# CMSC_641_Project2

Compressing a text file using Huffman algorithm.

Huffman Algorithm:
Huffman coding is a lossless data compression algorithm. The idea is to assign variable-length codes to input characters, lengths of the assigned codes are based on the frequencies of corresponding characters. The most frequent character gets the smallest code and the least frequent character gets the largest code.

How to run the code:
 1. Download all the files in to your local sandbox.(Can use Visual Studio Code).
 2. Create a new test.txt file in the same directory.
 3. Run the main.py file.
 4. The code generates a compressed file along with the de-compressed file.
 5. We can verify the code by comparing the original text file with the de-compressed file.

Methodology
- The text file is read and the frequency of each unique character is calculated. 
- A leaf node for each character is created and a minimum heap of all leaf ndoes is built.
- Then we extract the two nodes with minimum frequency from the min heap.
- An internal node with frequency equal to the sum of the two node frequencies is created by making first node as left child and second node as right child. This tree is appended to the heap.
- The above two steps are repeated until the heap contains only one node. In this way, the tree is complete and a binary code is generated.
- The code generated is encoded and padded. It returns an byte array.
- The bytes array is now stored in a new compressed bin file.
- File de-compression is performed by first removing the padding.
- Then the text is de-coded according to the reversed code generated and the result is saved in another text file.
