import numpy as np
import pandas as pd
import pickle

def buy_sell_hold(*args):
	cols = [c for c in args]
	requirement = 0.002
	for col in cols:
		if col > requirement:
			return 1                            #buy
		if col < -requirement:
			return -1							#sell
	return 0  									#hold