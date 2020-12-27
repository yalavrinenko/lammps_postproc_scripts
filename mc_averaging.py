#!/usr/bin/env python3

import numpy as np
import sys
import os

if len(sys.argv) > 2:
	slice = float(sys.argv[1])
	
	for path in sys.argv[2:]:
		print(path)
		with open(path, "r") as f:
			for l in f:
				if '#' in l:
					print(l.strip())
		raw = np.loadtxt(path, comments='#')

		filter_set = set(raw[:, 1])
		if (len(filter_set) == 2 and filter_set = set([0, 1]))
			data = [d for d in raw if d[1] == 1]
		else:
			data = raw
			
		print(len(data))

		data = data[int(len(data) * slice):]

		print ("\t".join(str(v) for v in np.mean(data, axis=0)))
