${c.html_prolog%c.encoding}
<html>
    <head>
        ${c.html_head%c.encoding}
        <link type="text/css" rel="stylesheet" href="css/html4css1.css"/>
        <link rel="stylesheet" type="text/css" href="css/blog.css" media="screen" />
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
        <div id="middle">
            ${c.html_title}
            ${c.fragment}
            ${c.footer}
        </div>
	</div>
    </body>
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
</html>
