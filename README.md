# [GameScraper](https://mighty-oasis-10011.herokuapp.com/)
![](https://github.com/TR-1000/GameScraper/blob/master/staticfiles/img/GameCapture.PNG?raw=true)

# What This App Does and Why I Built It:
GameScraper is a web application that scrapes the web for video game news and deals. 

When I first started learning Python and was looking for something to apply it to I had a hard time finding something that interested me. Then as I was installing some addons on Kodi I noticed there was quite a lot of Python involved! And I also saw the Beautiful Soup logo. So then it dawned on me that maybe Beautiful Soup was used to scrape information about the various movies and television shows and that inspired me to learn about web scraping. So for my capstone project I wanted to combine my interest in data collection and my love for videogames into a web application.

At this time GameScraper collects data from PC Gamer, Steam, The Verge, and Techspot to aggregate the latest news and deals. The search function collects data from Gamespot and the RAWG API. It used to also utilized the Bing Web Search API but only during my 2-week trial.

# Built With
* Python
* Django
* BeautifulSoup

# Challenges

### Getting images from the Steam specials tab
The images that are used on the steam home page are small. A lot smaller than what I wanted to display in my app. Resizing the images to make them bigger just made them blurry. So instead of extracting the image URL with Beautiful Soup, I extracted the games' Steam app id from the data-ds-appid attribute in the `<a>` tag and inserted them into a header url:

In this example, the app id is "275850", which is the game No Man's Sky.

![](https://github.com/TR-1000/GameScraper/blob/master/staticfiles/img/CaptureInspect.PNG?raw=true)

Once I found a way to get app id's from the `<a>` tags it was only a matter of figuring out the proper way to construct the image URL. The header images for games on Steam all follow the same pattern:

```html
https://steamcdn-a.akamaihd.net/steam/apps/THE GAME'S APP ID GOES HERE/header.jpg?
```

So all I needed to do was format the URL string to include the app id:
```python
app_id = result.get("data-ds-appid")
image = f"https://steamcdn-a.akamaihd.net/steam/apps/{app_id}/header.jpg?"
```

That worked fine for most games, but I ran into a problem. Some games had more than one app id in the data-ds-appid attribute. For instance, The Witcher 3: Wild Hunt Game of the Year Edition had three app ids because it's comprised of three separate apps, the base game, and two DLC expansions, each with its own id:

![](https://github.com/TR-1000/GameScraper/blob/master/staticfiles/img/CaptureInspectWitcher.png?raw=true)


After extraction, the ids all came back as one string: `"292030,378649,378648"` So I just refactored the code to split the string into a list and assigned the first element of the list(which is the app id of the base game) to the app_id variable:
```python
if "," in result.get("data-ds-appid"):
    app_split = result.get("data-ds-appid").split(",")
    app_id = app_split[0]
else:
app_id = result.get("data-ds-appid")
```
It's not a perfect solution since I'd still like to get the image the Game of the Year edition, but this is a good workaround for now since the extracted title identifies the game as the Game of the Year edition.

And here's how the complete code for the steam deals scrape as it appears in the views.py file of the app:
<br/>

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

### The Search:
![](https://github.com/TR-1000/GameScraper/blob/master/staticfiles/img/CaptureSearch.PNG?raw=true)


One of the features I wanted for this app was the ability to search for a game and get back information. I used the great RAWG API but I wanted to add results from GameSpot as well.

The problem with GameSpot was that the HTML code was not always consistent across different games and my scraper would break when I would search for one game but be totally fine for another. This was very common when trying to get titles in particular but happened with the release date and description fields also. So I just wrapped everything in try and except blocks. It's not pretty but so far nothings breaking. 

I plant to clean this up eventually:
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
        description = ''
    
    gamespot_search.append({
        'title' : title,
        'url' : url,
        'image' : image,
        'released' : released,
        'description': description
    })
    
  
```


# Issues
* Scrapers can and will break
* The search feature doesn't always return the expected results


# Features I'd Like to Add
* Move scraper code from views.py to seperate file and import it's function into views.py
* Save scrape results to the database
* User login and ability to comment on other users favorites.
* Only the user who created the favorite can edit it.


# Help Along The Way
* [CommonLounge Web Development with Django Path](https://https://www.commonlounge.com//)
* [Beautiful Soup Docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Stack Overflow](https://stackoverflow.com/)
* [W3Schools](https://www.w3schools.com/howto/howto_css_tooltip.asp)
