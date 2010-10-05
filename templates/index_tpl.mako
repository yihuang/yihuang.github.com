<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
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
	<div id="header">
        <a href="/blog/"><h1 style="display:none">${cfg.blogname}</h1><img alt="${cfg.blogname}" src="images/logo.png"/></a>
            <div class="nav-icons">
                <p class="nav">
                    % for name,url,src,class_ in cfg.nav_icons:
                    % if name=='break':
                    <br/>
                    % else:
                    <a title="${name}" href="${url}" class="${class_}"><img src="${src}" alt="${name}"/></a>
                    % endif
                    % endfor
                </p>
                <p class="link">
                    % for name,url,src,class_ in cfg.link_icons:
                    % if name=='break':
                    <br/>
                    % else:
                    <a title="${name}" href="${url}" class="${class_}"><img src="${src}" alt="${name}"/></a>
                    % endif
                    % endfor
                </p>
            </div>
        </div>
        <div id="content">
            <div id="right">
                % for article in articles:
                <div class="post">
                    <a href="${article.filename_noext}.html"><h2>${article.title} <span class="date">${article.date.date()}</span></h2></a>
                    ${article.content}
                </div>
                % endfor
            </div>
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
