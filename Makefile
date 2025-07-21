ci:
	hatch run test
	git diff
test:
	hatch run test
examles:
	$(MAKE) -c examples

build:
	hatch build

upload:
	hatch publish

.PHONY: test build upload examples
