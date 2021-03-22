import pandas as pd
import numpy as np
from sklearn import datasets

#生成合成数据
X_data, y_label = datasets.make_classification(n_samples = 100, n_features = 10000, random_state = 101)

fisher_scores = []

#计算Fisher_score的值
def fisher_score(i):
    ith_all_data = []
    ith_true_data = []
    ith_false_data = []
    
    n_true = 0
    n_false = 0
    
    for k in range(0,100):
        temp = X_data[k][i]
        ith_all_data.append(temp)
        if y_label[k] == 1:
            n_true = n_true + 1
            ith_true_data.append(temp)
        else:
            n_false = n_false + 1
            ith_false_data.append(temp)
    
    mu_all = np.mean(ith_all_data)
    mu_true = np.mean(ith_true_data)
    mu_false = np.mean(ith_false_data)
    sigma_all = np.var(ith_all_data)
    
    ans = (n_true*(mu_true - mu_all)**2 + n_false*(mu_false - mu_all)**2)/sigma_all
    return ans

#依次计算每个fisher_score
for i in range(0, 1000):
    fisher_scores.append(fisher_score(i))

print(fisher_scores)
