import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

file_path = r"C:\Programming\Python\python\Lab6\cost.csv"

st.title(":flag-tw: 家庭收支調查")
st.header(':grey[縣市每人平均月消費]', divider='rainbow')
st.markdown('[*資料來源：行政院主計總處家庭收支調查*](https://www.stat.gov.tw/cp.aspx?n=3914)')

cost = pd.read_csv(file_path, encoding='utf-8')
columns = cost.columns
options = st.multiselect('選擇想要顯示的縣市...', columns, default=["年別"])
st.subheader(f'表1：民國 {cost["年別"].iloc[0]} 至 {cost["年別"].iloc[-1]} 年', divider='grey')
#st.dataframe(cost[options])
st.write(cost[options])
st.divider()
