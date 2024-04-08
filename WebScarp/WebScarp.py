#importing Libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

# Initialize the WebDriver
driver = webdriver.Chrome()

baseURl = 'https://basobaas.com'

#GETTING THE URL
links = pd.read_csv('unmatched_links.csv')

#append the all list to base url and open in driver
urls = [baseURl + link for link in links['Link']]

# Initialize an empty list to store data dictionaries
all_data = []

# Iterate through the list of URLs
for url in urls:
    driver.get(url)
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Extracting data
    details = soup.find_all('div', class_="detail-cate")
    newvalue = soup.find_all('div', class_="value")
    price = newvalue[0].text.strip()
    bedroom = newvalue[1].text.strip()
    bathroom = newvalue[2].text.strip()
    floor = newvalue[3].text.strip()
    parking = newvalue[4].text.strip()
    address = soup.find('div', class_="address").text.strip()

    rows = details[1].find_all('div', class_="row")
    all_divs = str(rows)

    # Define patterns for each key-value pair
    patterns = {
        "property_face": r"<b>Property Face<!-- --> :</b> <!-- -->(.*?)<br",
        "build_year": r"<b>Build Year<!-- --> :</b> (.*?)<br",
        "area_covered": r"<b>Area Covered<!-- --> :</b> <!-- -->(.*?)<br",
        "road_access": r"<b>Road Access<!-- --> :</b> <!-- -->(.*?)<br",
        "build_up_area": r"<b>Build Up Area<!-- --> :</b> <!-- -->(.*?)<br",
        "posted": r"<b>Posted<!-- --> :</b> <!-- -->(.*?)</div>",
    }

    # Extract values using regular expressions
    extracted_values = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, all_divs, re.DOTALL)
        extracted_values[key] = match.group(1).strip() if match else ""

    property_face = extracted_values['property_face']
    build_year = extracted_values['build_year']
    area_covered = extracted_values['area_covered'].replace('<!-- -->', '')
    road_access = extracted_values['road_access'].replace('<!-- -->', '')
    build_up_area = extracted_values['build_up_area'].replace('<!-- -->', '')
    posted = extracted_values['posted']

    # Append data to the list
    all_data.append({
        "Address": address,
        "Bedroom": bedroom,
        "Bathroom": bathroom,
        "Floor": floor,
        "Parking": parking,
        "Property Face": property_face,
        "Build Year": build_year,
        "Area Covered": area_covered,
        "Road Access": road_access,
        "Build Up Area": build_up_area,
        "Posted Date": posted,
        "Price": price
    })

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(all_data)

# Save the DataFrame to a CSV file
df.to_csv("UpdateData.csv", index=False)