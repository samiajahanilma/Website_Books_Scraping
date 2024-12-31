import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

page_count = 1
data = []

while True:
  page_url = f"https://books.toscrape.com/catalogue/page-{page_count}.html"
  status = requests.get(page_url).status_code

  # break the loop if we exceed the total page count
  if status == 404:
    break
  
  def scrape_page(page_url):
    books_data = []
    page_content = requests.get(page_url).content
    page_soup = BeautifulSoup(markup=page_content, parser="html.parser")
    page_books = page_soup.find_all(name="li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
    for book in page_books:
      book_url = book.findChild(name="a").get("href")
      book_url = urljoin(base_url, book_url)

    def scrape_book(book_url):
      book_info = requests.get(book_url).content
      book_soup = BeautifulSoup(markup=book_info, parser="html.parser")
      book_data = {}
    
      name = book_soup.find(name="h1").getText()
      book_data['name'] = name

      description_tag = book_soup.find('meta', {'name': 'description'})
      if description_tag:
        book_description = description_tag.get('content').strip()
      else:
        book_description = "No description available."
    
      book_table_data = book_soup.find_all(name="tr")
      for row in book_table_data:
        key = row.find(name="th").getText()
        value = row.find(name="td").getText()
        book_data[key] = value
    
      book_data['url'] = book_url
      return book_data
  
    book_data = scrape_book(book_url)
    books_data.append(book_data)
    return books_data


  page_data = scrape_page(page_url)
  data.extend(page_data) # do not use .append() since the function returns a list
  print(f"Page: {page_count} is SUCCESSFULLY scraped")

  page_count += 1

page_data