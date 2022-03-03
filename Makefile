local := ~/.local/bin ~/.local/share ~/.local/state ~/.local/src
bin := $(wildcard bin/*)
target := $(subst bin/,~/.local/bin/,$(bin))

install: $(local) $(target)

.PHONY: print
print:
	@echo 'bin:'
	@echo $(bin)
	@echo -e '\ntarget:'
	@echo $(target)
	@echo -e '\nlocal:'
	@echo $(local)

~/.local/bin:
	mkdir $@

~/.local/share:
	mkdir $@

~/.local/state:
	mkdir $@

~/.local/src:
	mkdir $@

~/.local/bin/%: bin/%
	cp $^ ~/.local/bin/ && chmod 744 $@

uninstall:
	rm -f $(target)

.PHONY: coffee
coffee:
	@echo -e ' (\n  )\nc[]'
