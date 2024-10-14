import pandas as pd

# Define the data
data = {"data": [[0.4, 0.6]]}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save DataFrame to a CSV file
df.to_csv('test_data.csv', index=False, header=False, quoting=1)  # quoting=1 adds quotes around the JSON-like format
