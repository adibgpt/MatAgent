import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.neural_network import MLPRegressor

# Load the dataset
data = pd.read_csv('superconduct_train new.csv')

# Separate features and target variable
target = 'critical_temp'
X = data.drop(columns=[target])
y = data[target]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize and train the Support Vector Machine model
svm_model = SVR(kernel='rbf')
svm_model.fit(X_train_scaled, y_train)

# Predict and evaluate the SVM model
svm_predictions = svm_model.predict(X_test_scaled)
svm_mae = mean_absolute_error(y_test, svm_predictions)
svm_rmse = mean_squared_error(y_test, svm_predictions, squared=False)

# Initialize and train the Neural Network model
nn_model = MLPRegressor(hidden_layer_sizes=(100,), max_iter=500, random_state=42)
nn_model.fit(X_train_scaled, y_train)

# Predict and evaluate the Neural Network model
nn_predictions = nn_model.predict(X_test_scaled)
nn_mae = mean_absolute_error(y_test, nn_predictions)
nn_rmse = mean_squared_error(y_test, nn_predictions, squared=False)

# Output the evaluation metrics
(svm_mae, svm_rmse, nn_mae, nn_rmse)