root=../
texts=$(wildcard ../src/*.txt)
htmls=$(patsubst ../src/%,../%,$(patsubst %.txt,%.html,$(wildcard ../src/*.txt)))
templates=$(wildcard templates/*.mako)

comm_dep=*.py docutils.conf

$(root)%.html : $(root)src/%.txt templates/detail_tpl.mako $(comm_dep)
	./imgmathhack.py $< | python gen_detail.py $(patsubst %.txt,%.html,$<)

detailpages=$(htmls)
indexpage=$(root)index.html
listpage=$(root)list.html

all : $(indexpage) $(detailpages)
detail : $(detailpages)
index : $(indexpage) $(listpage)

$(indexpage) $(listpage) : $(texts) templates/index_tpl.mako templates/list_tpl.mako $(comm_dep)
	ls -1r $(root)src/*.txt | grep -v "^_" | python gen_list.py
	ls -1r $(root)src/*.txt | grep -v "^_" | python gen_rss.py

clean :
	rm $(root)*.html
