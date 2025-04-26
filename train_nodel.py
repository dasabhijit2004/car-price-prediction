import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# Load your dataset (modify the path accordingly)
data = pd.read_csv('car_data.csv')

# Feature engineering (adjust these columns based on your dataset)
X = data[['Year', 'Present_Price', 'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner']]
y = data['Selling_Price']

# Encode categorical columns (if necessary)
labelencoder = LabelEncoder()
X['Fuel_Type'] = labelencoder.fit_transform(X['Fuel_Type'])
X['Seller_Type'] = labelencoder.fit_transform(X['Seller_Type'])
X['Transmission'] = labelencoder.fit_transform(X['Transmission'])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'car_price_model.pkl')
print("Model trained and saved successfully!")
