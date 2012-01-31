<!DOCTYPE html>
<html>
    <head>
        ${c.html_head%c.encoding}
        <meta name="viewport" contect="width=device-width"></meta>
        <link rel="alternate" type="application/rss+xml" title="blog post summary feeds" href="rss.xml" />
        <link type="text/css" rel="stylesheet" href="css/html4css1.css"/>
        <link rel="stylesheet" type="text/css" href="css/blog.css" media="screen" />
        <link type="text/css" rel="stylesheet" href="css/pygments.css"/>
        <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon"/>
        <style type="text/css">
            .contents {
            margin-top:0;
            }
        </style>
    </head>
    <body>
        <div id="wrapper">
            <%include file="header.mako"/>
            <div id="middle">
                <div class="postdetail">
                    ${c.html_title}
                    % if date:
                    <p class="author">${date} 黄毅</p>
                    % endif
                    ${c.fragment}
                    <br/>
                    <div id="disqus_thread"></div>
                    <script type="text/javascript">
                        var disqus_shortname = 'yi-programmer';
                        var disqus_identifier = '${identifier}';
                        var disqus_url = '${url}';

                        (function() {
                        var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
                        dsq.src = 'http://' + disqus_shortname + '.disqus.com/embed.js';
                        (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
                        })();
                    </script>
                    <noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
                    <a href="http://disqus.com" class="dsq-brlink">blog comments powered by <span class="logo-disqus">Disqus</span></a>

                    <p class="announce">转载请注明出处，收藏或分享这篇文章到：</p>
                    <p class="share-icons">
                        <a target="_blank" title="分享到豆瓣" href="http://www.douban.com/recommend/?url=${url}&title=${c.title}"><img src="images/icons/douban.png" alt="分享到豆瓣"/></a>
                        <a target="_blank" title="收藏到delicious" href="http://del.icio.us/post?url=${url}&title=${c.title}"><img src="images/icons/delicious.png" alt="收藏到delicious"/></a>
                        <a target="_blank" title="收藏到QQ书签" href="http://shuqian.qq.com/post?from=3&title=${c.title}&uri=${url}&jumpback=2&noui=1"><img src="images/icons/qqbookmark.gif" alt="收藏到QQ书签"/></a>
                        <a target="_blank" title="收藏到google书签" href="https://www.google.com/bookmarks/mark?op=add&bkmk=${url}&title=${c.title}"><img src="images/icons/google.gif" alt="收藏到google书签"/></a>
                        <a target="_blank" title="收藏到百度搜藏" href="http://cang.baidu.com/do/add?iu=${url}&it=${c.title}&fr=ien#nw=1"><img src="images/icons/baidu.gif" alt="收藏到百度搜藏"/></a>
                        <a target="_blank" title="分享到新浪围脖" href="http://v.t.sina.com.cn/share/share.php?url=${url}&title=${c.title}&source=bookmark"><img src="images/icons/sina-t.jpg" alt="分享到新浪围脖"/></a>
                        <a target="_blank" title="分享到facebook" href="http://www.facebook.com/sharer.php?u=${url}&t=${c.title}"><img src="images/icons/facebook.png" alt="分享到facebook"/></a>
                        <a target="_blank" title="分享到人人网" href="http://share.renren.com/share/buttonshare.do?link=${url}&title=${c.title}"><img src="images/icons/renren.gif" alt="分享到人人网"/></a>
                        <a target="_blank" title="分享到开心网" href="http://www.kaixin001.com/repaste/share.php?rtitle=${c.title}&rurl=${url}&rcontent=${url}"><img src="images/icons/kaixin.gif" alt="分享到开心网"/></a>
                        <a target="_blank" title="分享到QQ空间" href="http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url=${url}"><img src="images/icons/qzone.gif" alt="分享到QQ空间"/></a>
                        <a target="_blank" title="分享到MySpace" href="http://www.myspace.cn/Modules/PostTo/Pages/Default.aspx?u=${url}&t=${c.title}"><img src="images/icons/myspace.jpg" alt="分享到MySpace"/></a>
                    </p>
                </div>
                ${c.footer}
                <%include file="footer.mako"/>
            </div>
        </div>
                <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
        <script type="text/javascript" src="js/main.js"></script>
        <script type="text/javascript">
            var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
            document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
        </script>
        <script type="text/javascript">
            try{
            var pageTracker = _gat._getTracker("UA-415070-6");
            pageTracker._trackPageview();
            } catch(err) {}
        </script>
    </body>
</html>
