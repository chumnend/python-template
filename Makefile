MODULE_NAME = template

.PHONY: init
init:
	@pipenv install --three -r requirements.txt
	
.PHONY: start
start:
	@python -m $(MODULE_NAME)

.PHONY: test
test:
	nosetests