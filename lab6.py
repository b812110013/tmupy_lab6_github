import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

file_path = r"C:\Programming\Python\python\Lab6\cost.csv"

st.title(":flag-tw: 家庭收支調查")
st.header(':grey[縣市每人平均月消費]', divider='rainbow')
st.markdown('[*資料來源：行政院主計總處家庭收支調查*](https://www.stat.gov.tw/cp.aspx?n=3914)')

cost = pd.read_csv(file_path, encoding='utf-8')

col1, col2 = st.columns(2)
with col1:
    city = st.multiselect('選擇想要顯示的**縣市**...', cost.columns, default=["年別"])

with col2:
    year_range = st.slider('選擇想要顯示的**年份**...', cost['年別'].unique()[0], cost['年別'].unique()[-1], (100, 101), step=1)
    year = [i for i in range(year_range[0], year_range[1]+1, 1)]

st.subheader(f'表1：民國 {year_range[0]} 至 {year_range[1]} 年', divider='grey')
st.write(cost[cost["年別"].isin(year)][city])
st.divider()