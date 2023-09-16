all:

setup:
	test -d venv || python3 -m venv venv
	venv/bin/pip install -r requirements.txt

run:
	cd cat_crm ; python manage.py runserver

format:
	venv/bin/black cat_crm