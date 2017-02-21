#!/usr/bin/python
import sys

# command line arguments: the lact.sam file and the size of the reference genome

n = int(sys.argv[2])

genome_change = [0] * n

f = open(sys.argv[1],"rb")

for line in f.readlines():
	if not (line.startswith('@')):
		item = line.split("\t")
		if (int(item[1]) & 4 != 4): # take all mapped reads
			genome_change[int(item[3])] += 1
			genome_change[int(item[3]) + len(item[9])] -= 1

f.close()

print "fixedStep chrom=genome start=1 step=1 span=1\n" # print the heading of the wiggle file

current_coverage = 0
                    
for i in range (0,n):   
	current_coverage += genome_change[i]
	print current_coverage
