SHELL := /bin/bash

.SILENT:

.PHONY: help
.DEFAULT_GOAL := help
help:  ## Prints all the targets in all the Makefiles
	@grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: list
list:  ## List all make targets
	@${MAKE} -pRrn : -f $(MAKEFILE_LIST) 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | egrep -v -e '^[^[:alnum:]]' -e '^$@$$' | sort

##########################
### Env Common Targets ###
##########################

.PHONY: check-env
check-env: ## Checks if the virtual environment is activated
ifndef VIRTUAL_ENV
	$(error 'Virtualenv is not activated, please activate the Python virtual environment by running "$$(make env_source)".')
endif

.PHONY: env_create
env_create:  ## Create the env; must be execute like so: $(make env_create)
	python3 -m venv venv

.PHONY: env_source
env_source:  ## Source the env; must be execute like so: $(make env_source)
	@echo 'source venv/bin/activate'

##########################
### Pip Common Targets ###
##########################

.PHONY: pip_freeze
pip_freeze: check-env ## Freeze the pip requirements
	pip freeze > requirements.txt

.PHONY: pip_install
pip_install: check-env ## Install the pip requirements
	pip install -r requirements.txt

#############################
### Python Common Targets ###
#############################

.PHONY: py_format
py_format: check-env  ## Format the python code
	black .
	isort .

####################
### Your stuff   ###
####################

.PHONY: generate_feed
generate_feed: check-env  ## Generate the feed
	python generate_feed.py