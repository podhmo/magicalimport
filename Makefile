ci:
	$(MAKE) test examples
	git diff
test:
	python setup.py test
examles:
	$(MAKE) -c examples

build:
#	pip install wheel
	python setup.py bdist_wheel

upload:
#	pip install twine
	twine check dist/magicalimport-$(shell cat VERSION)*
	twine upload dist/magicalimport-$(shell cat VERSION)*

.PHONY: test build upload examples
