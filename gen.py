#!/usr/bin/python
class Klass(object):
    def __init__(self, d):
        self.__dict__.update(d)

def dict2obj(d):
    return Klass(d)

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_parts, default_description

description = ('Generates (X)HTML documents from standalone reStructuredText '
               'sources. Uses `pygments` to colorize the content of'
               '"code-block" directives. Needs an adapted stylesheet' 
               + default_description)

# Define a new directive `code-block` that uses the `pygments` source
# highlighter to render code in color. 
#
# Code from the `pygments`_ documentation for `Using Pygments in ReST
# documents`_.

from docutils import nodes
from docutils.parsers.rst import directives
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

pygments_formatter = HtmlFormatter()

def pygments_directive(name, arguments, options, content, lineno,
                       content_offset, block_text, state, state_machine):
    try:
        lexer = get_lexer_by_name(arguments[0])
    except ValueError:
        # no lexer found - use the text one instead of an exception
	#lexer = get_lexer_by_name('text')
	raise
    parsed = highlight(u'\n'.join(content), lexer, pygments_formatter)
    return [nodes.raw('', parsed, format='html')]
pygments_directive.arguments = (1, 0, 1)
pygments_directive.content = 1
directives.register_directive('code-block', pygments_directive)

# Call the docutils publisher to render the input as html::
import os
from mako.lookup import TemplateLookup
loader = TemplateLookup(directories=['./templates'], output_encoding='utf-8')
listtpl = loader.get_template('list_tpl.mako')
indextpl = loader.get_template('index_tpl.mako')

path = './src/'
namelist = []
for filename in os.listdir(path):
    if filename.endswith('.txt'):
        fullpath = os.path.join(path, filename)
        parts = dict2obj(publish_parts(source=open(fullpath).read(), writer_name='html', settings_overrides={'initial_header_level': 2, 'language_code':'zh_cn'}))
        content = listtpl.render(c=parts)

        basename = os.path.splitext(filename)[0]
        destname = os.path.join('./html/',basename+'.html')
        open(destname, 'w').write(content)
        print destname
        namelist.append(fullpath)

#content = indextpl.render(c=namelist)
#open('html/index.html', 'w').write(content)
