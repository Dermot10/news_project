from django.shortcuts import render
from newsapi import NewsApiClient


def index(request):
    newsApi = NewsApiClient(api_key="0f78a239350041f4b02f2537e9fb6160")
    headLines = newsApi.get_top_headlines(sources='bbc-news')
    articles = headLines['articles']
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
    mylist = zip(news, desc, img)

    return render(request, 'main/index.html', context={"mylist": mylist})
