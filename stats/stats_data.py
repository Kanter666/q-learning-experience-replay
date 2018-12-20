import pickle 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import preprocessing


ITERATIONS = 50
N_EPISODES = 200
FRONT_CUT = 20
ENVIRONMENT_ID = 1

#read pickle
results = pickle.load(open('./server.pickle','rb'))

environments = ['CartPole-v0', 'MountainCar-v0', 'Acrobot-v1']
er_types = ['none', 'uniform', 'combined', 'prioritized']
metrics = ['durations', 'mean_TD_error', 'median_TD_error', 'max_TD_error', 'std_TD_error', 'correlation_count']

# best duration per iteration
# mean TD error per iteration
# mean correlation count per iteration

environment = environments[ENVIRONMENT_ID]
idx = 0
matrix = np.zeros((ITERATIONS*4, 4))
for er_idx, er_type in enumerate(er_types):
	for iteration in range(ITERATIONS):
		#Change to max for CartPole
		matrix[idx, 0] = min(results[environment][er_type][iteration][metrics[0]][FRONT_CUT-10: ])
		matrix[idx, 1] = np.mean(results[environment][er_type][iteration][metrics[1]][FRONT_CUT: ])
		matrix[idx, 2] = np.mean(results[environment][er_type][iteration][metrics[5]][FRONT_CUT: ])
		matrix[idx, 3] = er_idx
		idx += 1

#Prepare data for output
min_max_scaler = preprocessing.MinMaxScaler()
normalised_features = min_max_scaler.fit_transform(matrix[:,:3])



def convert_to_pandas(matrix, title):
	data = pd.DataFrame(matrix,
						 columns=['BEST_DURATION',
						 		 'MEAN_TD_ERROR', 
						 		 'MEAN_CORRELATION']
						)

	#output data
	data.to_csv('output_data/' + title + '.csv')

	return data


convert_to_pandas(normalised_features, environment)



















