#!/usr/bin/python
import sys

#usage: python (path to deviations.py) [lact.sam] [size of reference genome] [mean] [standard deviation] > output_wiggle_file.wig

f = open(sys.argv[1],"rb")
n = int(sys.argv[2])
mean = int(sys.argv[3])
sd = float(sys.argv[4])

deviations = [0] * n
genome_insert = [0] * n

for line in f.readlines():
	if not (line.startswith('@')):
		item = line.split("\t")
		if (int(item[1]) & 3 == 3) and (int(item[8]) > 0): # both reads align correctly and length > 0
			genome_insert[int(item[3])] = abs(int(item[7]) + len(item[9]) - int(item[3])) #calculate the genomic insert
			if abs(genome_insert[int(item[3])] - mean) > sd*2: #insert length is above or below n=2 standard deviation
				deviations[int(item[3])] += 1
				deviations[int(item[7]) + len(item[9])] -= 1

f.close()

print "fixedStep chrom=genome start=1 step=1 span=1\n" # print the heading of the wiggle file

coverage2 = 0

for i in range (0,n):
	if deviations[i] != 0:
		coverage2 += deviations[i]
	print coverage2
