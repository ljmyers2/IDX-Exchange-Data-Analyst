import pandas as pd
import glob
from pathlib import Path

all_files = glob.glob("C:/Users/lilly/IDX Exchange Fall 2026/csv/*.csv") #finds all csv files in folder
file_list = [pd.read_csv(file) for file in all_files] #creates list of dataframes from each file

folder_path = Path("C:/Users/lilly/IDX Exchange Fall 2026/csv/")
file_count = sum(1 for item in folder_path.iterdir() if item.is_file())
print(file_count)

total_rows = []
for file, df in zip(all_files, file_list): #adds number of rows of each dataframe to a list
    total_rows.append(len(df))

print(f"Total Rows: {sum(total_rows)}") #returns total number of rows: 1451277 rows

files = pd.concat(file_list, ignore_index = True) #concatenates all dataframes into one dataframe
files = files[files["PropertyType"] == "Residential"] #filters dataframe to only include residential properties

print(f"Number of total residential data: {len(files)}") #returns rows of residential listings: 945193 rows

sold_files = glob.glob("C:/Users/lilly/IDX Exchange Fall 2026/csv/CRMLSSold*.csv") #finds all sold files 
sold_list = [pd.read_csv(file) for file in sold_files] #creates list of dataframes from sold

sold_rows = []
for file, df in zip(sold_files, sold_list): #adds number of rows of each sold dataframe to a list
    sold_rows.append(len(df))

print(f"Total Sold Rows: {sum(sold_rows)}") #returns total of rows of sold data: 603958 rows

sold = pd.concat(sold_list, ignore_index = True) #concatenates sold dataframes into one
sold = sold[sold["PropertyType"] == "Residential"] #filters sold dataframe to residential only

print(f"Number of residential solds: {len(sold)}") #returns number of rows of residential sold data:  405917

listing_files = glob.glob("C:/Users/lilly/IDX Exchange Fall 2026/csv/CRMLSListing*.csv") #finds all listing files
listing_list = [pd.read_csv(file) for file in listing_files] #creates list of dataframes from listing

listing_rows = []
for file, df in zip(listing_files, listing_list): #adds number of rows of each listing dataframe to a list
    listing_rows.append(len(df))

print(f"Total Listing Rows: {sum(listing_rows)}") #returns total of rows of listing data: 847319 rows

listing = pd.concat(listing_list, ignore_index = True) #concatenates listing dataframes into one
listing = listing[listing["PropertyType"] == "Residential"] #filters listing dataframe to residential only

print(f"Number of residential listings: {len(listing)}") #returns number of rows of residential listing data: 539276 rows

#before and after concatenation check: 603958 + 847319 = 1451277

#before and after filtering for residential properties: 405917 + 539276 = 945193