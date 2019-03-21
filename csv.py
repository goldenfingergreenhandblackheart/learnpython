#! /usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import re
def read(file):
	rf = open(file, 'r')
	content = []
	reader = csv.reader(rf)
	for row in reader:
		content.append(row)
	print('Last    First    Salary')
	for i in range(len(content)):
		for j in range(len(content[i])):
			if re.search(r'\d+$', content[i][j]) != None:
				print('{0:.2f}'.format(float(content[i][j])))
			else:
				print('{0}'.format(content[i][j]), end = '    ')