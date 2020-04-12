from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Game
from . forms import GameForm
from . game_soup import get_steam_deals, get_verge_gaming, get_pcgamer_news, get_techspot
# from django.core.cache import cache
from bs4 import BeautifulSoup
import requests
import json


################################################################################
# HOME VIEW
################################################################################

@cache_page(60*35) # number of sec. til cache expires (60 secs time 60 mins )
@csrf_protect
def home(request):

    # Verge gaming news
    try:
        verge_articles = get_verge_gaming()
    except:
        verge_articles = None



    #Steam News Scrape
    try:
        steam_news = get_steam_deals()
    except:
        steam_news = None



    #Techspot News
    try:
        techspot_articles = get_techspot()
    except:
        techspot_articles = None



    #PC Gamer News
    try:
        pcgamer_news = get_pcgamer_news()
    except:
        pcgamer_news = None


    # Return and render results to template
    return render(request, 'games_index.html',{
        'search' : False,
        'pcgamer_news': pcgamer_news,
        'steam_news': steam_news,
        'verge_articles' : verge_articles,
        'techspot_articles': techspot_articles,
    })


################################################################################
# FAVORITES VIEW
################################################################################

def favorites(request):
    form = GameForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            form.save()
            return redirect('favorites')
    games = Game.objects.all().order_by('-id')
    return render(request, 'favorites.html', {'form': form, 'games': games})


################################################################################
# SEARCH
################################################################################

def search(request):

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
            try:
                if result.p != None:
                    description = result.p.text.strip()
                    print(description)
            except:
                description = ''

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
                    })


        #Steam search scrape
        try:
            steam_search_page = requests.get("https://store.steampowered.com/search/?term=" + game_title,headers={"User-Agent":"Defined"})
            steam_search_soup = BeautifulSoup(steam_search_page.content, "html.parser")
            steam_search_results = steam_search_soup.select("a.search_result_row")
            steam_search = []
            #print(results)
            for result in steam_search_results[:8]:
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
        except:
            steam_search = None


        #Amazon scrape search request
        amazon_page = requests.get("https://www.amazon.com/s?k="+ game_title +"&rh=n%3A468642&dc&qid=1578698986&rnid=2941120011&ref=sr_nr_n_1", headers={"User-Agent":"Defined"})
        amazon_soup = BeautifulSoup(amazon_page.content, "html.parser")
        amazon_results = amazon_soup.select("div.s-result-list.s-search-results.sg-row")
        try:
            results = amazon_results[0].select("div.a-section.a-spacing-medium")
            amazon_search = []
            for result in results:
                title = result.h2.text
                image = result.img.get('src')
                url = "https://www.amazon.com" + result.a.get('href')
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

        except:
            amazon_search = None



        #rawg api data request
        rawg_api_response = requests.get(f'https://api.rawg.io/api/games?page_size=1&search={game_title}')
        try:
            rawg_api = json.loads(rawg_api_response.content)
        except:
            rawg_api = None

        #Return and render results to template
        return render(request, 'search.html', {
                                                        'search': True,
                                                        'game_title' : game_title,
                                                        'rawg_api': rawg_api,
                                                        'amazon_search': amazon_search,
                                                        'steam_search': steam_search,
                                                        'gamespot_search': gamespot_search
                                                    })

    else:
        return redirect('home') # Redirect to home() view



################################################################################
# UPDATE VIEW
################################################################################

def update(request, game_id):
    games = Game.objects.all().order_by('-id')
    game = Game.objects.get(pk=game_id)
    form = GameForm(request.POST or None, instance=game)
    if form.is_valid():
        form.save()
        return redirect(favorites)

    else:
        form = GameForm(instance=game)

    return render(request, 'update.html', {'form': form, 'games': games})



################################################################################
# DELETE
################################################################################

def delete(request, game_id):
    game = Game.objects.get(pk=game_id)
    game.delete()
    messages.success(request, ("Game has been removed from your favorites"))
    return redirect(favorites)
