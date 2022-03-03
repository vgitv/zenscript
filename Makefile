local := ~/.local/bin ~/.local/share ~/.local/state ~/.local/src ~/.local/lib ~/.local/etc
bin := $(wildcard bin/*)
target := $(subst bin/,~/.local/bin/,$(bin))
css := ~/.local/src/css_styles/main-dark.css
etc := ~/.local/etc/homesync/exclude

install: $(local) $(target) $(css) $(etc)

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

~/.local/lib:
	mkdir $@

~/.local/etc:
	mkdir $@

# binaires (implicit rule)
~/.local/bin/%: bin/%
	cp $^ ~/.local/bin/ && chmod 750 $@

# css styles (implicit rule)
~/.local/src/css_styles/%: ~/.local/src/css_styles src/css_styles/%
	cp $(word 2,$^) ~/.local/src/css_styles/ && chmod 640 $@

~/.local/src/css_styles:
	mkdir $@

# etc
~/.local/etc/homesync/%: ~/.local/etc/homesync etc/homesync/%
	cp $(word 2,$^) ~/.local/etc/homesync/ && chmod 640 $@

~/.local/etc/homesync:
	mkdir $@

# remove all file targets but not directories
uninstall:
	rm -f $(target)
	rm -f $(css)

.PHONY: coffee
coffee:
	@echo -e ' (\n  )\nc[]'
