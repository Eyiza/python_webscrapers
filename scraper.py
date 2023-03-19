import requests
from bs4 import BeautifulSoup
import csv
import json
import re


'''
This is a Python program to scrape book information from Book Depository.
The program scrapes the following information for each book:
- Book Title
- Author
- Price
- Average Rating
- Number of Ratings
- Product URL
Once the book information is scraped, it is saved to a CSV file using the csv library and also to a json file using the json library.
'''

def scrape(url):
    response = requests.get(url) # making a request
    response_text = response.text # getting the html

    soup = BeautifulSoup(response_text, 'html.parser')

    books = soup.findAll('div', class_ = 'item-info') # getting info of all the books

    scraped_books = [] # empty list to store the scraped books
    count = 0 

    for book in books:
        # if count == 10:
        #     break
        title_element = book.find('h3', class_ = 'title')
        title = title_element.text.strip()

        author = book.find('p', class_ = 'author').text.strip()

        price_element = book.find('p', class_ = 'price')
        price = price_element.find('span').text.strip('US')

        product_url = url + title_element.find('a').attrs.get('href').strip('?ref=grid-view')

        # Make a new request to the product page
        product_response = requests.get(product_url)
        product_soup = BeautifulSoup(product_response.text, 'html.parser')
        
        rating = product_soup.find('span', attrs={'itemprop': 'ratingValue'}) # Extract the book rating
        num_ratings = product_soup.find('span', class_='rating-count') # Extract the number of ratings

        if rating is None:
            continue

        rating = rating.text.strip()
        num_ratings = num_ratings.text.strip()
        num_ratings = re.sub('[^0-9]', '', num_ratings) # Remove the non-numeric characters from the number of ratings
        
        scraped_books.append({
        "title": title,
        "author": author,
        "price": price,
        "rating": rating,
        "number_of_ratings": num_ratings,
        "product_url": product_url
        })
        count += 1

        # print(f"Title: {title} \nAuthor: {author} \nPrice: {price} \nRating: {rating} \nNumber_of_ratings: {num_ratings} \nProduct URL: {product_url}\n")


    # writing the scraped data to a csv file
    with open('book_info.csv', 'w', newline='') as f:
        w = csv.DictWriter(f,['title', 'author', 'price', 'rating', 'number_of_ratings', 'product_url'])
        w.writeheader()
        w.writerows(scraped_books) # writing the scraped data to a csv file


    # writing the scraped data to a json file
    with open ('book_info.json', 'w') as file: # writing the scraped data to a json file
        books_as_json = json.dumps({
            'books': scraped_books,
            'number_of_books': len(scraped_books)
        }, indent = 4, sort_keys = True)
        file.write(books_as_json) # writing the json data to the file


url = 'https://www.bookdepository.com'
scrape(url) 