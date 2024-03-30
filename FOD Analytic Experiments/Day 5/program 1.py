import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

data = {
    'CustomerID': [1234, 1243, 1534],
    'TotalAmount': [4000, 5000, 3000],
    'FrequencyOfVisits': [3, 4, 3]
}

transaction_data = pd.DataFrame(data)

X = transaction_data[['TotalAmount', 'FrequencyOfVisits']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

k = 1

kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
kmeans.fit(X_scaled)

transaction_data['Cluster'] = kmeans.labels_

print(transaction_data)

plt.scatter(transaction_data['TotalAmount'], transaction_data['FrequencyOfVisits'], c=kmeans.labels_, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', label='Centroids')
plt.title('Clusters of Customers')
plt.xlabel('Total Amount')
plt.ylabel('Frequency of Visits')
plt.legend()
plt.show()
