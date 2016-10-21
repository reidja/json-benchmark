all: samples rust_runner cpp_runner

run: samples rust_runner cpp_runner
	@echo "+python,5MB"
	/usr/bin/time -f "m:%MKB\nu:%U" ./test_python 5MB_sample.json 5MB_python.json
	@echo "+cpp,5MB"
	/usr/bin/time -f "m:%MKB\nu:%U" ./test_cpp 5MB_sample.json 5MB_cpp.json
	@echo "+rust,5MB"
	/usr/bin/time -f "m:%MKB\nu:%U" ./test_rust 5MB_sample.json 5MB_rust.json
	@echo "+python,75MB"
	/usr/bin/time -f "m:%MKB\nu:%U" ./test_python 75MB_sample.json 75MB_python.json
	@echo "+cpp,75MB"
	/usr/bin/time -f "m:%MKB\nu:%U" ./test_cpp 75MB_sample.json 75MB_cpp.json
	@echo "+rust,75MB"
	/usr/bin/time -f "m:%MKB\nu:%U" ./test_rust 75MB_sample.json 75MB_rust.json

results:
	$(RM) results.txt
	$(RM) *.csv
	./test_runner.sh
	python results.py

5MB_sample.json:
	python generate.py 20 1010 5MB_sample.json

75MB_sample.json:
	python generate.py 20 15250 75MB_sample.json

samples: 5MB_sample.json 75MB_sample.json

rust_runner:
	$(MAKE) -C rust/runner all

cpp_runner:
	$(MAKE) -C cpp/ all

clean:
	$(MAKE) -C rust/runner clean
	$(MAKE) -C cpp/ clean
	$(RM) results.txt
	$(RM) *.csv
	$(RM) 5MB.json 75MB.json
	$(RM) cpp.json rust.json python.json
