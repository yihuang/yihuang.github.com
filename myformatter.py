from pygments.util import get_bool_opt
from pygments.formatters import html
from pygments.formatters.html import HtmlFormatter, _get_ttype_class
from pygments.token import Token, Text, STANDARD_TYPES

SHADOW = '0px 0px 8px'

html.CSSFILE_TEMPLATE = '''\
td.linenos { background-color: #f0f0f0; padding-right: 10px; }
span.lineno { background-color: #f0f0f0; padding: 0 5px 0 5px; }
pre { line-height: 150%%; background:black url('bg.jpg'); text-shadow:white '''+SHADOW+'''; -webkit-text-stroke:1px white; -moz-text-stroke:1px white;font-weight:bolder; font-size:24px; color:white; text-fill-color:transparent; -webkit-text-fill-color:transparent;-moz-text-fill-color:transparent;}
%(styledefs)s
'''

html.DOC_HEADER = '''\
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN"
   "http://www.w3.org/TR/html4/strict.dtd">

<html>
<head>
  <title>%(title)s</title>
  <meta http-equiv="content-type" content="text/html; charset=%(encoding)s">
  <style type="text/css">
''' + html.CSSFILE_TEMPLATE + '''
  </style>
</head>
<body>
<h2>%(title)s</h2>

'''



class MyHtmlFormatter(HtmlFormatter):

    name = 'MYHTML'
    aliases = ['myhtml']
    filenames = ['*.html', '*.htm']

    def __init__(self, **options):
        super(MyHtmlFormatter, self).__init__(**options)
        self.linediv = get_bool_opt(options, 'linediv', False)
        self.extra_cssclass = options.get('extra_cssclass', '')

    def _create_stylesheet(self):
        t2c = self.ttype2class = {Token: ''}
        c2s = self.class2style = {}
        cp = self.classprefix
        for ttype, ndef in self.style:
            name = cp + _get_ttype_class(ttype)
            style = ''
            if ndef['color']:
                style += 'color: #%s; '%ndef['color']
                style += 'text-fill-color:transparent; '
                style += '-webkit-text-fill-color:transparent; '
                style += '-moz-text-fill-color:transparent; '
                style += 'text-shadow: #%s %s; '%(ndef['color'], SHADOW)
                style += 'text-stroke: #%s 1px; '%ndef['color']
                style += '-webkit-text-stroke: #%s 1px; '%ndef['color']
                style += '-moz-text-stroke: #%s 1px; '%ndef['color']
            if ndef['bold']:
                style += 'font-weight: bold; '
            if ndef['italic']:
                style += 'font-style: italic; '
            if ndef['underline']:
                style += 'text-decoration: underline; '
            if ndef['bgcolor']:
                style += 'background-color: #%s; ' % ndef['bgcolor']
            if ndef['border']:
                style += 'border: 1px solid #%s; ' % ndef['border']
            if style:
                t2c[ttype] = name
                # save len(ttype) to enable ordering the styles by
                # hierarchy (necessary for CSS cascading rules!)
                c2s[name] = (style[:-2], ttype, len(ttype))

    def _wrap_linediv(self, inner):
        for t, line in inner:
            yield t, '<div class="line" id="LC%d">%s</div>'%(t, line)

    def _wrap_div(self, inner):
        style = []
        if (self.noclasses and not self.nobackground and
            self.style.background_color is not None):
            style.append('background: %s' % (self.style.background_color,))
        if self.cssstyles:
            style.append(self.cssstyles)
        style = '; '.join(style)

        yield 0, ('<div' + (self.cssclass and ' class="%s %s"' % (self.cssclass, self.extra_cssclass))
                  + (style and (' style="%s"' % style)) + '>')
        for tup in inner:
            yield tup
        yield 0, '</div>\n'

    def format_unencoded(self, tokensource, outfile):
        source = self._format_lines(tokensource)
        if self.hl_lines:
            source = self._highlight_lines(source)
        if not self.nowrap:
            if self.linenos == 2:
                source = self._wrap_inlinelinenos(source)
            if self.lineanchors:
                source = self._wrap_lineanchors(source)
            if self.linediv:
                source = self._wrap_linediv(source)
            source = self.wrap(source, outfile)
            if self.linenos == 1:
                source = self._wrap_tablelinenos(source)
            if self.full:
                source = self._wrap_full(source, outfile)

        for t, piece in source:
            outfile.write(piece)
