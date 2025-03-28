# HW7
Take the code that was written in class for K-means and make it work for a 3D data sets. Using the Spotify_ YouTube.csv data set, read in the following three columns: Liveness, Energy, Loudness. Using an elbow graph, find the optimal number of K and use that to visualize the data and groups based on that K. Graphs should be appropriately labeled with an x, y, and z axis along with a title and legend. Then write what your results might mean to you.

Then, take each of the individual columns and run hierarchical clustering on them. Are there any? distinct groups. If so, how would you define each group? Graphs should be appropriately labeled. Then write what your results might mean to you.

Grading (Out of 100 points)
• 70 points: Cover what you did to update the code to work for 3D data and visualization along with what number of K you found to be optimal and the graphs showing the results of running K-means and what your results mean.
• 30 points: Report your findings for running Hierarchical clustering.

How to turn in
Turn in the final report and code that you wrote to Githbub




# Spotify-YouTube Clustering Analysis

This project performs clustering analysis on music tracks from a Spotify-YouTube dataset. It includes both **3D K-means clustering** and **1D hierarchical clustering** using the features: `Liveness`, `Energy`, and `Loudness`.

## Contents

- `kmeans_hierarchical_analysis.py` – Python script for running all analysis and saving visual outputs.
- `Spotify_Youtube.csv` – The dataset used.

## Methodology

### K-means Clustering (3D)
- Selected features: **Liveness**, **Energy**, **Loudness**
- Used the **Elbow Method** to determine optimal `K = 3`
- Visualized results in a **3D scatter plot** with clusters color-coded

### Hierarchical Clustering (1D)
- Applied individually to each feature
- Used dendrograms to identify group separation
- Cut the tree at 2 clusters to analyze distinctions


### Final Report

K-means Clustering

We applied K-means clustering on the Liveness, Energy, and Loudness features from the dataset. After standardizing the data, we used the elbow method to determine the optimal number of clusters. The elbow graph indicated that K=3 was ideal.

We visualized the K-means results in a 3D plot, where three distinct clusters emerged:

One group represents high-energy, loud tracks with live performance qualities.

Another includes quieter, lower-energy tracks, likely studio recordings.

The third cluster is a mid-range group with average values across all three features.

This grouping can help categorize songs into mood or production-style-based playlists.

Hierarchical Clustering

We also performed hierarchical clustering on each feature separately:

Liveness: Formed two distinct clusters, differentiating live-like recordings from studio-like ones.

Energy: Clear division into high and low energy songs, which can be used to segment tracks by mood.

Loudness: Separated louder, more intense tracks from quieter ones.
