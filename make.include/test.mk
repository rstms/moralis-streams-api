# test - testing with pytest and tox

options ?= -x --log-cli-level=CRITICAL
testfiles ?= $(wildcard tests/test_*.py)
options := $(if $(test),$(options) -k $(test),$(options))

tox_options ?=

.PHONY: test

### run tests;  example: make options=-svvx test=cli test 
test:
	env TESTING=1 python setup.py test


.PHONY: tox
### test with tox if sources have changed
tox: .tox 
.tox: $(src) tox.ini
	$(call gitclean)
	env PYTEST_OPTIONS='$(tox_options)' tox
	@touch $@

toxclean:
	rm -rf .tox

test-clean: toxclean
