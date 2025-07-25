# Import required libraries
from bs4 import BeautifulSoup  
import requests       
import json

# Target URL to scrape
giftmandu_url = "https://www.giftmandu.com/friendship-day-delight-chocolates-personalized-photo-treats-for-her/"

# Custom headers to mimic a real browser (optional but helps bypass bot protection)
HEADERS = {
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "upgrade-insecure-requests": "1",
    "user-agent": (
        "Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Mobile Safari/537.36"
    )
}

# Send an HTTP GET request to the website with headers
response = requests.get(giftmandu_url, headers=HEADERS)

# Parse the returned HTML using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Try to find a <script> tag with ID "main-content"
script_tag = soup.find("script", type="application/ld+json")
# Store and print the found script tag (or None if not found)
data = json.load(script_tag.string)
print(data['props']['pageProp']['data']['product']['price'].keys())



#we can make it more easier 
initial_data = data["props"]['PageProp']["InitialData"]["data"]
product_data = initial_data["product_data"]
reviews_data = initial_data.get("reviews", {})

product_info = {
    "price": product_data["priceInfo"]["currentPirce"]["price"],
    "review_count": reviews_data.get("totalReviewCount",0)
}

print(product_info)