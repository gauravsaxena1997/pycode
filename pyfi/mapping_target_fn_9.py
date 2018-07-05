import numpy as np
import pandas as pd
import pickle
from target_fn_8 import buy_sell_hold
from prepeocessing_for_ml_7 import proces_data_for_labels

def extract_featuresets (ticker):
	ticker, df = proces_data_for_labels()
