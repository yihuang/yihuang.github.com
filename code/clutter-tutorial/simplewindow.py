#!/usr/bin/python
import clutter
stage = clutter.Stage()
stage.set_title('simple')
stage.set_size(256,256)
stage.set_color(clutter.color_from_string('black'))

stage.show()
stage.connect("destroy", clutter.main_quit)

clutter.main()
