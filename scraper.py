import requests
from bs4 import BeautifulSoup

def get_amazon_price(product):
    url = f"https://www.amazon.in/s?k={product.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    results = []
    for item in soup.select(".s-result-item")[:5]:
        name = item.select_one("h2 a span")
        price = item.select_one(".a-price-whole")
        link = item.select_one("h2 a")
        if name and price and link:
            results.append({
                "name": name.text.strip(),
                "price": price.text.strip(),
                "link": "https://www.amazon.in" + link['href']
            })
    return results or [{"name": "No result found", "price": "-", "link": "#"}]

def get_flipkart_price(product):
    url = f"https://www.flipkart.com/search?q={product.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    results = []
    for item in soup.select("._1AtVbE")[:5]:
        name = item.select_one("._4rR01T")
        price = item.select_one("._30jeq3")
        link = item.select_one("a")
        if name and price and link:
            results.append({
                "name": name.text.strip(),
                "price": price.text.strip(),
                "link": "https://www.flipkart.com" + link['href']
            })
    return results or [{"name": "No result found", "price": "-", "link": "#"}]
