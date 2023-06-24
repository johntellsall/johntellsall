all:

test:
	venv/bin/pytest -v
	
setup:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt

clean:
	-find . -name __pycache__ | xargs $(RM) -rf
	-find . -name .pytest_cache | xargs $(RM) -rf

distclean: clean
	-$(RM) -rf venv

list:
	find . -type f

reset:
	-$(RM) func.py test_func.py
