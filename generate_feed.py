import datetime

import requests
from bs4 import BeautifulSoup

# Constants
BASE_URL = "https://www.paulgraham.com/"
ARTICLES_URL = BASE_URL + "articles.html"
FEED_FILE = "feed.xml"
FEED_FILE_WITHOUT_CONTENT = "feed_without_content.xml"


def fetch_article_content(url):
    """Fetches the content of a single article."""
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the main content. Most PG essays are inside <font> tags.
    content = ""
    for font_tag in soup.find_all("font"):
        content += font_tag.get_text(separator="\n", strip=True)

    return content.strip()


def fetch_articles():
    """Fetches the list of articles with title, URL, and content."""
    response = requests.get(ARTICLES_URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")

    articles = []
    articles_without_content = []

    # TODO_HACK: Num of links to skip. The first 3 links are not the most recent essays.
    # Rather, Paul shares the best essays to start "if you're not sure which to read [first]

    # Skipping the first 3 links (non-recent, recommended essays)
    num_links_to_skip = 3

    # Find all 'a' tags with hrefs, skip those that have no actual text
    for link in soup.find_all("a", href=True)[num_links_to_skip + 1 :]:
        href = link["href"]
        title = link.get_text(strip=True)  # Extracts only the text, skips inner HTML tags
        if href.endswith(".html") and title:  # Only process if title has actual text
            url = BASE_URL + href
            content = fetch_article_content(url)  # Fetch the content of each article
            articles.append({"title": title, "url": url, "content": content})
            articles_without_content.append({"title": title, "url": url})

    return articles, articles_without_content


def generate_rss_feed(articles):
    """Generates the RSS feed with articles and their content."""
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
        if "content" in article:
            rss_feed += f"""
            <item>
            <title>{article['title']}</title>
            <link>{article['url']}</link>
            <description><![CDATA[{article['content']}]]></description>
            </item>
            """
        else:
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


def save_rss_feed(rss_feed, file):
    """Saves the RSS feed to a file."""
    with open(file, "w") as f:
        f.write(rss_feed)


def main():
    """Main entry point of the script."""
    articles, articles_without_content = fetch_articles()
    rss_feed = generate_rss_feed(articles)
    save_rss_feed(rss_feed, FEED_FILE)
    rss_feed_without_content = generate_rss_feed(articles_without_content)
    save_rss_feed(rss_feed_without_content, FEED_FILE_WITHOUT_CONTENT)
    print(f"RSS feed generated with {len(articles)} articles")


if __name__ == "__main__":
    main()
