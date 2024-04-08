import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np
import os

# Load the dataset
df = pd.read_csv('roaddistanceupdate.csv')

# Preprocess the 'Area Covered' column to fill NaN with an empty string
df['Area Covered'] = df['Area Covered'].fillna('')

# Use TF-IDF Vectorizer to convert 'Area Covered' text data into numerical data
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['Area Covered'])

# Determine the optimal number of clusters using the elbow method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=np.random.randint(1000))
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# Find the number of clusters where the decrease in WCSS begins to slow down (elbow point)
k_optimal = np.argmax(np.diff(wcss)) + 2

# Apply KMeans clustering with the optimal number of clusters
kmeans = KMeans(n_clusters=k_optimal, random_state=np.random.randint(1000))
kmeans.fit(X)

# Add the cluster labels to the dataframe
df['Cluster'] = kmeans.labels_

# Create a directory for clustered CSV files if it doesn't exist
clustered_dir = 'clustered_files'
if not os.path.exists(clustered_dir):
    os.makedirs(clustered_dir)

# Save each cluster to a separate CSV file
for cluster_label in df['Cluster'].unique():
    cluster_df = df[df['Cluster'] == cluster_label]
    cluster_df.to_csv(f'{clustered_dir}/cluster_{cluster_label}.csv', index=False)

print(f"The dataset has been successfully clustered into {k_optimal} clusters based on the unique structure of the 'Area Covered' column and saved to separate CSV files in the '{clustered_dir}' directory.")
