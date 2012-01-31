<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <meta name="viewport" contect="width=device-width"></meta>
        <meta name="KEYWords" contect="黃毅 yihuang codeplayer python haskell web"></meta>
        <link rel="alternate" type="application/rss+xml" title="blog post summary feeds" href="rss.xml" />
        <link rel="stylesheet" type="text/css" href="css/blog.css" media="screen" />
        <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon"/>
    </head>
    <body>
	<div id="wrapper">
        <%include file="header.mako"/>
        <div id="middle">
            <h1>博客文章列表</h1>
            <dl>
            % for d, l in date_group:
            <dt>
            ${d.date()}
            </dt>
            % for article in l:
            <dd><a href="${article.filename_noext}.html">${article.title}</a></dd>
            % endfor
            % endfor
            </dl>
            <hr>
            <%include file="footer.mako"/>
        </div>
	</div>
    </body>
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
</html>
