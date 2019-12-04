ci:
	$(MAKE) test examples
	git diff
test:
	python setup.py test
examles:
	$(MAKE) -c examples
.PHONY: examples
