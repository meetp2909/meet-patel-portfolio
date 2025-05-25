from bs4 import BeautifulSoup
import json

# Step 1: Read the HTML file
with open("index.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Step 2: Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Step 3: Find all <a> tags
a_tags = soup.find_all("a")

# Step 4: Extract text and href
scraped_links = []
for tag in a_tags:
    text = tag.get_text(strip=True)
    href = tag.get("href", "")
    scraped_links.append({"text": text, "href": href})

# Step 5: Save to JSON file
with open("scraped_links.json", "w", encoding="utf-8") as json_file:
    json.dump(scraped_links, json_file, indent=4)

# Step 6: Save to TXT file
with open("scraped_links.txt", "w", encoding="utf-8") as txt_file:
    for item in scraped_links:
        txt_file.write(f"{item['text']} - {item['href']}\n")

# Step 7: Print to console
print("✅ Scraping complete.")
print("🔗 Links found:")
for item in scraped_links:
    print(f"{item['text']} --> {item['href']}")
