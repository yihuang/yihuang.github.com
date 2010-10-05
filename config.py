# coding: utf-8
from utils import *
domain = 'yi-programmer.com'
blogurl = 'http://%s/blog/'%domain
blogname=u'精确编程'
description=u''
links=[
    u'<a href="/">Home</a>',
    u'<a href="/blog/">Blog</a>',
    u'<a href="https://groups.google.com/group/yi-programmer-comment" target="_blank">Comments</a>',
    u'<a href="http://9.douban.com/subject/9361637/" target="_blank">豆瓣九点</a>',
]
nav_icons = [
    (u'首页', '/', 'images/icons/home.png', 'main'),
    (u'博客', '/blog/', 'images/icons/blog.png', 'main'),
]
link_icons = [
    (u'Delicious', 'http://www.delicious.com/huangyi', 'http://www.delicious.com/favicon.ico',''),
    (u'Google Reader Share', 'http://www.google.com/reader/shared/yi.codeplayer', 'http://www.google.com/reader/ui/favicon.ico',''),
    (u'豆瓣', 'http://www.douban.com/people/huangyi/', 'http://img3.douban.com/favicon.ico',''),
    (u'9点', 'http://9.douban.com/subject/9361637/', 'http://9.douban.com/pics/newnine/9.ico',''),
    (u'啄木鸟社区', 'http://wiki.woodpecker.org.cn/moin/HuangYi', 'http://wiki.woodpecker.org.cn/favicon.ico',''),
    (u'42区', 'http://42qu.com/-10000020', 'http://42qu.com/favicon.ico',''),
    (u'KanRss', 'http://kanrss.com/@yihuang', 'http://kanrss.com/favicon.ico',''),
]
boxes=[
    u'''
<h2>个人简介</h2>
<img align="left" src="images/avatar.jpg" style="margin:10px 5px 5px 5px"/>
<p>
黃毅&nbsp;&nbsp;<br/>现居:广东深圳<br/><br/>
编程爱好者，python社区活跃分子。<br/>
旧博客入口： <a target="_blank" href="http://codeplayer.blogspot.com/">http://codeplayer.blogspot.com/</a>
</p>
    ''',
    u'''
<h2>友情链接</h2>
<ul style="list-style:none;padding-left:15px;">
<li><a href="http://www.caomoxuan.com/" target="_blank">三饱三倒</a></li>
<li><a href="http://kjam.org/cn/" target="_blank">Kern.Jam</a></li>
</ul>
    ''',
    u'''
<h2>有谁在看</h2>
<p>
<script type="text/javascript" src="http://9.douban.com/service/badge/community/9361637/?show=&n=12&columns=3" ></script>
</p>
''',
u'''
<h2>Google Reader分享<h2>
<script type="text/javascript" src="http://www.google.com/reader/ui/publisher-zh_CN.js"></script>
<script type="text/javascript" src="http://www.google.com/reader/public/javascript/user/15378179180142400162/state/com.google/broadcast?n=5&callback=GRC_p(%7Bc%3A%22green%22%2Ct%3A%22%22%2Cs%3A%22true%22%2Cn%3A%22true%22%2Cb%3A%22false%22%7D)%3Bnew%20GRC"></script>
''',
u'''
<script type="text/javascript" src="http://feeds.delicious.com/v2/js/huangyi?title=%E7%BE%8E%E5%91%B3%E4%B9%A6%E7%AD%BE&count=10&bullet=%C2%BB&sort=date&extended"></script>
''',
u'''
<script type="text/javascript" src="http://feeds.delicious.com/v2/js/networkbadge/huangyi?showadd&icon=m&name&itemcount&nwcount&fancount"></script>
''',
u'''
<script type="text/javascript" src="http://feeds.delicious.com/v2/js/tags/huangyi?title=%E7%BE%8E%E5%91%B3Tag&count=30&sort=alpha&flow=cloud&color=73adff-3274d0&size=12-35"></script>
''',
]
