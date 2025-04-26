# Import necessary libraries
import streamlit as st
import pandas as pd
import pickle
import datetime

import joblib
model = joblib.load('model.pkl')

# Load the trained model from the pickle file
try:
    model = pickle.load(open('car_price_model.pkl', 'rb'))
except Exception as e:
    st.error(f"Error loading model: {e}")
    model = None

# Streamlit interface for user input
def user_input_features():
    st.sidebar.header('User Input Features')
    
    # Collect inputs for each feature
    fuel_type = st.sidebar.selectbox('Fuel Type', ['Petrol', 'Diesel', 'CNG'])
    seller_type = st.sidebar.selectbox('Seller Type', ['Dealer', 'Individual'])
    transmission = st.sidebar.selectbox('Transmission', ['Manual', 'Automatic'])
    
    # User inputs for other numerical features (you can add more as needed)
    present_price = st.sidebar.slider('Present Price (in lakhs)', 0.0, 100.0, 10.0)
    kms_driven = st.sidebar.slider('Kms Driven (in km)', 0, 100000, 10000)
    owner = st.sidebar.selectbox('Number of Owners', [0, 1, 2, 3])
    
    # Instead of 'Age', ask for 'Year' of manufacture
    year_of_manufacture = st.sidebar.slider('Year of Manufacture', 2000, datetime.datetime.now().year, 2010)
    
    # Create a dictionary with features in the EXACT same order as training
    input_data = {
        'Year': year_of_manufacture,
        'Present_Price': present_price,
        'Kms_Driven': kms_driven,
        'Fuel_Type': 0 if fuel_type == 'Petrol' else (1 if fuel_type == 'Diesel' else 2),
        'Seller_Type': 0 if seller_type == 'Dealer' else 1,
        'Transmission': 0 if transmission == 'Manual' else 1,
        'Owner': owner
    }
    
    # Create DataFrame and ensure the columns are in the exact same order as training
    columns = ['Year', 'Present_Price', 'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner']
    features = pd.DataFrame([input_data], columns=columns)
    
    return features

# Main function to run the app
def main():
    st.title("Car Price Prediction App")
    
    # Get user input
    features = user_input_features()

    # Display input features
    st.subheader("Input Details:")
    
    # Create a more user-friendly display of the inputs
    display_data = features.copy()
    # Convert encoded values back to labels for display
    display_data['Fuel_Type'] = display_data['Fuel_Type'].map({0: 'Petrol', 1: 'Diesel', 2: 'CNG'})
    display_data['Seller_Type'] = display_data['Seller_Type'].map({0: 'Dealer', 1: 'Individual'})
    display_data['Transmission'] = display_data['Transmission'].map({0: 'Manual', 1: 'Automatic'})
    
    st.write(display_data)
    
    if model is not None:
        try:
            # Make predictions
            prediction = model.predict(features)
            
            # Display prediction
            st.subheader("Predicted Selling Price:")
            st.header(f"₹ {prediction[0]:,.2f} Lakhs")
        except Exception as e:
            st.error(f"Prediction error: {e}")
            st.info("Detailed error information:")
            st.code(str(e))
    else:
        st.warning("Model not loaded. Please check if the model file exists and is valid.")

joblib.dump(model, 'model.pkl')

if __name__ == '__main__':
    main()