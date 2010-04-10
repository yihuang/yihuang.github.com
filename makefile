texts=$(wildcard src/*.txt)
htmls=$(patsubst src/%,html/%,$(patsubst %.txt,%.html,$(wildcard src/*.txt)))
templates=$(wildcard templates/*.mako)

html/%.html : src/%.txt templates/detail_tpl.mako *.py
	./imgmathhack.py $< | python gen_detail.py $(patsubst %.txt,%.html,$<)

detailpages=$(htmls)
listpage=html/index.html

all : $(listpage) $(detailpages)

$(listpage) : $(texts) templates/index_tpl.mako *.py
	ls src/*.txt -1r | python gen_list.py

clean :
	rm html/*.html
