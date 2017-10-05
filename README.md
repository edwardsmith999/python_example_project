# python_example_project  [![Build Status](https://travis-ci.org/edwardsmith999/python_example_project.svg?branch=master)](https://travis-ci.org/edwardsmith999/python_example_project)

This project shows a minimal example of a Python module complete with Travis continuous integration testing.

## Installing the module
Options specifying how the module shoud be installed are set in the `setup.py` file. The module can be 
installed with `pip`, the python package manager, using the following command

```bash
git clone https://github.com/edwardsmith999/python_example_project.git
cd python_example_project
pip install .
```

## Running the tests
Typically each submodule of a python package should have a `tests` directory containing python
scripts in which the module/submodule functionality is tested. Tests can be run using `py.test` 
by executing the following command from the top level directory

```bash
py.test -v python_example_project
```

## Advanced test examples
Some examples of more advanced test features can be found in the
[`stream_proc`](./python_example_project/stream_proc) submodule. This submodule demonstrates the
basics of polymorphism in python; illustrates how to use mocking and test fixtures in tests; and 
demonstrates the use of custom exception classes and testing for the raising of exceptions.
