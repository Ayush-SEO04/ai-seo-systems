# clustering_demo.py
"""
AI Keyword Clustering Demo

This script shows how AI embeddings can group keywords into meaningful clusters.
It's a minimal, educational example for SEO + AI applications.
"""

# ---------------------------
# Step 1: Sample keywords
# ---------------------------
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

print("Number of keywords:", len(keywords))

# ---------------------------
# Step 2: Generate embeddings
# ---------------------------
from sentence_transformers import SentenceTransformer

print("\nGenerating embeddings...")
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(keywords)

print("Embedding shape:", embeddings.shape)

# ---------------------------
# Step 3: Apply clustering
# ---------------------------
from sklearn.cluster import KMeans

num_clusters = 3
print(f"\nClustering into {num_clusters} groups...")

kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(embeddings)

print("\nCluster assignments:")
for i, keyword in enumerate(keywords):
    print(f"{keyword} -> Cluster {kmeans.labels_[i]}")
