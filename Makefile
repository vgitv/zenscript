bin := $(wildcard bin/*)
target := $(subst bin/,~/.local/bin/,$(bin))

install: $(target)

.PHONY: print
print:
	@echo 'bin:'
	@echo $(bin)
	@echo 'target:'
	@echo $(target)

~/.local/bin/%: bin/%
	cp $^ ~/.local/bin/ && chmod 744 $@

uninstall:
	rm -f $(target)

.PHONY: coffee
coffee:
	@echo -e ' (\n  )\nc[]'
