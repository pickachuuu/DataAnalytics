import pandas as pd
import plotly.express as px

# Get or Load Data set
bar_df = pd.read_csv("bar_assignment.csv")

# Transform 'COUNT': 1 -> "Yes", 0 -> "No"
bar_df["COUNT"] = bar_df["COUNT"].map({1: "Yes", 0: "No"})

# Aggregate counts for stacked bar plot
bar_plot_data = bar_df.groupby(["LABEL", "COUNT"]).size().unstack(fill_value=0)

# Create a horizontal stacked bar chart using Plotly
fig_bar = px.bar(
    bar_plot_data,
    orientation='h',
    title="Horizontal Stacked Bar Chart",
    labels={"value": "Count", "LABEL": "Category"},
)

# Update layout for consistent font and styling
fig_bar.update_layout(
    font=dict(family="Arial", size=12),
    barmode="stack"
)

# Show bar chart
fig_bar.show()
