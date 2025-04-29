import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Preview_Data (1).csv')

top_10_data = data.sort_values(by='aqi', ascending=False).head(10)

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']

plt.figure(figsize=(10, 6))
plt.bar(top_10_data['sitename'], top_10_data['aqi'], color=plt.cm.tab10.colors)

plt.title('Top 10 AQI 測站', fontsize=16)
plt.xlabel('測站名稱', fontsize=12)
plt.ylabel('AQI', fontsize=12)

plt.xticks(rotation=45, fontsize=10)
plt.tight_layout()

plt.show()