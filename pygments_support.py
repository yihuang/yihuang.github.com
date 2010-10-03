# Define a new directive `code-block` that uses the `pygments` source
# highlighter to render code in color. 
#
# Code from the `pygments`_ documentation for `Using Pygments in ReST
# documents`_.

from docutils import nodes
from docutils.parsers.rst import Directive,directives
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from myformatter import MyHtmlFormatter

class CodeBlock(Directive):
    option_spec = {
        'filename':directives.unchanged,
        'width':directives.length_or_percentage_or_unitless,
    }
    optional_arguments = 0
    required_arguments = 1
    final_argument_whitespace = False
    has_content = True

    def run(self):
        try:
            lexer = get_lexer_by_name(self.arguments[0])
        except ValueError:
            # no lexer found - use the text one instead of an exception
            #lexer = get_lexer_by_name('text')
            raise

        options = self.options
        if 'filename' in options:
            content = open(self.options['filename']).read().decode(options.get('encoding','utf-8'))
        else:
            content = u'\n'.join(self.content)

        width = options.get('width')
        formatter_options = {}
        if width:
            formatter_options['cssstyles'] = 'width:'+width
        parsed = highlight(content, lexer, MyHtmlFormatter(**formatter_options))
        return [nodes.raw('', parsed, format='html')]

directives.register_directive('code-block', CodeBlock)

