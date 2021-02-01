import feedparser
from flask import Flask, render_template

app = Flask(__name__)

ITUNE_FEEDS = {'new-release': 'https://rss.itunes.apple.com/api/v1/us/apple-music/new-releases/all/10/explicit.rss',
                'top-songs':'https://rss.itunes.apple.com/api/v1/us/apple-music/top-songs/all/10/explicit.rss',
                'top-albums':'https://rss.itunes.apple.com/api/v1/us/apple-music/top-albums/all/10/explicit.rss',
                'coming-soon' : 'https://rss.itunes.apple.com/api/v1/us/apple-music/coming-soon/all/10/explicit.rss'
               }


@app.route("/<feed_type>")
def get_feed(feed_type='new-release'):
    feed = feedparser.parse(ITUNE_FEEDS[feed_type])
    return render_template("home.html", items=feed['entries'])
app.env="development"
app.run(debug=True)