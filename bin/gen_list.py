#!/usr/bin/env python
# coding: utf-8
import functools
import config
from itertools import islice
from article import *

def render(articles):
    from mako.lookup import TemplateLookup
    loader = TemplateLookup(directories=['./templates'],
            output_encoding='utf-8', input_encoding='utf-8')
    indextpl = loader.get_template('index_tpl.mako')
    html = indextpl.render(articles=articles, cfg=config)
    open('../index.html', 'w').write(html)

if __name__ == '__main__':
    from StringIO import StringIO
    testfile = StringIO('''
src/2010-04-27_blog-claim.txt
    '''
    )
    p = init_publisher()    
    articles = map(functools.partial(writedoc, p),
            islice(trans_doclist(parse_doclist(p, load_articles())), 5))
    render(articles)
