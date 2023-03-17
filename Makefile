local := ~/.local/bin ~/.local/share ~/.local/state ~/.local/src
bin := $(wildcard bin/*)
target := $(subst bin/,~/.local/bin/,$(bin))
css := ~/.local/src/css_styles/main-dark.css

install: $(local) $(target) $(css)

.PHONY: print
print:
	@echo 'bin:'
	@echo $(bin)
	@echo -e '\ntarget:'
	@echo $(target)
	@echo -e '\nlocal:'
	@echo $(local)

# local arborescence
~/.local/bin:
	mkdir $@

~/.local/share:
	mkdir $@

~/.local/state:
	mkdir $@

~/.local/src:
	mkdir $@

# binaires (implicit rule)
~/.local/bin/%: bin/%
	cp $^ ~/.local/bin/ && chmod 750 $@

# css styles (implicit rule)
~/.local/src/css_styles/%: ~/.local/src/css_styles src/css_styles/%
	cp $(word 2,$^) ~/.local/src/css_styles/ && chmod 640 $@

~/.local/src/css_styles:
	mkdir $@

# remove all file targets but not directories
uninstall:
	rm -f $(target)
	rm -f $(css)

.PHONY: coffee
coffee:
	@echo -e ' (\n  )\nc[]'
