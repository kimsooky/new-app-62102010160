import feedparser
from flask import Flask

app = Flask(__name__)

ITUNE_FEEDS = {'new-release': 'https://rss.itunes.apple.com/api/v1/us/apple-music/new-releases/all/10/explicit.rss',
           'top-songs':'https://rss.itunes.apple.com/api/v1/us/apple-music/top-songs/all/10/explicit.rss',
                'top-albums':'https://rss.itunes.apple.com/api/v1/us/apple-music/top-albums/all/10/explicit.rss'
               }

@app.route("/new-release")
def new_release():
    return get_feed('new-release')
@app.route("/top-songs")
def top_songs():
    return get_feed('top-songs')


def get_feed(feed_type):
    feed = feedparser.parse(ITUNE_FEEDS[feed_type])
    first_item = feed['entries'][0]
    return """<html>
       <body>
           <h1>{0}</h1>
           <b>{1}</b> <br/>
           <i>{2}</i> <br/>
           <a href="{3}">{3}</a> <br/>
       </body>
   </html>""".format(feed_type, first_item.get("title"), first_item.
                     get("description"), first_item.get("link"))


app.env="development"
app.run(debug=True)