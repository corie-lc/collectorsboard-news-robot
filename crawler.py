import requests
from bs4 import BeautifulSoup
import create_post



def check_duplicate(username, text):
    robot_posts = create_post.get_user_posts(username)

    for item in robot_posts:
        if text in item[5]:
            return True
    
    return False
    


def pokemon_news_robot():

    news_dict = {}

    URL = "https://www.pokeguardian.com/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    for item in soup.find_all("article", {"class": "jw-news-post"}):
        tdTags = item.find_all("h2", {"class": "jw-news-post__title"})
        for tag in tdTags:
            if check_duplicate("PokemonRobot",str(tag.text).replace("  ", "")) == False:    
                create_post.create_post("PokemonTCG", "null", "PokemonRobot", str(tag.text).replace("  ", ""), "on", "PokemonTCG", "no data", "no data", "no data", "no data") 


