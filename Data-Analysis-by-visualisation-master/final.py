import pandas as pd
import csv
import plotly.graph_objects as pgo

data = pd.read_csv("/Users/new/Downloads/Data-Analysis-by-visualisation-master/data.csv")

student_data = data.loc[data["student_id"] == "TRL_987"]

plot_data = pgo.Figure(pgo.Bar(
    x = student_data.groupby("level")["attempt"].mean(),
    y = ["Level1", "Level2", "Level3", "Level4"],
    orientation = "h"
))
plot_data.show()