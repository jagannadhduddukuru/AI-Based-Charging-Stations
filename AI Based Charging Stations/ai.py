import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from geopy.distance import great_circle

# Sample data: EV demand points (latitude, longitude)
ev_demand_points = np.array([
    [37.7749, -122.4194],  # San Francisco
    [34.0522, -118.2437],  # Los Angeles
    [40.7128, -74.0060],   # New York
    [41.8781, -87.6298],   # Chicago
    [47.6062, -122.3321]   # Seattle
])

# Number of charging stations to place
num_stations = 3

# Applying K-Means clustering to find optimal locations
kmeans = KMeans(n_clusters=num_stations, random_state=42, n_init=10)
kmeans.fit(ev_demand_points)
optimal_locations = kmeans.cluster_centers_

# Displaying optimized charging station locations
print("Optimal Charging Station Locations (Latitude, Longitude):")
for loc in optimal_locations:
    print(f"{loc[0]:.4f}, {loc[1]:.4f}")
