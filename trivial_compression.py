# Trivial compression
# Converting gene nucleotides from a string representation to a bit-string represetation

# The class CompressedGene is provided with a str of characters representing the nucleotides in a gene
# And it internally stores the sequence of nucleotides as a bit string

class CompressedGene:
    # The __init__() method's to initilaize the bit-string construct with the appropriate data
    def __init__(self, gene: str) -> None:  # __str__() special method
        self._compress(gene)

    # Performing the compression with the _compress() method
    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1  # start with sentinel
        for nucleotide in gene.upper():
            self.bit_string <<= 2  # shift left two bits
            if nucleotide == "A":  # change last two bits to 00
                self.bit_string |= 0b00
            elif nucleotide == "C": # change last two bits to 01
                self.bit_string |= 0b01
            elif nucleotide == "G":  # change last two bits to 10
                self.bit_string |= 0b10
            elif nucleotide == "T":  # change last two bits to 11
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide:{}".format(nucleotide))

    # Implementing the decompression and the __str__() method that uses it
    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):  # -1 to exclude defined sentinel
            bits: int = self.bit_string >> i & 0b11  # get two relevant bits
            if bits == 0b00:  # A
                gene += "A"
            elif bits == 0b01:  # "C"
                gene += "C"
            elif bits == 0b10:  # "G"
                gene += "G"
            elif bits == 0b11:  # "T"
                gene += "T"
            else:
                raise ValueError("Invalid bits:{}".format(bits))
        return gene[::-1]  # [::-1] reverses the string by slicing backward

    def __str__(self) -> str:  # string representation for pretty printing
        return self.decompress()

# Using the sys.getsizeof() method
# We can indicate in the output whether we did save almost 75% of memory cost
# Of storing the gene through this compression scheme

if __name__=="__main__":
    from sys import getsizeof
    original: str = "TAGC" * 10
    print("Original is {} bytes".format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)  # compress
    print("Compressed is {} bytes".format(getsizeof(compressed.bit_string)))
    print(compressed)  # decompress
    print("original and decompressed are the same: {}".format(original == compressed.decompress()))
