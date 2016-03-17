#!/usr/bin/python

"""
input file - connection matrix for a graph
numbers with ; as separator

ex.

0;1;2
1;0;3
2;3;0
"""

import sys

#Initial node for search \ start element in result chain.
start = 0;

all_paths = []

def deep (path, result):
	for i in range(path[-1], len(matrix[0])):
		if matrix[path[-1]][i] == 0:
			new_path = list(path)
			new_result = list(result)

			new_path.append(i)

			for j in range(0, len(new_result)):
				new_result[j] = new_result[j] | matrix[i][j]

			if all(v > 0 for v in new_result):
				print "PATH: {0}".format(new_path)
				all_paths.append(new_path)
				return 1
			else:
				deep (new_path, new_result)

	return 0


f = open (sys.argv[1])
matrix = [ map(int,line.split(';')) for line in f ]


while True:
	my_path = [ start ]
	my_result = list(matrix[start])
	deep( my_path, my_result )
	if len(matrix[0]) > start + 1:
		start += 1
	else:
		break