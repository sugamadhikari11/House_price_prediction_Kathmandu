from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get('https://basobaas.com/search?q=kathmandu')

# Wait for the page to load
time.sleep(5)

#clicking loadmore button
button = driver.find_element(By.ID, "loadingBtn")

for i in range (40):
    button.click()
    time.sleep(2)

html = driver.page_source

# Pass the HTML through BeautifulSoup for parsing
soup = BeautifulSoup(html, 'html.parser')

print("Page Title:", soup.title.text)

# find the a tag with class name
a_tag = soup.find_all('a', class_="property-card")

# extracting the link
links = []
for a in a_tag:
    links.append(a['href'])

# creating CSV of the links
df = pd.DataFrame({
    "Link": links
})

# Save DataFrame to CSV
df.to_csv("basobaas_ktm.csv", index=False)

# Close the WebDriver
driver.quit()
