#################################################################
# Random Forest Regression - ABC Grocery Task
#################################################################


#################################################################
# Libraries
#################################################################

import pandas as pd
import pickle
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.metrics import r2_score
from feature_engine.encoding import OneHotEncoder
from sklearn.inspection import permutation_importance



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
# It may, however, reduce computational time.



#################################################################
# Model Training
#################################################################

regressor = RandomForestRegressor(random_state = 42)
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

# Feature Importance

feature_importance = pd.DataFrame(regressor.feature_importances_)
feature_names = pd.DataFrame(X.columns)
feature_importance_summary = pd.concat([feature_names, feature_importance], axis = 1)
feature_importance_summary.columns = ["input_variable", "feature_importance"]
feature_importance_summary.sort_values(by = "feature_importance", inplace = True)

plt.barh(feature_importance_summary["input_variable"], feature_importance_summary["feature_importance"])
plt.title("Feature Importance of Random Forest")
plt.xlabel("Feature Importance")
plt.tight_layout()
plt.show()

# Permutation Importance

result = permutation_importance(regressor, X_test, y_test, n_repeats = 10, random_state = 42)

permutation_importance = pd.DataFrame(result["importances_mean"])
feature_names = pd.DataFrame(X.columns)
permutation_importance_summary = pd.concat([feature_names, permutation_importance], axis = 1)
permutation_importance_summary.columns = ["input_variable", "permutation_importance"]
permutation_importance_summary.sort_values(by = "permutation_importance", inplace = True)

plt.barh(permutation_importance_summary["input_variable"], permutation_importance_summary["permutation_importance"])
plt.title("Permutation Importance of Random Forest")
plt.xlabel("Permutation Importance")
plt.tight_layout()
plt.show()


# Predictions under the hood

y_pred[0]
new_data = [X_test.iloc[0]]
regressor.estimators_

predictions = []
tree_count = 0

for tree in regressor.estimators_:
    prediction = tree.predict(new_data)[0]
    predictions.append(prediction)
    tree_count += 1

print(predictions)
sum(predictions) / tree_count


# Export model and objects
import pickle
pickle.dump(regressor, open("data/random_forest_regression_model.p", "wb"))
pickle.dump(ohe_enc, open("data/random_forest_regression_ohe.p", "wb"))











