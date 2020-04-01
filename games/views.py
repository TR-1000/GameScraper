from django.views.decorators.cache import cache_page
from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Game
from . forms import GameForm
from django.contrib.auth.decorators import login_required

@cache_page(60*30)
def home(request):
    from bs4 import BeautifulSoup
    import requests
    import json
    import os

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
            if result.p != None:
                description = result.p.text.strip()

            gamespot_search.append({
                'title' : title,
                'url' : url,
                'image' : image,
                'released' : released
                })



        #Steam search scrape
        try:
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
        except Exception as error:
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

        except Exception as error:
            amazon_search = None
        print(amazon_search)




        #rawg api data request
        rawg_api_response = requests.get(f'https://api.rawg.io/api/games?page_size=1&search={game_title}')
        try:
            rawg_api = json.loads(rawg_api_response.content)
        except Exception as error:
            rawg_api = "Error loading api data..."

        return render(request, 'games_index.html', {'search': True, 'game_title' : game_title, 'rawg_api': rawg_api, 'amazon_search': amazon_search, 'steam_search': steam_search, 'gamespot_search': gamespot_search})

    else:
        ## LANDING PAGE ##
        import requests
        from bs4 import BeautifulSoup


        # Verge gaming news
        try:
            verge_gaming_page = requests.get("https://www.theverge.com/games",headers={"User-Agent":"Defined"})
            verge_gaming_soup = BeautifulSoup(verge_gaming_page.content,"html.parser")
            verge_gaming_articles = verge_gaming_soup.select("div.c-entry-box--compact.c-entry-box--compact--article")
            verge_articles = []
            for article in verge_gaming_articles[:6]:
                verge_articles.append({
                    'url': article.a.get("href"),
                    'image': article.find_all("img")[1].get("src"),
                    'title': article.h2.text,
                    'date': article.time.text.strip()
                })

        except Exception as error:
            verge_articles = None



        #Amazon Featured
        try:
            amazon_page = requests.get("https://www.amazon.com/s?k=video+games&rh=n%3A468642&dc&qid=1578698986&rnid=2941120011&ref=sr_nr_n_1",headers={"User-Agent":"Defined"})
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
        except Exception as error:
            amazon_featured = None
        print(amazon_featured)





        #Steam News Scrape
        try:
            steam_news_page = requests.get("https://store.steampowered.com/",headers={"User-Agent":"Defined"})
            soup = BeautifulSoup(steam_news_page.text, "html.parser")
            steam_results = soup.find("div", {"id": "tab_specials_content"}).select("a")
            steam_news = []
            for result in steam_results[:6]:
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

        except Exception as error:
            steam_news = None




        #PC Gamer news
        try:
            pcgamer_news_page = requests.get("https://www.pcgamer.com/",headers={"User-Agent":"Defined"})
            pcgamer_news_soup = BeautifulSoup(pcgamer_news_page.content, "html.parser")
            pcgamer_featured = pcgamer_news_soup.find_all("div", {"class": "feature-block-item-wrapper"})
            pcgamer_news = []
            for article in pcgamer_featured[1:]:
                try:
                    pcgamer_news.append({
                        'url': article.a.get('href'),
                        'title': article.a.get('aria-label'),
                        'image': article.source.get('data-original-mos'),
                    })
                except:
                    pcgamer_news.append({
                        'url': article.a.get('href'),
                        'title': article.a.get('aria-label'),
                        'image': article.img.get("src"),
                    })

        except Exception as error:
            pcgamer_news = None

        return render(request, 'games_index.html',
        {'search' : False, 'pcgamer_news': pcgamer_news, 'steam_news': steam_news, 'amazon_featured': amazon_featured, 'verge_articles' : verge_articles})



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
