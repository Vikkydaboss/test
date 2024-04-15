import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

@st.cache_data
def data():
    df = pd.read_csv('car_models.csv')
    df['Model Year Range'] = df['Model Year Range'].str.replace("Present", "2024").str.replace("present", "2024")
    return df

# df = data()
# st.write(df.head())'''

df = data()
st.title('Car Models App')
st.sidebar.title('Filters')
st.header("my first app")
st.dataframe(df.head(5))

size = df.shape
st.header(f'The size of the dataset is: {size}')
st.text('We used the df(head) function to only display five rows from the table')


# filter for the comapny 
car_company = df['Company'].unique()

# Selection (multiselect)
selected_company = st.sidebar.multiselect("Company", car_company, [car_company[0], car_company[30]])

#filter by selection 
filtered_company = df[df['Company'].isin(selected_company)]

st.subheader("filtered table")
if not selected_company:
    st.error("Please make a selection")
else:
    st.dataframe(filtered_company)