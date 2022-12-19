
# Libraries

import pandas as pd
import pickle

# Import customers for scoring

to_be_scored = pickle.load(open("data/abc_regression_scoring.p", "rb"))

# Import model and model objects

regressor = pickle.load(open("data/random_forest_regression_model.p", "rb"))
ohe_enc = pickle.load(open("data/random_forest_regression_ohe.p", "rb"))

# Drop unused columns

to_be_scored.drop(["customer_id"], axis = 1, inplace = True)

# Drop missing values

to_be_scored.dropna(inplace = True)

# Apply One Hot Encoding

to_be_scored = ohe_enc.transform(to_be_scored)

# Make our predictions!

loyalty_predictions = regressor.predict(to_be_scored)
