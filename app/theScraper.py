import requests
from bs4 import BeautifulSoup
import json



def get_books():
    r = requests.get('https://www.goodreads.com/list/show/9440.100_Best_Books_of_All_Time_The_World_Library_List')


    soup = BeautifulSoup(r.text, 'lxml')


    booklist = soup.find_all('a', {'class': 'bookTitle'})

    with open('all_books.txt', 'w') as f:
        for book in booklist:
            f.write(book['href']+'\n')



def get_book_data():
    '''
    We want to extract 
    book title
    author
    ratings
    genre.
    '''
    with open('all_books.txt') as f:
        bookList = f.readlines()

    all_data = []
    for idx, book in enumerate(bookList):
        print(f'Extracting data for book {idx+1}')
        r = requests.get('https://www.goodreads.com/'+ book)
        soup = BeautifulSoup(r.text, 'lxml')

        data = {
            'title': soup.find('h1', {'id':'bookTitle'}).text,
            'author':soup.find('span', {'itemprop':'name'}).text,
            'ratings': soup.find('span', {'itemprop':'ratingValue'}).text,
            'genre': soup.find('a', {'class':'actionLinkLite bookPageGenreLink'}).text
        }
        all_data.append(data)

        

    with open('result.json', 'w') as f:
        f.write((json.dumps(all_data)))

get_book_data()