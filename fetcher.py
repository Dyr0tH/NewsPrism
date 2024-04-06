import requests

def fetch_news(api_key, query, sources=None):
    """
    Fetches news JSON data from the News API.

    Parameters:
        - api_key (str): Your News API key.
        - query (str): The search query for news articles.
        - sources (list, optional): List of news sources (e.g., ['bbc-news', 'cnn']). Defaults to None.

    Returns:
        - dict: A dictionary containing the JSON response from the News API.
    """

    if query:
        url = 'https://newsapi.org/v2/everything'
        params = {
            'q': query,
            'apiKey': api_key,
            'language': 'en',
            'sortBy': 'publishedAt'
        }
        if sources:
            params['sources'] = ','.join(sources)

        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            print(f"Error fetching news: {data.get('message')}")
            return None

    else:
        url = f"https://newsapi.org/v2/top-headlines"
        params = {
            'apiKey': api_key,
            'country': 'in'
        }
        response = requests.get(url, params=params)
        data = response.json()
        return data



def fetchmain(query=None):
    api_key = open('env').readline()

    query = query

    # Optional: news sources (e.g., ['bbc-news', 'cnn'])
    sources = None

    # Fetch news data
    news_data = fetch_news(api_key, query, sources)

    if news_data:
        articles = []
        for article in news_data.get('articles'):
            articles.append({
                'img_src': article.get('urlToImage', ''),
                'news_title': article.get('title', ''),
                'desc_text': article.get('description', ''),
                'publish_date': article.get('publishedAt', ''),
                'news_link': article.get('url', '')
            })

        return articles

    else:
        print("Failed to fetch news data.")
        return None
