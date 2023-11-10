
#!/usr/bin/python3

# os.system("cp /localdisk/data/BPSM/Lecture11/plain_genomic_seq.txt . ")

# os.system("efetch -db nuccore -id AJ223353 -format fasta | grep =v ">" > remote_seq)



l_seq = open("local_seq").read()
r_seq = open("remote_seq").read().upper()

set(list(l_seq.rstrip()))
l_seq_real = l_seq.replace("X","").replace("K","").replace("t","T").replace("L","")

l_exon1 = l_seq_real[0:63]
l_exon2 = l_seq_real[90:]
l_intron = l_seq_real[63:90]

l_exon1_out = open("l_exon_1.fasta", "w")
l_exon1_out.write(">AJ223353_l_exon1_length" + str
r_coding = r_seq[28:409]
r_intron1 = r_seq[0:28]
r_intron2 = r_seq[409:]

