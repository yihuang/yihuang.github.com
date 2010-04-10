${c.html_prolog%c.encoding}
<html>
    <head>
        ${c.html_head%c.encoding}
        <link type="text/css" rel="stylesheet" href="css/html4css1.css"></link>
        <link rel="stylesheet" type="text/css" href="css/blog.css" media="screen" />
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
        <div id="middle">
            ${c.html_title}
            ${c.fragment}
        </div>
    </body>
    <link type="text/css" rel="stylesheet" href="css/pygments.css"></link>
</html>
