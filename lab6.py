import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pylab import matplotlib
from matplotlib import font_manager


file_path = r"C:\Programming\Python\python\Lab6\cost.csv"
font_file = r"C:\Kevin\font\jf-openhuninn-2.0.ttf"

st.title(":flag-tw: 家庭收支調查")
st.header(':grey[縣市每人平均月消費]', divider='rainbow')
st.markdown('[*資料來源：行政院主計總處家庭收支調查*](https://www.stat.gov.tw/cp.aspx?n=3914)')

cost = pd.read_csv(file_path, encoding='utf-8')
col1, col2 = st.columns(2)
with col1:
    city = st.multiselect('選擇想要顯示的**縣市**...', cost.columns, default=["年別", "新北市", "臺北市", "桃園市", "臺中市", "臺南市", "高雄市"])

with col2:
    year_range = st.slider('選擇想要顯示的**年份**...', cost['年別'].unique()[0], cost['年別'].unique()[-1], (109, 111), step=1)
    year = [i for i in range(year_range[0], year_range[1]+1, 1)]

st.subheader(f'表1：民國 {year_range[0]} 至 {year_range[1]} 年', divider='grey')
cost_select = cost[cost["年別"].isin(year)][city]
st.write(cost_select)
st.divider()

# setup fonts for display mandarin characters
font_manager.fontManager.addfont(font_file)
matplotlib.rcParams['font.family'] = ['jf-openhuninn-2.0', 'sans-serif']

# 長條圖
st.pyplot(cost_select.plot(x='年別', kind='bar',title='長條圖').legend(bbox_to_anchor=(1.0, 1.0), fontsize='small').figure)
st.divider()

# 堆疊長條圖
st.pyplot(cost_select.plot(x='年別', kind='bar',title='堆疊長條圖', stacked=True).legend(bbox_to_anchor=(1.0, 1.0), fontsize='small').figure)
st.divider()

# 面積圖
st.pyplot(cost_select.plot(x='年別', kind='area',title='面積圖', stacked=False).legend(bbox_to_anchor=(1.0, 1.0), fontsize='small').figure)
st.divider()

# 堆疊長條圖
st.pyplot(cost_select.plot(x='年別', kind='area',title='堆疊面積圖', stacked=True).legend(bbox_to_anchor=(1.0, 1.0), fontsize='small').figure)
st.divider()

# 折線圖
st.pyplot(cost_select.plot(x='年別', kind='line',title='折線圖').legend(bbox_to_anchor=(1.0, 1.0), fontsize='small').figure)
st.divider()

# 折線圖，變換線條形式
st.pyplot(cost_select.plot(x='年別', kind='line',title='折線圖-o', style='-o').legend(bbox_to_anchor=(1.0, 1.0), fontsize='small').figure)
st.divider()

# 折線圖，指定線條形式
st.pyplot(cost_select.plot(x='年別', kind='line',title='折線圖，指定線題形式', style={"臺北市":"-."}).legend(bbox_to_anchor=(1.0, 1.0), fontsize='small').figure)
st.divider()