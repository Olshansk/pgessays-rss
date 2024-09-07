import datetime

import requests
from bs4 import BeautifulSoup

# Constants
BASE_URL = "https://www.paulgraham.com/"
ARTICLES_URL = BASE_URL + "articles.html"
FEED_FILE = "pgessays.rss"


def fetch_articles():
    response = requests.get(ARTICLES_URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")

    articles = []

    # TODO_HACK: Num of links to skip. The first 3 links are not the most recent essays.
    # Rather, Paul shares the best essays to start "if you're not sure which to read [first]".
    num_links_to_skip = 3

    # Find all 'a' tags with hrefs, skip those that have no actual text
    for link in soup.find_all("a", href=True)[num_links_to_skip + 1 :]:
        href = link["href"]
        title = link.get_text(strip=True)  # Extracts only the text, skips inner HTML tags
        # Ensure we capture only relevant essay links with titles
        # print(title)
        # print(link)
        if href.endswith(".html") and title:  # Only process if title has actual text
            url = BASE_URL + href
            articles.append({"title": title, "url": url})

    return articles


def generate_rss_feed(articles):
    now = datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")

    rss_feed = f"""<?xml version="1.0"?>
    <rss version="2.0">
    <channel>
      <title>Paul Graham: Essays</title>
      <link>{BASE_URL}</link>
      <description>Scraped feed of essays from paulgraham.com</description>
      <lastBuildDate>{now}</lastBuildDate>
    """

    for article in articles:
        rss_feed += f"""
        <item>
          <title>{article['title']}</title>
          <link>{article['url']}</link>
        </item>
        """

    rss_feed += """
    </channel>
    </rss>
    """
    return rss_feed


def save_rss_feed(rss_feed):
    with open(FEED_FILE, "w") as f:
        f.write(rss_feed)


def main():
    articles = fetch_articles()
    rss_feed = generate_rss_feed(articles)
    save_rss_feed(rss_feed)
    print(f"RSS feed generated with {len(articles)} articles")


if __name__ == "__main__":
    main()
