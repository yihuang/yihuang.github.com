#!/usr/bin/python
# coding: utf-8
import clutter

def create_sqare(stage, color):
    sqare = clutter.Rectangle()
    sqare.set_color(color)
    sqare.set_size(100, 150)
    # 设置锚点的相对坐标，position将以锚点为基准，
    # 旋转的时候也以锚点为中心
    sqare.set_anchor_point(50, 75)
    sqare.set_position(128, 128)
    stage.add(sqare)
    return sqare

stage = clutter.Stage()
stage.set_title('rotate')
stage.set_color(clutter.color_from_string('#000000'))
stage.set_size(256, 256)

colors = ['#ccffffaa', '#ffffccaa', '#ffccffaa', '#ffff00aa', '#00ffffaa']
sqares = [create_sqare(stage, clutter.color_from_string(color)) for color in colors]

rotate = 0
def on_new_frame(stage,event,data=None):
    global rotate
    rotate += 0.3
    for i,sqare in enumerate(sqares):
        # 围绕Z轴和X轴进行旋转，哈哈，看到3D效果了吧
        # 你也可以尝试只围绕 Z 轴旋转，那就是在平面上进行旋转了
        sqare.set_rotation(clutter.Z_AXIS, rotate*i,0,0,0)
        sqare.set_rotation(clutter.X_AXIS, rotate*i,0,0,0)

# timeline是clutter动画接口的核心
timeline = clutter.Timeline(60)
# 每进入一帧，将调用回调函数
timeline.connect('new-frame', on_new_frame)
# 动画循环播放
timeline.set_loop(True)
timeline.start()

def on_button_press(stage, event, data=None):
    # 如果觉得方框太多，点击即可隐藏
    selected = stage.get_actor_at_pos(clutter.PICK_ALL, event.x, event.y)
    if selected!=stage:
        selected.hide()

stage.show()
stage.connect("destroy", clutter.main_quit)
stage.connect("button-press-event", on_button_press)

clutter.main()
