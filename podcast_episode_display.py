import feedparser
import pprint as pp

# List of podcast RSS feed URLs
podcast_feeds = [
    "https://dataskeptic.libsyn.com/rss",
    "https://anchor.fm/s/758d304/podcast/rss",
    "https://feeds.megaphone.fm/cyberwire-daily-podcast",
    "https://feeds.megaphone.fm/cyberwire-research-saturday",
    "https://feeds.megaphone.fm/COPILOT2233030486",
    "https://feeds.acast.com/public/shows/6dab3ca4-41f5-4fd4-bba6-224ab53f5113",
    "https://magneticmemorymethod.libsyn.com/rss",
    "https://machinelearningguide.libsyn.com/rss",
    "https://changelog.com/practicalai/feed",
    "https://mlcafe.libsyn.com/rss",
    "https://anchor.fm/s/1e4a0eac/podcast/rss",
    "https://feeds.megaphone.fm/MLN2155636147",
    "https://www.aidatatoday.com/feed/podcast/",
    "https://feed.podbean.com/aiandyou/feed.xml",
    "https://feeds.soundcloud.com/users/soundcloud:users:253585900/sounds.rss",
    "https://media.rss.com/learning-from-machine-learning/feed.xml",
    "https://www.codingblocks.net/feed/podcast/",
    "https://www.omnycontent.com/d/playlist/c4157e60-c7f8-470d-b13f-a7b30040df73/564f493f-af32-4c48-862f-a7b300e4df49/ac317852-8807-44b8-8eff-a7b300e4df52/podcast.rss",
    "https://www.voiceamerica.com/rss/itunes/3959",
    "https://anchor.fm/s/1ee700cc/podcast/rss",
    "https://talkpython.fm/episodes/rss",
    "https://pythonbytes.fm/episodes/rss",
    "https://api.substack.com/feed/podcast/1662473.rss",
    "https://feeds.transistor.fm/python-people",
    "https://feeds.transistor.fm/test-code-in-python",
    # ... add all other URLs here ...
]


# Function to get the most recent episode from a podcast feed


def get_recent_episodes(feed_url, num_episodes_to_display=3):
    feed = feedparser.parse(feed_url)
    episodes = []
    for entry in feed.entries[:num_episodes_to_display]:
        if hasattr(entry, 'link'):
            episodes.append({
                "title": entry.get("title", "No title available"),
                "published": entry.get("published", "No publish date available"),
                "link": entry.link
            })
        else:
            episodes.append({
                "title": entry.get("title", "No title available"),
                "published": entry.get("published", "No publish date available"),
                "link": "No link available"
            })
    return episodes

def get_most_recent_episode(feed_url):
    feed = feedparser.parse(feed_url)
    if feed.entries:
        latest_entry = feed.entries[0]
        episode_info = {
            "title": latest_entry.get("title", "No title available"),
            "published": latest_entry.get("published", "No publish date available")
        }
        # Handling missing 'link' attribute
        if hasattr(latest_entry, 'link'):
            episode_info["link"] = latest_entry.link
        else:
            episode_info["link"] = "No link available"

        return episode_info
    else:
        return None


# Main function to display recent episodes
def main():
    choice = int(input("episodes? or only most recent? (input 1 or 2): "))
    if choice == 2:
        for url in podcast_feeds:
            episode_info = get_most_recent_episode(url)
            if episode_info:
                print(f"Title: {episode_info['title']}\nPublished: {episode_info['published']}\nLink: {episode_info['link']}\n")
            else:
                print(f"No episodes found for feed: {url}\n")
    elif choice == 1:
        num_of_episodes_to_get = int(input("How many episodes from most recent do you want (integer)? > "))
        for url in podcast_feeds:
            episodes_info = get_recent_episodes(url, num_of_episodes_to_get)
            if episodes_info:
                for episode in episodes_info:
                    # Access fields of each episode dictionary
                    print(f"\033[36mTitle: {episode['title']}\n\033[34mPublished: {episode['published']}\n\033[33mLink: {episode['link']}\n\033[0m")
            else:
                print(f"\033[31mNo episodes info found for feed:\033[0m {url}")


if __name__ == "__main__":
    main()
