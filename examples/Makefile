default: 00 01 02 03 04 05 06

00:
	python $@*/main.py |& tee $$(echo $@*/)output.txt
01:
	python $@*/main.py |& tee $$(echo $@*/)output.txt
02:
	python $@*/main.py | tee $$(echo $@*/)output.txt
03:
	python $@*/main.py | tee $$(echo $@*/)output.txt
04:
	python $@*/main.py | tee $$(echo $@*/)output.txt
05:
	python $@*/main.py | tee $$(echo $@*/)output.txt
06:
	python $@*/here_is_none.py | sed 's@$(shell pwd)/@@g' | tee $$(echo $@*/)output.here_is_none.txt
	python $@*/here_is_file.py | sed 's@$(shell pwd)/@@g' | tee $$(echo $@*/)output.here_is_file.txt
	python $@*/here_is_cwd.py | sed 's@$(shell pwd)/@@g' | tee $$(echo $@*/)output.here_is_cwd.txt
	# python $@*/here_is_dot.py | sed 's@$(shell pwd)/@@g' | tee $$(echo $@*/)output.here_is_dot.txt
