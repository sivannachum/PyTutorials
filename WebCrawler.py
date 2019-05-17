import requests
from bs4 import BeautifulSoup
import DownloadImage


def spider(maxPages):
    page = 1
    while page <= maxPages:
        # Change the page we're looking at each time
        if page is 1:
            url = 'https://animals.howstuffworks.com/arachnids/spider.htm'
        else:
            url = 'https://animals.howstuffworks.com/arachnids/spider' + str(page-1) + '.htm'
        # Getting that html stuff that doesn't tell a human much
        sourceCode = requests.get(url)
        # Text, images, etc of a website
        plainText = sourceCode.text
        # BeautifulSoup needs data formatted in a special way to be able to sift through it easily
        soup = BeautifulSoup(plainText, features="html.parser")

        # Get the headings from the webpage
        for text in soup.findAll('div', {'class': 'article-media-body title-name'}):
            header = text.string
            print(header)
        # Some of the headings are under headers with numbers so let's get those too
        for text in soup.findAll('article', {'class': 'editorial-body infinite-container'}):
            headers = text.findAll('h1')
            headers = headers + text.findAll('h2')
            headers = headers + text.findAll('h3')
            for h in headers:
                print(h.string)

        # Get all the images on the page and save them
        for pic in soup.findAll('img', {'class': 'media-hero'}):
            url = pic.get('data-src')
            DownloadImage.downloadImage(url)

        page += 1


spider(10)