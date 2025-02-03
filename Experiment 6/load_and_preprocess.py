import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = pd.read_csv('concrete.csv')

# Check for missing values
df.isnull().sum()

# Handle missing values if any (here we assume there are none for simplicity)
# df.fillna(df.mean(), inplace=True)

# Split the dataset into features and target
X = df.drop('strength', axis=1)
y = df['strength']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Return the shapes of the training and testing sets
X_train_scaled.shape, X_test_scaled.shape, y_train.shape, y_test.shape