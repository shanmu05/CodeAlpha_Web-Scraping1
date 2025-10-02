# task1_scraper.py
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Step 1: Choose the target website
base_url = "http://books.toscrape.com/catalogue/page-{}.html"

# Step 2: Prepare storage
books_data = []

# Step 3: Loop through multiple pages (pagination)
for page in range(1, 4):  # scrape first 3 pages as sample
    url = base_url.format(page)
    print(f"Scraping page: {url}")
    response = requests.get(url)
    
    # Step 4: Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.select("article.product_pod")
    
    # Step 5: Extract info
    for book in books:
        title = book.h3.a["title"]
        price = book.select_one(".price_color").get_text(strip=True)
        stock = book.select_one(".availability").get_text(strip=True)
        
        books_data.append({
            "title": title,
            "price": price,
            "availability": stock
        })
    
    # Step 6: Be polite (sleep between requests)
    time.sleep(1)

# Step 7: Save dataset
df = pd.DataFrame(books_data)
df.to_csv("books_dataset.csv", index=False)
print(" Scraping complete! Saved to books_dataset.csv")
df = pd.read_csv("books_dataset.csv")
print(df.head())        # shows first 5 rows
print(df.shape)         # shows number of rows and columns
