# Parsing a Fasta File
# 151212
# Neno Svrzikapa

from Bio import SeqIO
from Bio.Seq import Seq

genome =""
#This is compatible with multiple fasta files too
for seq_record in SeqIO.parse("lambda_virus.fa", "fasta"):
    print seq_record.description
    genome = str(seq_record.seq)
    print len(seq_record)
    print genome
    

#Making a seq object out of the genome enables seq manipulation functions
rc_genome = Seq(genome).reverse_complement()
print rc_genome
