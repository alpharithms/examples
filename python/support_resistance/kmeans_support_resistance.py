import statistics

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import plotly.express as px
import plotly.graph_objs as go

"""
Step 1: Import CSV data as Pandas Dataframe
"""

# Load local CSV file and parse into dataframe object
btc = pd.read_csv('BTC-USD.06282017-06282022.csv')

# Parse date as DateTime
btc['Date'] = pd.to_datetime(btc['Date'])

# Set the date as the index
btc.set_index(['Date'], inplace=True)

"""
Step 2: Convert to NumPy array, perform KMeans
"""
# Convert adjusted closing price to numpy array
btc_prices = np.array(btc["Adj Close"])
# print("BTC Prices:\n", btc_prices)

# Perform cluster analysis
K = 10
kmeans = KMeans(n_clusters=K).fit(btc_prices.reshape(-1, 1))

# predict which cluster each price is in
clusters = kmeans.predict(btc_prices.reshape(-1, 1))
print("Clusters:\n", clusters)

"""
Step 3: Plot clusters in Plotly
"""
pd.options.plotting.backend = 'plotly'

# Define 6 colors for our 6 clusters
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo']

# Create Scatter plot, assigning each point a color where
# point group = color index.
fig = btc.plot.scatter(
    x=btc.index,
    y="Adj Close",
    color=[colors[i % len(colors)] for i in clusters],
)

# Make it pretty
layout = go.Layout(
    plot_bgcolor='#efefef',
    showlegend=False,
    # Font Families
    font_family='Monospace',
    font_color='#000000',
    font_size=20,
    xaxis=dict(
        rangeslider=dict(
            visible=False
        ))
)
fig.update_layout(layout)
# fig.show()

"""
Finding minimum and maximum values in each cluster
"""
# Create list to hold values, initialized with infinite values
min_max_values = []

# init for each cluster group
for i in range(K):

    # Add values for which no price could be greater or less
    min_max_values.append([np.inf, -np.inf])

print(min_max_values)

# Get min/max for each cluster
for i in range(len(btc_prices)):

    # Get cluster assigned to price
    cluster = clusters[i]

    # Compare for min value
    if btc_prices[i] < min_max_values[cluster][0]:
        min_max_values[cluster][0] = btc_prices[i]

    # Compare for max value
    if btc_prices[i] > min_max_values[cluster][1]:
        min_max_values[cluster][1] = btc_prices[i]

"""
Graph Cluster Min/Max lines
"""
import plotly.graph_objects as go

# Again, assign an arbitrary color to each of the 6 clusters
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo']

# Create Scatter plot, assigning each point a color where
# point group = color index.
# fig = btc.plot.scatter(
#     x=btc.index,
#     y="Adj Close",
#     color=[colors[i] for i in clusters],
# )

# # Add horizontal lines
# for cluster_min, cluster_max in min_max_values:
#     fig.add_hline(y=cluster_min, line_width=1, line_color="blue")
#     fig.add_hline(y=cluster_max, line_width=1, line_color="blue")
#
# # Add a trace of the price for better clarity
# fig.add_trace(go.Trace(
#     x=btc.index,
#     y=btc['Adj Close'],
#     line_color="black",
#     line_width=1
# ))
#
# # Make it pretty
# layout = go.Layout(
#     plot_bgcolor='#efefef',
#     showlegend=False,
#     # Font Families
#     font_family='Monospace',
#     font_color='#000000',
#     font_size=20,
#     xaxis=dict(
#         rangeslider=dict(
#             visible=False
#         ))
# )
# fig.update_layout(layout)


"""
Combine Cluster Min/Max values by sorting, averaging, then ploting again
"""
print("Initial Min/Max Values:\n", min_max_values)

# Create container for combined values
output = []

# Sort based on cluster minimum
s = sorted(min_max_values, key=lambda x: x[0])
print("Sorted Min/Max Values:\n", s)

# For each cluster get average of
for i, (_min, _max) in enumerate(s):

    # Append min from first cluster
    if i == 0:
        output.append(_min)

    # Append max from last cluster
    if i == len(min_max_values) - 1:
        output.append(_max)

    # Append average from cluster and adjacent for all others
    else:
        output.append(sum([_max, s[i+1][0]]) / 2)
print("Filtered min/max:\n", output)


# Again, assign an arbitrary color to each of the 6 clusters
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo']

# Create Scatter plot, assigning each point a color where
# point group = color index.
fig = btc.plot.scatter(
    x=btc.index,
    y="Adj Close",
    color=[colors[i % len(colors)] for i in clusters],
)

# Add horizontal lines
for cluster_avg in output[1:-1]:
    fig.add_hline(y=cluster_avg, line_width=1, line_color="blue")

# Add a trace of the price for better clarity
fig.add_trace(go.Trace(
    x=btc.index,
    y=btc['Adj Close'],
    line_color="black",
    line_width=1
))

# Make it pretty
layout = go.Layout(
    plot_bgcolor='#efefef',
    showlegend=False,
    # Font Families
    font_family='Monospace',
    font_color='#000000',
    font_size=20,
    xaxis=dict(
        rangeslider=dict(
            visible=False
        ))
)
fig.update_layout(layout)
# fig.show()

"""
Elbow method for selecting optimal cluster count
"""
# values = []
# K = range(1, 10)
# for k in K:
#     kmeans_n = KMeans(n_clusters=k)
#     kmeans_n.fit(btc_prices.reshape(-1, 1))
#     values.append(kmeans_n.inertia_)


# fig = go.Figure()
#
# fig.add_trace(go.Trace(
#     x=list(K),
#     y=values,
#     line_color="black",
#     line_width=1
# ))
#
# # Make it pretty
# layout = go.Layout(
#     plot_bgcolor='#efefef',
#     showlegend=False,
#     # Font Families
#     font_family='Monospace',
#     font_color='#000000',
#     font_size=20,
#     xaxis=dict(
#         rangeslider=dict(
#             visible=False
#         ))
# )
# fig.update_layout(layout)
# fig.show()


"""
Get cluster counts
"""
cluster_counts = {}
for c in clusters:
    if c in cluster_counts:
        cluster_counts[c] += 1
    else:
        cluster_counts[c] = 1

# Get cluster counts in sorted order
cluster_counts = {k: v for k, v in sorted(cluster_counts.items(), key=lambda x: x[0])}
print("Cluster Counts:\n", cluster_counts)

# get statistics
mean = statistics.mean(cluster_counts.values())
stdev = statistics.stdev(cluster_counts.values())
print("mean:", mean)
print('stdev:', stdev)

# Filter for 1/2 stddev
kept_clusters = [c for c, v in cluster_counts.items() if v > mean - .5 * stdev]
print("kept:", kept_clusters)

# Again, assign an arbitrary color to each of the 6 clusters
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo']

# Create Scatter plot, assigning each point a color where
# point group = color index.
fig = btc.plot.scatter(
    x=btc.index,
    y="Adj Close",
    color=[colors[i % len(colors)] for i in clusters],
)

# Add horizontal lines
for kept_cluster in kept_clusters:
    fig.add_hline(y=output[kept_cluster], line_width=1, line_color="blue")

# Add a trace of the price for better clarity
fig.add_trace(go.Trace(
    x=btc.index,
    y=btc['Adj Close'],
    line_color="black",
    line_width=1
))

# Make it pretty
layout = go.Layout(
    plot_bgcolor='#efefef',
    showlegend=False,
    # Font Families
    font_family='Monospace',
    font_color='#000000',
    font_size=20,
    xaxis=dict(
        rangeslider=dict(
            visible=False
        ))
)
fig.update_layout(layout)
fig.show()





