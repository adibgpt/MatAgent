import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the dataset with low_memory=False to handle mixed types
df = pd.read_csv('superconduct_train new.csv', low_memory=False)

# Attempt to convert all columns to numeric, forcing errors to NaN
df = df.apply(pd.to_numeric, errors='coerce')

# Drop rows with NaN values
df.dropna(inplace=True)

# Separate features and target variable
X = df.drop('critical_temp', axis=1)
y = df['critical_temp']

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Output the shape of the datasets
X_train_scaled.shape, X_test_scaled.shape, y_train.shape, y_test.shape