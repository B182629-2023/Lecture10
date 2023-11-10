#!/usr/bin/python3
 
# Task 1
DNA_seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

A = DNA_seq.count("A")
print(f"The number of A nucleotides are: {A}")

T = DNA_seq.count("T")
print(f"The number of T nucleotides are: {T}")

AT_content = ((A + T) / len(DNA_seq))
print(f"The proportion of AT in the sequence is: {AT_content}")

# Task 2
DNA_seq_2 = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
complement_lower = DNA_seq_2.replace("A", "t").replace("T", "a").replace("G", "c").replace("C", "g")
print(f"The complement of\n{DNA_seq_2}\nis\n{complement_lower.upper()}")

# Task 3
DNA_seq_3 = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
motif = "AATTC"
print(f"The length of the first fragment is: {DNA_seq_3.find(motif,1,)}")
print(f"The length of the second fragment is: {len(DNA_seq_3) - DNA_seq_3.find(motif,1,)}")

#Task 4
DNA_seq_4 = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = DNA_seq_4[0:63]
exon2 = DNA_seq_4[90:]

print(f"The coding sequence is: {exon1 + exon2}")
print(f"{((len(exon1) + len(exon2)) / len(DNA_seq_4)) * 100}% of the DNA sequence is a coding sequence")

intron = DNA_seq_4[63:90]

print(f"The original genomic DNA sequence is: {exon1 + intron.lower() + exon2}")
