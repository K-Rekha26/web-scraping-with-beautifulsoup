import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Fetch Webpage Content
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
response = requests.get(url)
html_content = response.content

# Step 2: Parse HTML Content
soup = BeautifulSoup(html_content, 'html.parser')

# Step 3: Extract Relevant Information
tables = soup.find_all('table', class_='wikitable')

# Define a function to extract data from each table
def extract_data(table):
    data = []
    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all(['th', 'td'])
        row_data = [cell.text.strip() for cell in cells]
        if row_data:
            data.append(row_data)
    return data

# Extract data from each table
table_data = [extract_data(table) for table in tables]

# Step 4: Store Data
# Save data to CSV file
with open('countries_gdp.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for i, data in enumerate(table_data):
        writer.writerow([f'Table {i + 1}'])
        for row in data:
            writer.writerow(row)
        writer.writerow([])  # Add an empty row between tables
