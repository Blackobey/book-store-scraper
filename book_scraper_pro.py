import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

all_books = []
book_elements = soup.find_all('article', class_='product_pod')

for book in book_elements:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').get_text()
    all_books.append({'Title': title, 'Price': price})
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
file_path = os.path.join(desktop_path, 'books_list.csv')

df = pd.DataFrame(all_books)
df.to_csv(file_path, index=False)

print(f"Done! Check your Desktop for books_list.csv")