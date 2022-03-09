# target directories
local := ~/.local/bin ~/.local/share ~/.local/state ~/.local/src ~/.local/lib ~/.local/etc

# bin
sourcebin := $(wildcard bin/*)
targetbin := $(subst bin/,~/.local/bin/,$(sourcebin))

# src
sourcecss := $(wildcard src/css_styles/*)
targetcss := $(subst src/,~/.local/src/,$(sourcecss))

targeteadmin := ~/.local/src/eadmin/main.tex

targetsrc := $(targetcss) $(targeteadmin)

# etc
etc := ~/.local/etc/homesync/exclude

install: $(local) $(targetbin) $(targetsrc) $(etc)

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
	@echo -e '\ntarget src:'
	@echo $(targetsrc)

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

~/.local/src/eadmin/%: ~/.local/src/eadmin src/eadmin/%
	cp $(word 2,$^) ~/.local/src/eadmin/ && chmod 640 $@

~/.local/src/eadmin:
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
