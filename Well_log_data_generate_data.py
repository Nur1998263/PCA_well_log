import numpy as np
import pandas as pd

# Generate synthetic well log data for sandstone and shale
np.random.seed(42)  # For reproducibility,

# Sandstone: Low gamma ray, high porosity, moderate density
sandstone_gamma_ray = np.random.normal(40, 10, 50)  # Mean 40, std dev 10
sandstone_density = np.random.normal(2.4, 0.1, 50)  # Mean 2.4, std dev 0.1
sandstone_porosity = np.random.normal(20, 3, 50)    # Mean 20, std dev 3

# Shale: High gamma ray, low porosity, high density
shale_gamma_ray = np.random.normal(80, 10, 50)      # Mean 80, std dev 10
shale_density = np.random.normal(2.6, 0.1, 50)      # Mean 2.6, std dev 0.1
shale_porosity = np.random.normal(10, 2, 50)        # Mean 10, std dev 2

# Combine data into a single DataFrame
gamma_ray = np.concatenate([sandstone_gamma_ray, shale_gamma_ray])
density = np.concatenate([sandstone_density, shale_density])
porosity = np.concatenate([sandstone_porosity, shale_porosity])

well_log_data = pd.DataFrame({
    'Gamma_Ray': gamma_ray,
    'Density': density,
    'Porosity': porosity,
})
# Convert DataFrame to csv file
well_log_data.to_csv("well_log_data_2.csv", index = False)
