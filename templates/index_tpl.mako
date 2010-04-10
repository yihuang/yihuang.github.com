<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
    <head>
        <title>${cfg.blogname}</title>
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
        <div id="content">
            <div id="right">
                % for article in articles:
                <div class="post">
                    <h2><a href="${article.filename_noext}.html">${article.title and article.title+' - ' or ''}${article.date}</a></h2>
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
    </body>
</html>
