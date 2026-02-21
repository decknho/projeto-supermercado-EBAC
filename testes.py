import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv("supermercado.csv")

df.head(10)

(df['Categoria']).value_counts()