import requests
from bs4 import BeautifulSoup
import json

url = "https://www.shl.com/solutions/products/product-catalog/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

cards = soup.find_all("a")

data = []

for card in cards:
    title = card.get_text(strip=True)
    link = card.get("href")

    if title and link:
        if "/products/" in link:

            if not link.startswith("http"):
                link = "https://www.shl.com" + link

            data.append({
                "name": title,
                "url": link
            })

# remove duplicates
unique_data = []
seen = set()

for item in data:
    if item["url"] not in seen:
        seen.add(item["url"])
        unique_data.append(item)

with open("catalog.json", "w", encoding="utf-8") as f:
    json.dump(unique_data, f, indent=4)

print(f"Saved {len(unique_data)} assessments")