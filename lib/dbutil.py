import pandas as pd
from config import *

def getData(name, parse_dates='date'):
	if parse_dates is None:
		return pd.read_csv('/'.join([projectPaths['dataset'], projectFiles[name]]))
	else:
		return pd.read_csv('/'.join([projectPaths['dataset'], projectFiles[name]]), parse_dates=[parse_dates])
