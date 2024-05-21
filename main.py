import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit_option_menu import option_menu
from home import Home
from age import Age

with st.sidebar:
    selected = option_menu(
        menu_title = "Main Menu",
        options = ["Home", "India Analysis", "Age Analysis", "About Us"]
    )

if selected == "Home":
    st.title("Covid-19 Analysis")
    df = pd.read_csv('C:\\Users\\MY PC\\OneDrive\\Desktop\\Covid-19 Analysis\\Covid-19 Analysis Report\\src\\Dataset\\covid_19_data.csv')
    #st.write(df)

    df1 = df.sort_values(by=['Confirmed'], ascending=False)
    df2 = df1.dropna()

    df3 = df2.groupby(['Country/Region'], sort=False)[['Confirmed', 'Recovered']].max()
    #st.write(df3.head(10))

    columns = df3.columns.tolist()

    selected_column = st.radio("",columns, horizontal=True)

    if selected_column == 'Confirmed':

        fig = px.bar(df3['Confirmed'])
        fig.update_layout(title=dict(text="Confirmed Cases", x=0.35), title_font=dict(size=20, family='Courier', weight='bold', color='gray'))
        fig.update_xaxes(title_text='Countries', title_font=dict(size=18, family='Courier', weight='bold', color='gray'))
        fig.update_yaxes(title_text='Cases', title_font=dict(size=18, family='Courier', weight='bold', color='gray'))
        st.plotly_chart(fig)

    else:

        fig1 = px.bar(df3['Recovered'])
        fig1.update_layout(title=dict(text="Recovered Cases", x=0.35), title_font=dict(size=20, family='Courier', weight='bold', color='gray'))
        fig1.update_xaxes(title_text='Countries', title_font=dict(size=18, family='Courier', weight='bold', color='gray'))
        fig1.update_yaxes(title_text='Cases', title_font=dict(size=18, family='Courier', weight='bold', color='gray'))
        st.plotly_chart(fig1)

if selected == "India Analysis":
    Home()

if selected == "Age Analysis":
    Age()

if selected == "About Us":
    st.title("Hi I am there to help you.")