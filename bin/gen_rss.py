#!/usr/bin/python
from datetime import datetime
from collections import defaultdict
from PyRSS2Gen import RSS2, RSSItem, Guid
import config
from article import init_publisher, gen_doclist

p = init_publisher()
articles = gen_doclist(p)

def render_rss():
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

    rss_path = '../rss.xml'
    rss.write_xml(open(rss_path, 'w'))
    print 'generated feeds', rss_path

render_rss()

def render_list():
    date_group = defaultdict(list)
    for article in articles:
        date_group[article.date].append(article)
    from mako.lookup import TemplateLookup
    loader = TemplateLookup(directories=['./templates'],
            output_encoding='utf-8', input_encoding='utf-8')
    listtpl = loader.get_template('list_tpl.mako')
    sorted_group = sorted(date_group.items(), key=lambda (k,v):k, reverse=True)
    html = listtpl.render(date_group=sorted_group, cfg=config)
    open('../list.html', 'w').write(html)
    print 'generated list page'

render_list()
