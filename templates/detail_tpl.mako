${c.html_prolog%c.encoding}
<html>
    <head>
        ${c.html_head%c.encoding}
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
        <div id="header">
            <a href="/blog/"><h1 style="display:none">${cfg.blogname}</h1><img alt="${cfg.blogname}" src="images/logo.png" class="logo"/></a>
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
        <div id="middle">
            ${c.html_title}
            ${c.fragment}
            ${c.footer}
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
