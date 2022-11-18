TEMPLATES_AUTO_RELOAD=True

run:
	flask --app main.py --debug run
deps:
	pip install -r requirements.txt