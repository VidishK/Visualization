import pandas as pd
import plotly.express as px

# Load your CSV
df = pd.read_csv("golf_stats.csv")

# Print columns to inspect
print(df.columns)

# Let's plot SG: Approach the Green for each golfer:
metric = "SG: Approach the Green"
row = df[df["Metric"] == metric].iloc[0]
golfer_names = df.columns[1:]
values = row[1:].astype(float)  # convert from string to float if needed

fig = px.bar(x=golfer_names, y=values, labels={"x": "Golfer", "y": metric})

# Save the figure as an image
fig.write_image("plot.png")  # <--- ADD THIS LINE HERE

fig.show()
