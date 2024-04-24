import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select(".titleline a")
votes = soup.select(".score")
pure_links = []
for link in range(len(links)):
  if links[link].get("href")[0] == 'h':
    pure_links.append(links[link].get("href"))

final_list = []
vote_list = []

def get_highest_voted_news(limit):
  for i in range(len(votes)):
    vote_list.append(int(votes[i].contents[0].split(' ')[0]))
  final_list = list(zip(pure_links, vote_list))
  final_list = sorted(final_list, key=lambda x: x[1], reverse=True)
  for y in range(limit):
    print(f"Title: {links[y].getText()} Link: {final_list[y][0]} Votes: {final_list[y][1]}")

get_highest_voted_news(20)

