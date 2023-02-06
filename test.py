import requests
from bs4 import BeautifulSoup

url = "https://app.prizepicks.com/"

# send a request to the website
response = requests.get(url)

# parse the html content
soup = BeautifulSoup(response.content, "html.parser")

# find all the elements with class .projection .proj-container .player-container .player .name
player_names = soup.select(".projection .proj-container .player-container .player .name")

# extract the player names from the elements and print them
for name in player_names:
    print(name.text)

print(soup.select("title"))