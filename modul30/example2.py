from bs4 import BeautifulSoup

html_content = """
<html>
<head>
    <title>Page</title>
</head>
<body>
    <h1>Welcome to bs4</h1>
    <p class="Intro">BeautifulSoup makes web scraping easy</p>
    <div id="content">
        <p>Here are some links :</p>
        <a href="https://example.com/page1">Link 1</a>
        <a href="https://example.com/page2">Link 2</a>
        <a href="https://example.com/page3">Link 3</a>
    </div>


</body>
</html>

"""


soup=BeautifulSoup(html_content, 'html.parser')
print("Title of the document:", soup.title.text)

intro_tetxt = soup.find('p', class_='Intro').text
print("Intro paragraph:", intro_tetxt)

div_content = soup.find('div', id='content')
links = div_content.find_all('a')
for link in links:
    print("Link:",link['href'])

first_link=soup.find("a")
print("First link text:", first_link.text)
print("Next sibling of the first link:", first_link.next_sibling.text)

paragraphs = soup.select('div#content  p')
for paragraph in paragraphs:
    print("Paragraph in content div:", paragraph.text)

new_tag=soup.new_tag('b')
new_tag.string="Importatnt"
soup.h1.append(new_tag)

print("Modified h1 tag:", soup.h1)
