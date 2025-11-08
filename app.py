from flask import Flask, render_template, request
import requests
import urllib.parse
app = Flask(__name__)
API_KEY = "YOUR_SERPAPI_KEY_HERE"

def get_prices(query):
    """Fetch real-time Indian product data using SerpAPI (Google Shopping)."""
    url = "https://serpapi.com/search.json"
    params = {
        "engine": "google_shopping",
        "q": query,
        "location": "Bangalore, India",  # 🇮🇳 India-based results
        "gl": "in",                      # Country code = India
        "hl": "en",                      # Language = English
        "api_key": API_KEY
    }

    try:
        res = requests.get(url, params=params, timeout=10)
        data = res.json()
    except Exception as e:
        print("Error fetching data:", e)
        return []

    results = []

    for item in data.get("shopping_results", [])[:15]:
        # Get link (prefer product_link, fallback to link)
        link = item.get("product_link") or item.get("link", "")

        # Clean Google redirect URLs (so they open real stores)
        if "google.com" in link and "url=" in link:
            parsed = urllib.parse.parse_qs(urllib.parse.urlparse(link).query)
            link = parsed.get("url", [link])[0]

        # Add ₹ symbol if missing
        price = item.get("price")
        if price and not price.startswith("₹"):
            price = f"₹ {price}"

        results.append({
            "title": item.get("title"),
            "source": item.get("source"),
            "price": price or "₹ N/A",
            "link": link,
            "image": item.get("thumbnail")
        })

    # In case no data found
    if not results:
        results.append({
            "title": "No results found for this item.",
            "source": "—",
            "price": "₹ —",
            "link": "#",
            "image": "https://via.placeholder.com/150"
        })

    return results


@app.route("/")
def home():
    """Show search page."""
    return render_template("index.html")


@app.route("/compare", methods=["POST"])
def compare():
    """Handle search request and display product list."""
    product = request.form["product"]
    results = get_prices(product)
    return render_template("results.html", product=product, results=results)


if __name__ == "__main__":
    app.run(debug=True)
