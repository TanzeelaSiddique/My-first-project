# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 16:06:52 2023

@author: wajiz.pk
"""
import pandas as pd
import streamlit as st
file = r'C:/Users/wajiz.pk/OneDrive/Desktop/Billionaire.csv'
#reading the file
df = pd.read_csv(file)
#find the most popular source of income
st.header('Billionaire Dataset')

all_countries = df['Country'].unique()
#Interactivity
c1, c2 = st.columns(2)
selected_country = c1.selectbox('Select Your Country',all_countries)
subset_country = df[df['Country'] == selected_country]
Source = sorted(subset_country['Source'].unique())
selected_source = c2.selectbox('Select source of Income',Source)
subset_source = subset_country[subset_country['Source'].isin(selected_source)]
main_string = '{} -Billionaries'.format(selected_country)
c2.header(main_string)
c2.table(subset_country)
c2.header('Source wise info')
c2.table(subset_source)

