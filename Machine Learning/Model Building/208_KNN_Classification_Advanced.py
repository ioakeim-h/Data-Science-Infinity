#################################################################
# KNN for Classification - ABC Grocery Task
#################################################################


#################################################################
# Libraries
#################################################################

import pandas as pd
import pickle
import matplotlib.pyplot as plt
import numpy as np

from sklearn.neighbors import KNeighborsClassifier
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import RFECV

from feature_engine.encoding import OneHotEncoder


#################################################################
# Import sample data
#################################################################

# Import

data_for_model = pickle.load(open("data/abc_classification_modelling.p", "rb"))

# Drop uneccessary columns

data_for_model.drop("customer_id", axis = 1, inplace = True)

# Shuffle data

data_for_model = shuffle(data_for_model, random_state = 42)

# Class balance

data_for_model["signup_flag"].value_counts(normalize = True)


#################################################################
# Deal with missing values
#################################################################

data_for_model.isna().sum()
data_for_model.dropna(inplace = True)


#################################################################
# Deal with outliers
#################################################################

outlier_investigation = data_for_model.describe()

outlier_columns = ["distance_from_store","total_sales", "total_items"]

for column in outlier_columns:
    
    lower_quartile = data_for_model[column].quantile(0.25)
    upper_quartile = data_for_model[column].quantile(0.75)
    iqr = upper_quartile - lower_quartile
    iqr_extended = iqr * 2
    min_border = lower_quartile - iqr_extended
    max_border = upper_quartile + iqr_extended
    
    outliers = data_for_model[(data_for_model[column] < min_border) | (data_for_model[column] > max_border)].index
    print(f"{len(outliers)} outliers detected in column {column}")
    
    data_for_model.drop(outliers, inplace=True)


#################################################################
# Split Input Variables & Output Variable
#################################################################

X = data_for_model.drop(["signup_flag"], axis = 1)
y = data_for_model["signup_flag"]


#################################################################
# Split Training & Test sets
#################################################################

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42, stratify = y)


#################################################################
# Deal with Categorical Variables
#################################################################

ohe_enc = OneHotEncoder(top_categories = None,
                        variables = ["gender"], 
                        drop_last = True)

X_train = ohe_enc.fit_transform(X_train)
X_test = ohe_enc.transform(X_test)


#################################################################
# Feature Scaling
#################################################################

scale_norm = MinMaxScaler()
X_train = pd.DataFrame(scale_norm.fit_transform(X_train), columns = X_train.columns)
X_test = pd.DataFrame(scale_norm.transform(X_test), columns = X_test.columns)


#################################################################
# Feature Selection
#################################################################

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(random_state = 42)
feature_selector = RFECV(clf)

fit = feature_selector.fit(X_train, y_train)

optimal_feature_count = feature_selector.n_features_
print(f"Optimal number of features: {optimal_feature_count}")

X_train = X_train.loc[:, feature_selector.get_support()]
X_test = X_test.loc[:, feature_selector.get_support()]


plt.plot(range(1, len(fit.cv_results_['mean_test_score']) + 1), fit.cv_results_['mean_test_score'], marker = "o")
plt.ylabel("Model Score")
plt.xlabel("Number of Features")
plt.title(f"Feature Selection using RFE \n Optimal number of features is {optimal_feature_count} (at score of {round(max(fit.cv_results_['mean_test_score']),4)})")
plt.tight_layout()
plt.show()


#################################################################
# Model Training
#################################################################

clf = KNeighborsClassifier()
clf.fit(X_train, y_train)


#################################################################
# Model Assessment
#################################################################

y_pred_class = clf.predict(X_test)
y_pred_prob = clf.predict_proba(X_test)[:,1]

# Confusion Matrix

conf_matrix = confusion_matrix(y_test, y_pred_class)

plt.style.use("seaborn-poster")
plt.matshow(conf_matrix, cmap = "coolwarm")
plt.gca().xaxis.tick_bottom()
plt.title("Confusion Matrix")
plt.ylabel("Actual Class")
plt.xlabel("Predicted Class")
for (i, j), corr_value, in np.ndenumerate(conf_matrix):
    plt.text(j, i, corr_value, ha = "center", va = "center", fontsize = 20)
plt.show()

# Accuracy (the number of correct classifications out of all attempted classifications)
accuracy_score(y_test, y_pred_class)

# Precision (of all observations that were predicted as positive, how many were actually positive)
precision_score(y_test, y_pred_class)

# Recall (of all positive observations how many did we predict as positive)
recall_score(y_test, y_pred_class)

# F1-Score (the harmonic mean of precision and recall)
f1_score(y_test, y_pred_class)


#################################################################
# Finding the optimal value of k
#################################################################

k_list = list(range(2,25))
accuracy_scores = []

for k in k_list:
    clf = KNeighborsClassifier(n_neighbors = k)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracy = f1_score(y_test, y_pred)
    accuracy_scores.append(accuracy)

max_accuracy = max(accuracy_scores)
max_accuracy_idx = accuracy_scores.index(max_accuracy)
optimal_k_value = k_list[max_accuracy_idx]

# Plot of max depths

plt.plot(k_list, accuracy_scores)
plt.scatter(optimal_k_value, max_accuracy, marker = "x", color = "red")
plt.title(f"Accuracy (F1 Score) by k \n Optimal Value for k: {optimal_k_value} (Accuracy: {round(max_accuracy, 4)}")
plt.xlabel("k")
plt.ylabel("Accuracy (F1 Score)")
plt.tight_layout()
plt.show()




















