# [GameScraper](https://mighty-oasis-10011.herokuapp.com/)
![](https://github.com/TR-1000/GameScraper/blob/master/staticfiles/img/GameCapture.PNG?raw=true)

# What This App Does and Why I Built It:
GameScraper is a web application that scrapes the web for video game news and deals. When I first started learning Python and was looking for something to apply it to I had a hard time finding something that interested me and after a while, I stopped coding. Then as I was installing some addons on Kodi I noticed there was quite a lot of Python involved! And I also saw the Beautiful Soup logo. So then it dawned on me that maybe Beautiful Soup was used to scrape information about the various movies and television shows. I like to know the day, month, and year a movie came out or an episode of a show first aired. I really do enjoy data. And I also love videogames. So I wanted to combine that with my love for Python.

At this time GameScraper collects data from PC Gamer, Steam, The Verge, and Techspot to aggregate the latest news and deals. The search function collects data from Gamespot and RAWG API. It used to also utilized the Bing Web Search API but only during the 2-week trial.

# Challenges

### Getting images from the Steam Specials tab
The images that are used on the steam home page are small. A lot smaller than what I wanted to display on my app. Resizing the images to make them bigger just made them blurry. So instead of extracting the images with Beautiful Soup, I extracted the games' Steam app id from the data-ds-appid attribute in the `<a>` tag:
    
```html
<a href="https://store.steampowered.com/app/275850/No_Mans_Sky/?snr=1_4_4__tab-Specials_1" class="tab_item app_impression_tracked focus" data-ds-appid="275850" data-ds-itemkey="App_275850" data-ds-tagids="[1100689,1695,1755,3834,3942,1662,3839]" data-ds-crtrids="[34051164]">
    ...
</a>
```
In this example, the app id is "275850", which is the game No Man's Sky.
![](https://github.com/TR-1000/GameScraper/blob/master/staticfiles/img/GameInspect.PNG?raw=true)

Once I found a way to extract app id's from the `<a>` tags it was only a matter of figuring out the proper way to construct the image URL. The header images for games on Steam all follow the same pattern. This is the header image URL for No Man's Sky: 
`https://steamcdn-a.akamaihd.net/steam/apps/275850/header.jpg?`

So after extraction the app id of each game all I needed to do was format the URL string to include the game app id:
```python
app_id = result.get("data-ds-appid")
image = f"https://steamcdn-a.akamaihd.net/steam/apps/{app_id}/header.jpg?"
```

That worked fine for maost games, but I ran into a problem. Some games had more than one app id in the data-ds-appid attribute. For instance The Witcher 3: Wild Hunt Game of the Year Edition had three app ids because it's comprised of three seperate apps, the base game and two DLC expansions, each with it's own id.

```html
<a href="https://store.steampowered.com/sub/124923/?snr=1_7_7_151_150_1" data-ds-packageid="124923" data-ds-appid="292030,378649,378648" data-ds-itemkey="Sub_124923" data-ds-tagids="[122,1695,1742,4166,5611,1684,21]" data-ds-descids="[1,5]" data-ds-crtrids="[32989758]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;sub&quot;,&quot;id&quot;:124923,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag  app_impression_tracked" data-search-page="1">
            <div class="col search_capsule">
    ...
</a>
```


After extraction I the ids all came back as one string: `"292030,378649,378648"` So I just refactored the code to split the string into a list and assign the first element of the list(which is the app id of the base game) to the app_id variable:
```python
if "," in result.get("data-ds-appid"):
    app_split = result.get("data-ds-appid").split(",")
    app_id = app_split[0]
else:
app_id = result.get("data-ds-appid")
```
It's not a perfect solution since I'd still like to get the image the Game of the Year edition, but this is a good workaround for now since the extracted title identified the game as the Game of the Year edition. 

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


One of the features I wanted for this app was the ability fo search for a game and get back information. I used the great RAWG API but I wanted to add results from GameSpot as well. They either didn't have an API or I just couldn't figure out how to use it. So I decided to just scrape the info I needed! 

The problem with GameSpot was that the HTML code was not always consistent across different games and my scraper would break when I would search for one game but be totally fine for another. This was very common when trying to get titles in particular but happened with the release date and description fields also. So I just wrapped every in try and except blocks. It's not pretty but so far nothings breaking. 

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
        description = '
    
    gamespot_search.append({
        'title' : title,
        'url' : url,
        'image' : image,
        'released' : released,
        'description': description
    })
    
  
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
