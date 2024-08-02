# Load the main dataset
import streamlit as st
import pandas as pd
csv_file_path = 'Travel.csv
df = pd.read_csv(csv_file_path)

# Load the names and interests dataset
names_interests_path = 'names_intrest.csv'
names_interests_df = pd.read_csv(names_interests_path)
df1 = pd.merge = pd.concat([df, names_interests_df], axis=1)
df1.head()
# Function to display the homepage
def display_home():
    st.title("Welcome to the Party Platform!")
    st.write("A place where divorced and single individuals can meet for a party.")

    # Add a button to register
    if st.button("Register Now"):
        st.session_state.page = "register"

    # Add a button to view profiles
    if st.button("View Profiles"):
        st.session_state.page = "profiles"

# Function to display the registration form
def display_register():
    st.title("Register for the Party")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=18, max_value=100)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    marital_status = st.selectbox("Marital Status", ["Divorced", "Single"])
    interests = st.text_area("Interests")

    if st.button("Submit"):
        # Save the registration data
        new_data = pd.DataFrame({
            'Name': [name],
            'Age': [age],
            'Gender': [gender],
            'MaritalStatus': [marital_status],
            'Interests': [interests]
        })
        st.session_state.df = pd.concat([st.session_state.df, new_data], ignore_index=True)
        st.session_state.page = "profiles"

# Function to display profiles
def display_profiles():
    st.title("Profiles")
    # Filter for divorced and single individuals
    filtered_df = st.session_state.df[(st.session_state.df['MaritalStatus'] == 'Divorced') | (st.session_state.df['MaritalStatus'] == 'Single')]

    for index, row in filtered_df.iterrows():
        st.subheader(row['Name'])
        st.write(f"Age: {row['Age']}")
        st.write(f"Gender: {row['Gender']}")
        st.write(f"Marital Status: {row['MaritalStatus']}")
        st.write(f"Interests: {row['Interests']}")
        st.write("---")

    if st.button("Back to Home"):
        st.session_state.page = "home"

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = "home"
if 'df' not in st.session_state:
    st.session_state.df = df1[[ 'Age', 'Gender', 'MaritalStatus', 'Interests']].dropna()

# Display the appropriate page
if st.session_state.page == "home":
    display_home()
elif st.session_state.page == "register":
    display_register()
elif st.session_state.page == "profiles":
    display_profiles()
