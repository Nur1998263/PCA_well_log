import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Download your file here
well_log_data = pd.read_csv("well_log_data_2.csv")

# Assume the first 50 rows are sandstone and the next 50 rows are shale
well_log_data['Rock_Type'] = ['Sandstone'] * 50 + ['Shale'] * 50

# Standardize the data (only the numerical columns)
scaled_data = StandardScaler().fit_transform(well_log_data[['Gamma_Ray', 'Density', 'Porosity']])

# Apply PCA technique
pca = PCA(n_components=2)  # Reduce to 2 principal components (2D scatter plot)
pca_data = pca.fit_transform(scaled_data)

# Convert PCA results to a DataFrame and add the 'Rock_Type' column
pca_df = pd.DataFrame(data=pca_data, columns=['PC1', 'PC2'])
pca_df['Rock_Type'] = well_log_data['Rock_Type']  # Use the generated 'Rock_Type' column

# Plot the PCA-transformed data, to distinguish sandstone from shale
plt.figure(figsize=(12, 6))
for rock_type, color in zip(['Sandstone', 'Shale'], ['blue', 'green']):
    subset = pca_df[pca_df['Rock_Type'] == rock_type]
    plt.scatter(subset['PC1'], subset['PC2'], alpha=0.7, label=rock_type, color=color)

# Adding some anomalous points manually to simulate anomalies in data
anomalous_points = np.array([[3.5, -3], [-3, 3.5], [2.5, 2.5]])  # Random anomalies
plt.scatter(anomalous_points[:, 0], anomalous_points[:, 1], color='r', marker='x', s=100, label='Anomalies')

# Labeling the plot
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA of Well Log Data: Sandstone vs Shale with Anomalies')
plt.legend()
plt.show()

