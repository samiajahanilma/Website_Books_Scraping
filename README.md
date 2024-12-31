# Website_Books_Scraping
Web scraping is a technique used to extract large amounts of data from websites. It involves programmatically visiting web pages and extracting information from them.

Creating a Repository where I have scraped book information like, name of book, description, genre, price, reviews,availability etc. from a e-commerce platform and the URl: https://books.toscrape.com/index.htmll which is designed using HRML & CSS.As per the current task, I have scraped around 1000 books, distributed on multiple pages(50 pages where each page contains 20 books). Here, I have used requests module here to fetch the content of webpage.Usually whenever we load some URL in browser it makes a GET request to that particular endpoint and then respected server responds with the HTML code for corresponding page. Also from bs4 library I have imported BeautifulSoup module parse the web content and allows user to extract data from specific tags. Also The urljoin method from urllib.parse module is a very popular and error-free way to convert  relative URL into complete absolute URL ( basicalling adding base URL of the server to each book URL). I have used multiple functions from those modules and libraries.

find(): This method is used to find the first tag that matches a given criteria. For example, soup.find('div') would find the first div tag in the HTML document. You can also pass attributes to refine the search, like soup.find('div', class_='example')
find_all(): Unlike find() , find_all() retrieves all tags that match the criteria. It's useful when you want to extract information from multiple tags of the same type. For example, soup.find_all('a') would return a list of all anchor tags in the document.
get() : pings the URL and returns with the corresonding details.
getText(): to get the text present between any tags.

There are 3 files in this repository where the first file contains python code on extracting a single books information of a page out of 20 books among 50 pages of the website, second file contains python code of scraping all 20 books of a page among 50 pages of the website.Finally, third one is a .py file on extracting all 20 books data fromm all 50 pages of the website.

