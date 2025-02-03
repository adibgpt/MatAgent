import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
concrete_data = pd.read_csv('concrete.csv')

# Feature Importance using Random Forest
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Define features and target
X = concrete_data.drop('strength', axis=1)
Y = concrete_data['strength']

# Split the data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Train Random Forest model
rf_model = RandomForestRegressor()
rf_model.fit(X_train, Y_train)

# Get feature importances
importances = rf_model.feature_importances_
features = X.columns

# Create a DataFrame for visualization
importance_df = pd.DataFrame({'Feature': features, 'Importance': importances})
importance_df = importance_df.sort_values(by='Importance', ascending=False)

# Plotting Feature Importance
plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=importance_df)
plt.title('Feature Importance for Concrete Strength Prediction')
plt.xlabel('Importance Score')
plt.ylabel('Features')
plt.savefig('feature_importance_concrete_strength.png')
plt.show()