import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

import streamlit as st
import folium

import folium

st.set_page_config(page_title="選択式サイドバー", page_icon=":map:", layout="wide")

# データフレームを作成
data = {'選択肢': ['選択肢1', '選択肢2', '選択肢3', '選択肢4'],
        'latitude': [35.681167, 35.689487, 35.691704, 35.709823],
        'longitude': [139.767052, 139.774803, 139.774503, 139.811614]}
df = pd.DataFrame(data)

# 左側に選択肢を表示
selected_option = st.sidebar.selectbox("選択してください", df['選択肢'])

# 右側に地図を表示
selected_row = df.loc[df['選択肢'] == selected_option]
latitude, longitude = selected_row[['latitude', 'longitude']].values[0]
m = folium.Map(location=[latitude, longitude], zoom_start=12)
st.write(m)





# 地図を表示する関数
def show_map(location):
    map = folium.Map(location=location, zoom_start=13)
    return map

# 場所のリスト
locations = [
    [37.7749, -122.4194],
    [40.7128, -74.0060],
    [35.6895, 139.6917],
    [51.5074, -0.1278]
]

# 場所のラベル
labels = [
    "San Francisco",
    "New York",
    "Tokyo",
    "London"
]

# サイドバーに表示する選択式
selected_location = st.sidebar.selectbox("Select a location", labels)

# 選択された場所
location = locations[labels.index(selected_location)]

# 右側に地図を表示する
st.header("Location: " + selected_location)
st.write(show_map(location))


# サイドバーに表示する項目
options = ['Option 1', 'Option 2', 'Option 3']

# サイドバーで選択された項目
selected_option = st.sidebar.selectbox('Select an option', options)

# 選択された項目に対応するデータフレーム
if selected_option == 'Option 1':
    df = pd.DataFrame(np.random.rand(10, 2), columns=['A', 'B'])
elif selected_option == 'Option 2':
    df = pd.DataFrame(np.random.rand(20, 3), columns=['A', 'B', 'C'])
else:
    df = pd.DataFrame(np.random.rand(5, 5), columns=['A', 'B', 'C', 'D', 'E'])

# 右側に選択された項目に対応するグラフを表示
st.line_chart(df)



st.title('streamlit入門')

st.write('DataFrame')


df = pd.DataFrame({
    '1列目': [1,2,3,4],
    '2列目': [10,20,30,40]
})

st.write(df)

#動的なテーブル
st.dataframe(df.style.highlight_max(axis=0),width=500, height=500)

#静的なテーブル
st.table(df)

"""
# 大
## 中
### 小

"""

ds = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b', 'c' ]
)

st.line_chart(ds)

st.area_chart(ds)

st.bar_chart(ds)


dg = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69, 139.70],
    columns=['lat','lon']
)

st.map(dg)


if st.checkbox('show image'):
     img = Image.open('/Users/yuhei-aihara/Downloads/#7-rev-2023-01-07-00_00_2023-01-07-23_59_Sentinel-2_L2A_True_color.png')
     st.image(img, caption='yuhei aihara', use_column_width=True)

option = st.selectbox(
        'あなたな好きな数字を教えてください',
        list(range(1,11))
)

'あなたの好きな数字は、', option, 'です'


text = st.sidebar.text_input('あなたの趣味を教えてください')
'あなたの趣味', text

condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション', condition

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右からむ')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')


st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)


import time 

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(1)