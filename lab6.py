import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


st.title("家庭收支調查：縣市平均每人月消費")
st.markdown('[資料來源：行政院主計總處家庭收支調查](https://www.stat.gov.tw/cp.aspx?n=3914)')

cost = pd.read_csv('./dataset/cost.csv', encoding='utf-8')
st.dataframe(cost)