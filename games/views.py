from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Game
from . forms import GameForm


def home(request):
    import requests
    import json

    # Import required modules.
    from azure.cognitiveservices.search.websearch import WebSearchAPI
    from azure.cognitiveservices.search.websearch.models import SafeSearch
    from msrest.authentication import CognitiveServicesCredentials

    if request.method == 'POST':
        #set variable for searched game
        game_title = request.POST['game_search']

        #rawg api data request
        rawg_api_response = requests.get(f'https://api.rawg.io/api/games?page_size=1&search={game_title}')

        try:
            rawg_api = json.loads(rawg_api_response.content)
        except Exception as error:
            rawg_api = "Error loading api data..."


        subscription_key = "d934abc86e314ea0bada2199dd27cadf"
        assert subscription_key
        search_url = "https://api.cognitive.microsoft.com/bing/v7.0/search"
        headers = {"Ocp-Apim-Subscription-Key": subscription_key}
        params = {"q": game_title}
        bing_api_response = requests.get(search_url, headers=headers, params=params)
        bing_api_response.raise_for_status()
        # bing_api = bing_api_response.json()
        bing_api = json.loads(bing_api_response.content)

        return render(request, 'games_index.html', {'rawg_api': rawg_api, 'bing_api': bing_api})

        #return render(request, 'games_index.html', {'rawg_api': rawg_api})

    else:
        return render(request, 'games_index.html', {'game_search': 'Enter a game title', 'rawg_api': {
"count": 102,
"next": "https://api.rawg.io/api/games?page=2&page_size=1&search=fallout+76",
"previous": None,
"results": [
{
"slug": "fallout-76",
"name": "Fallout 76",
"promo": "e3",
"playtime": 0,
"platforms": [
{
"platform": {
"id": 4,
"name": "PC",
"slug": "pc"
}
},
{
"platform": {
"id": 1,
"name": "Xbox One",
"slug": "xbox-one"
}
},
{
"platform": {
"id": 18,
"name": "PlayStation 4",
"slug": "playstation4"
}
}
],
"stores": [
{
"store": {
"id": 3,
"name": "PlayStation Store",
"slug": "playstation-store"
}
},
{
"store": {
"id": 2,
"name": "Xbox Store",
"slug": "xbox-store"
}
}
],
"released": "2018-11-14",
"tba": False,
"background_image": "https://media.rawg.io/media/games/cbe/cbe5ea823ac880435f6f31c4d2019483.jpg",
"rating": 2.68,
"rating_top": 1,
"ratings": [
{
"id": 1,
"title": "skip",
"count": 53,
"percent": 37.32
},
{
"id": 4,
"title": "recommended",
"count": 39,
"percent": 27.46
},
{
"id": 3,
"title": "meh",
"count": 39,
"percent": 27.46
},
{
"id": 5,
"title": "exceptional",
"count": 11,
"percent": 7.75
}
],
"ratings_count": 141,
"reviews_text_count": 1,
"added": 579,
"added_by_status": {
"yet": 26,
"owned": 341,
"beaten": 8,
"toplay": 136,
"dropped": 37,
"playing": 31
},
"metacritic": None,
"charts": {
"year": {
"year": 2018,
"change": "equal",
"position": 55
}
},
"comments_count": 0,
"comments_parent_count": 0,
"suggestions_count": 381,
"id": 58585,
"score": "98.02428",
"clip": {
"clip": "https://media.rawg.io/media/stories-640/43f/43f75778ad93aa4ae0e1b1f564e394c8.mp4",
"clips": {
"320": "https://media.rawg.io/media/stories-320/0b7/0b753827351ff0f3cc8339dc77fdf814.mp4",
"640": "https://media.rawg.io/media/stories-640/43f/43f75778ad93aa4ae0e1b1f564e394c8.mp4",
"full": "https://media.rawg.io/media/stories/824/8248189223392b387c565740e1de7c20.mp4"
},
"preview": "https://media.rawg.io/media/stories-previews/d32/d329ec96a8167822eaddb143cbfa57ac.jpg"
},
"user_game": None,
"reviews_count": 142,
"saturated_color": "0f0f0f",
"dominant_color": "0f0f0f",
"short_screenshots": [
{
"id": -1,
"image": "https://media.rawg.io/media/games/cbe/cbe5ea823ac880435f6f31c4d2019483.jpg"
},
{
"id": 804226,
"image": "https://media.rawg.io/media/screenshots/948/9483758eb45611098a1556bee929609a.jpg"
},
{
"id": 804227,
"image": "https://media.rawg.io/media/screenshots/690/6907cbfe39cdb83f964c1b8e72d1e6d2.jpg"
},
{
"id": 804228,
"image": "https://media.rawg.io/media/screenshots/b91/b91f859a48633fbb9873797d50c26302.jpg"
},
{
"id": 804229,
"image": "https://media.rawg.io/media/screenshots/9e5/9e558c6ca8e84fbdc49a4ed3be1c15b6.jpg"
},
{
"id": 804230,
"image": "https://media.rawg.io/media/screenshots/b1c/b1cf4ddeee3d9b44b76809e35aa6d2ae.jpg"
},
{
"id": 804231,
"image": "https://media.rawg.io/media/screenshots/393/393d3c8d7150a8a8e946f7378b450911.jpg"
}
],
"parent_platforms": [
{
"platform": {
"id": 1,
"name": "PC",
"slug": "pc"
}
},
{
"platform": {
"id": 2,
"name": "PlayStation",
"slug": "playstation"
}
},
{
"platform": {
"id": 3,
"name": "Xbox",
"slug": "xbox"
}
}
],
"genres": [
{
"id": 3,
"name": "Adventure",
"slug": "adventure"
},
{
"id": 4,
"name": "Action",
"slug": "action"
},
{
"id": 5,
"name": "RPG",
"slug": "role-playing-games-rpg"
}
]
}
]
}, 'bing_api': {   '_type': 'SearchResponse',
    'entities': {   'value': [   {   'bingId': '2750cdf0-b4be-5e68-e560-0bab97ebf598',
                                     'contractualRules': [   {   '_type': 'ContractualRules/LicenseAttribution',
                                                                 'license': {   'name': 'CC-BY-SA',
                                                                                'url': 'http://creativecommons.org/licenses/by-sa/3.0/'},
                                                                 'licenseNotice': 'Text '
                                                                                  'under '
                                                                                  'CC-BY-SA '
                                                                                  'license',
                                                                 'mustBeCloseToContent': True,
                                                                 'targetPropertyName': 'description'},
                                                             {   '_type': 'ContractualRules/LinkAttribution',
                                                                 'mustBeCloseToContent': True,
                                                                 'targetPropertyName': 'description',
                                                                 'text': 'Wikipedia',
                                                                 'url': 'http://en.wikipedia.org/wiki/Fallout_76'},
                                                             {   '_type': 'ContractualRules/MediaAttribution',
                                                                 'mustBeCloseToContent': True,
                                                                 'targetPropertyName': 'image',
                                                                 'url': 'http://en.wikipedia.org/wiki/Fallout_76'}],
                                     'description': 'Fallout 76 is an online '
                                                    'action role-playing game '
                                                    'in the Fallout series '
                                                    'developed by Bethesda '
                                                    'Game Studios and '
                                                    'published by Bethesda '
                                                    'Softworks. Released for '
                                                    'Microsoft Windows, '
                                                    'PlayStation 4, and Xbox '
                                                    'One on November 14, 2018, '
                                                    'it is a prequel to '
                                                    'previous series games. '
                                                    'Fallout 76 is Bethesda '
                                                    "Game Studios's first "
                                                    'multiplayer game; players '
                                                    'explore the open world, '
                                                    'which has been torn apart '
                                                    'by nuclear war, with '
                                                    'others. Bethesda '
                                                    'developed the game using '
                                                    'a modified version of its '
                                                    'Creation Engine, which '
                                                    'allowed the accommodation '
                                                    'of multiplayer gameplay '
                                                    'and a more detailed game '
                                                    'world.',
                                     'entityPresentationInfo': {   'entityScenario': 'DominantEntity',
                                                                   'entityTypeDisplayHint': 'Action '
                                                                                            'Role-Playing '
                                                                                            'Game',
                                                                   'entityTypeHints': [   'VideoGame']},
                                     'id': 'https://api.cognitive.microsoft.com/api/v7/#Entities.0',
                                     'image': {   'height': 150,
                                                  'hostPageUrl': 'https://images.ctfassets.net/rporu91m20dc/3CxsghWblSOiqU0yO4iq8O/a98a21e0fd16cc9c4a250947b4437059/Fallout76_BoxArtStandard_BETA_900x1108-01.png?w=190',
                                                  'name': 'Fallout 76',
                                                  'provider': [   {   '_type': 'Organization',
                                                                      'url': 'http://en.wikipedia.org/wiki/Fallout_76'}],
                                                  'sourceHeight': 234,
                                                  'sourceWidth': 190,
                                                  'thumbnailUrl': 'https://www.bing.com/th?id=AMMS_d945867e5a8ce9bc6fe1a2f235e77e78&w=100&h=150&c=7&rs=1&qlt=80&cdv=1&pid=16.1',
                                                  'width': 100},
                                     'name': 'Fallout 76',
                                     'webSearchUrl': 'https://www.bing.com/entityexplore?q=Fallout+76&filters=sid:%222750cdf0-b4be-5e68-e560-0bab97ebf598%22&elv=AXXfrEiqqD9r3GuelwApulrLKnMiEg8OQC0TX07zgPN!Lp*5rLpBHBc*6OUPIEGLNQxPaopMMcIP4Pk22*gERBdF0KAXgLCUBVdggE*AdFo4'}]},
    'images': {   'id': 'https://api.cognitive.microsoft.com/api/v7/#Images',
                  'isFamilyFriendly': True,
                  'readLink': 'https://api.cognitive.microsoft.com/api/v7/images/search?q=fallout+76&qpvt=fallout+76',
                  'value': [   {   'contentSize': '160672 B',
                                   'contentUrl': 'https://cdn.wccftech.com/wp-content/uploads/2018/06/fallout76_powerarmor_art.jpg',
                                   'datePublished': '2018-06-25T10:14:00.0000000Z',
                                   'encodingFormat': 'jpeg',
                                   'height': 1080,
                                   'hostPageDisplayUrl': 'https://wccftech.com/why-fallout-76-could-be-massive-hit/',
                                   'hostPageUrl': 'https://wccftech.com/why-fallout-76-could-be-massive-hit/',
                                   'insightsMetadata': {   'recipeSourcesCount': 0,
                                                           'shoppingSourcesCount': 1},
                                   'name': 'Why Fallout 76 Could Be A Massive '
                                           'Hit for Bethesda',
                                   'thumbnail': {'height': 266, 'width': 474},
                                   'thumbnailUrl': 'https://tse1.mm.bing.net/th?id=OIP.QG5I4YEr1AAJewgAplPehQHaEK&pid=Api',
                                   'webSearchUrl': 'https://www.bing.com/images/search?q=fallout+76&id=AB83341BB2BEED882D6517E21A1FC3A484ABCC04&FORM=IQFRBA',
                                   'width': 1920},
                               {   'contentSize': '1452486 B',
                                   'contentUrl': 'https://www.pcgamesn.com/wp-content/uploads/2018/07/Fallout-76-machinegun.jpg',
                                   'datePublished': '2018-10-07T06:16:00.0000000Z',
                                   'encodingFormat': 'jpeg',
                                   'height': 1080,
                                   'hostPageDisplayUrl': 'https://www.pcgamesn.com/fallout-76/fallout-76-release-date',
                                   'hostPageUrl': 'https://www.pcgamesn.com/fallout-76/fallout-76-release-date',
                                   'insightsMetadata': {   'recipeSourcesCount': 0,
                                                           'shoppingSourcesCount': 0},
                                   'name': 'Fallout 76 release date and '
                                           'multiplayer news – all the latest '
                                           'details | PCGamesN',
                                   'thumbnail': {'height': 266, 'width': 474},
                                   'thumbnailUrl': 'https://tse1.mm.bing.net/th?id=OIP.VovQAWt8FX0Brxr5YNp36AHaEK&pid=Api',
                                   'webSearchUrl': 'https://www.bing.com/images/search?q=fallout+76&id=23B8A7AEACA6DEA5D023571A7F9ACE2D12413F1A&FORM=IQFRBA',
                                   'width': 1920},
                               {   'contentSize': '1966335 B',
                                   'contentUrl': 'https://www.pcgamesn.com/wp-content/uploads/2018/07/fallout-76-t51-power-armor.jpg',
                                   'datePublished': '2018-09-15T23:15:00.0000000Z',
                                   'encodingFormat': 'jpeg',
                                   'height': 1080,
                                   'hostPageDisplayUrl': 'https://www.pcgamesn.com/fallout-76/fallout-76-release-date',
                                   'hostPageUrl': 'https://www.pcgamesn.com/fallout-76/fallout-76-release-date',
                                   'insightsMetadata': {   'recipeSourcesCount': 0,
                                                           'shoppingSourcesCount': 0},
                                   'name': 'Fallout 76 release date and '
                                           'multiplayer news – all the latest '
                                           'details | PCGamesN',
                                   'thumbnail': {'height': 266, 'width': 474},
                                   'thumbnailUrl': 'https://tse1.mm.bing.net/th?id=OIP.K9GhJOrlqh45ssLNA4a3FwHaEK&pid=Api',
                                   'webSearchUrl': 'https://www.bing.com/images/search?q=fallout+76&id=23B8A7AEACA6DEA5D023D87FEA6A5DDE65E7ACCC&FORM=IQFRBA',
                                   'width': 1920},
                               {   'contentSize': '993567 B',
                                   'contentUrl': 'https://www.pcgamesn.com/wp-content/uploads/2018/06/fallout-76-brotherhood-of-steel.jpg',
                                   'datePublished': '2018-11-14T18:17:00.0000000Z',
                                   'encodingFormat': 'jpeg',
                                   'height': 1080,
                                   'hostPageDisplayUrl': 'https://www.pcgamesn.com/fallout-76/builds-best-characters',
                                   'hostPageUrl': 'https://www.pcgamesn.com/fallout-76/builds-best-characters',
                                   'insightsMetadata': {   'recipeSourcesCount': 0,
                                                           'shoppingSourcesCount': 0},
                                   'name': 'Fallout 76 builds: 7 of the best '
                                           'character builds to help you '
                                           'survive | PCGamesN',
                                   'thumbnail': {'height': 266, 'width': 474},
                                   'thumbnailUrl': 'https://tse1.mm.bing.net/th?id=OIP.Kbv8CpPMrwTwAk308iITAQHaEK&pid=Api',
                                   'webSearchUrl': 'https://www.bing.com/images/search?q=fallout+76&id=F4826852A9FF36C9675D968DB00E16E71FB3201E&FORM=IQFRBA',
                                   'width': 1920},
                               {   'contentSize': '374832 B',
                                   'contentUrl': 'https://www.gamespace.com/wp-content/uploads/2018/06/Fallout76_E3_PowerArmors_1528639320.jpg',
                                   'datePublished': '2018-06-12T15:24:00.0000000Z',
                                   'encodingFormat': 'jpeg',
                                   'height': 720,
                                   'hostPageDisplayUrl': 'https://www.gamespace.com/all-games/fallout-76/',
                                   'hostPageUrl': 'https://www.gamespace.com/all-games/fallout-76/',
                                   'insightsMetadata': {   'recipeSourcesCount': 0,
                                                           'shoppingSourcesCount': 0},
                                   'name': 'Fallout 76 - GameSpace.com',
                                   'thumbnail': {'height': 266, 'width': 474},
                                   'thumbnailUrl': 'https://tse1.mm.bing.net/th?id=OIP.6A56xJU5ZKsHA--BEDljZwHaEK&pid=Api',
                                   'webSearchUrl': 'https://www.bing.com/images/search?q=fallout+76&id=6F6A223D3F9E97F6C3EB6F066B8FA0DDAF07E122&FORM=IQFRBA',
                                   'width': 1280},
                               {   'contentSize': '277061 B',
                                   'contentUrl': 'https://cdn.gamer-network.net/2018/usgamer/fallout-76-creature.jpg',
                                   'datePublished': '2018-06-19T10:33:00.0000000Z',
                                   'encodingFormat': 'jpeg',
                                   'height': 1080,
                                   'hostPageDisplayUrl': 'https://www.usgamer.net/articles/19-06-2018-fallout-76-release-date-platforms-setting-everything-we-know-so-far/',
                                   'hostPageUrl': 'https://www.usgamer.net/articles/19-06-2018-fallout-76-release-date-platforms-setting-everything-we-know-so-far/',
                                   'insightsMetadata': {   'recipeSourcesCount': 0,
                                                           'shoppingSourcesCount': 0},
                                   'name': 'Fallout 76 Release Date, Gameplay, '
                                           'Trailer, Map Size, Screenshots - '
                                           'Everything We Know | USgamer',
                                   'thumbnail': {'height': 266, 'width': 474},
                                   'thumbnailUrl': 'https://tse1.mm.bing.net/th?id=OIP.Y0K3yGOdIDZgreR1--2k6QHaEK&pid=Api',
                                   'webSearchUrl': 'https://www.bing.com/images/search?q=fallout+76&id=481A2775CAD3F0DFBB8C3A5814187B369C027B7B&FORM=IQFRBA',
                                   'width': 1920},
                               {   'contentSize': '64556 B',
                                   'contentUrl': 'https://i.gadgets360cdn.com/large/fallout-76_1538378009421.jpg',
                                   'datePublished': '2018-12-22T14:09:00.0000000Z',
                                   'encodingFormat': 'jpeg',
                                   'height': 720,
                                   'hostPageDisplayUrl': 'https://gadgets.ndtv.com/games/news/fallout-76-beta-download-size-45gb-1924910',
                                   'hostPageUrl': 'https://gadgets.ndtv.com/games/news/fallout-76-beta-download-size-45gb-1924910',
                                   'insightsMetadata': {   'recipeSourcesCount': 0,
                                                           'shoppingSourcesCount': 1},
                                   'name': 'Fallout 76 Beta Download Size '
                                           'Revealed | Technology News',
                                   'thumbnail': {'height': 266, 'width': 474},
                                   'thumbnailUrl': 'https://tse1.mm.bing.net/th?id=OIP.jJ4Fb0BNw1EaIYKXtk8vIgHaEK&pid=Api',
                                   'webSearchUrl': 'https://www.bing.com/images/search?q=fallout+76&id=ED1B8951B61AF417E8002B847A6D242B9D7592A9&FORM=IQFRBA',
                                   'width': 1280},
                               {   'contentSize': '292884 B',
                                   'contentUrl': 'https://cdn.gearnuke.com/wp-content/uploads/2018/11/fallout-76-max-level-1-1.jpg',
                                   'datePublished': '2018-12-11T21:14:00.0000000Z',
                                   'encodingFormat': 'jpeg',
                                   'height': 1080,
                                   'hostPageDisplayUrl': 'https://gearnuke.com/fallout-76-camp-disappearance/',
                                   'hostPageUrl': 'https://gearnuke.com/fallout-76-camp-disappearance/',
                                   'insightsMetadata': {   'recipeSourcesCount': 0,
                                                           'shoppingSourcesCount': 1},
                                   'name': 'Fallout 76 Camp Disappeared, '
                                           'Fallout 76 Camp Disappearance Bug',
                                   'thumbnail': {'height': 266, 'width': 474},
                                   'thumbnailUrl': 'https://tse1.mm.bing.net/th?id=OIP._pH3hMGoHntnQHB_w3NQQQHaEK&pid=Api',
                                   'webSearchUrl': 'https://www.bing.com/images/search?q=fallout+76&id=DD3C035D34507AE465A441BD90E571700F80F6FA&FORM=IQFRBA',
                                   'width': 1920},
                               {   'contentSize': '3331862 B',
                                   'contentUrl': 'https://assets.vg247.com/current/2018/06/Fallout-76.png',
                                   'datePublished': '2018-06-11T12:00:00.0000000Z',
                                   'encodingFormat': 'png',
                                   'height': 1080,
                                   'hostPageDisplayUrl': 'https://www.vg247.com/2018/06/11/fallout-76-e3-2018-bethesda/',
                                   'hostPageUrl': 'https://www.vg247.com/2018/06/11/fallout-76-e3-2018-bethesda/',
                                   'insightsMetadata': {   'recipeSourcesCount': 0,
                                                           'shoppingSourcesCount': 0},
                                   'name': 'Fallout 76 is an online '
                                           'multiplayer game about the first '
                                           'people to leave the vault',
                                   'thumbnail': {'height': 266, 'width': 474},
                                   'thumbnailUrl': 'https://tse1.mm.bing.net/th?id=OIP.8ebVcAKd7zyCetp7E1DDTQHaEK&pid=Api',
                                   'webSearchUrl': 'https://www.bing.com/images/search?q=fallout+76&id=F8357E486C4E129BB5150A20157ABD9ACDDDB0FB&FORM=IQFRBA',
                                   'width': 1920},
                               {   'contentSize': '426763 B',
                                   'contentUrl': 'https://assets.rockpapershotgun.com/images/2018/10/fallout-76-b.jpg',
                                   'datePublished': '2018-10-10T12:00:00.0000000Z',
                                   'encodingFormat': 'jpeg',
                                   'height': 1080,
                                   'hostPageDisplayUrl': 'https://www.rockpapershotgun.com/2018/10/10/fallout-76-mod-support-might-take-a-year/',
                                   'hostPageUrl': 'https://www.rockpapershotgun.com/2018/10/10/fallout-76-mod-support-might-take-a-year/',
                                   'insightsMetadata': {   'recipeSourcesCount': 0,
                                                           'shoppingSourcesCount': 0},
                                   'name': 'Fallout 76 might not get mod '
                                           'support before November 2019 | '
                                           'Rock Paper Shotgun',
                                   'thumbnail': {'height': 266, 'width': 474},
                                   'thumbnailUrl': 'https://tse1.mm.bing.net/th?id=OIP.dQWsVJFzaxYMLhH8uS_rVgHaEK&pid=Api',
                                   'webSearchUrl': 'https://www.bing.com/images/search?q=fallout+76&id=8BEC1B396515A770DD0A465FAAA1931A024F6577&FORM=IQFRBA',
                                   'width': 1920},
                               {   'contentSize': '127200 B',
                                   'contentUrl': 'https://static.gamespot.com/uploads/scale_super/1552/15524586/3398833-fallout76-e3thumb-8.jpg',
                                   'datePublished': '2019-03-03T12:52:00.0000000Z',
                                   'encodingFormat': 'jpeg',
                                   'height': 720,
                                   'hostPageDisplayUrl': 'https://www.gamespot.com/articles/e3-2018-bethesdas-press-conference-news-recap-fall/1100-6459564/',
                                   'hostPageUrl': 'https://www.gamespot.com/articles/e3-2018-bethesdas-press-conference-news-recap-fall/1100-6459564/',
                                   'insightsMetadata': {   'recipeSourcesCount': 0,
                                                           'shoppingSourcesCount': 0},
                                   'name': "E3 2018: Bethesda's Press "
                                           'Conference News Recap -- Fallout '
                                           '76, Elder Scrolls 6, Starfield, '
                                           'And ...',
                                   'thumbnail': {'height': 266, 'width': 474},
                                   'thumbnailUrl': 'https://tse1.mm.bing.net/th?id=OIP.5SNQJZ5I_HKlmCo99ZmT2gHaEK&pid=Api',
                                   'webSearchUrl': 'https://www.bing.com/images/search?q=fallout+76&id=E63F5BADD8863FC3F8CD2BF5C3198A0CB3ED940C&FORM=IQFRBA',
                                   'width': 1280},
                               {   'contentSize': '1068205 B',
                                   'contentUrl': 'https://static.gamespot.com/uploads/screen_kubrick/1579/15792183/3454375-fallout76.png',
                                   'datePublished': '2018-11-02T21:30:00.0000000Z',
                                   'encodingFormat': 'png',
                                   'height': 720,
                                   'hostPageDisplayUrl': 'https://www.gamespot.com/gallery/fallout-76-beta-guide-tips-and-what-to-do-first/2900-2333/',
                                   'hostPageUrl': 'https://www.gamespot.com/gallery/fallout-76-beta-guide-tips-and-what-to-do-first/2900-2333/',
                                   'insightsMetadata': {   'recipeSourcesCount': 0,
                                                           'shoppingSourcesCount': 0},
                                   'name': 'Fallout 76 Survival Guide, Tips, '
                                           'And Important Locations To Visit '
                                           'First - GameSpot',
                                   'thumbnail': {'height': 266, 'width': 474},
                                   'thumbnailUrl': 'https://tse1.mm.bing.net/th?id=OIP.WuOwlfR9456MYUP1ofSabwHaEK&pid=Api',
                                   'webSearchUrl': 'https://www.bing.com/images/search?q=fallout+76&id=5288E51027FB2663712963B62B67B02B9BF4F1AF&FORM=IQFRBA',
                                   'width': 1280},
                               {   'contentSize': '544184 B',
                                   'contentUrl': 'https://assets.vg247.com/current/2018/06/fallout_76-2.jpg',
                                   'datePublished': '2018-06-13T12:00:00.0000000Z',
                                   'encodingFormat': 'jpeg',
                                   'height': 1114,
                                   'hostPageDisplayUrl': 'https://www.vg247.com/2018/06/13/fallout-76-is-a-live-game-with-a-huge-emphasis-on-crafting/',
                                   'hostPageUrl': 'https://www.vg247.com/2018/06/13/fallout-76-is-a-live-game-with-a-huge-emphasis-on-crafting/',
                                   'insightsMetadata': {   'recipeSourcesCount': 0,
                                                           'shoppingSourcesCount': 0},
                                   'name': 'Fallout 76 is a "live game" with a '
                                           'huge emphasis on crafting - VG247',
                                   'thumbnail': {'height': 266, 'width': 474},
                                   'thumbnailUrl': 'https://tse1.mm.bing.net/th?id=OIP.x6MbN5i1uiBDFMykw--KTgHaEK&pid=Api',
                                   'webSearchUrl': 'https://www.bing.com/images/search?q=fallout+76&id=8E3C23DE10F550F26AF3B4A32E0BAD52123032F4&FORM=IQFRBA',
                                   'width': 1980},
                               {   'contentSize': '2498722 B',
                                   'contentUrl': 'https://www.pcgamesn.com/wp-content/uploads/2018/07/fallout-76-grafton.jpg',
                                   'datePublished': '2018-10-07T06:16:00.0000000Z',
                                   'encodingFormat': 'jpeg',
                                   'height': 1080,
                                   'hostPageDisplayUrl': 'https://www.pcgamesn.com/fallout-76/fallout-76-release-date',
                                   'hostPageUrl': 'https://www.pcgamesn.com/fallout-76/fallout-76-release-date',
                                   'name': 'Fallout 76 release date and '
                                           'multiplayer news – all the latest '
                                           'details | PCGamesN',
                                   'thumbnail': {'height': 266, 'width': 474},
                                   'thumbnailUrl': 'https://tse1.mm.bing.net/th?id=OIP.rUU3yjd8kywJB9c-Ixjs-wHaEK&pid=Api',
                                   'webSearchUrl': 'https://www.bing.com/images/search?q=fallout+76&id=23B8A7AEACA6DEA5D023B4675B4D980F08094AD4&FORM=IQFRBA',
                                   'width': 1920},
                               {   'contentSize': '7483025 B',
                                   'contentUrl': 'https://static.gamespot.com/uploads/original/1576/15769789/3399055-fallout76_e3_wendigo_1528639337.png',
                                   'datePublished': '2018-08-15T23:09:00.0000000Z',
                                   'encodingFormat': 'png',
                                   'height': 2160,
                                   'hostPageDisplayUrl': 'https://www.gamespot.com/articles/fallout-76-pvp-perks-release-date-and-what-we-know/1100-6459293/',
                                   'hostPageUrl': 'https://www.gamespot.com/articles/fallout-76-pvp-perks-release-date-and-what-we-know/1100-6459293/',
                                   'insightsMetadata': {   'recipeSourcesCount': 0,
                                                           'shoppingSourcesCount': 0},
                                   'name': 'Fallout 76: Release Date, PvP, And '
                                           'What We Know (So Far) - GameSpot',
                                   'thumbnail': {'height': 266, 'width': 474},
                                   'thumbnailUrl': 'https://tse1.mm.bing.net/th?id=OIP.5Da-H4l2M-egboL0cChspAHaEK&pid=Api',
                                   'webSearchUrl': 'https://www.bing.com/images/search?q=fallout+76&id=868B12495AE17963EEFC60FBB4A3A2A8D9B8AFA8&FORM=IQFRBA',
                                   'width': 3840},
                               {   'contentSize': '365785 B',
                                   'contentUrl': 'https://cdn.gamer-network.net/2018/usgamer/fallout-76-liberator-.jpg',
                                   'datePublished': '2018-06-19T10:33:00.0000000Z',
                                   'encodingFormat': 'jpeg',
                                   'height': 1080,
                                   'hostPageDisplayUrl': 'https://www.usgamer.net/articles/19-06-2018-fallout-76-new-creatures-all-the-new-wildlife-animals-and-enemies-in-fallout-76',
                                   'hostPageUrl': 'https://www.usgamer.net/articles/19-06-2018-fallout-76-new-creatures-all-the-new-wildlife-animals-and-enemies-in-fallout-76',
                                   'insightsMetadata': {   'recipeSourcesCount': 0,
                                                           'shoppingSourcesCount': 0},
                                   'name': 'Fallout 76 Creatures - All the new '
                                           'Wildlife, Animals and Enemies in '
                                           'Fallout 76 | USgamer',
                                   'thumbnail': {'height': 266, 'width': 474},
                                   'thumbnailUrl': 'https://tse1.mm.bing.net/th?id=OIP.ehOIyS3QmpuLUPTN61jBeAHaEK&pid=Api',
                                   'webSearchUrl': 'https://www.bing.com/images/search?q=fallout+76&id=97C551CA6BC1B7EE23912793CAB1AAA4AC6E7585&FORM=IQFRBA',
                                   'width': 1920},
                               {   'contentSize': '246711 B',
                                   'contentUrl': 'https://www.psu.com/app/uploads/2018/06/fallout-76-multiplayer02.jpg',
                                   'datePublished': '2018-07-03T08:10:00.0000000Z',
                                   'encodingFormat': 'jpeg',
                                   'height': 1075,
                                   'hostPageDisplayUrl': 'https://www.psu.com/news/fallout-76-beta-access-starts-testing-ps4-xbox/',
                                   'hostPageUrl': 'https://www.psu.com/news/fallout-76-beta-access-starts-testing-ps4-xbox/',
                                   'insightsMetadata': {   'recipeSourcesCount': 0,
                                                           'shoppingSourcesCount': 0},
                                   'name': 'Fallout 76 Beta Access Starts '
                                           'Soon, Testing On PS4, But Xbox One '
                                           'First',
                                   'thumbnail': {'height': 265, 'width': 474},
                                   'thumbnailUrl': 'https://tse1.mm.bing.net/th?id=OIP.BKXUPjNxcCE5bfbQxOdT9AHaEJ&pid=Api',
                                   'webSearchUrl': 'https://www.bing.com/images/search?q=fallout+76&id=60147D481F25478D0F232111D4171B6BB2B11461&FORM=IQFRBA',
                                   'width': 1920},
                               {   'contentSize': '2109125 B',
                                   'contentUrl': 'https://www.pcgamesn.com/wp-content/uploads/2018/11/fallout-76-farm-XP.jpg',
                                   'datePublished': '2019-01-03T03:28:00.0000000Z',
                                   'encodingFormat': 'jpeg',
                                   'height': 1080,
                                   'hostPageDisplayUrl': 'https://www.pcgamesn.com/fallout-76/leveling-guide-farm-xp',
                                   'hostPageUrl': 'https://www.pcgamesn.com/fallout-76/leveling-guide-farm-xp',
                                   'insightsMetadata': {   'recipeSourcesCount': 0,
                                                           'shoppingSourcesCount': 0},
                                   'name': 'Fallout 76 leveling guide: how to '
                                           'farm XP and level up fast | '
                                           'PCGamesN',
                                   'thumbnail': {'height': 266, 'width': 474},
                                   'thumbnailUrl': 'https://tse1.mm.bing.net/th?id=OIP.LV35czvyVx6w9wlKXZnY_QHaEK&pid=Api',
                                   'webSearchUrl': 'https://www.bing.com/images/search?q=fallout+76&id=C682F9756916A3683E68A9400C56B600B98ADFAD&FORM=IQFRBA',
                                   'width': 1920},
                               {   'contentSize': '60078 B',
                                   'contentUrl': 'https://static.gamespot.com/uploads/screen_kubrick/1552/15524586/3414897-fallout76-e3thumb-3.jpg',
                                   'datePublished': '2018-07-21T20:53:00.0000000Z',
                                   'encodingFormat': 'jpeg',
                                   'height': 720,
                                   'hostPageDisplayUrl': 'https://www.gamespot.com/articles/fallout-76-release-date-and-everything-we-know-so-/1100-6459293/',
                                   'hostPageUrl': 'https://www.gamespot.com/articles/fallout-76-release-date-and-everything-we-know-so-/1100-6459293/',
                                   'insightsMetadata': {   'recipeSourcesCount': 0,
                                                           'shoppingSourcesCount': 0},
                                   'name': 'Fallout 76: Release Date, Beta, '
                                           'And Everything We Know So Far - '
                                           'GameSpot',
                                   'thumbnail': {'height': 266, 'width': 474},
                                   'thumbnailUrl': 'https://tse1.mm.bing.net/th?id=OIP.85kTux8e_Yo_7UGRp6k_8QHaEK&pid=Api',
                                   'webSearchUrl': 'https://www.bing.com/images/search?q=fallout+76&id=C5ADD16C4D93FA8C548A8FAF8F9C172E91240519&FORM=IQFRBA',
                                   'width': 1280},
                               {   'contentSize': '166985 B',
                                   'contentUrl': 'http://gamingtrend.com/wp-content/uploads/2018/11/fallout-76.jpg',
                                   'datePublished': '2018-12-15T00:42:00.0000000Z',
                                   'encodingFormat': 'jpeg',
                                   'height': 1080,
                                   'hostPageDisplayUrl': 'http://gamingtrend.com/feature/reviews/worst-virginia-fallout-76-review/',
                                   'hostPageUrl': 'http://gamingtrend.com/feature/reviews/worst-virginia-fallout-76-review/',
                                   'insightsMetadata': {   'recipeSourcesCount': 0,
                                                           'shoppingSourcesCount': 0},
                                   'name': 'Worst Virginia — Fallout 76 review '
                                           '– GAMING TREND',
                                   'thumbnail': {'height': 266, 'width': 474},
                                   'thumbnailUrl': 'https://tse1.mm.bing.net/th?id=OIP.-OV1wbVh4Mww5bzzu-kIdgHaEK&pid=Api',
                                   'webSearchUrl': 'https://www.bing.com/images/search?q=fallout+76&id=B43795EE2779D44C3F999D8335B5F2554B292FA2&FORM=IQFRBA',
                                   'width': 1920}],
                  'webSearchUrl': 'https://www.bing.com/images/search?q=fallout+76&qpvt=fallout+76'},
    'news': {   'id': 'https://api.cognitive.microsoft.com/api/v7/#News',
                'readLink': 'https://api.cognitive.microsoft.com/api/v7/news/search?q=Fallout+76',
                'value': [   {   'contractualRules': [   {   '_type': 'ContractualRules/TextAttribution',
                                                             'text': 'MMORPG'}],
                                 'datePublished': '2019-09-11T20:04:00.0000000Z',
                                 'description': 'Refrigerators are expensive. '
                                                "I've had to get close to 3 in "
                                                'a single calendar year thanks '
                                                'to issues buying used ones '
                                                'just to save a buck. But '
                                                'should digital fridges be '
                                                'expensive? Thanks to a new '
                                                'item sold in Fallout 76, that '
                                                'discussion has now been '
                                                'explored.',
                                 'image': {   'contentUrl': 'https://images.mmorpg.com/images/heroes/news/53677.jpg',
                                              'thumbnail': {   'contentUrl': 'https://www.bing.com/th?id=ON.3D6FEF8D4D3E0AAD173B8183DC9A7C16&pid=News',
                                                               'height': 400,
                                                               'width': 700}},
                                 'name': 'Fallout 76 Stirs Player Backlash By '
                                         'Selling $7 Refrigerator',
                                 'provider': [   {   '_type': 'Organization',
                                                     'image': {   'thumbnail': {   'contentUrl': 'https://www.bing.com/th?id=AR_713df50a4c96be7e5be4ef1a36ee65e8&pid=news'}},
                                                     'name': 'MMORPG'}],
                                 'url': 'https://www.mmorpg.com/fallout-76/news/fallout-76-stirs-player-backlash-by-selling-7-refrigerator-1000053677'},
                             {   'category': 'ScienceAndTechnology',
                                 'contractualRules': [   {   '_type': 'ContractualRules/TextAttribution',
                                                             'text': 'Polygon'}],
                                 'datePublished': '2019-09-11T17:22:00.0000000Z',
                                 'description': 'Fallout 76 is in a perilous '
                                                'place for an online game as a '
                                                'service. Despite an '
                                                'infamously rocky launch and '
                                                'persistent gameplay issues, '
                                                'the game has cultivated a '
                                                'cult fanbase who are sticking '
                                                'around to build custom CAMPs, '
                                                'roleplay characters, and '
                                                'build their ...',
                                 'image': {   'contentUrl': 'https://cdn.vox-cdn.com/thumbor/rHf1fwkDL47tSMnKmTu9sBXLcjI=/0x0:3840x2010/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/11449905/fallout_76_trailer_computer_desk_3840.jpg',
                                              'thumbnail': {   'contentUrl': 'https://www.bing.com/th?id=ON.A99BE1BDE47EEE12EE8EAC00BB717075&pid=News',
                                                               'height': 366,
                                                               'width': 700}},
                                 'name': 'Fallout 76 fans are furious over the '
                                         'newest cash shop items',
                                 'provider': [   {   '_type': 'Organization',
                                                     'image': {   'thumbnail': {   'contentUrl': 'https://www.bing.com/th?id=AR_cae4c7e8b10ef00caaadc6ad8e9177c8&pid=news'}},
                                                     'name': 'Polygon'}],
                                 'url': 'https://www.polygon.com/2019/9/11/20860869/fallout-76-atomic-shop-refrigerator-scrap-collector-controversy'},
                             {   'category': 'ScienceAndTechnology',
                                 'contractualRules': [   {   '_type': 'ContractualRules/TextAttribution',
                                                             'text': 'PC '
                                                                     'Gamer'}],
                                 'datePublished': '2019-09-13T17:58:00.0000000Z',
                                 'description': 'As Fraser pointed out '
                                                'yesterday, many Fallout 76 '
                                                'players are unhappy with two '
                                                'new items for sale in the '
                                                'Atomic Shop: a refrigerator '
                                                'that slows down the '
                                                'decomposition of food and a '
                                                'robot that collects junk for '
                                                'you. They cost 700 and 500 '
                                                'Atoms respectively ...',
                                 'image': {   'contentUrl': 'https://cdn.mos.cms.futurecdn.net/7SARnv3ssQGhNbM3iEFw4g-1200-80.jpg',
                                              'thumbnail': {   'contentUrl': 'https://www.bing.com/th?id=ON.40C9F7D7E56CF578C9302B9B69B18DE5&pid=News',
                                                               'height': 425,
                                                               'width': 700}},
                                 'name': "Fallout 76's $5 junk bot was "
                                         'apparently meant to be in the base '
                                         'game',
                                 'provider': [   {   '_type': 'Organization',
                                                     'image': {   'thumbnail': {   'contentUrl': 'https://www.bing.com/th?id=AR_d8972baf41fa83f611250bab3a91d501&pid=news'}},
                                                     'name': 'PC Gamer'}],
                                 'url': 'https://www.pcgamer.com/fallout-76s-dollar5-junk-bot-was-apparently-meant-to-be-in-the-base-game/'},
                             {   'category': 'Business',
                                 'contractualRules': [   {   '_type': 'ContractualRules/TextAttribution',
                                                             'text': 'TweakTown'}],
                                 'datePublished': '2019-09-12T18:32:00.0000000Z',
                                 'description': 'Fallout 76 now has even more '
                                                'microtransactions that have a '
                                                'tangible effect on gameplay, '
                                                "breaking Bethesda's original "
                                                "promise. Despite Bethesda's "
                                                'original assurances, Fallout '
                                                "76 hasn't had cosmetic-only "
                                                'monetization for a while now. '
                                                'In fact, it never ...',
                                 'image': {   'contentUrl': 'https://images.tweaktown.com/news/6/7/67543_5_fallout-76-gets-another-non-cosmetic-microtransaction_full.png',
                                              'thumbnail': {   'contentUrl': 'https://www.bing.com/th?id=ON.5AEED41F23A0397E48CE4FDC8ACFEF5B&pid=News',
                                                               'height': 373,
                                                               'width': 700}},
                                 'name': 'Fallout 76 gets more non-cosmetic '
                                         'microtransactions',
                                 'provider': [   {   '_type': 'Organization',
                                                     'image': {   'thumbnail': {   'contentUrl': 'https://www.bing.com/th?id=AR_dd973dc339c04808e9ead51d33eba707&pid=news'}},
                                                     'name': 'TweakTown'}],
                                 'url': 'https://www.tweaktown.com/news/67543/fallout-76-gets-more-non-cosmetic-microtransactions/index.html'},
                             {   'contractualRules': [   {   '_type': 'ContractualRules/TextAttribution',
                                                             'text': 'Comicbook.com'}],
                                 'datePublished': '2019-09-11T18:00:00.0000000Z',
                                 'description': 'Fallout 76 players are '
                                                'currently in the middle of an '
                                                'event where they’re tasked '
                                                'with cleaning up Appalachia '
                                                'with one another, but that '
                                                'doesn’t mean they’re supposed '
                                                'to go around picking up ...',
                                 'image': {   'contentUrl': 'https://media.comicbook.com/2019/09/fallout-76-1187080-640x320.jpeg',
                                              'thumbnail': {   'contentUrl': 'https://www.bing.com/th?id=ON.3FF2096686B31FC85F225724754E425E&pid=News',
                                                               'height': 320,
                                                               'width': 640}},
                                 'name': 'Fallout 76 Launches a Six-Week Event',
                                 'provider': [   {   '_type': 'Organization',
                                                     'image': {   'thumbnail': {   'contentUrl': 'https://www.bing.com/th?id=AR_3d601e66865cb02df5c96a1e27d47209&pid=news'}},
                                                     'name': 'Comicbook.com'}],
                                 'url': 'https://comicbook.com/gaming/2019/09/11/fallout-76-launches-six-week-event/'}]},
    'queryContext': {'originalQuery': 'fallout 76'},
    'rankingResponse': {   'mainline': {   'items': [   {   'answerType': 'News',
                                                            'value': {   'id': 'https://api.cognitive.microsoft.com/api/v7/#News'}},
                                                        {   'answerType': 'WebPages',
                                                            'resultIndex': 0,
                                                            'value': {   'id': 'https://api.cognitive.microsoft.com/api/v7/#WebPages.0'}},
                                                        {   'answerType': 'WebPages',
                                                            'resultIndex': 1,
                                                            'value': {   'id': 'https://api.cognitive.microsoft.com/api/v7/#WebPages.1'}},
                                                        {   'answerType': 'WebPages',
                                                            'resultIndex': 2,
                                                            'value': {   'id': 'https://api.cognitive.microsoft.com/api/v7/#WebPages.2'}},
                                                        {   'answerType': 'WebPages',
                                                            'resultIndex': 3,
                                                            'value': {   'id': 'https://api.cognitive.microsoft.com/api/v7/#WebPages.3'}},
                                                        {   'answerType': 'Images',
                                                            'value': {   'id': 'https://api.cognitive.microsoft.com/api/v7/#Images'}},
                                                        {   'answerType': 'WebPages',
                                                            'resultIndex': 4,
                                                            'value': {   'id': 'https://api.cognitive.microsoft.com/api/v7/#WebPages.4'}},
                                                        {   'answerType': 'WebPages',
                                                            'resultIndex': 5,
                                                            'value': {   'id': 'https://api.cognitive.microsoft.com/api/v7/#WebPages.5'}},
                                                        {   'answerType': 'Videos',
                                                            'value': {   'id': 'https://api.cognitive.microsoft.com/api/v7/#Videos'}},
                                                        {   'answerType': 'WebPages',
                                                            'resultIndex': 6,
                                                            'value': {   'id': 'https://api.cognitive.microsoft.com/api/v7/#WebPages.6'}},
                                                        {   'answerType': 'WebPages',
                                                            'resultIndex': 7,
                                                            'value': {   'id': 'https://api.cognitive.microsoft.com/api/v7/#WebPages.7'}},
                                                        {   'answerType': 'WebPages',
                                                            'resultIndex': 8,
                                                            'value': {   'id': 'https://api.cognitive.microsoft.com/api/v7/#WebPages.8'}},
                                                        {   'answerType': 'WebPages',
                                                            'resultIndex': 9,
                                                            'value': {   'id': 'https://api.cognitive.microsoft.com/api/v7/#WebPages.9'}},
                                                        {   'answerType': 'RelatedSearches',
                                                            'value': {   'id': 'https://api.cognitive.microsoft.com/api/v7/#RelatedSearches'}}]},
                           'sidebar': {   'items': [   {   'answerType': 'Entities',
                                                           'resultIndex': 0,
                                                           'value': {   'id': 'https://api.cognitive.microsoft.com/api/v7/#Entities.0'}}]}},
    'relatedSearches': {   'id': 'https://api.cognitive.microsoft.com/api/v7/#RelatedSearches',
                           'value': [   {   'displayText': 'fallout 76 '
                                                           'gameplay videos',
                                            'text': 'fallout 76 gameplay '
                                                    'videos',
                                            'webSearchUrl': 'https://www.bing.com/search?q=fallout+76+gameplay+videos'},
                                        {   'displayText': 'fallout 76 '
                                                           'download pc',
                                            'text': 'fallout 76 download pc',
                                            'webSearchUrl': 'https://www.bing.com/search?q=fallout+76+download+pc'},
                                        {   'displayText': 'bethesda fallout '
                                                           '76',
                                            'text': 'bethesda fallout 76',
                                            'webSearchUrl': 'https://www.bing.com/search?q=bethesda+fallout+76'},
                                        {   'displayText': 'how much is '
                                                           'fallout 76',
                                            'text': 'how much is fallout 76',
                                            'webSearchUrl': 'https://www.bing.com/search?q=how+much+is+fallout+76'},
                                        {   'displayText': 'fallout 76 '
                                                           'gameplay',
                                            'text': 'fallout 76 gameplay',
                                            'webSearchUrl': 'https://www.bing.com/search?q=fallout+76+gameplay'},
                                        {   'displayText': 'all about fallout '
                                                           '76',
                                            'text': 'all about fallout 76',
                                            'webSearchUrl': 'https://www.bing.com/search?q=all+about+fallout+76'},
                                        {   'displayText': 'fallout 76 story',
                                            'text': 'fallout 76 story',
                                            'webSearchUrl': 'https://www.bing.com/search?q=fallout+76+story'},
                                        {   'displayText': 'digital download '
                                                           'fallout 76',
                                            'text': 'digital download fallout '
                                                    '76',
                                            'webSearchUrl': 'https://www.bing.com/search?q=digital+download+fallout+76'}]},
    'videos': {   'id': 'https://api.cognitive.microsoft.com/api/v7/#Videos',
                  'isFamilyFriendly': True,
                  'readLink': 'https://api.cognitive.microsoft.com/api/v7/videos/search?q=fallout+76',
                  'scenario': 'List',
                  'value': [   {   'allowHttpsEmbed': True,
                                   'allowMobileEmbed': True,
                                   'contentUrl': 'https://www.youtube.com/watch?v=1uRaGUF-bgw',
                                   'datePublished': '2019-06-10T01:09:27.0000000',
                                   'description': 'Trailer for the Year 2 '
                                                  'Wastelanders update, from '
                                                  "Bethesda's conference at E3 "
                                                  '2019.',
                                   'duration': 'PT1M18S',
                                   'embedHtml': '<iframe width="1280" '
                                                'height="720" '
                                                'src="http://www.youtube.com/embed/1uRaGUF-bgw?autoplay=1" '
                                                'frameborder="0" '
                                                'allowfullscreen></iframe>',
                                   'encodingFormat': 'mp4',
                                   'height': 720,
                                   'hostPageDisplayUrl': 'https://www.youtube.com/watch?v=1uRaGUF-bgw',
                                   'hostPageUrl': 'https://www.youtube.com/watch?v=1uRaGUF-bgw',
                                   'isAccessibleForFree': True,
                                   'isSuperfresh': False,
                                   'motionThumbnailUrl': 'https://tse3.mm.bing.net/th?id=OM.mqJ2-JZ6VriOPw_1563774706&pid=Api',
                                   'name': 'Fallout 76 Wastelanders Official '
                                           'Reveal Trailer - E3 2019',
                                   'publisher': [{'name': 'YouTube'}],
                                   'thumbnail': {'height': 120, 'width': 160},
                                   'thumbnailUrl': 'https://tse3.mm.bing.net/th?id=OVP.HVizEhwFx1ENz3Rsm_ulcgEsDh&pid=Api',
                                   'viewCount': 39081,
                                   'webSearchUrl': 'https://www.bing.com/videos/search?q=fallout%2076&view=detail&mid=3F8EB8567A96F876A29A3F8EB8567A96F876A29A',
                                   'width': 1280},
                               {   'allowHttpsEmbed': True,
                                   'allowMobileEmbed': True,
                                   'contentUrl': 'https://www.youtube.com/watch?v=tOTzmOOORw0',
                                   'datePublished': '2019-06-10T00:50:12.0000000',
                                   'description': 'FALLOUT 76: WASTELANDERS '
                                                  'DLC Walkthrough coming Fall '
                                                  '2019! Order here (FREE with '
                                                  'Fallout 76): Amazon US: PS4 '
                                                  'https://amzn.to/2Wz7SPj // '
                                                  'Xbox One '
                                                  'https://amzn.to/2MBZOJ2 // '
                                                  'PC https://amzn.to/2MBhiFi '
                                                  'Amazon Canada: PS4 '
                                                  'https://amzn.to/31nuwJd // '
                                                  'Xbox One '
                                                  'https://amzn.to/2WnIMOd // '
                                                  'PC https://amzn.to/2IvFP9z '
                                                  'Amazon UK: PS4 '
                                                  'https://amzn.to/2WzWMti ...',
                                   'duration': 'PT1M22S',
                                   'embedHtml': '<iframe width="1280" '
                                                'height="720" '
                                                'src="http://www.youtube.com/embed/tOTzmOOORw0?autoplay=1" '
                                                'frameborder="0" '
                                                'allowfullscreen></iframe>',
                                   'encodingFormat': 'mp4',
                                   'height': 720,
                                   'hostPageDisplayUrl': 'https://www.youtube.com/watch?v=tOTzmOOORw0',
                                   'hostPageUrl': 'https://www.youtube.com/watch?v=tOTzmOOORw0',
                                   'isAccessibleForFree': True,
                                   'isSuperfresh': False,
                                   'motionThumbnailUrl': 'https://tse1.mm.bing.net/th?id=OM.QpB-1a8xqlJLhA_1566759658&pid=Api',
                                   'name': 'FALLOUT 76: WASTELANDERS E3 2019 '
                                           'GAMEPLAY TRAILER',
                                   'publisher': [{'name': 'YouTube'}],
                                   'thumbnail': {'height': 120, 'width': 160},
                                   'thumbnailUrl': 'https://tse1.mm.bing.net/th?id=OVP.qVg9qnBhBSw3aG6YT1dbBgEsDh&pid=Api',
                                   'viewCount': 8963,
                                   'webSearchUrl': 'https://www.bing.com/videos/search?q=fallout%2076&view=detail&mid=844B52AA31AFD57E9042844B52AA31AFD57E9042',
                                   'width': 1280},
                               {   'allowHttpsEmbed': True,
                                   'allowMobileEmbed': True,
                                   'contentUrl': 'https://www.youtube.com/watch?v=DtQ2gLjDkvI',
                                   'datePublished': '2019-06-10T01:00:55.0000000',
                                   'description': 'Wastelanders is a massive '
                                                  'free update to Fallout 76 '
                                                  'that fundamentally changes '
                                                  'the Wasteland, coming Fall '
                                                  '2019. One year after the '
                                                  'opening of Vault 76, other '
                                                  'humans have returned to '
                                                  'Appalachia. Factions of '
                                                  'Settlers and Raiders aim to '
                                                  'make the world their own '
                                                  'and claim a rumored '
                                                  'fortune. Embark on a new '
                                                  'main quest of choice and '
                                                  'consequence ...',
                                   'duration': 'PT1M22S',
                                   'embedHtml': '<iframe width="1280" '
                                                'height="720" '
                                                'src="http://www.youtube.com/embed/DtQ2gLjDkvI?autoplay=1" '
                                                'frameborder="0" '
                                                'allowfullscreen></iframe>',
                                   'encodingFormat': 'mp4',
                                   'height': 720,
                                   'hostPageDisplayUrl': 'https://www.youtube.com/watch?v=DtQ2gLjDkvI',
                                   'hostPageUrl': 'https://www.youtube.com/watch?v=DtQ2gLjDkvI',
                                   'isAccessibleForFree': True,
                                   'isSuperfresh': False,
                                   'motionThumbnailUrl': 'https://tse2.mm.bing.net/th?id=OM.J5Xyk7Y4yRq2rQ_1563634980&pid=Api',
                                   'name': 'Fallout 76 - Official Wastelanders '
                                           'Gameplay Trailer | E3 2019',
                                   'publisher': [{'name': 'YouTube'}],
                                   'thumbnail': {'height': 120, 'width': 160},
                                   'thumbnailUrl': 'https://tse2.mm.bing.net/th?id=OVP.q8OSYLHVEuV3d6iegkxEtQEsDh&pid=Api',
                                   'viewCount': 10874,
                                   'webSearchUrl': 'https://www.bing.com/videos/search?q=fallout%2076&view=detail&mid=ADB61AC938B693F29527ADB61AC938B693F29527',
                                   'width': 1280},
                               {   'allowHttpsEmbed': True,
                                   'allowMobileEmbed': True,
                                   'contentUrl': 'https://www.youtube.com/watch?v=NsBRpyOPv1c',
                                   'datePublished': '2019-06-10T16:15:45.0000000',
                                   'description': 'Today we take a look at all '
                                                  'of the new details we '
                                                  "learned about Fallout 76's "
                                                  'upcoming DLC - '
                                                  'Wastelanders. This DLC '
                                                  'brings in new weapons, '
                                                  'armors, human NPCs and '
                                                  'dialogue choices. Merch: '
                                                  'https://juicehead.net/ '
                                                  'Twitter: '
                                                  'https://twitter.com/JuiceHead33 '
                                                  'Discord: '
                                                  'https://discord.gg/jzhzrhm '
                                                  'Sources: Wastelanders '
                                                  'Gameplay: '
                                                  'https://www.youtube.com ...',
                                   'duration': 'PT12M28S',
                                   'embedHtml': '<iframe width="1280" '
                                                'height="720" '
                                                'src="http://www.youtube.com/embed/NsBRpyOPv1c?autoplay=1" '
                                                'frameborder="0" '
                                                'allowfullscreen></iframe>',
                                   'encodingFormat': 'mp4',
                                   'height': 720,
                                   'hostPageDisplayUrl': 'https://www.youtube.com/watch?v=NsBRpyOPv1c',
                                   'hostPageUrl': 'https://www.youtube.com/watch?v=NsBRpyOPv1c',
                                   'isAccessibleForFree': True,
                                   'isSuperfresh': False,
                                   'motionThumbnailUrl': 'https://tse2.mm.bing.net/th?id=OM.Q6YcNa7sujGF3g_1566678865&pid=Api',
                                   'name': "Fallout 76's New Wastelanders DLC "
                                           'Explained - Human NPCs, Dialogue '
                                           'Choices, Trailer Breakdown',
                                   'publisher': [{'name': 'YouTube'}],
                                   'thumbnail': {'height': 120, 'width': 160},
                                   'thumbnailUrl': 'https://tse2.mm.bing.net/th?id=OVP.ypE1Lp_l-Ki6ZSdgTPLY-gEsDh&pid=Api',
                                   'viewCount': 299950,
                                   'webSearchUrl': 'https://www.bing.com/videos/search?q=fallout%2076&view=detail&mid=DE8531BAECAE351CA643DE8531BAECAE351CA643',
                                   'width': 1280},
                               {   'allowHttpsEmbed': True,
                                   'allowMobileEmbed': True,
                                   'contentUrl': 'https://www.youtube.com/watch?v=j_9U-OELyds',
                                   'datePublished': '2019-06-10T00:48:01.0000000',
                                   'description': 'Facebook: '
                                                  'http://facebook.com/gLpLayground '
                                                  'Twitter: '
                                                  'http://twitter.com/GLPFeed '
                                                  'Instagram: '
                                                  'http://instagram.com/glplaygr0und '
                                                  'Twitch: '
                                                  'http://twitch.tv/glplayground '
                                                  'Outro Song: '
                                                  'https://www.youtube.com/watch?v=G2Ohf... '
                                                  'OUR GRAPHICS CARD: '
                                                  'https://amzn.to/2DP7otI OUR '
                                                  'CAPTURE CARD: '
                                                  'https://amzn.to/2Sikjs0 OUR '
                                                  'PROCESSOR: '
                                                  'https://amzn.to/2DOfG57 OUR '
                                                  '...',
                                   'duration': 'PT2M27S',
                                   'embedHtml': '<iframe width="1280" '
                                                'height="720" '
                                                'src="http://www.youtube.com/embed/j_9U-OELyds?autoplay=1" '
                                                'frameborder="0" '
                                                'allowfullscreen></iframe>',
                                   'encodingFormat': 'mp4',
                                   'height': 720,
                                   'hostPageDisplayUrl': 'https://www.youtube.com/watch?v=j_9U-OELyds',
                                   'hostPageUrl': 'https://www.youtube.com/watch?v=j_9U-OELyds',
                                   'isAccessibleForFree': True,
                                   'isSuperfresh': False,
                                   'motionThumbnailUrl': 'https://tse1.mm.bing.net/th?id=OM.tlq0Hn8OM5Hc3g_1563783141&pid=Api',
                                   'name': 'FALLOUT 76 WASTELANDERS E3 Trailer '
                                           '(Human NPCs, New Questline, '
                                           'Choices)',
                                   'publisher': [{'name': 'YouTube'}],
                                   'thumbnail': {'height': 120, 'width': 160},
                                   'thumbnailUrl': 'https://tse1.mm.bing.net/th?id=OVP.NJOLQam8-vbqviIkAFiciAEsDh&pid=Api',
                                   'viewCount': 23699,
                                   'webSearchUrl': 'https://www.bing.com/videos/search?q=fallout%2076&view=detail&mid=DEDC91330E7F1EB45AB6DEDC91330E7F1EB45AB6',
                                   'width': 1280},
                               {   'allowHttpsEmbed': True,
                                   'allowMobileEmbed': True,
                                   'contentUrl': 'https://www.youtube.com/watch?v=QAWTfttqxko',
                                   'datePublished': '2019-03-13T17:06:50.0000000',
                                   'description': 'Today we released the first '
                                                  'slate of content for Wild '
                                                  'Appalachia, a free update '
                                                  'that brings a series of new '
                                                  'quests, features, events, '
                                                  'crafting systems and more '
                                                  'to Fallout 76. Players can '
                                                  'dive in now to start a '
                                                  'brand-new quest that will '
                                                  'teach them to brew up tasty '
                                                  'beverages that will help '
                                                  '(and potentially hinder) '
                                                  'their ability to take on '
                                                  'the ...',
                                   'duration': 'PT2M2S',
                                   'embedHtml': '<iframe width="1280" '
                                                'height="720" '
                                                'src="http://www.youtube.com/embed/QAWTfttqxko?autoplay=1" '
                                                'frameborder="0" '
                                                'allowfullscreen></iframe>',
                                   'encodingFormat': 'mp4',
                                   'height': 720,
                                   'hostPageDisplayUrl': 'https://www.youtube.com/watch?v=QAWTfttqxko',
                                   'hostPageUrl': 'https://www.youtube.com/watch?v=QAWTfttqxko',
                                   'isAccessibleForFree': True,
                                   'isSuperfresh': False,
                                   'motionThumbnailUrl': 'https://tse3.mm.bing.net/th?id=OM.ITRBkV0sQ-34qA_1565073306&pid=Api',
                                   'name': 'Fallout 76 Wild Appalachia Trailer '
                                           'PEGI',
                                   'publisher': [{'name': 'YouTube'}],
                                   'thumbnail': {'height': 120, 'width': 160},
                                   'thumbnailUrl': 'https://tse3.mm.bing.net/th?id=OVP.QNvAE1B39lyJ7JlQPVng3gEsDh&pid=Api',
                                   'viewCount': 183995,
                                   'webSearchUrl': 'https://www.bing.com/videos/search?q=fallout%2076&view=detail&mid=A8F8ED432C5D91413421A8F8ED432C5D91413421',
                                   'width': 1280},
                               {   'allowHttpsEmbed': True,
                                   'allowMobileEmbed': True,
                                   'contentUrl': 'https://www.youtube.com/watch?v=4sKoAgZxxWc',
                                   'datePublished': '2019-06-10T00:55:17.0000000',
                                   'description': 'Nuclear Winter is an '
                                                  'all-new 52-player PvP '
                                                  'Battle Royale mode, free '
                                                  'for Fallout 76 players. Get '
                                                  'a Sneak Peek starting June '
                                                  '10, 2019.',
                                   'duration': 'PT1M58S',
                                   'embedHtml': '<iframe width="1280" '
                                                'height="720" '
                                                'src="http://www.youtube.com/embed/4sKoAgZxxWc?autoplay=1" '
                                                'frameborder="0" '
                                                'allowfullscreen></iframe>',
                                   'encodingFormat': '',
                                   'height': 720,
                                   'hostPageDisplayUrl': 'https://www.youtube.com/watch?v=4sKoAgZxxWc',
                                   'hostPageUrl': 'https://www.youtube.com/watch?v=4sKoAgZxxWc',
                                   'isAccessibleForFree': True,
                                   'isSuperfresh': False,
                                   'motionThumbnailUrl': 'https://tse4.mm.bing.net/th?id=OM.BVDL5hgi9gd1cg_1566705329&pid=Api',
                                   'name': 'Fallout 76 – Official Nuclear '
                                           'Winter Battle Royale Gameplay '
                                           'Trailer | E3 2019',
                                   'publisher': [{'name': 'YouTube'}],
                                   'thumbnail': {'height': 120, 'width': 160},
                                   'thumbnailUrl': 'https://tse4.mm.bing.net/th?id=OVP.q8OSYLHVEuV3d6iegkxEtQEsDh&pid=Api',
                                   'viewCount': 106024,
                                   'webSearchUrl': 'https://www.bing.com/videos/search?q=fallout%2076&view=detail&mid=727507F62218E6CB5005727507F62218E6CB5005',
                                   'width': 1280},
                               {   'allowHttpsEmbed': True,
                                   'allowMobileEmbed': True,
                                   'contentUrl': 'https://www.youtube.com/watch?v=RjbrLgdBf1A',
                                   'datePublished': '2019-09-02T01:52:05.0000000',
                                   'description': 'What exactly happens when '
                                                  'we nuke the Crashed Space '
                                                  'Station? We decided to do '
                                                  'this experiment because the '
                                                  'location will be completely '
                                                  'changed when the '
                                                  'Wastelanders DLC drops in '
                                                  'November! EVEN MORE FALLOUT '
                                                  '76 ALIEN SECRETS - '
                                                  'https://www.youtube.com/watch?v=C3aXbZjxWBA&t=644s '
                                                  'Playlist of all the nuking '
                                                  'experiment episodes so far '
                                                  'below! -https ...',
                                   'duration': 'PT16M58S',
                                   'embedHtml': '<iframe width="1280" '
                                                'height="720" '
                                                'src="http://www.youtube.com/embed/RjbrLgdBf1A?autoplay=1" '
                                                'frameborder="0" '
                                                'allowfullscreen></iframe>',
                                   'encodingFormat': 'mp4',
                                   'height': 720,
                                   'hostPageDisplayUrl': 'https://www.youtube.com/watch?v=RjbrLgdBf1A',
                                   'hostPageUrl': 'https://www.youtube.com/watch?v=RjbrLgdBf1A',
                                   'isAccessibleForFree': True,
                                   'isSuperfresh': False,
                                   'motionThumbnailUrl': 'https://tse3.mm.bing.net/th?id=OM1.XWsVc5Sg9guUkQ&pid=Api',
                                   'name': 'Fallout 76 | What Happens if You '
                                           'Nuke the Crashed Space Station? '
                                           '(Fallout 76 Secrets)',
                                   'publisher': [{'name': 'YouTube'}],
                                   'thumbnail': {'height': 120, 'width': 160},
                                   'thumbnailUrl': 'https://tse3.mm.bing.net/th?id=OVP.sYHFJAN4tRMH_5vCpCIcOwHgFo&pid=Api',
                                   'viewCount': 35650,
                                   'webSearchUrl': 'https://www.bing.com/videos/search?q=fallout%2076&view=detail&mid=91940BF6A09473156B5D91940BF6A09473156B5D',
                                   'width': 1280},
                               {   'allowHttpsEmbed': True,
                                   'allowMobileEmbed': True,
                                   'contentUrl': 'https://www.youtube.com/watch?v=2fYzRlt8ScI',
                                   'datePublished': '2019-06-10T09:00:02.0000000',
                                   'description': 'Offizieller "Fallout 76" '
                                                  'Nuclear Winter Trailer '
                                                  'German Deutsch 2018 | '
                                                  'Abonnieren http://abo.yt/gc '
                                                  '| Official #Game #Trailer | '
                                                  'http://fb.com/GameCheckYT '
                                                  'Bethesda Game Studios, die '
                                                  'preisgekrönten Entwickler '
                                                  'von Skyrim und Fallout 4, '
                                                  'heißen euch bei Fallout 76 '
                                                  'willkommen! Bei diesem '
                                                  'Online-Prequel ist jeder '
                                                  'menschliche Überlebende ein '
                                                  'Spieler ...',
                                   'duration': 'PT2M14S',
                                   'embedHtml': '<iframe width="1280" '
                                                'height="720" '
                                                'src="http://www.youtube.com/embed/2fYzRlt8ScI?autoplay=1" '
                                                'frameborder="0" '
                                                'allowfullscreen></iframe>',
                                   'encodingFormat': '',
                                   'height': 720,
                                   'hostPageDisplayUrl': 'https://www.youtube.com/watch?v=2fYzRlt8ScI',
                                   'hostPageUrl': 'https://www.youtube.com/watch?v=2fYzRlt8ScI',
                                   'isSuperfresh': False,
                                   'motionThumbnailUrl': 'https://tse1.mm.bing.net/th?id=OM.7Qqfal5gQ-3BVQ_1566716982&pid=Api',
                                   'name': 'FALLOUT 76 - Battle Royale Trailer '
                                           'German Deutsch (E3 2019) Nuclear '
                                           'Winter',
                                   'publisher': [{'name': 'YouTube'}],
                                   'thumbnail': {'height': 120, 'width': 160},
                                   'thumbnailUrl': 'https://tse1.mm.bing.net/th?id=OVP.kifwKNcDZsl3ovpdKdhPwAEsDh&pid=Api',
                                   'viewCount': 9358,
                                   'webSearchUrl': 'https://www.bing.com/videos/search?q=fallout%2076&view=detail&mid=55C1ED43605E6A9F0AED55C1ED43605E6A9F0AED',
                                   'width': 1280},
                               {   'allowHttpsEmbed': True,
                                   'allowMobileEmbed': True,
                                   'contentUrl': 'https://www.youtube.com/watch?v=yEGmlpaQntI',
                                   'datePublished': '2019-06-15T20:06:58.0000000',
                                   'description': "I can't believe Fallout "
                                                  'turned Fortnite into a real '
                                                  'thing Twitter: '
                                                  'https://twitter.com/Kevduit '
                                                  'Twitch: '
                                                  'https://www.twitch.tv/kevduit '
                                                  'Website: '
                                                  'http://www.kevduit.com/ '
                                                  '#Fallout #Fallout76 '
                                                  '#Fallout76NuclearWinter',
                                   'duration': 'PT5M20S',
                                   'embedHtml': '<iframe width="1280" '
                                                'height="720" '
                                                'src="http://www.youtube.com/embed/yEGmlpaQntI?autoplay=1" '
                                                'frameborder="0" '
                                                'allowfullscreen></iframe>',
                                   'encodingFormat': 'mp4',
                                   'height': 720,
                                   'hostPageDisplayUrl': 'https://www.youtube.com/watch?v=yEGmlpaQntI',
                                   'hostPageUrl': 'https://www.youtube.com/watch?v=yEGmlpaQntI',
                                   'isAccessibleForFree': True,
                                   'isSuperfresh': False,
                                   'motionThumbnailUrl': 'https://tse1.mm.bing.net/th?id=OM.WQgC9qQ__Yzt_w_1563766309&pid=Api',
                                   'name': 'FALLOUT 76 ACTUALLY GETS IT RIGHT!',
                                   'publisher': [{'name': 'YouTube'}],
                                   'thumbnail': {'height': 120, 'width': 160},
                                   'thumbnailUrl': 'https://tse1.mm.bing.net/th?id=OVP.iq-bBmD8EEE_djpigh--BQEsDh&pid=Api',
                                   'viewCount': 208365,
                                   'webSearchUrl': 'https://www.bing.com/videos/search?q=fallout%2076&view=detail&mid=FFED8CFD3FA4F6020859FFED8CFD3FA4F6020859',
                                   'width': 1280}],
                  'webSearchUrl': 'https://www.bing.com/videos/search?q=fallout+76'},
    'webPages': {   'totalEstimatedMatches': 44300000,
                    'value': [   {   'about': [   {'name': 'Fallout'},
                                                  {'name': 'Fallout 76'},
                                                  {'name': 'Fallout'}],
                                     'dateLastCrawled': '2019-09-01T11:03:00.0000000Z',
                                     'displayUrl': 'https://fallout.bethesda.net',
                                     'id': 'https://api.cognitive.microsoft.com/api/v7/#WebPages.0',
                                     'isFamilyFriendly': True,
                                     'isNavigational': True,
                                     'language': 'en',
                                     'name': 'Fallout',
                                     'snippet': 'Bethesda Game Studios, the '
                                                'creators of Skyrim and '
                                                'Fallout 4, welcome you to '
                                                'Fallout 76, the online '
                                                'prequel where every surviving '
                                                'human is a real person. Work '
                                                'together, or not, to survive. '
                                                'Under the threat of nuclear '
                                                'annihilation, experience the '
                                                'largest world ever created in '
                                                'Fallout. Play solo or join '
                                                'together as you explore, '
                                                'quest, and triumph against '
                                                'the wasteland’s greatest '
                                                'threats.',
                                     'url': 'https://fallout.bethesda.net/'},
                                 {   'dateLastCrawled': '2019-09-03T05:01:00.0000000Z',
                                     'displayUrl': 'https://fallout.fandom.com/wiki/Fallout_76',
                                     'id': 'https://api.cognitive.microsoft.com/api/v7/#WebPages.1',
                                     'isFamilyFriendly': True,
                                     'isNavigational': False,
                                     'language': 'en',
                                     'name': 'Fallout 76 | Fallout Wiki | '
                                             'FANDOM powered by Wikia',
                                     'snippet': 'Fallout 76 is a multiplayer '
                                                'online game developed by '
                                                'Bethesda Game Studios and '
                                                'published by Bethesda '
                                                'Softworks. It is the newest '
                                                'installment in the Fallout '
                                                'series (ninth overall) and '
                                                'was released on Microsoft '
                                                'Windows, PlayStation 4, and '
                                                'Xbox One on November 14th, '
                                                '2018. The game is set in...',
                                     'url': 'https://fallout.fandom.com/wiki/Fallout_76'},
                                 {   'dateLastCrawled': '2019-09-02T15:40:00.0000000Z',
                                     'displayUrl': 'https://en.wikipedia.org/wiki/Fallout_76',
                                     'id': 'https://api.cognitive.microsoft.com/api/v7/#WebPages.2',
                                     'isFamilyFriendly': True,
                                     'isNavigational': False,
                                     'language': 'en',
                                     'name': 'Fallout 76 - Wikipedia',
                                     'snippet': 'Fallout 76 is an online '
                                                'action role-playing game in '
                                                'the Fallout series developed '
                                                'by Bethesda Game Studios and '
                                                'published by Bethesda '
                                                'Softworks. Released for '
                                                'Microsoft Windows, '
                                                'PlayStation 4, and Xbox One '
                                                'on November 14, 2018, it is a '
                                                'prequel to previous series '
                                                'games.',
                                     'snippetAttribution': {   'license': {   'name': 'CC-BY-SA',
                                                                              'url': 'http://creativecommons.org/licenses/by-sa/3.0/'},
                                                               'licenseNotice': 'Text '
                                                                                'under '
                                                                                'CC-BY-SA '
                                                                                'license'},
                                     'url': 'https://en.wikipedia.org/wiki/Fallout_76'},
                                 {   'dateLastCrawled': '2019-08-30T02:31:00.0000000Z',
                                     'displayUrl': 'https://www.reddit.com/r/fo76',
                                     'id': 'https://api.cognitive.microsoft.com/api/v7/#WebPages.3',
                                     'isFamilyFriendly': True,
                                     'isNavigational': False,
                                     'language': 'en',
                                     'name': 'Fallout 76 | Reddit',
                                     'snippet': 'FALLOUT 76: INSIDE THE VAULT '
                                                '– UPCOMING FIXES AND '
                                                'IMPROVEMENTS. Welcome back to '
                                                'Inside the Vault! This week, '
                                                'we’re sharing a look at a '
                                                'number of bug fixes and '
                                                'improvements coming with '
                                                'Patch 13. We’ve also got '
                                                'details for you on the '
                                                'Purveyor’s latest Legendary '
                                                'Sale Event, which starts '
                                                'today. ...',
                                     'url': 'https://www.reddit.com/r/fo76/'},
                                 {   'dateLastCrawled': '2019-09-01T08:12:00.0000000Z',
                                     'displayUrl': 'https://www.amazon.com/Fallout-76-PC/dp/B07DDD9VK7',
                                     'id': 'https://api.cognitive.microsoft.com/api/v7/#WebPages.4',
                                     'isFamilyFriendly': True,
                                     'isNavigational': False,
                                     'language': 'en',
                                     'name': 'Amazon.com: Fallout 76 - PC: '
                                             'Video Games',
                                     'snippet': 'Bethesda Game Studios, the '
                                                'award-winning creators of '
                                                'Skyrim and Fallout 4, welcome '
                                                'you to Fallout 76, the online '
                                                'prequel where every surviving '
                                                'human is a real person.Work '
                                                'together, or not, to '
                                                'survive.Under the threat of '
                                                'nuclear annihilation, you’ll '
                                                'experience the largest, most '
                                                'dynamic world ever created in '
                                                'the legendary Fallout '
                                                'universe. Reclamation Day, '
                                                '2102.',
                                     'url': 'https://www.amazon.com/Fallout-76-PC/dp/B07DDD9VK7'},
                                 {   'about': [{'name': 'Fallout'}],
                                     'dateLastCrawled': '2019-09-03T01:50:00.0000000Z',
                                     'displayUrl': 'https://www.youtube.com/watch?v=M9FGaan35s0',
                                     'id': 'https://api.cognitive.microsoft.com/api/v7/#WebPages.5',
                                     'isFamilyFriendly': True,
                                     'isNavigational': False,
                                     'language': 'en',
                                     'name': 'Fallout 76 – Official Trailer - '
                                             'YouTube',
                                     'snippet': 'Watch the official trailer '
                                                'for Fallout 76, arriving '
                                                'worldwide November 14, 2018. '
                                                'Visit Fallout at '
                                                'https://beth.games/2sV71qc '
                                                'Bethesda Game Studios, the '
                                                'award-winning creators of '
                                                'Skyrim and Fallout ...',
                                     'url': 'https://www.youtube.com/watch?v=M9FGaan35s0'},
                                 {   'dateLastCrawled': '2019-08-31T13:35:00.0000000Z',
                                     'displayUrl': 'https://www.xbox.com/en-US/games/fallout-76',
                                     'id': 'https://api.cognitive.microsoft.com/api/v7/#WebPages.6',
                                     'isFamilyFriendly': True,
                                     'isNavigational': False,
                                     'language': 'en',
                                     'name': 'Fallout 76 for Xbox One | Xbox',
                                     'snippet': 'Bethesda Game Studios, the '
                                                'award-winning creators of '
                                                'Skyrim and Fallout 4, welcome '
                                                'you to Fallout 76, the online '
                                                'prequel where every surviving '
                                                'human is a real person. Work '
                                                'together, or not, to survive. '
                                                'Under the threat of nuclear '
                                                'annihilation, you’ll '
                                                'experience the largest, most '
                                                'dynamic world ever ...',
                                     'url': 'https://www.xbox.com/en-US/games/fallout-76'},
                                 {   'dateLastCrawled': '2019-09-03T16:14:00.0000000Z',
                                     'displayUrl': 'https://fallout.fandom.com/wiki/Fallout_76_plans',
                                     'id': 'https://api.cognitive.microsoft.com/api/v7/#WebPages.7',
                                     'isFamilyFriendly': True,
                                     'isNavigational': False,
                                     'language': 'en',
                                     'name': 'Fallout 76 plans | Fallout Wiki '
                                             '| FANDOM powered by Wikia',
                                     'snippet': 'Plans are items in Fallout '
                                                '76. Plans are blueprints used '
                                                'to construct weapons, armor, '
                                                'mods and workshop/C.A.M.P. '
                                                'items.',
                                     'url': 'https://fallout.fandom.com/wiki/Fallout_76_plans'},
                                 {   'dateLastCrawled': '2019-09-04T15:56:00.0000000Z',
                                     'displayUrl': 'https://www.nexusmods.com/fallout76',
                                     'id': 'https://api.cognitive.microsoft.com/api/v7/#WebPages.8',
                                     'isFamilyFriendly': True,
                                     'isNavigational': False,
                                     'language': 'en',
                                     'name': 'Fallout 76 Nexus - Mods and '
                                             'community',
                                     'snippet': 'A few weeks ago we launched '
                                                'our first Screenshot '
                                                'Community Event giving '
                                                'everyone the opportunity to '
                                                'submit a screenshot for '
                                                'Skyrim, Skyrim SE, Enderal, '
                                                'Fallout 4, and Fallout 76 '
                                                'depicting the event theme '
                                                '"Conflict and Struggle" and '
                                                'potentially win one of three '
                                                'prizes which would be awarded '
                                                'at random to three different '
                                                'participants.',
                                     'url': 'https://www.nexusmods.com/fallout76'},
                                 {   'about': [   {'name': 'Fallout'},
                                                  {   'name': 'Fallout: New '
                                                              'Vegas'}],
                                     'dateLastCrawled': '2019-05-27T01:41:00.0000000Z',
                                     'displayUrl': 'https://twitter.com/Fallout',
                                     'id': 'https://api.cognitive.microsoft.com/api/v7/#WebPages.9',
                                     'isFamilyFriendly': True,
                                     'isNavigational': False,
                                     'language': 'en',
                                     'name': 'Fallout (@Fallout) | Twitter',
                                     'snippet': 'The latest Tweets from '
                                                'Fallout (@Fallout). War. War '
                                                'never changes. Vault-Tec '
                                                'Industries HQ',
                                     'url': 'https://twitter.com/Fallout'}],
                    'webSearchUrl': 'https://www.bing.com/search?q=fallout+76'}}})






def about(request):
    return render(request, 'about.html', {})





def favorites(request):
    if request.method == 'POST':
        form = GameForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("This game has been added to your favorites"))
            return redirect('favorites')
    games = Game.objects.all()
    return render(request, 'favorites.html', {'games': games})




def delete(request, game_id):
    game = Game.objects.get(pk=game_id)
    game.delete()
    messages.success(request, ("Game has been removed from your favorites"))
    return redirect(favorites)
