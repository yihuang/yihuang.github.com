<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <meta name="viewport" contect="width=device-width"></meta>
        <meta name="KEYWords" contect="黃毅 yihuang codeplayer python haskell web"></meta>
        <link rel="alternate" type="application/rss+xml" title="blog post summary feeds" href="/blog/rss.xml" />
        <title>${cfg.blogname}</title>
        <link rel="stylesheet" type="text/css" href="css/html4css1.css" />
        <link rel="stylesheet" type="text/css" href="css/blog.css" media="screen" />
        <link rel="stylesheet" type="text/css" href="css/pygments.css"/>
        <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon"/>
    </head>
    <body>
	<div id="wrapper">
        <%include file="header.mako"/>
        <div id="content">
            <div id="right">
                % for article in articles:
                <div class="post">
                    <a href="${article.filename_noext}.html"><h2>${article.title} <span class="date">${article.date.date()}</span></h2></a>
                    ${article.content}
                </div>
                % endfor
                <p class="more"><a href="/blog/list.html">查看全部文章>></a></p>
            </div>
        </div>
        <hr>
        <%include file="footer.mako"/>
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
