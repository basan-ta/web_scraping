from bs4 import BeautifulSoup
import requests

giftmandu_url = "https://www.giftmandu.com/occasions/birthday/"

response = requests.get(giftmandu_url)
html = response.text
print(html)


