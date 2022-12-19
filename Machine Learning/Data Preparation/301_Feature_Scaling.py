
# Standardisation
 
from sklearn.preprocessing import StandardScaler
 
scale_standard = StandardScaler()
 
# Standardize all columns
scale_standard.fit_transform(df)
 
# Standardize columns in list
scale_standard.fit_transform(df[["col1", "col2"]])
 
"The scaler will return the scaled values in a numpy array. \
If we want to turn them back into a pandas column we can run: "
 
df_standardised = pd.DataFrame(scale_standard.fit_transform(df),
                               columns = df.columns)



# Normalisation
from sklearn.preprocessing import MinMaxScaler
 
scale_norm = MinMaxScaler()
scale_norm.fit_transform(df)
df_normalised = pd.DataFrame(scale_norm.fit_transform(df),
                             columns = df.columns)
