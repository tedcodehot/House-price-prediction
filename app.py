import joblib
import streamlit as st
import snowflake.connector




conn = snowflake.connector.connect(
    user="Teddy",
    password="Alliswell@1111",
    account="ZPFYXBE-TC33496"
)

model=joblib.load("xgb_regression_best_params.pkl")


st.title("House Price Prediction")

square_footage	= st.number_input("Square Footage",min_value=0, max_value=10000, step=1, value=1000)
num_bedrooms	= st.number_input("Num Bedrooms",min_value=0, max_value=20, step=1, value=5)
num_bathrooms	=st.number_input("Num Bathrooms",min_value=0, max_value=10, step=1, value=3)
year_built      =st.number_input("Year Built",min_value=1900, max_value=2025, step=1, value=1950)
lot_size	= st.number_input("Lot Size",min_value=0.0, max_value=10.0, step=0.1, value=2.00)
garage_size	= st.number_input("Garage Size",min_value=0, max_value=10, step=1, value=2)
neighborhood_quality =st.number_input("Neighborhood Quality",min_value=0, max_value=10, step=1, value=2)

prediction =None
if st.button("Predict"):
    user_input = [[square_footage,num_bedrooms,num_bathrooms,year_built,lot_size,garage_size,neighborhood_quality]]
    prediction = model.predict(user_input)[0]
if prediction is not None:
    st.success(f"The price of the house is {prediction} $")
