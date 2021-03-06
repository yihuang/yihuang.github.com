#!/usr/bin/env python
"""
Convert latex math to images.  Treats the default and ``texmath`` roles as
inline LaTeX math and the ``texmath::`` directive as display latex math.

If you include a file which also needs mathhack/imgmathhack preprocessing,
write a name containing ``.mathhack`` in the include directive and it will be
replaced with ``.imgmathhack`` when preprocessed by this script (of course,
you should create both preprocessed versions of the file).

.. note::
    This runs external commands and leaves files after itself!  To reduce
    running time when images are not changed and to reuse images for equal
    fomulas, image names are md5 of the formula (hoping that no collisions
    will happen) and images that already exist are not rebuilt.  You should
    purge the ``imgmath`` subdirectory manually to get rid of unused formulas.

    You'll need:

    - ``tex_to_images``, last version seems to live at the `speech_tools
      CVS`__.
      
      __ http://cvs.sourceforge.net/viewcvs.py/*checkout*/
         emu/speech_tools/scripts/tex_to_images.prl?rev=HEAD

      It, in turn, relies upon:

      - LaTeX
      - ``dviselect`` (part of ``dviutils``)
      - ``dvips``
      - Ghoscript
      - netpbm tools
"""

import os, os.path, hashlib

from rolehack import *

def system(cmd):
    import sys
    print >> sys.stderr, cmd
    os.system(cmd)

class Tex_to_images(object):
    """Feeds math to ``tex_to_images.prl``.  Always goes through ppm."""
    def __init__(self, dir='../imgmath', srcdir='imgmath/', options='-s 1.5',
                 converter='pnmtopng', extension='.png'):
        try:
            os.mkdir(dir)
        except OSError:
            pass
        self.options = options
        self.dir = dir
        self.srcdir = srcdir
        self.converter = converter
        self.extension = extension
    def process(self, text):
        """Returns output filename."""
        dir = self.dir
        srcdir = self.srcdir
        extension = self.extension
        options = self.options
        converter = self.converter
        fname = hashlib.md5(text).hexdigest()
        fpath = os.path.join(dir, fname)
        if not os.path.exists(fpath + extension):
            f = file(fpath, 'w')
            f.write('@Start\n%s\n@End\n' % (text,))
            f.close()
            system(('cd tex2image/;./tex_to_images.prl -f ppm -d ../%(dir)s -o %(fname)s.tmp '
                       '%(options)s < ../%(fpath)s > /dev/null' % vars()))
            if self.converter:
                system('%s < %s.tmp > %s%s' %
                          (self.converter, fpath, fpath, extension))
            else:
                os.rename(fpath + '.tmp', fpath + '.ppm')
            os.remove(fpath + '.tmp')
        return os.path.join(self.srcdir, fname) + extension
    def texmath(self, text):
        text = ' '.join(text.split())
        src = self.process(text)
        return '''\
image:: %(src)s
    :class: texmath align-middle
    :alt: %(text)s
''' % locals()
    def texdisplay(self, text):
        src = self.process(text)
        return '''\
image:: %(src)s
    :align: center
    :class: texdisplay
    :alt: %(text)s
''' % locals()

child = Tex_to_images()
texmath = child.texmath
texdisplay = child.texdisplay

def mangle_include(text):
    return 'include:: ' + text.replace('.mathhack', '.imgmathhack')


if __name__ == '__main__':
    main({'m': texmath}, None,
         {'m': texdisplay, 'include': mangle_include})
