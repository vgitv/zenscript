# target directories
local := ~/.local/bin ~/.local/share ~/.local/state ~/.local/src ~/.local/lib ~/.local/etc

# bin
sourcebin := $(wildcard bin/*)
targetbin := $(subst bin/,~/.local/bin/,$(sourcebin))

# css
sourcecss := $(wildcard src/css_styles/*)
targetcss := $(subst src/,~/.local/src/,$(sourcecss))

# etc
etc := ~/.local/etc/homesync/exclude

install: $(local) $(targetbin) $(targetcss) $(etc)

.PHONY: print
print:
	@echo 'local:'
	@echo $(local)
	@echo -e '\nsource bin:'
	@echo $(sourcebin)
	@echo -e '\ntarget bin:'
	@echo $(targetbin)
	@echo -e '\nsource css:'
	@echo $(sourcecss)
	@echo -e '\ntarget css:'
	@echo $(targetcss)

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
	rm -f $(targetbin)
	rm -f $(targetcss)

.PHONY: coffee
coffee:
	@echo -e ' (\n  )\nc[]'
