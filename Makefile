setup:
	pip install --upgrade pip
	pip install -r requirements.txt
#	python -m ipykernel install --user --name=firstEnv

format:
	black *.py

lint:
	pylint --disable=R,C app/main.py

test:
	python -m pytest -vv --cov=app tests/test_main.py

all: setup format lint test