from Huffman import HuffmanCode
import os

def init():
    code = {}
    reverse = {}

class Compress:
    def encoded(text,code):
        encoded_text = ''
        for char in text:
            encoded_text += code[char]
            
        return encoded_text 

    def padded_text(encoded_text):
        padding = 8 - (len(encoded_text)%8)
        for i in range(padding):
            encoded_text += '0'
        padded_info = "{0:08b}".format(padding)
        padded_encoded_text = padded_info + encoded_text

        array = []
        for i in range(0,len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i+8]
            array.append(int(byte,2))
        return array

    def __Compression__(self, path):
        filename, file_extension = os.path.splitext(path)
        output_path = filename + '_compressed'+'.bin'
        with open (path, 'r+') as file, open (output_path, 'wb') as output:
            text = file.read()
            text = text.rstrip()

            frequency_dict = HuffmanCode.get_frequency(text)
            print('Frequency ' , frequency_dict)

            b_heap = HuffmanCode.build_heap(frequency_dict)
            b_Tree = HuffmanCode.build_Binarytree(b_heap)
            self.code, self.reverse = HuffmanCode.generate_tree_code(HuffmanCode, b_Tree)
            # print('Reverse ', self.reverse )
            init.code = self.code
            init.reverse = self.reverse
            encoded_text = self.encoded(text,self.code)
            bytes_array = self.padded_text(encoded_text)
            # print('encoded bytes ' , bytes_array)
            final_bytes = bytes(bytes_array)
            output.write(final_bytes)
            print("Compressed")
            return output_path

class Decompress:

    def remove_padding(text):
        padded_info = text[:8]
        extra_padding = int(padded_info,2)
        text = text[8:]
        padding_removed_text = text[:-1*extra_padding]
        return padding_removed_text

    def deCompress_text(text):
        decoded_text = ''
        current_bits = ''
        reverse_code = init.reverse
        # print('Reverse ' , reverse_code)
        for bit in text:
            current_bits += bit
            if current_bits in reverse_code:
                character = reverse_code[current_bits]
                decoded_text += character
                current_bits = ""
        return decoded_text


    def __deCompress__(self,input_path):
        filename, file_extension = os.path.splitext(input_path)
        output_path = filename + '_decompressed'+'.txt'
        with open(input_path,'rb') as file , open(output_path,'w') as output:       
            bit_string = ''
            byte = file.read(1)
            while  byte:
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8,'0')
                bit_string += bits
                byte = file.read(1)

            actual_text = self.remove_padding(bit_string)
            decompressed_text = self.deCompress_text(actual_text)
            print('Actual Text ' , actual_text)
            output.write(decompressed_text)
            return output_path