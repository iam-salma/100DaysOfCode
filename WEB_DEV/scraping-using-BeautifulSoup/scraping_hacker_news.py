from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()
yc_web_pg = response.text

soup = BeautifulSoup(yc_web_pg, "html.parser")
article_list = soup.find_all(name="span", class_="titleline") # article_list = soup.select(".titleline")
score_txt = soup.select(".score") # score_txt = soup.find_all(name="span", class_="score")
articles, links, scores = [], [], []

for article, score in zip(article_list, score_txt):
    anchor_tag = article.select_one(selector="span a")
    articles.append(anchor_tag.getText())
    links.append(anchor_tag.get("href"))
    points = int(score.getText().split(" ")[0])
    scores.append(points)

print(articles)
print(links)
print(scores)

largest_no_of_upvotes = max(scores)
index = scores.index(largest_no_of_upvotes)
print(articles[index])
print(links[index])
