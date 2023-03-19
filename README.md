# Web Scraping in Python
This is a simple Python web scraper that can be used to extract data from websites. The scraper uses the [`requests`](https://pypi.org/project/requests/) library to make HTTP requests and the [`BeautifulSoup`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library to parse HTML.


## Installation

1. **Virtual Environment** - This keeps your dependencies for each project separate and organized. <br>
If you've not already installed virtualenv
```
pip install virtualenv
```

Initialize and activate a virtual environment called `env` using:
```
python -m venv env
source env/bin/activate
```

Note - In Windows, the `env` does not have a `bin` directory. Therefore, you'd use the analogous command shown below:
```
source env/Scripts/activate
```

2. **PIP Dependencies** - Once the virtual environment is setup and running, run the following command to install the required libraries:
```
pip install -r requirements.txt
```
All required packages are included in the `requirements` file. 


## Usage
The `scraper.py` file contains a python program to scrape book information from [Book Depository](https://www.bookdepository.com).
The program scrapes the following information for each book:
- Book Title
- Author
- Price
- Average Rating
- Number of Ratings
- Product URL <br>

Once the book information is scraped, it is saved to a [CSV file](./book_info.csv) using the csv library and also to a [json file](./book_info.json) using the json library.

To use the scraper, you can also modify the `scraper.py` file to extract the data that you need. The file contains a `scrape()` function that you can modify to extract the data that you need.
For example, if you wanted to extract the title of a webpage, you could modify the scrape() function as follows:

```
def scrape(url):
    # Make a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the title of the webpage
    title = soup.title.string

    # Return the title
    return title
```

You can then call the `scrape()` function with the URL of the webpage that you want to scrape:

```
title = scrape('https://www.example.com')
print(title)
```
This will output the title of the webpage.

## Run the application
To run the application, run the following command from your activated virtual environment: <br>
For Mac/Linux
```
python3 scraper.py
```
For Windows PowerShell:
```
python scraper.py
```



## Disclaimer
Please be aware that web scraping may be prohibited by some websites. Make sure to check the terms of service of the websites that you are scraping before doing so.