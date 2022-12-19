
# Feature Selection using a simple Correlation Matrix

import pandas as pd
df = pd.read_csv("feature_selection_sample_data.csv")

# Correlation matrix
correlation_matrix = df.corr()
