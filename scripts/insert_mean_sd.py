#!/usr/bin/python
import math
import sys

#usage: python (path to insert_mean_sd.py) [wiggle file with insertions length]

f = open(sys.argv[1],"rb")

count_values = 0
total_sum = 0
total_sum_square = 0

for line in f.readlines():
	item = line.split("\n")
	if item[0].isdigit() and int(item[0]) != 0:
		total_sum += int(item[0])
		total_sum_square += pow(int(item[0]),2)
		count_values += 1

mean = total_sum/count_values

sd = math.sqrt(count_values*total_sum_square-pow(total_sum,2))/count_values

print "mean: ", mean, " standard deviation: ", sd

f.close()
