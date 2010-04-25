# coding: utf-8
import os, re, sys
from cStringIO import StringIO
import functools
from datetime import datetime
import pygments_support
import imgmathhack
from utils import *
import config

def init_publisher():
    from docutils.core import Publisher
    from docutils.io import StringOutput
    p = Publisher(destination_class=StringOutput)
    p.set_components('standalone', 'restructuredtext', 'html')
    p.get_settings()
    return p

def load_articles():
    src_dir = 'src/'
    filename_reg = re.compile(r'^(\d+-\d+-\d+)_(.*)')
    for fullname in sys.stdin.readlines():
        fullname = fullname.strip()
        filename = os.path.basename(fullname)
        if filename.endswith('.txt'):
            m = filename_reg.match(filename)
            if m:
                date = m.group(1)
                year,month,day=map(int, date.split('-'))
                dateobj = datetime(year,month,day)
                filename_noext=os.path.splitext(filename)[0]
                print 'load article', fullname
                yield Klass(date=dateobj, fullname=fullname, filename=filename, filename_noext=filename_noext, url='%s%s.html'%(config.blogurl,filename_noext))

def parse_doclist(p, article_list):
    for article in article_list:
        result = imgmathhack.process(open(article.fullname).read(), {'m': imgmathhack.texmath}, None,
                {'m': imgmathhack.texdisplay})

        p.set_source(source=StringIO(result), source_path=article.fullname)
        p.document = p.reader.read(p.source, p.parser, p.get_settings())
        p.apply_transforms()
        article.doc = p.document
        article.ndoc = p.reader.new_document()
        yield article

def trans_doclist(article_list):
    # 算法，从文档中萃取简介和目录
    # 简单段落，取全部
    # 有标题的段落，取标题和第一段
    # 有标题有topic的，取标题和topic
    # 有标题有topic的有简介的，取标题和topic和简介
    for article in article_list:
        doc,ndoc = article.doc,article.ndoc
        rootlist = filter(lambda n:n.tagname!='decoration', doc.children)
        resultlist = []
        if rootlist[0].tagname == 'title':
            article.title = rootlist[0].astext()
            for idx,node in enumerate(rootlist):
                if node.tagname=='topic':
                    break
            else:
                idx=-1
            if idx==-1: # no topic
                resultlist = rootlist[1:]
            else:
                resultlist = rootlist[1:idx+1]
        else:
            article.title = u'碎片'
            resultlist = rootlist[:]

        ndoc.children = resultlist
        yield article

def writedoc(p, article):
    buf = StringIO()
    p.set_destination()
    p.writer.write(article.ndoc, p.destination)
    p.writer.assemble_parts()
    article.content = p.writer.parts['fragment']
    #article.title = p.writer.parts['title'].strip()
    #article.content = p.destination.destination.decode('utf-8')
    return article

def gen_doclist(p):
    return map(functools.partial(writedoc, p), trans_doclist(parse_doclist(p, load_articles())))
