from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Game
from . forms import GameForm
from django.contrib.auth.decorators import login_required

def home(request):
    from bs4 import BeautifulSoup
    import requests
    import json
    import os

    # Bing API required modules.
    from azure.cognitiveservices.search.websearch import WebSearchAPI
    from azure.cognitiveservices.search.websearch.models import SafeSearch
    from msrest.authentication import CognitiveServicesCredentials

    if request.method == 'POST':
        #set variable for searched game
        game_title = request.POST['game_search']

        #Gamespot Search
        gamespot_search_page = requests.get("https://www.gamespot.com/search/?header=1&q=" + game_title,headers={"User-Agent":"Defined"})

        gamespot_search_soup = BeautifulSoup(gamespot_search_page.content, "html.parser")

        gamespot_search_results = gamespot_search_soup.select("li.media")
        #print(gamespot_search_results)

        gamespot_search = []

        for result in gamespot_search_results:
            title = result.span.a.text
            url = "https://www.gamespot.com" + result.a.get('href')
            image = result.img.get('src')
            released = result.time.span.text
            if result.p != None:
                description = result.p.text.strip()
            gamespot_search.append({
                'title' : title,
                'url' : url,
                'image' : image,
                'released' : released,
                'description': description
                })

        #Steam search scrape
        steam_search_page = requests.get("https://store.steampowered.com/search/?term=" + game_title,headers={"User-Agent":"Defined"})

        steam_search_soup = BeautifulSoup(steam_search_page.content, "html.parser")

        steam_search_results = steam_search_soup.select("a.search_result_row")

        steam_search = []

        #print(results)
        for result in steam_search_results:
            url = result.get('href')
            #print(url)
            image = result.img.get('src').replace('capsule_sm_120', 'header')
            #print(image)
            title = result.span.text
            #print(title)
            price_tag = result.select("div.search_price")
            price = price_tag[0].text.strip()
            #print(price)
            released_tag = result.select("div.search_released")
            released = released_tag[0].text
            #print(released)
            steam_search.append({
            'title' : title,
            'image' : image,
            'url' : url,
            'price' : price,
            'released' : released
            })


        #Amazon scrape search request
        amazon_page = requests.get("https://www.amazon.com/s?k=" + game_title + "&i=videogames&i=videogames&ref=nb_sb_noss",headers={"User-Agent":"Defined"})
        amazon_soup = BeautifulSoup(amazon_page.content, "html.parser")
        amazon_results = amazon_soup.select("div.s-result-list.s-search-results.sg-row")
        try:
            results = amazon_results[0].select("div.a-section.a-spacing-medium")
            amazon_search = []
            for result in results:
                title = result.h2.text
                image = result.img.get('src')
                url = result.a.get('href')
                price_span = result.select("span.a-offscreen")
                if price_span == []:
                    price = "NA"
                else:
                    price = price_span[0].text
                    #print(title)
                    #print(price)
                    amazon_search.append({
                    'title' : title,
                    'image' : image,
                    'url' : url,
                    'price' : price
                    })

        except Exception as error:
            amazon_search = None

        #rawg api data request
        rawg_api_response = requests.get(f'https://api.rawg.io/api/games?page_size=1&search={game_title}')
        try:
            rawg_api = json.loads(rawg_api_response.content)
        except Exception as error:
            rawg_api = "Error loading api data..."

        #Bing api request
        API_KEY = os.getenv("API_KEY")
        subscription_key = API_KEY
        assert subscription_key
        search_url = "https://api.cognitive.microsoft.com/bing/v7.0/search"
        headers = {"Ocp-Apim-Subscription-Key": subscription_key}
        params = {"q": game_title}
        bing_api_response = requests.get(search_url, headers=headers, params=params)
        bing_api_response.raise_for_status()
        # bing_api = bing_api_response.json()
        bing_api = json.loads(bing_api_response.content)

        ##########################################
        ##########################################
        ##########################################
        return render(request, 'games_index.html', {'search': True, 'game_title' : game_title, 'rawg_api': rawg_api, 'bing_api': bing_api, 'amazon_search': amazon_search, 'steam_search': steam_search, 'gamespot_search': gamespot_search})

    else:

        import requests
        from bs4 import BeautifulSoup

        #ign featured news scrape
        ign_page = requests.get("https://www.ign.com/",headers={"User-Agent":"Defined"})

        ign_soup = BeautifulSoup(ign_page.content, "html.parser")

        ign_results = ign_soup.select("article.jsx-1665423064.card")
        #print(steam_search_results)

        ign_news = []

        for result in ign_results:
            title = result.h3.text
            url = "https://www.ign.com" + result.a.get('href')
            image = result.img.get('src')
            ign_news.append({
                'title' : title,
                'url' : url,
                'image' : image
            })

        #Amazon Scrape
        amazon_page = requests.get("https://www.amazon.com/s?k=video+games&rh=n%3A468642&dc&qid=1568839232&rnid=2941120011&ref=sr_nr_n_1",headers={"User-Agent":"Defined"})

        amazon_soup = BeautifulSoup(amazon_page.content, "html.parser")

        amazon_featured = []

        amazon_results = amazon_soup.select("div.s-result-list.s-search-results.sg-row")
        results = amazon_results[0].select("div.a-section.a-spacing-medium")
        for result in results:
            title = result.h2.text
            image = result.img.get('src')
            url = "https://www.amazon.com/" + result.a.get('href')
            price_span = result.select("span.a-offscreen")
            if price_span == []:
                price = "Price NA"
            else:
                price = price_span[0].text
                amazon_featured.append({
                'title' : title,
                'image' : image,
                'url' : url,
                'price' : price
                })

        #Steam News Scrape
        steam_news_page = requests.get("https://store.steampowered.com/news/",headers={"User-Agent":"Defined"})
        soup = BeautifulSoup(steam_news_page.text, "html.parser")
        steam_news = []
        steam_results = soup.select("div.body")
        for result in steam_results:
            if result.a != None:
                url = result.a.get('href')
                title = result.text.strip()
                image = result.img.get('src')
                steam_news.append({
                'url' : url,
                'title' : title,
                'image' : image,
                })

        #Gamespot search
        gamespot_news_page = requests.get("https://www.gamespot.com/",headers={"User-Agent":"Defined"})
        gamespot_news_soup = BeautifulSoup(gamespot_news_page.content, "html.parser")
        gamespot_news_results = gamespot_news_soup.select("section.editorial.river.js-load-forever-container")
        #print(steam_search_results)
        gamespot_news = []

        article_section = gamespot_news_results[0]
        #print(article_section)
        gamespot_articles = article_section.select("article")
        #print(gamespot_articles)
        for result in gamespot_articles:
            title = result.h3.text
            url = "https://www.gamespot.com" + result.a.get('href')
            image = result.img.get('src')
            description = result.p.text
            gamespot_news.append({
                'title':title,
                'description':description,
                'url':url,
                'image':image,
            })

        ##########################################
        ##########################################
        ##########################################
        return render(request, 'games_index.html',
        {'search' : False, 'gamespot_news': gamespot_news, 'steam_news': steam_news, 'amazon_featured': amazon_featured, 'ign_news' : ign_news})

##############################################################################################################

def favorites(request):
    form = GameForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            form.save()
            messages.success(request, ("This game has been added to your favorites"))
            return redirect('favorites')
    games = Game.objects.all()
    return render(request, 'favorites.html', {'form': form, 'games': games})



##############################################################################################################

def update(request, game_id):
    games = Game.objects.all()
    game = Game.objects.get(pk=game_id)
    form = GameForm(request.POST or None, instance=game)
    if form.is_valid():
        form.save()
        return redirect(favorites)

    else:
        form = GameForm(instance=game)

    return render(request, 'update.html', {'form': form, 'games': games})

##############################################################################################################

def delete(request, game_id):
    game = Game.objects.get(pk=game_id)
    game.delete()
    messages.success(request, ("Game has been removed from your favorites"))
    return redirect(favorites)
