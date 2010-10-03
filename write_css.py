#!/usr/bin/env python

from myformatter import MyHtmlFormatter
from pygments.formatters.html import HtmlFormatter

defaultcss = HtmlFormatter().get_style_defs('.highlight')
mycss = MyHtmlFormatter().get_style_defs('.effects')
open('html/css/pygments.css', 'w').write(defaultcss+'\n'+mycss)

print 'success'
