def scrape_single_book(single_book_url):
  single_book_info = requests.get(single_book_url)
  single_booksoup = BeautifulSoup(markup= single_book_info.content,parser="html.parser")

  single_book_data = dict()

  single_book_name = single_booksoup.find(name = 'h1').getText()
  single_book_data['Name of book'] = single_book_name

  description_tag = single_booksoup.find('meta', {'name': 'description'})
  if description_tag:
        single_book_description = description_tag.get('content').strip()
  else:
        single_book_description = "No description available."
    
  single_book_data['book description'] = single_book_description

  single_book_Product_info_table_content = single_booksoup.find_all(name = 'tr')
  for rw in single_book_Product_info_table_content:
    key = rw.find(name= 'th').getText()
    value = rw.find(name = 'td').getText()
    single_book_data[key] = value



  single_book_data['book image'] = single_booksoup.find(name = 'img').get('src')

  single_book_data['book URL'] = single_book_url

  return single_book_data

scrape_single_book('https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html')