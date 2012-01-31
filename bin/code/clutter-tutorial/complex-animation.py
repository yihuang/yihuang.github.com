#!/usr/bin/python
# coding: utf-8
import clutter

def create_sqare(stage, color):
    sqare = clutter.Rectangle()
    sqare.set_color(color)
    sqare.set_size(100, 150)
    sqare.set_anchor_point(50, 75)
    sqare.set_position(128, 128)
    stage.add(sqare)
    return sqare

stage = clutter.Stage()
stage.set_title('complex')
stage.set_color(clutter.color_from_string('#000000'))
stage.set_size(256, 256)

colors = ['#ccffffaa', '#ffffccaa', '#ffccffaa', '#ffff00aa', '#00ffffaa']
sqares = [create_sqare(stage, clutter.color_from_string(color)) for color in colors]

rotate = 0
def on_rotate_frame(stage,event,data=None):
    global rotate
    rotate += 0.3
    for i,sqare in enumerate(sqares):
        sqare.set_rotation(clutter.Z_AXIS, rotate*i,0,0,0)
        sqare.set_rotation(clutter.X_AXIS, rotate*i,0,0,0)

scale = 0
speed = 0.1
def on_scale_frame(stage,event,data=None):
    global scale,speed
    scale += speed
    if scale>1.0:
        scale = 1.0
        speed = -speed
    elif scale<0.0:
        scale = 0.0
        speed = -speed

    scale_amount = scale+1.0
    for i,sqare in enumerate(sqares):
        # 设置缩放，两个参数代表方框平面上两个维度上的缩放
        sqare.set_scale(scale_amount, scale_amount)

rotate_timeline = clutter.Timeline(60)
rotate_timeline.connect('new-frame', on_rotate_frame)

scale_timeline = clutter.Timeline(60)
scale_timeline.connect('new-frame', on_scale_frame)

# score 对象用来管理多个timeline对象的组合
# 组合方式可以是并行，也可以是串行
score = clutter.Score()
score.append(rotate_timeline)
# 两个timeline并行执行
score.append(scale_timeline)
score.set_loop(True)
score.start()

def on_button_press(stage, event, data=None):
    # 如果觉得方框太多，点击即可隐藏
    selected = stage.get_actor_at_pos(clutter.PICK_ALL, event.x, event.y)
    if selected!=stage:
        selected.hide()

stage.show()
stage.connect("destroy", clutter.main_quit)
stage.connect("button-press-event", on_button_press)

clutter.main()
