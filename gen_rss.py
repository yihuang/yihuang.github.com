#!/usr/bin/python
from datetime import datetime
from PyRSS2Gen import RSS2, RSSItem, Guid
import config
from article import init_publisher, gen_doclist

p = init_publisher()
articles = gen_doclist(p)

rss = RSS2(
        title = config.blogname,
        link = config.blogurl,
        description = config.description,
        lastBuildDate = datetime.now(),
        items = [
            RSSItem(
                title = article.title,
                link = article.url,
                description = article.content,
                guid = Guid(article.url),
                pubDate = article.date
            )
            for article in articles
        ]
)

rss_path = 'html/rss.xml'
rss.write_xml(open(rss_path, 'w'))
print 'generated feeds', rss_path
