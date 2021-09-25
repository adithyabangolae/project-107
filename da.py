import csv
import pandas as pd
import plotly.graph_objects as pxg

df = pd.read_csv("data.csv")
print(df.groupby("level")["attempt"].mean())
fig = pxg.Figure(pxg.Scatter(
    x = df.groupby("student_id").mean(),
    y = ['Level 1','Level 2','Level 3','Level 4'],size="attempt"))

fig.show()
