# -*- coding: utf-8 -*-
"""

@author: jacob
"""

import numpy as np
import esig.tosig as ts

#generate random array, 2-dim path length 10
np.random.seed(123)
data = np.random.random(size=(10,2))
data

#compute signature to degree 2
sig = ts.stream2sig(data, 2)
sig
#[1., -0.16491781, 0.24568825, 0.01359894, 0.02409578, -0.06461415, 0.03018136]

#2-dim path from figure 9a in primer, page 22
X_1 = np.array([1., 3., 5., 8.]).reshape((-1,1))
X_2 = np.array([1., 4., 2., 6.]).reshape((-1,1))
path = np.append(X_1,X_2, axis=1)

#compute signature to degree 2
signature = ts.stream2sig(path, 2)
signature
#[1., 7., 5., 24.5., 19., 16., 12.5]

#compute log sig
logsig = ts.stream2logsig(path, 2)
#[7, 5, 1.5] = [S(1),S(2),S[1,2]]

#verify relationship between sig and logsig
logsig[2] == .5*(signature[4]-signature[5])

#verify shuffle product
signature[1]*signature[2] == signature[4] + signature[5]
sig[1]*sig[2] == sig[4] + sig[5]

#lead lag transform in fig 7c
X_lead = np.array([1., 4., 4., 2., 2., 6., 6.]).reshape((-1,1))
X_lag = np.array([1., 1., 4., 4., 2., 2., 6.]).reshape((-1,1))
leadlag = np.append(X_lead,X_lag, axis=1)

LLsig = ts.stream2sig(leadlag, 2)
#[ 1. ,  5. ,  5. , 12.5, 27. , -2. , 12.5]
