# [GameScraper](https://mighty-oasis-10011.herokuapp.com/)
![](https://raw.githubusercontent.com/TR-1000/my_portfolio/master/projects/static/img/project3.png)

# What This App Does and Why I Built It:
GameScraper is a web application that scrapes the web for video game news and deals. When I first started learning Python and was looking for something to apply it to I had a hard time finding something that interested me and after a while, I stopped coding. Then as I was installing some addons on Kodi I noticed there was quite a lot of Python involved! And I also saw the Beautiful Soup logo. So then it dawned on me that maybe Beautiful Soup was used to scrape information about the various movies and television shows. I like to know the day, month, and year a movie came out or an episode of a show first aired. I really do enjoy data. And I also love videogames. So I wanted to combine that with my love for Python.

At this time GameScraper collects data from PC Gamer, Steam, The Verge, and Gamespot to get the latest news and deals. The search function collects data from Gamespot and RAWG API. It used to also utilized the Bing Web Search API but only during the 2-week trial.

# Challenges


```python
#Steam News Scrape
try:
    steam_news_page = requests.get("https://store.steampowered.com/",headers={"User-Agent":"Defined"})
    soup = BeautifulSoup(steam_news_page.text, "html.parser")
    steam_results = soup.find("div", {"id": "tab_specials_content"}).select("a")
    steam_news = []
    for result in steam_results[:10]:
        if "," in result.get("data-ds-appid"):
            app_split = result.get("data-ds-appid").split(",")
            app_id = app_split[0]
        else:
            app_id = result.get("data-ds-appid")
        steam_news.append({
            'url': result.get("href"),
            'image': f"https://steamcdn-a.akamaihd.net/steam/apps/{app_id}/header.jpg",
            'title': result.find("div", {"class": "tab_item_name"}).text,
            'original_prince': result.find("div", {"class": "discount_original_price"}).text,
            'price': result.find("div", {"class": "discount_final_price"}).text,
            'app_id': app_id
        })
except:
    steam_news = None
```



```python
# Gamespot Search
gamespot_search_page = requests.get("https://www.gamespot.com/search/?header=1&q=" + game_title,headers={"User-Agent":"Defined"})
gamespot_search_soup = BeautifulSoup(gamespot_search_page.content, "html.parser")
gamespot_search_results = gamespot_search_soup.select("li.media")
#print(gamespot_search_results)
gamespot_search = []
for result in gamespot_search_results:
    try:
        title = result.span.a.text
    except:
        title = ''
    try:
        url = "https://www.gamespot.com" + result.a.get('href')
    except:
        url = ''
    try:
        image = result.img.get('src')
    except:
        image = ''
    try:
        released = result.time.span.text
    except:
        released = ''
    try
        if result.p != None:
            description = result.p.text.strip()
            print(description)
    except:
        description = '
    try:
        gamespot_search.append({
            'title' : title,
            'url' : url,
            'image' : image,
            'released' : released,
            'description': description
            })
    except:
        gamespot_search.append({
            'title' : title,
            'url' : url,
            'image' : image,
            'released' : released,
            }
  
```


# Built With
* Python
* Django
* BeautifulSoup


# Issues
* Sometimes Amazon search requests don't got through the first time.


# Features I'd Like to Add
* Save scrape results to the database
* User login and ability to comment on other users favorites.
* Only the user who created the favorite can edit it.


# Help Along The Way
* [CommonLounge Web Development with Django Path](https://https://www.commonlounge.com//)
* [Stack Overflow](https://stackoverflow.com/)
* [W3Schools](https://www.w3schools.com/howto/howto_css_tooltip.asp)
