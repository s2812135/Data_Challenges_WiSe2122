# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 17:39:38 2021

@author: dariu
"""

import numpy as np
from matplotlib import pyplot as plt

from sklearn.datasets import make_biclusters
from sklearn.cluster import SpectralCoclustering
from sklearn.metrics import consensus_score

data_t, rows_t, columns_t = make_biclusters(
    shape=(300, 300), n_clusters=5, noise=5, shuffle=False, random_state=0
)

plt.matshow(data_t, cmap=plt.cm.Blues)
plt.title("Original dataset")

# shuffle clusters
rng = np.random.RandomState(0)
row_idx_t = rng.permutation(data_t.shape[0])
col_idx_t = rng.permutation(data_t.shape[1])
data_t = data_t[row_idx_t][:, col_idx_t]

plt.matshow(data_t, cmap=plt.cm.Blues)
plt.title("Shuffled dataset")

model_t = SpectralCoclustering(n_clusters=5, random_state=0)
model_t.fit(data_t)
score_t = consensus_score(model_t.biclusters_, (rows_t[:, row_idx_t], columns_t[:, col_idx_t]))

print("consensus score: {:.3f}".format(score_t))

fit_data_t = data_t[np.argsort(model_t.row_labels_)]
fit_data_t = fit_data_t[:, np.argsort(model_t.column_labels_)]

plt.matshow(fit_data_t, cmap=plt.cm.Blues)
plt.title("After biclustering; rearranged to show biclusters")

plt.show()
