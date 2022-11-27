TEMPLATES_AUTO_RELOAD=True

run:
	flask --app main.py --debug run
deps:
	pip install -r requirements.txt
build-docker:
	docker build -t saadhan .
docker:
	docker run -p 5000:5000 saadhan