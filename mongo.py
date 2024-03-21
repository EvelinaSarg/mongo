import streamlit as st
from pymongo import MongoClient

# Connect to MongoDB Atlas
client = MongoClient("your_connection_string")
db = client["your_database_name"]
collection = db["your_collection_name"]

# Streamlit UI
st.title("Data Entry Form")

# User input fields
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, max_value=150)
email = st.text_input("Enter your email:")

# Submit button
if st.button("Submit"):
    # Data validation
    if name and age and email:
        # Create document to be inserted
        user_data = {
            "name": name,
            "age": age,
            "email": email
        }
        # Insert data into MongoDB Atlas
        result = collection.insert_one(user_data)
        st.success("Data saved successfully!")
    else:
        st.error("Please fill in all the fields.")
