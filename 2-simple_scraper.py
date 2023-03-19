import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.geeksforgeeks.org/')

soup = BeautifulSoup(req.content, 'html.parser')

# Print the prettified version of the soup
print(soup.prettify())

# Get the title of the page
print(soup.title)

# Print the soup without any tags
print(soup.get_text())

