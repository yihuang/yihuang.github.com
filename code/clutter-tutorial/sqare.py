#!/usr/bin/python
import clutter

stage = clutter.Stage()
stage.set_title('sqare')
stage.set_color(clutter.color_from_string('black'))
stage.set_size(256, 256)

sqare = clutter.Rectangle()
sqare.set_color(clutter.color_from_string('blue'))
sqare.set_size(100, 100)
sqare.set_position(50, 50)

stage.add(sqare)

stage.show()
stage.connect("destroy", clutter.main_quit)

clutter.main()
