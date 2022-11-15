TEMPLATES_AUTO_RELOAD=True

run:
	flask --app app.py --debug run
deps:
	pip install -r requirements.txt