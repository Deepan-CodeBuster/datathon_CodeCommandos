import pandas as pd
import numpy as np
from datetime import datetime
import joblib
import streamlit as st
from xgboost import XGBRegressor

# Load the pre-trained model
model = joblib.load('xgboost_model.pkl')

# Constants for Inventory Management
AVG_SALES = 50  # Example: Average sales per day
SAFETY_STOCK_PERCENTAGE = 0.2  # Keep 20% as safety stock
LEAD_TIME_DAYS = 5  # Average lead time in days

# Streamlit application
def main():
    st.title("Sales Quantity & Inventory Management")

    # Input Fields for user
    date_input = st.date_input("Select Date", min_value=datetime(2025, 1, 1))
    daily_sales_percentage = st.number_input("Daily Sales Percentage", min_value=0.0, max_value=1.0, value=0.034463806)
    market_share = st.number_input("Market Share", min_value=0, max_value=100, value=35)
    political = st.selectbox("Political Situation", [0, 1], index=1)
    marketing = st.selectbox("Marketing Strategy", [0, 1], index=1)
    budget = st.number_input("Marketing Budget", min_value=0.0, value=5000.56)
    machineries = st.selectbox("Infrastructure Machinery", ['Backhoe Loader', 'Excavators(crawler)', 'Loaders (Wheeled)', 
                                                            'Skid Steer Loaders', 'Compactors', 'Tele Handlers'])
    region = st.selectbox("Region", ['Sherrichester', 'Other_Region'])  

    # Prediction button
    if st.button('Predict Sales Quantity'):
        # Prepare new data
        new_data = pd.DataFrame({
            'Date': [date_input],
            'Daily_Sales _Percentage': [daily_sales_percentage],
            'Market_Share': [market_share],
            'Political': [political],
            'Marketing': [marketing],
            'Budget': [budget],
            'Infrastructure_Machineries': [machineries],
            'Region': [region]
        })

        # Process new data similar to training data
        new_data['Date'] = pd.to_datetime(new_data['Date'])
        new_data['year'] = new_data['Date'].dt.year
        new_data['month'] = new_data['Date'].dt.month
        new_data['day'] = new_data['Date'].dt.day
        new_data['dayofweek'] = new_data['Date'].dt.dayofweek

        # Ensure all columns match training data
        new_data_encoded = pd.get_dummies(new_data, columns=['Infrastructure_Machineries', 'Region'])
        for col in model.feature_names_in_:
            if col not in new_data_encoded.columns:
                new_data_encoded[col] = 0
        new_data_encoded = new_data_encoded[model.feature_names_in_]

        # Predict sales quantity
        predicted_quantity = model.predict(new_data_encoded)[0]

        # Calculate Safety Stock & Reorder Point
        safety_stock = SAFETY_STOCK_PERCENTAGE * predicted_quantity
        reorder_point = (predicted_quantity * LEAD_TIME_DAYS) + safety_stock

        # Inventory Management Suggestions
        if predicted_quantity > AVG_SALES:
            inventory_suggestion = "Increase stock levels to meet demand."
        elif predicted_quantity < AVG_SALES * 0.5:
            inventory_suggestion = "Reduce inventory to avoid overstocking."
        else:
            inventory_suggestion = "Maintain current inventory levels."

        # Display results
        st.write(f'Predicted Sales Quantity: {predicted_quantity}')
        st.write(f'Safety Stock: {safety_stock}')
        st.write(f'Reorder Point: {reorder_point}')
        st.write(f'Inventory Suggestion: {inventory_suggestion}')

if __name__ == "__main__":
    main()
