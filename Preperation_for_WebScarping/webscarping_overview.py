from bs4 import BeautifulSoup
import re

# Read the HTML content from the file
with open('index.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Create a Beautiful Soup object
soup = BeautifulSoup(html_content, 'html.parser')

details = soup.find_all('div', class_="detail-cate")

# Find rows containing property information
rows = details[1].find_all('div', class_="row")
all_divs = ""
all_divs = str(rows)
print(all_divs)

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

print("Property Face:", property_face)
print("Build Year:", build_year)
print("Area Covered:", area_covered)
print("Road Access:", road_access)
print("Build Up Area:", build_up_area)
print("Posted:", posted)
