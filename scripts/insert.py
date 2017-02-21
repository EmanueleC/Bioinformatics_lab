#!/usr/bin/python
import sys

# command line arguments: the lact.sam file and the size of the reference genome

n = int(sys.argv[2])

genome_insert = [0] * n

f = open(sys.argv[1],"rb")

for line in f.readlines():
	if not (line.startswith('@')):
		item = line.split("\t")
		if (int(item[1]) & 3 == 3) and (int(item[8]) > 0): # both reads align correctly and length > 0
			genome_insert[int(item[3])] = abs(int(item[7]) + len(item[9]) - int(item[3])) #calculate the genomic insert

f.close()

print "fixedStep chrom=genome start=1 step=1 span=1\n"

for i in range (0,n):
	print genome_insert[i]
