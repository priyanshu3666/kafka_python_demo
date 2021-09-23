import requests,bs4
base_url = 'https://books.toscrape.com/catalogue/category/books_1/page-{}.html'



two_star_books =[]
for num in range(1,10):
    scrape_url = base_url.format(num)
    results = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(results.text,'lxml')
    books = soup.select('.product_pod')

    for book in books:
        if len(book.select('.star-rating.Two'))!=0:
            book_title = book.select('a')[1]['title']
            two_star_books.append(book_title)

