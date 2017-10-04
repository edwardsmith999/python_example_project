default: test
	echo "Default"
test:
	python python_example_project/tests/test_number_fns.py
	python python_example_project/tests/test_number_class.py
