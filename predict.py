"""

Prediction via machine learning
--------------------------------
Author: Jordan Cave

"""

import numpy as np
import matplotlib.pyplot as plt
import csv

from sklearn import linear_model, datasets, metrics
from sklearn.model_selection import train_test_split
from sklearn.neural_network import BernoulliRBM
from sklearn.pipeline import Pipeline

def import_data(csv_file):
	data = []
	with open(csv_file, 'rt') as csvfile:
		reader = csv.reader(csvfile, delimiter = ',')
		next(reader, None)
		data = np.asarray([data for data in reader], dtype = float)
	return data

def linear_reg(data):
	pass

def main():
	test_data = import_data('fake_data.csv')
	print(test_data.shape)
    

if __name__ == "__main__":
	print(__doc__)
	main()
            

