import pandas as pd
import plotly.express as px
import csv

file = pd.read_csv('data.csv')

mean = file.groupby(["student_id", "level"], as_index = False)["attempt"].mean()

figure = px.scatter(mean, x="student_id", y="level", size="attempt", color="attempt")
figure.show()
