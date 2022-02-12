import csv
import pandas as pd
import plotly.graph_objects as pgo

data = pd.read_csv("/Users/new/Downloads/Data-Analysis-by-visualisation-master/data.csv")
print(data.groupby(["level", "student_id"])["attempt"].mean())

plot_data = pgo.Figure(pgo.Bar(
    x = data.groupby("level")["attempt"].mean(),
    y = ["Level1", "Level2", "Level3", "Level4"],
    orientation = 'h'
))

plot_data.show()