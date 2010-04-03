htmls=$(patsubst src/%,html/%,$(patsubst %.txt,%.html,$(wildcard src/*.txt)))

html/%.html : src/%.txt
	python gen.py $<

detailpages : $(htmls) templates
	
all : detailpages
