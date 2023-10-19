import numpy as np


def CharlesTries():
	
	log2delta = (1/2) * (1/(np.emath.log(64 - 8)+ 8)) * (64 - 8)
	print("ln 64 {} ln 8 {} ln 64 minus ln 8 {} equal {}".format(np.emath.log(64), np.emath.log(8), round(np.emath.log(64) - np.emath.log(8), 0), round((np.emath.log(64) - np.emath.log(8)), 0) == round(log2delta, 0)))
	print("log delta {}".format(round(log2delta, 0)))
CharlesTries()