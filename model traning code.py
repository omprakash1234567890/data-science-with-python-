import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

# Sample DataFrame
data = {
    'square_feet': [1500, 2500, 800, 1200],
    'num_bedrooms': [3, 4, 2, 3],
    'num_bathrooms': [2, 3, 1, 2],
    'year_built': [2000, 2015, 1980, 1995],
    'location': ['A', 'B', 'A', 'C'],
    'price': [300000, 500000, 200000, 250000]
}
df = pd.DataFrame(data)

# Feature Engineering
df['log_square_feet'] = np.log(df['square_feet'])
df['age'] = 2024 - df['year_built']
df['bed_bath_ratio'] = df['num_bedrooms'] / df['num_bathrooms']
df['is_new'] = df['year_built'] > 2010

# Principal Component Analysis (PCA)
features = ['square_feet', 'num_bedrooms', 'num_bathrooms', 'age', 'log_square_feet', 'bed_bath_ratio']
X = df[features]

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA
pca = PCA(n_components=2)
principal_components = pca.fit_transform(X_scaled)

# Add principal components to DataFrame
df['pc1'] = principal_components[:, 0]
df['pc2'] = principal_components[:, 1]

# Encode categorical variables
df_encoded = pd.getDummies(df, columns=['location'], drop_first=True)

# Features and target
X = df_encoded.drop(['price'], axis=1)
y = df_encoded['price']

# Train a Random Forest model
model = RandomForestRegressor()
model.fit(X, y)

# Feature importance
importances = model.feature_importances_
feature_importance_df = pd.DataFrame({'feature': X.columns, 'importance': importances}).sort_values(by='importance', ascending=False)

print("Feature Importance:\n", feature_importance_df)

# Cross-validation
lr = LinearRegression()
scores = cross_val_score(lr, X, y, cv=5, scoring='neg_mean_squared_error')
print("Cross-validated MSE: ", -np.mean(scores))

