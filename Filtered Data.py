import pandas as pd

sold = pd.read_csv("sold.csv", low_memory = False)
listing = pd.read_csv("listing.csv", low_memory = False)

# Dataset Undertanding

print("\n Sold Dataset: ")

print(f"First 5 rows:\n{sold.head()}")

print(f"Columns: {sold.columns}")

print(f"Dimensions: {sold.shape}") #603,958 x 85

print(f"Data types:\n{sold.dtypes}")

print(f"Unique Property Types in Sold Data: {sold['PropertyType'].unique()}")

solds = sold[sold["PropertyType"] == "Residential"]

print(f"Filtered Residential Sold Data: {solds.shape}")

print(f"Null Count in Filtered Sold Data:\n{solds.isna().sum()}")

print("\n Listing Dataset: ")

print(f"First 5 rows:\n{listing.head()}")

print(f"Columns: {listing.columns}")

print(f"Dimensions: {listing.shape}") #847,319, 85

print(f"Data types:\n{listing.dtypes}") 

print(f"Unique Property Types in Listing Data: {listing['PropertyType'].unique()}")

listings = listing[listing["PropertyType"] == "Residential"]

print(f"Filtered Residential Listing Data: {listings.shape}")

print(f"Null Count in Filtered Listing Data:\n{listings.isna().sum()}")


# Missing Value Analysis

null_count_sold = solds.isna().sum()
null_percentage_sold = null_count_sold / len(solds) * 100

null_sold_df = pd.DataFrame({
    'Null Count': null_count_sold,
    'Null Percentage': null_percentage_sold
})

null_sold_df = null_sold_df.sort_values(by='Null Percentage', ascending=False)
print(f"Missing Value Summary for Sold Data: \n{null_sold_df}")
    
high_null_sold_columns = null_sold_df[null_sold_df['Null Percentage'] > 90]
print(f"Number of columns with more than 90% null values: {len(high_null_sold_columns)}")
print(f"Columns with more than 90% null values:\n{high_null_sold_columns}")

null_count_listing = listings.isna().sum()
null_percentage_listing = null_count_listing / len(listings) * 100

null_listing_df = pd.DataFrame({
    'Null Count': null_count_listing,
    'Null Percentage': null_percentage_listing
})

null_listing_df = null_listing_df.sort_values(by='Null Percentage', ascending=False)
print(f"Missing Value Summary for Listing Data: \n{null_listing_df}")
    
high_null_listing_columns = null_listing_df[null_listing_df['Null Percentage'] > 90]
print(f"Number of columns with more than 90% null values: {len(high_null_listing_columns)}")
print(f"Columns with more than 90% null values:\n{high_null_listing_columns}") 

null_sold_df.to_csv("sold_null_summary.csv")
null_listing_df.to_csv("listing_null_summary.csv")

# Numeric Distribution Review

numeric_fields = ['ClosePrice', 'LivingArea', 'DaysOnMarket']

sold_distribution_summary = solds[numeric_fields].describe(percentiles=[.25, .5, .75, .9, .95, .99]).T
print(f"Numeric Distribution Summary for Sold Data: \n{sold_distribution_summary}")

listing_distribution_summary = listings[numeric_fields].describe(percentiles=[.25, .5, .75, .9, .95, .99]).T
print(f"Numeric Distribution Summary for Listing Data: \n{listing_distribution_summary}")

sold_distribution_summary.to_csv("sold_numeric_distribution_summary.csv")
listing_distribution_summary.to_csv("listing_numeric_distribution_summary.csv")

# Data Visualization

import matplotlib.pyplot as plt

for column in numeric_fields:
    plt.figure(figsize=(8,5))
    plt.hist(solds[column].dropna(),bins = 30)
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.title(f"Distribution of {column} in Sold Data")
    plt.show()

    plt.figure(figsize=(8,5))
    plt.boxplot(solds[column].dropna())
    plt.xlabel(column)
    plt.ylabel("Value")
    plt.title(f"Boxplot of {column} in Sold Data")
    plt.show()

for column in numeric_fields:
    plt.figure(figsize=(8,5))
    plt.hist(listings[column].dropna(),bins = 30)
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.title(f"Distribution of {column} in Listing Data")
    plt.show()

    plt.figure(figsize=(8,5))
    plt.boxplot(listings[column].dropna())
    plt.xlabel(column)
    plt.ylabel("Value")
    plt.title(f"Boxplot of {column} in Listing Data")
    plt.show()

print(f"Top 10 largest values in Sold ClosePrice:\n{solds['ClosePrice'].nlargest(10)}")
print(f"Top 10 largest values in Sold LivingArea:\n{solds['LivingArea'].nlargest(10)}")
print(f"Top 10 largest values in Sold DaysOnMarket:\n{solds['DaysOnMarket'].nlargest(10)}")

print(f"Top 10 smallest values in Sold ClosePrice:\n{solds['ClosePrice'].nsmallest(10)}")
print(f"Top 10 smallest values in Sold LivingArea:\n{solds['LivingArea'].nsmallest(10)}")
print(f"Top 10 smallest values in Sold DaysOnMarket:\n{solds['DaysOnMarket'].nsmallest(10)}")

print(f"Top 10 largest values in Listing ClosePrice:\n{listings['ClosePrice'].nlargest(10)}")
print(f"Top 10 largest values in Listing LivingArea:\n{listings['LivingArea'].nlargest(10)}")
print(f"Top 10 largest values in Listing DaysOnMarket:\n{listings['DaysOnMarket'].nlargest(10)}")

print(f"Top 10 smallest values in Listing ClosePrice:\n{listings['ClosePrice'].nsmallest(10)}")
print(f"Top 10 smallest values in Listing LivingArea:\n{listings['LivingArea'].nsmallest(10)}")
print(f"Top 10 smallest values in Listing DaysOnMarket:\n{listings['DaysOnMarket'].nsmallest(10)}")

# No obvious outliers in Sold ClosePrice
# Possible outlier in Sold LivingArea : Index 329133, Value 17021321
# Possible outlier in Sold DaysOnMarket: Index 148252, Value 12430, strange negative values?

# No obvious outliers in Listing ClosePrice 
# Possible outlier in Listing LivingArea: Index 490091, Value 17021321
# Strange negative values in Listing DaysOnMarket

