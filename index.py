python
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
real_estate_data = pd.read_csv('abu_dhabi_real_estate.csv')

# Filter data for a specific year
year_data = real_estate_data[real_estate_data['Year'] == 2023]

# Analyze average property prices by neighborhood
average_prices = year_data.groupby('Neighborhood')['Property Price'].mean()

# Plot the average property prices
plt.figure(figsize=(10, 6))
average_prices.plot(kind='bar')
plt.title('Average Property Prices by Neighborhood in 2023')
plt.xlabel('Neighborhood')
plt.ylabel('Average Property Price')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
