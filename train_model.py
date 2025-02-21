import pickle
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge

# Load the dataset (replace 'train.csv' with the correct path)
df = pd.read_csv("C:\\Users\\Bhoomika NS\\OneDrive\\Tài liệu\\Data_Frames\\train.csv")

# Select relevant features and target variable
features = ["GrLivArea", "BedroomAbvGr", "FullBath", "HalfBath", "TotalBsmtSF", "YrSold", "YearBuilt"]
target = "SalePrice"

X = df[features]
y = df[target]

# Handle missing values (optional, adjust based on your dataset)
X = X.fillna(X.mean())

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train Ridge Regression Model
ridge_model = Ridge(alpha=100)
ridge_model.fit(X_train_scaled, y_train)

# Save the trained Ridge model
with open("C:/Users/Bhoomika NS/house-price-predictor/ridge_model.pkl", "wb") as model_file:
    pickle.dump(ridge_model, model_file)

# Save the scaler (important to scale input before predicting)
with open("scaler.pkl", "wb") as scaler_file:
    pickle.dump(scaler, scaler_file)

print("✅ Ridge model and scaler saved successfully!")
