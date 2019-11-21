.PHONY: init
init:
	@pipenv install --three -r requirements.txt

.PHONY: test
test:
	nosetests