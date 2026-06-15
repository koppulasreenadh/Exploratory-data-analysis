import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Set random seed for consistency
np.random.seed(42)

# Generate realistic data
num_rows = 500
categories = ["Electronics", "Clothing", "Home & Kitchen", "Books", "Beauty"]
days = [datetime(2026, 1, 1) + timedelta(days=int(i)) for i in np.random.randint(0, 90, num_rows)]

data = {
    "Order_ID": 1000 + np.arange(num_rows),
    "Order_Date": days,
    "Category": np.random.choice(categories, num_rows, p=[0.3, 0.25, 0.2, 0.15, 0.1]),
    "Total_Sales": np.round(np.random.exponential(scale=150, size=num_rows) + 10, 2),
    "Customer_Age": np.random.randint(18, 70, num_rows)
}

df = pd.DataFrame(data)

# Inject some missing values and duplicates to test your cleaning pipeline
df.loc[df.sample(frac=0.05).index, 'Customer_Age'] = np.nan
df = pd.concat([df, df.head(5)], ignore_index=True)

# Save the dataset
df.to_csv("mock_sales_data.csv", index=False)
print("-> Success: 'mock_sales_data.csv' has been generated with 505 records!")