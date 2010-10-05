texts=$(wildcard src/*.txt)
htmls=$(patsubst src/%,html/%,$(patsubst %.txt,%.html,$(wildcard src/*.txt)))
templates=$(wildcard templates/*.mako)

comm_dep=*.py docutils.conf

html/%.html : src/%.txt templates/detail_tpl.mako $(comm_dep)
	./imgmathhack.py $< | python gen_detail.py $(patsubst %.txt,%.html,$<)

detailpages=$(htmls)
indexpage=html/index.html
listpage=html/list.html

all : $(indexpage) $(detailpages)
detail : $(detailpages)
index : $(indexpage) $(listpage)

$(indexpage) $(listpage) : $(texts) templates/index_tpl.mako templates/list_tpl.mako $(comm_dep)
	ls -1r src/*.txt | python gen_list.py
	ls -1r src/*.txt | python gen_rss.py

clean :
	rm html/*.html
