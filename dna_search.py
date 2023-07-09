# Storing DNA
# A nucleotide can be represented with a simple IntEnum - class; Enum where members are also (and must be) ints - with four cases

from enum import IntEnum
from typing import Tuple, List  # tuple and List are imported to assist with type hints

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]  # type alias for codons
Gene = List[Codon]  # type alias for genes

gene_str: str = "ACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTTT"

# A function to convert a str into a Gene
def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for _ in range(0, len(s), 3):
        if (_ + 2) >= len(s):  # not to run off the string end
            return gene
        # init codon out of three nucleotides
        codon: Codon = (Nucleotide[s[_]], Nucleotide[s[_ + 1]], Nucleotide[s[_ + 2]])
        gene.append(codon)
    return gene

my_gene: Gene = string_to_gene(gene_str)

# Defining a linear search
# It simply goes through each element in a data structure and checks for its match to the item being sought
def linear_contains(gene: Gene, key_codon: Codon) -> bool:
    for codon in gene:
        if codon == key_codon:
            return True
        return False
acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)
'''Using liner_contains() is for illustrative purposes, 
    Python built-in sequence types all implement the __contains__() method, which allows for search with the in operator
 print(linear_contains(my_gene, acg))  # True
 print(linear_contains(my_gene, gat))  # False'''
 
print(acg in my_gene)  # true
print(gat in my_gene)  # false
