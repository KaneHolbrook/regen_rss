import feedparser


def display_multiple_feeds(feed_urls):
    for url in feed_urls:
        feed = feedparser.parse(url)

        print(f"\nProcessing feed: {url}")

        # Check if 'feed' attribute exists and has a 'title'
        if hasattr(feed, 'feed') and hasattr(feed.feed, 'title'):
            print(f"Feed Title: {feed.feed.title}")
        else:
            print("Feed title not available")

        # Check if 'feed' attribute exists and has a 'link'
        if hasattr(feed, 'feed') and hasattr(feed.feed, 'link'):
            print(f"Feed Link: {feed.feed.link}")
        else:
            print("Feed link not available")

        print("\n--- Latest Entries ---")

        if not feed.entries:
            print("No entries found in this feed")
        else:
            for entry in feed.entries[:3]:  # Display top 3 entries per feed
                print(f"\nTitle: {entry.get('title', 'No title available')}")
                print(f"Link: {entry.get('link', 'No link available')}")
                print(f"Published: {entry.get('published', 'No publication date available')}")
                summary = entry.get('summary', 'No summary available')
                print(f"Summary: {summary[:150]}..." if len(summary) > 150 else summary)

        print("-" * 50)


# Example usage
rss_urls = [
    "https://civileats.com/feed",
    "https://rodaleinstitute.org/feed",
    "https://kisstheground.com/category/regenerative-agriculture/feed"
]

display_multiple_feeds(rss_urls)
