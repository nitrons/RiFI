import requests
from bs4 import BeautifulSoup

# link to our rss page
page = requests.get("https://www.hcl.hr/feed/")

# get content of the page
content = page.content

# parse the page content
soup = BeautifulSoup(content, "html.parser")

item = soup.find_all("item")

for element in item:
	# extract title, link, category, date
	title = element.title.string

	link = element.guid.string

	category = element.category.string

	date = element.pubdate.string
	
	print(title + "\n" + link + "\n" + category + "\n" + date + "\n")
