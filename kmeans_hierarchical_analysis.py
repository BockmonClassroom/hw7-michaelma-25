import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import Axes3D
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

# Load dataset
df = pd.read_csv("Data/Spotify_Youtube.csv")

# Select features
features = df[['Liveness', 'Energy', 'Loudness']].dropna()

# Standardize features for K-means
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Elbow method for optimal K
inertia = []
K_range = range(1, 11)
for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_features)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(K_range, inertia, marker='o')
plt.title('Elbow Method For Optimal K')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia')
plt.grid(True)
plt.savefig("elbow_plot.png")
plt.close()

# K-means clustering with optimal K=3
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(scaled_features)
features_with_clusters = features.copy()
features_with_clusters['Cluster'] = clusters

# 3D Scatter plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(
    features_with_clusters['Liveness'],
    features_with_clusters['Energy'],
    features_with_clusters['Loudness'],
    c=features_with_clusters['Cluster'],
    cmap='viridis',
    s=50
)
ax.set_title('3D K-means Clustering (K=3)')
ax.set_xlabel('Liveness')
ax.set_ylabel('Energy')
ax.set_zlabel('Loudness')
legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
ax.add_artist(legend1)
plt.savefig("kmeans_3d_plot.png")
plt.close()

# Hierarchical clustering on individual features
for feature in ['Liveness', 'Energy', 'Loudness']:
    Z = linkage(features[[feature]], method='ward')
    plt.figure(figsize=(10, 5))
    dendrogram(Z, truncate_mode='lastp', p=20, leaf_rotation=45., leaf_font_size=12.)
    plt.title(f'Hierarchical Clustering Dendrogram for {feature}')
    plt.xlabel('Sample Index or (Cluster Size)')
    plt.ylabel('Distance')
    plt.savefig(f'dendrogram_{feature}.png')
    plt.close()
