# Price Comparison Website (Flask Project)

This is a simple price comparison website built using Python and Flask.  
It shows real-time product prices from Google Shopping through the SerpAPI.

When you search for a product (for example “iPhone 15” or “Realme Phone”), the website shows:
- Product name  
- Price in Indian Rupees (₹)  
- Website name (Amazon, Croma, Reliance Digital, etc.)  
- A “View Deal” button that opens the real product page  

It’s a small but useful project that demonstrates how Flask can work with real APIs.

## How it works
1. The user types a product name on the home page.
2. The Flask app sends the name to SerpAPI.
3. SerpAPI returns product information from Google Shopping.
4. The app displays the products with their names, prices, and links.

Basically, it works like a mini price search engine for real products.

## Technologies used
- Python (Flask) for the backend
- HTML, CSS, Bootstrap for the frontend
- SerpAPI (Google Shopping API) to get real product data
- Requests and JSON for handling API data
- urllib.parse for cleaning URLs
- Git and GitHub for version control

## Project files
- app.py → main Flask application
- scraper.py → handles API requests and cleans data
- templates/ → HTML pages (index, results, and base layout)
- static/css/style.css → for custom styling
- requirements.txt → list of libraries used

## How to run the project
1. Install all dependencies:
   pip install -r requirements.txt

2. Run the Flask app:
   python app.py

3. Open your browser and go to:
   http://127.0.0.1:5000

Then type any product name to see live results.

## About this project
I created this project to learn how Flask works with REST APIs.  
It connects with SerpAPI (Google Shopping API) and shows live data in Indian Rupees (₹).  
The results are updated automatically based on what’s currently available online.
