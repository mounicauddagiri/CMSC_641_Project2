from FileCompress import Compress
from FileCompress import Decompress
if __name__ == "__main__":
    path = "test.txt"
    out = Compress.__Compression__(Compress,path)
    print(out)
    # decompressed_file = "test.bin"
    out1 = Decompress.__deCompress__(Decompress,out)
    # print(out1)

