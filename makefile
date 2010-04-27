texts=$(wildcard src/*.txt)
htmls=$(patsubst src/%,html/%,$(patsubst %.txt,%.html,$(wildcard src/*.txt)))
templates=$(wildcard templates/*.mako)

comm_dep=*.py docutils.conf

html/%.html : src/%.txt templates/detail_tpl.mako $(comm_dep)
	./imgmathhack.py $< | python gen_detail.py $(patsubst %.txt,%.html,$<)

detailpages=$(htmls)
listpage=html/index.html

all : $(listpage) $(detailpages)
detail : $(detailpages)
index : $(listpage)

$(listpage) : $(texts) templates/index_tpl.mako  $(comm_dep)
	ls src/*.txt -1r | python gen_list.py
	ls src/*.txt -1r | python gen_rss.py

clean :
	rm html/*.html
