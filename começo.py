import kagglehub

# Download latest version
path = kagglehub.dataset_download("teocalvo/teomewhy-loyalty-system")

print("Path to dataset files:", path)

import pandas as pd

df = pd.read_csv("Datasets\customers.csv")
print(df)