from bs4 import BeautifulSoup
# import lxml

with open("website.html", encoding='utf8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# soup = BeautifulSoup(contents, "lxml")

print(soup.title) # displays the whole tag HTML ; ie <title>ANGELA's WEBSITE</title>
print(soup.title.name) # name of the tag ; ie title
print(soup.title.string) # gets u the str contained in the title tag ; ie ANGELA's WEBSITE

print(soup) # prints the entire HTML
print(soup.prettify()) # prints the entire HTML but without any indents

print(soup.a) # prints the first anchor tag
print(soup.p) # prints the first paragraph tag

all_a_tags = soup.find_all(name="a") # prints all anchor tags of our HTML file

for tag in all_a_tags:
    print(tag.getText()) # gets the text of each anchor tag
    print(tag.get("href")) # gets all the links in each anchor tag

print(soup.find(name="h1", id="name")) # finds and prints the first element with the info
print(soup.find(name="h3", class_="heading").getText()) # we use class_

print(soup.select_one(selector="p a")) # to get the anchor tag which is inside paragraph tag
print(soup.select_one("#name")) # gets the element with id "name"
print(soup.select_one(".heading")) # gets the first element with class "heading"
print(soup.select(".heading")) # gets all the elements with class "heading" in a list format