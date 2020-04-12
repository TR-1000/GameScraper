import requests
from bs4 import BeautifulSoup
import pprint
pp = pprint.PrettyPrinter(indent=4)
# header={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'})


def get_gamepedia_articles():
    gamepedia_news_page = requests.get("https://www.gamepedia.com/",headers={"User-Agent":"Defined"})
    gamepedia_soup = BeautifulSoup(gamepedia_news_page.text, "html.parser")
    gamepedia_articles = []
    gamepedia_results = gamepedia_soup.select('article')
    #print(results)
    for result in gamepedia_results:
        url = result.a.get('href')
        image = result.a.img.get('src')
        title = result.h2.a.text
        author = result.span.text
        time = result.abbr.text
        gamepedia_articles.append({
            'title' : title,
            'author' : author,
            'time' : time,
            'url' : url,
            'image' : image
        })

    print(gamepedia_articles)



def get_amazon_search():
    amazon_page = requests.get("https://www.amazon.com/s?k=gta+v",headers={"User-Agent":"Defined"})
    amazon_soup = BeautifulSoup(amazon_page.content, "html.parser")
    amazon_results = amazon_soup.select("span.a-offscreen")
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
    print(amazon_soup)



def get_amazon_featured():
    amazon_page = requests.get("https://www.amazon.com/s?k=video+games&rh=n%3A6427831011&ref=nb_sb_noss",headers={"User-Agent":"Defined"})
    # sess = cachecontrol.CacheControl(requests.Session())
    # resp = sess.get("https://www.amazon.com/s?k=video+games&i=videogames&ref=nb_sb_noss",headers={"User-Agent":"Defined"})
    amazon_soup = BeautifulSoup(amazon_page.content, "html.parser")
    amazon_featured = []
    amazon_results = amazon_soup.select("div.sg-col-20-of-24.s-result-item.s-asin")

    try:
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

    pp.pprint(amazon_results)



def get_ign_news():
    ign_page = requests.get("https://www.ign.com",headers={"User-Agent":"Defined"})
    ign_soup = BeautifulSoup(ign_page.content, "html.parser")
    ign_results = ign_soup.select("article.jsx-4177878793.card")
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

    print(ign_news)



def get_gamespot_news():
    gamespot_news_page = requests.get("https://www.gamespot.com/",headers={"User-Agent":"Defined"})
    gamespot_news_soup = BeautifulSoup(gamespot_news_page.content, "html.parser")

    gamespot_articles = gamespot_news_soup.find("section", {"class": "editorial"}).find_all("div", {"class": "horizontal-card-item"})
    gamespot_news = []
    for result in gamespot_articles[:5]:
        title = result.h4.text
        url = "https://www.gamespot.com" + result.a.get('href')
        image = result.img.get('src')
        description = ""
        gamespot_news.append({
            'title':title,
            'description':description,
            'url':url,
            'image':image,
            })

    pp.pprint(gamespot_news)



def get_steam_deals():
    steam_news_page = requests.get("https://store.steampowered.com/",headers={"User-Agent":"Defined"})
    soup = BeautifulSoup(steam_news_page.text, "html.parser")
    steam_results = soup.find("div", {"id": "tab_specials_content"}).select("a")
    steam_deals = []
    for result in steam_results:
        try:
            if len(steam_deals) < 10:
                if "," in result.get("data-ds-appid"):
                    app_split = result.get("data-ds-appid").split(",")
                    app_id = app_split[0]
                else:
                    app_id = result.get("data-ds-appid")

                steam_deals.append({
                    'url': result.get("href"),
                    'image': f"https://steamcdn-a.akamaihd.net/steam/apps/{app_id}/header.jpg",
                    'title': result.find("div", {"class": "tab_item_name"}).text,
                    'original_prince': result.find("div", {"class": "discount_original_price"}).text,
                    'price': result.find("div", {"class": "discount_final_price"}).text,
                    'app_id': app_id
                })
        except Exception as e:
            print(e)
            continue

    return steam_deals



def get_pcgamer_news():
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

    pcgamer_articles = pcgamer_news_soup.select("div.listingResults.all div.listingResult")
    for article in pcgamer_articles:
        if len(pcgamer_news) < 10:
            try:
                pcgamer_news.append({
                'title': article.a.get('aria-label'),
                'url': article.a.get('href'),
                'image': article.img.get('data-original-mos')
                })
            except Exception as e:
                print(e)
                continue


    return pcgamer_news



def get_verge_gaming():
    verge_gaming_page = requests.get("https://www.theverge.com/games",headers={"User-Agent":"Defined"})
    verge_gaming_soup = BeautifulSoup(verge_gaming_page.content,"html.parser")
    verge_gaming_articles = verge_gaming_soup.select("div.c-entry-box--compact.c-entry-box--compact--article")
    verge_articles=[]

    for article in verge_gaming_articles:
        if len(verge_articles) < 10:
            try:
                verge_articles.append({
                    'url': article.a.get("href"),
                    'image': article.find_all("img")[1].get("src"),
                    'title': article.h2.text,
                    'date': article.time.text.strip()
                })

            except Exception as e:

                print(e, f'{article.h2.text} was skipped')
                continue
        else:
            break


    return verge_articles



def get_techspot():
    techspot_request = requests.get("https://www.techspot.com/category/gaming/",headers={"User-Agent":"Defined"})
    techspot_soup  = BeautifulSoup(techspot_request.content,"html.parser")
    techspot_results = techspot_soup.select("article")
    techspot_articles = []
    for result in techspot_results:
        if len(techspot_articles) < 10:
            try:
                techspot_articles.append({
                        'title': result.h2.text.replace("\xa0"," ").strip(),
                        'url': result.a.get("href"),
                        'image': result.img.get("data-src"),
                        'intro': result.find("div", {"class": "intro"}).text
                    })
            except Exception as e:
                print(e)
                continue

        else:
            break

    return techspot_articles
