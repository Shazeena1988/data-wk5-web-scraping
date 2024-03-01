from bs4 import BeautifulSoup
import requests
import pandas as pd

rating_to_int = {
    "One" : 1,
    "Two" : 2,
    "Three" : 3,
    "Four" : 4,
    "Five" : 5,
}

title_collection = []
price_collection = []
rating_collection = []

for page_num in range(1, 51):
    html_text = requests.get(f'http://books.toscrape.com/catalogue/page-{page_num}.html').text
    soup = BeautifulSoup(html_text, 'lxml')
    titles = soup.find_all('h3')

    for book_title in titles:
        print("Title : ", book_title.find('a').get('title').strip())
        title_collection.append(book_title.find('a').get('title').strip())
        price = book_title.find_next('p', class_="price_color")
        
        print("Price: ", price.text.strip('Â'))
        price_collection.append(float(price.text.strip('Â£')))
        
        rating = book_title.find_previous('p', class_='star-rating').get('class')[1]
        print(rating_to_int.get(rating))
        rating_collection.append(rating_to_int.get(rating))

df = pd.DataFrame({
    "Title" : title_collection,
    "Price": price_collection,
    "Rating / 5" : rating_collection
})

# print(df)

# df.to_excel("Books.xlsx", index=False)

#ACTIVITY 2

df = pd.read_excel("Books.xlsx")
# print(df)

max_book_price = df["Price"].max()
# print(max_book_price)

four_star_books = df.query("`Rating / 5` == 4")
# print("Number of books printed 4 stars:")
# print(four_star_books.shape[0])

mean_book_price = df ["Price"].mean()
print(mean_book_price)