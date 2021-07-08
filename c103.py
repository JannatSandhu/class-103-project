import csv
import pandas as pd
import plotly.express as px

#scatter
db= pd.read_csv("Copy+of+data+-+data (3).csv")
fig= px.scatter(db,x="date",y="cases", color="country")
fig.show()