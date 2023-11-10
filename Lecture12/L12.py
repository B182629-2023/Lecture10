#!/usr/bin/python3

#Task 1
input_txt = open('input.txt').read().upper().replace("ATTCGATTATAAGCA", "").split()

#FORMAT: with open('NEWFILE', 'w') as OBJECT:
#	for ITEMS in FILE:
#		OBJECT.write(ITEMS = '\n')
#		ITEMS


with open('clean_seqs.txt', 'w') as clean:
	for seqs in input_txt:
		clean.write(seqs + '\n')
		seqs

print(open('clean_seqs.txt').read().rstrip())

#Task 2

genomic_dna = open('genomic_dna2.txt').read().upper()

exons = open('exons.txt').read().rsplit()

counter = 0

for exon in exons:
	counter += 1
	print(counter, exon)

with open('coding_sequence.fasta', 'w') as coding:
	coding.write('>Coding_seq\n')
	for exon in exons:
		counter += 1
		startexon = int(exon.split(',') [0])-1
		endexon = int(exon.split(',') [1])
		exonwanted = genomic_dna[startexon :endexon]
		coding.write(exonwanted)
		regionsumm = 'Exon' + str(counter) + ' runs from index position ' + str(startexon) + ' upto but not including ' + str(endexon) + '.'
		print(regionsumm, '\n', exonwanted)
