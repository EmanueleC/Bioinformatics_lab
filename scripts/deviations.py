#!/usr/bin/python
#import math

# command line arguments: the wiggle file with the insertions, the mean and the
# standard deviation

import sys

f = open(sys.argv[1],"rb")
mean = int(sys.argv[2])
sd = float(sys.argv[3])

print "fixedStep chrom=genome start=1 step=1 span=1\n"

for line in f.readlines():
	item = line.split("\n")
	if item[0].isdigit() and int(item[0]) != 0 and (int(item[0])-mean) > sd*3: # insert is above/below standard deviation thrice
		print item[0]
	else: print 0 #optional

f.close()
