# clustering_viz.py
"""
AI Keyword Clustering with Visualization

This script extends the basic demo by adding PCA-based visualization.
"""

from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Sample keywords
keywords = [
    "digital marketing",
    "seo strategy",
    "content automation",
    "ai tools",
    "keyword clustering",
    "technical seo",
    "storytelling in marketing",
    "growth hacking",
    "link building",
    "search engine optimization"
]

# Generate embeddings
print("Generating embeddings...")
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(keywords)

# Cluster
num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(embeddings)

# PCA for 2D visualization
pca = PCA(n_components=2)
reduced = pca.fit_transform(embeddings)

plt.figure(figsize=(8, 6))
scatter = plt.scatter(reduced[:, 0], reduced[:, 1], c=kmeans.labels_, cmap="viridis", s=100)

# Annotate points
for i, keyword in enumerate(keywords):
    plt.annotate(keyword, (reduced[i, 0]+0.02, reduced[i, 1]+0.02))

plt.title("Keyword Clustering (PCA projection)")
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.colorbar(scatter, label="Cluster")
plt.show()
