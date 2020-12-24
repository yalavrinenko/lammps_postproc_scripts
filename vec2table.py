#!/usr/bin/env python3
import sys
import numpy as np
import pandas as pd
import os

if len(sys.argv) < 2:
 	sys.exit(1)

path = sys.argv[1]

raw = np.loadtxt(path)

key1 = pd.Index(raw[:, 0]).unique()
key2 = pd.Index(raw[:, 1]).unique()

def create_table(col_keys, row_keys, data, data_column):   
	mat = pd.DataFrame(np.zeros((len(row_keys), len(col_keys))), index = key2, columns=key1)

	for line in data:
		mat[line[0]][line[1]] = line[data_column]
	
	return mat

for transform in sys.argv[2:]:
	[index, name] = transform.strip().split('-')
	index = int(index)

	data = create_table(key1, key2, raw, index)
	data.to_csv(os.path.splitext(path)[0]+".{0}.csv".format(name), index=True, header=True, sep='\t')

# Pressure = create_table(key1, key2, raw, 2)
# Energy = create_table(key1, key2, raw, 3)

# Pressure.to_csv(path+"_pressure.csv", index=True, header=True, sep='\t')
# Energy.to_csv(path+"_energy.csv", index=True, header=True, sep='\t')