#################################################################
# Regression Tree - ABC Grocery Task
#################################################################


#################################################################
# Libraries
#################################################################

import pandas as pd
import pickle
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.metrics import r2_score
from feature_engine.encoding import OneHotEncoder



#################################################################
# Import sample data
#################################################################

# Import

data_for_model = pickle.load(open("data/abc_regression_modelling.p", "rb"))

# Drop uneccessary columns

data_for_model.drop("customer_id", axis = 1, inplace = True)

# Shuffle data

data_for_model = shuffle(data_for_model, random_state = 42)


#################################################################
# Deal with missing values
#################################################################

data_for_model.isna().sum()
data_for_model.dropna(inplace = True)


#################################################################
# Deal with outliers
#################################################################

# Decision trees don't care about outliers



#################################################################
# Split Input Variables & Output Variable
#################################################################

X = data_for_model.drop(["customer_loyalty_score"], axis = 1)
y = data_for_model["customer_loyalty_score"]


#################################################################
# Split Training & Test sets
#################################################################

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)


#################################################################
# Deal with Categorical Variables
#################################################################

ohe_enc = OneHotEncoder(top_categories = None,
                        variables = ["gender"], 
                        drop_last = True)

X_train = ohe_enc.fit_transform(X_train)
X_test = ohe_enc.transform(X_test)


#################################################################
# Feature Selection
#################################################################

# Feature selection does not matter for decision trees in terms of model accuracy
# It may, however, reduce computational time



#################################################################
# Model Training
#################################################################

regressor = DecisionTreeRegressor(random_state = 42, max_depth = 4)
regressor.fit(X_train, y_train)


#################################################################
# Model Assessment
#################################################################

# Predict on the Test Set

y_pred = regressor.predict(X_test)

# Calculate R-Squared

r_squared = r2_score(y_test, y_pred)
print(r_squared)

# Cross Validation

cv = KFold(n_splits = 4, shuffle = True, random_state = 42)
cv_scores = cross_val_score(regressor, X_train, y_train, cv = cv, scoring = "r2")
cv_scores.mean()

# Calculate Adjusted R-Squared

num_data_points, num_input_vars = X_test.shape
adjusted_r_squared = 1 - (1 - r_squared) * (num_data_points - 1) / (num_data_points - num_input_vars - 1)
print(adjusted_r_squared)

# A demonstration of overfitting

y_pred_training = regressor.predict(X_train)
r2_score(y_train, y_pred_training)

# Finding the best max_depth

max_depth_list = list(range(1,9))
accuracy_scores = []

for depth in max_depth_list:
    regressor = DecisionTreeRegressor(max_depth = depth, random_state = 42)
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)
    accuracy = r2_score(y_test, y_pred)
    accuracy_scores.append(accuracy)

max_accuracy = max(accuracy_scores)
max_accuracy_idx = accuracy_scores.index(max_accuracy)
optimal_depth = max_depth_list[max_accuracy_idx]

# Plot of max depths

plt.plot(max_depth_list, accuracy_scores)
plt.scatter(optimal_depth, max_accuracy, marker = "x", color = "red")
plt.title(f"Accuracy by Max Depth \n Optimal Tree Depth: {optimal_depth} (Accuracy: {round(max_accuracy, 4)}")
plt.xlabel("Max Depth of Decision Tree")
plt.ylabel("Accuracy")
plt.tight_layout()
plt.show()

# Plot model

plt.figure(figsize=(25,15))
tree = plot_tree(regressor,
                 feature_names = X.columns,
                 filled = True,
                 rounded = True,
                 fontsize = 16)





