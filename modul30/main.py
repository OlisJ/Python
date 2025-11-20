from bs4 import BeautifulSoup

html_content = "<html><body><p>hello world</p></body></html>"

soup=BeautifulSoup(html_content, 'html.parser')

paragraph = soup.find('p').text

print(paragraph)