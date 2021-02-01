import feedparser
from flask import Flask, render_template

app = Flask(__name__)

ITUNE_FEEDS = {'new-release': 'https://rss.itunes.apple.com/api/v1/us/apple-music/new-releases/all/10/explicit.rss',
                'top-songs':'https://rss.itunes.apple.com/api/v1/us/apple-music/top-songs/all/10/explicit.rss',
                'top-albums':'https://rss.itunes.apple.com/api/v1/us/apple-music/top-albums/all/10/explicit.rss'
               }

@app.route("/<feed_type>")
def get_feed(feed_type='new-release'):
    feed = feedparser.parse(ITUNE_FEEDS[feed_type])
    first_item = feed['entries'][0]
    return render_template("home.html",
                      title=first_item.get("title"),
                      description=first_item.get("description"),
                      link=first_item.get("link"))
app.env="development"
app.run(debug=True)