all:

setup:
	test -d venv || python3 -m venv venv
	source venv/bin/activate
	venv/bin/pip install -r requirements/local.txt
	venv/bin/python manage.py migrate

run:
	cd cat_crm ; python manage.py runserver

format:
	venv/bin/black $$(git ls-files '*.py')

list:
	git ls-files '*.py'
