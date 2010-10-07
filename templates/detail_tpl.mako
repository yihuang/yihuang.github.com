<!DOCTYPE html>
<html>
    <head>
        ${c.html_head%c.encoding}
        <meta name="viewport" contect="width=device-width"></meta>
        <link rel="alternate" type="application/rss+xml" title="blog post summary feeds" href="/blog/rss.xml" />
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
            </div>
            ${c.footer}
            <%include file="footer.mako"/>
        </div>
	</div>
    </body>
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
</html>
