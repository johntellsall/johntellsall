all:

setup:
	test -d venv || python3 -m venv venv
	venv/bin/pip install -r requirements.txt

run:
	venv/bin/python3 gsearch.py -v

run2:
	venv/bin/python3 gsearch.py -v --limit=0 jm-john-search.yaml

test:
	venv/bin/pytest -v

distclean:
	-$(RM) -rf venv __pycache__