<div id="header">
    <a href="index.html"><h1>${cfg.blogname}</h1></a>
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
            <a title="${name}" href="${url}" class="${class_}"><img width="16" src="${src}" alt="${name}"/></a>
            % endif
            % endfor
        </p>
    </div>
</div>
