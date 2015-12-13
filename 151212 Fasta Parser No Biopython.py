"""
Proposed Code:
by Ben Langmead, PhD, Jacob Pritt
"""

def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if not line[0] == '>':
                genome += line.rstrip()
    return genome


"""
Knowing that .fa files (excluding multiple .fa) are standardized:
There is no need to check for every line if it has '>' at index 0
Not as efficient to be checking this.
It would be better to save the Description as a header
and pop the first line.

Neno Svrzikapa
20151212
Fasta Parser Without Biopython

"""



def readGenomeB(filename):
    header = ''
    genome = ''
    with open(filename, 'r') as f:
        list_of_lines = f.readlines()
        #grab the first line by popping it out of the list of lines
        header = list_of_lines.pop(0).rstrip()
        genome = genome.join([line.rstrip() for line in list_of_lines])
    return genome
        





"""
Alternatively if you don't want to save it
You could just use next to skip the first line.
"""

def readGenomeC(filename):
    genome = ''
    with open(filename, 'r') as f:
        next(f)
        for line in f:
            genome += line.rstrip()
    return genome



genome = readGenome('lambda_virus.fa')
print genome[:100]

genomeB = readGenomeB('lambda_virus.fa')
print genomeB[:100]

genomeC = readGenomeC('lambda_virus.fa')
print genomeC[:100]