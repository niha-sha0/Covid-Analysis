import pandas as pd
import streamlit as st
import plotly.express as px

def Age():
    st.title("Age Group Analysis")
    
    ageGroup = pd.read_csv("C:\\Users\\MY PC\\OneDrive\\Desktop\\Covid-19 Analysis\\Covid-19 Analysis Report\\src\\Dataset\\AgeGroupDetails.csv")
    st.write(ageGroup)

    fig = px.bar(ageGroup, title='Age Group Distribution')
    fig.show()
