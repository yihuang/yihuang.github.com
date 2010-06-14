<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <meta name="viewport" contect="width=device-width"></meta>
        <meta name="KEYWords" contect="黃毅 yihuang codeplayer python haskell web"></meta>
        <link rel="alternate" type="application/rss+xml" title="blog post summary feeds" href="/blog/rss.xml" />
        <title>${cfg.blogname}</title>
        <link rel="stylesheet" type="text/css" href="css/blog.css" media="screen" />
        <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon"/>
    </head>
    <body>
        <div id="header">
            <h1><a href="/blog/">${cfg.blogname}</a></h1>
            <div class="description">${cfg.description}</div>
            <div id="menu">
                <ul id="nav">
                    % for link in cfg.links:
                    <li>${link}</li>
                    % endfor
                </ul>
            </div>
        </div>
        <div id="content">
            <div id="right">
                % for article in articles:
                <div class="post">
                    <h2><a href="${article.filename_noext}.html">${article.title and article.title+' - ' or ''}${article.date.date()}</a></h2>
                    ${article.content}
                </div>
                % endfor
            </div>
            <div id="left">
                % for box in cfg.boxes:
                <div class="box">
                    ${box}
                </div>
                % endfor
            </div>
        </div>
        <link type="text/css" rel="stylesheet" href="css/pygments.css"/>
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
