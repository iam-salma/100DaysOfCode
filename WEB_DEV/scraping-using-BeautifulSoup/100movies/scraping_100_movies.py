from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "html.parser")

movies = soup.find_all(name="h3", class_="title")   # DON'T USE THIS : movies = soup.select(".title")
movie_titles_rev = [title.getText() for title in movies]
movie_titles = movie_titles_rev[::-1] # for n in range(len(movie_titles)-1: -1: -1)
                                      #     print(movie_titles[n])

with open("movies.txt", mode="w", encoding='utf-8') as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")
