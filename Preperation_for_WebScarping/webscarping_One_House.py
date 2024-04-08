#importing libraries
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
links = pd.read_csv('basobaas.csv')

#append the all list to base url and open in driver
url = baseURl + links['Link'][0]

#open the url in driver
driver.get(url)
time.sleep(3)
#getting the page source
html = driver.page_source
with open('index.html', 'w', encoding='utf-8') as file:
    file.write(html)
    
soup = BeautifulSoup(html, 'html.parser')

data = []

# print("Page Title:", soup.title.text)

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


lis = ['Address','Bedroom','Bathroom','Floor','Parking','Property Face','Build Year','Area Covered','Road Access','Build Up Area','Posted Date','Price']

df = pd.DataFrame(
    {
        "Indexes":lis,
        "Values":[address,bedroom,bathroom,floor,parking,property_face,build_year,area_covered,road_access,build_up_area,posted, price]
    }
)

df.to_csv("Home.csv",index=False)

# Close the WebDriver
driver.quit()





