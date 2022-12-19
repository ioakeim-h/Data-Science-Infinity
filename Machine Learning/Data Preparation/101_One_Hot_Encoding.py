
import pandas as pd
import numpy as np


X_train = pd.DataFrame({
    "output" : [1,2,3,4],
    "input1" : ["a","b",np.nan,"d"],
    "input2" : ["aa","bb","cc",np.nan]})



# Encoding categories with one hot encoder

from sklearn.preprocessing import OneHotEncoder

categorical_vars = ["input1", "input2"]

ohe_enc = OneHotEncoder(sparse=False, drop = "First")
enc_vars_array = ohe_enc.fit_transform(X_train[categorical_vars])
enc_feature_names = ohe_enc.get_feature_names(categorical_vars)

enc_vars_df = pd.DataFrame(enc_vars_array, columns = enc_feature_names_out)

X_train = pd.concat([X_train.reset_index(drop=True), enc_vars_df.reset_index(drop=True)], axis = 1)
X_train.drop(categorical_vars, axis = 1, inplace = True)

# One one variable...





# Encode multiple columns
categorical_vars = ["col2"]
ohe_enc = OneHotEncoder(sparse = False)




from feature_engine.wrappers import SklearnTransformerWrapper




ohe_enc = OneHotEncoder(top_categories = None,
                        variables = ["var1","var2"],
                        drop_last = True)

df_enc = ohe_enc.fit_transform(df)

